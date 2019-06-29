import os
import argparse
import torch
import numpy as np

#training_data_tsv = "/home/ying/Cluster/izkf/projects/ENCODEImputation/local/TSV/metadata_training_data.tsv"
model_loc = "/home/ying/Cluster/EmbeddingRegression"
save_loc = '/home/ying/PycharmProjects/test/imputation_challenge/embedding_weights'
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

cell = ['C02', 'C20', 'C35', 'C45', 'C05', 'C06', 'C07', 'C08', 'C11', 'C15', 'C16', 'C17', 'C18', 'C19', 'C21',
        'C22', 'C23', 'C24', 'C27', 'C28', 'C30', 'C32', 'C33', 'C39', 'C40', 'C41', 'C42', 'C43', 'C44', 'C46',
        'C47', 'C48', 'C49', 'C51', 'C12', 'C25', 'C31', 'C34', 'C01', 'C03', 'C09', 'C10', 'C13', 'C36', 'C37',
        'C38', 'C50', 'C04', 'C29', 'C14', 'C26']
assay = ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15',
         'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30',
         'M31', 'M32', 'M33', 'M34', 'M35']

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--chrom", type=str, default='all')
    #parser.add_argument("-n", "--name", type=str, default=None)
    return parser.parse_args()

args = parse_args()

def l_dict(l):
    result = {}
    l_25_chrom = chrom_size_dict[args.chrom]
    l_250_chrom = l_25_chrom//10 + 1
    l_5k_chrom = l_25_chrom//200 + 1
    if len(l)==51:
        for i in range(len(l)):
            result[cell[i]] = l[i]
    elif len(l)==35:
        for i in range(len(l)):
            result[assay[i]] = l[i]
    elif len(l)== l_25_chrom:
        for i in range(l_25_chrom):
            result[i] = l[i]
    elif len(l)== l_250_chrom:
        for i in range(l_250_chrom):
            result[i] = l[i]
    elif len(l)== l_5k_chrom:
        for i in range(l_5k_chrom):
            result[i] = l[i]
    else:
        print('wrong length for input')

    return result

def main():
    model_path = os.path.join(model_loc, "{}.pth".format(args.chrom))
    model_all = torch.load(model_path, map_location='cpu')

    cell_embedding_weight = model_all['cell_embedding.weight'].tolist()
    cell_dict = l_dict(cell_embedding_weight)
    np.save(os.path.join(save_loc, 'cell_{}'.format(args.chrom)), cell_dict)

    assay_embedding_weight = model_all['assay_embedding.weight'].tolist()
    assay_dict = l_dict(assay_embedding_weight)
    np.save(os.path.join(save_loc, 'assay_{}'.format(args.chrom)), assay_dict)

    positions_25bp_embedding_weight = model_all['positions_25bp_embedding.weight'].tolist()
    position_25bp_dict = l_dict(positions_25bp_embedding_weight)
    np.save(os.path.join(save_loc, 'position_25bp_{}'.format(args.chrom)), position_25bp_dict)

    positions_250bp_embedding_weight = model_all['positions_250bp_embedding.weight'].tolist()
    position_250bp_dict = l_dict(positions_250bp_embedding_weight)
    np.save(os.path.join(save_loc, 'position_250bp_{}'.format(args.chrom)), position_250bp_dict)

    positions_5kbp_embedding_weight = model_all['positions_5kbp_embedding.weight'].tolist()
    position_5kbp_dict = l_dict(positions_5kbp_embedding_weight)
    np.save(os.path.join(save_loc, 'position_5kbp_{}'.format(args.chrom)), position_5kbp_dict)


    print('Save all 5 embedding inputs... for {}'.format(args.chrom))

if __name__ == '__main__':
    main()