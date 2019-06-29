import os
import argparse
import numpy as np
import random
import time
import warnings

import torch
from torch import nn
from torch.nn import functional as F


training_data_tsv = "/home/ying/Cluster/izkf/projects/ENCODEImputation/local/TSV/metadata_training_data.tsv"
model_loc = "/home/ying/Cluster/izkf/projects/ENCODEImputation/exp/Li/Models/EmbeddingRegression"
chrom_size_dict = {'chr1': 9958247,
                   'chr2': 9687698,
                   'chr3': 7931798,
                   'chr4': 7608557,
                   'chr5': 7261460,
                   'chr6': 6832240,
                   'chr7': 6373839,
                   'chr8': 5805546,
                   'chr9': 5535789,
                   'chr10': 5351815,
                   'chr11': 5403465,
                   'chr12': 5331013,
                   'chr13': 4574574,
                   'chr14': 4281749,
                   'chr15': 4079648,
                   'chr16': 3613240,
                   'chr17': 3330298,
                   'chr18': 3214932,
                   'chr19': 2344705,
                   'chr20': 2577636,
                   'chr21': 1868374,
                   'chr22': 2032739,
                   'chrX': 6241636}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--chrom", type=str, default=None)
    parser.add_argument("-v", "--verbose", type=int, default=0)
    parser.add_argument("-l", "--cell", type=str, default=None)
    parser.add_argument("-a", "--assay", type=str, default=None)
    return parser.parse_args()


class Avocado(nn.Module):
    def __init__(self, n_cells, n_assays, n_positions_25bp, n_positions_250bp, n_positions_5kbp,
                 cell_embedding_dim=10, assay_embedding_dim=10, positions_25bp_embedding_dim=25,
                 positions_250bp_embedding_dim=25, positions_5kbp_embedding_dim=25, n_hidden_units=256):
        super(Avocado, self).__init__()

        # cell embedding matrix
        self.cell_embedding = nn.Embedding(num_embeddings=n_cells,
                                           embedding_dim=cell_embedding_dim)

        # assay embedding matrix
        self.assay_embedding = nn.Embedding(num_embeddings=n_assays,
                                            embedding_dim=assay_embedding_dim)

        # genomic positions embedding matrix
        self.positions_25bp_embedding = nn.Embedding(num_embeddings=n_positions_25bp,
                                                     embedding_dim=positions_25bp_embedding_dim)

        self.positions_250bp_embedding = nn.Embedding(num_embeddings=n_positions_250bp,
                                                      embedding_dim=positions_250bp_embedding_dim)

        self.positions_5kbp_embedding = nn.Embedding(num_embeddings=n_positions_5kbp,
                                                     embedding_dim=positions_5kbp_embedding_dim)

        in_features = cell_embedding_dim + assay_embedding_dim + positions_25bp_embedding_dim + \
                      positions_250bp_embedding_dim + positions_5kbp_embedding_dim

        self.linear1 = nn.Linear(in_features, n_hidden_units)
        self.linear2 = nn.Linear(n_hidden_units, n_hidden_units)
        self.linear_out = nn.Linear(n_hidden_units, 1)
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        cell_index = x[:, 0]
        assay_index = x[:, 1]
        positions_25bp_index = x[:, 2]
        positions_250bp_index = x[:, 3]
        positions_5kbp_index = x[:, 4]

        inputs = torch.cat((self.cell_embedding.weight[cell_index],
                            self.assay_embedding.weight[assay_index],
                            self.positions_25bp_embedding.weight[positions_25bp_index],
                            self.positions_250bp_embedding.weight[positions_250bp_index],
                            self.positions_5kbp_embedding.weight[positions_5kbp_index]), 1)

        x = F.relu(self.linear1(inputs))
        x = self.dropout(x)
        x = F.relu(self.linear2(x))
        out = self.linear_out(x)

        return out


def get_cells_assays():
    cells = []
    assays = []

    f = open(training_data_tsv)
    f.readline()

    for line in f.readlines():
        ll = line.strip().split("\t")
        if ll[1] not in cells:
            cells.append(ll[1])

        if ll[2] not in assays:
            assays.append(ll[2])
    f.close()
    print(cells, assays)
    return cells, assays


def main():
    args = parse_args()

    cells, assays = get_cells_assays()

    n_positions_25bp = chrom_size_dict[args.chrom]

    n_positions_250bp, n_positions_5kbp = n_positions_25bp // 10 + 1, n_positions_25bp // 200 + 1

    model_path = os.path.join(model_loc, "{}.pth".format(args.chrom))

    avocado = Avocado(n_cells=len(cells),
                      n_assays=len(assays),
                      n_positions_25bp=n_positions_25bp,
                      n_positions_250bp=n_positions_250bp,
                      n_positions_5kbp=n_positions_5kbp)

    if os.path.exists(model_path):
        avocado.load_state_dict(torch.load(model_path, map_location='cpu'))
        print('Model loaded...')

    if torch.cuda.is_available():
        avocado.cuda()

    avocado.eval()
    c_idx = cells.index(args.cell)
    a_idx = assays.index(args.assay)

    start = time.time()
    print('cell_index = {}'.format(c_idx), 'assay_index = {}'.format(a_idx))

    prediction = []

    for genomic_25bp_index in range(n_positions_25bp):

        genomic_250bp_index, genomic_5kbp_index = n_positions_25bp // 10, n_positions_25bp // 200
        x = np.array([[c_idx, a_idx, genomic_25bp_index, genomic_250bp_index, genomic_5kbp_index]])
        x = torch.as_tensor(x)
        if torch.cuda.is_available():
            y_pred = avocado(x.cuda()).reshape(-1)
            prediction.append(y_pred.tolist()[0])
        else:
            y_pred = avocado(x).reshape(-1)
            prediction.append(y_pred.tolist()[0])

    secs = time.time() - start
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    print('time: %dh %dm %ds' % (h, m, s))

    print('save the prediction...')
    np.save(
        '/home/ying/Cluster/izkf/projects/ENCODEImputation/exp/Ying/Preditions/avocado/NPY/{}{}_{}'.format(args.cell, args.assay,
                                                                                               args.chrom), prediction)

if __name__ == '__main__':
    main()