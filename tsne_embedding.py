# Author: Narine Kokhlikyan <narine@slice.com>
# License: BSD

print(__doc__)
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold
from matplotlib.ticker import NullFormatter
from time import time
from matplotlib import offsetbox

chrom_list = ['chr1', 'chr2', 'chr3',
              'chr4', 'chr5', 'chr6',
              'chr7', 'chr8', 'chr9',
              'chr10', 'chr11', 'chr12',
              'chr13', 'chr14', 'chr15',
              'chr16', 'chr17', 'chr18',
              'chr19', 'chr20', 'chr21',
              'chr22', 'chrX']

cells = ['C02', 'C20', 'C35', 'C45', 'C05', 'C06', 'C07', 'C08', 'C11', 'C15', 'C16', 'C17', 'C18', 'C19', 'C21', \
         'C22', 'C23', 'C24', 'C27', 'C28', 'C30', 'C32', 'C33', 'C39', 'C40', 'C41', 'C42', 'C43', 'C44', 'C46', \
         'C47', 'C48', 'C49', 'C51', 'C12', 'C25', 'C31', 'C34', 'C01', 'C03', 'C09', 'C10', 'C13', 'C36', 'C37', \
         'C38', 'C50', 'C04', 'C29', 'C14', 'C26']

assays = ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', \
          'M16', 'M17', 'M18', 'M19', 'M20', 'M21', 'M22', 'M23', 'M24', 'M25', 'M26', 'M27', 'M28', 'M29', 'M30', \
          'M31', 'M32', 'M33', 'M34', 'M35']

#parameter set
n_components = 2
(fig, subplots) = plt.subplots(2, 4, figsize=(25, 10))
perplexities = [5, 30, 50, 100]

loc = '/home/ying/Cluster/izkf/projects/ENCODEImputation/exp/Ying/Embedding_weights'
print('load files...')

def load_dict(type, lst):
    result_dict = {}
    for j in lst:
        result_dict[j] = []
    for i in chrom_list:
        para = np.load(os.path.join(loc, '{}_{}.npy'.format(type, i)), allow_pickle=True)
        para_dict = para.tolist()
        for j in lst:
            result_dict[j].extend(para_dict[j])
    result_array = []
    for i in result_dict:
        result_array.append(result_dict[i])
    return np.array(result_array)

def plot_tsne(X, y, color):

    for i, perplexity in enumerate(perplexities):
        ax = subplots[0][i]

        t0 = time()
        tsne = manifold.TSNE(n_components=n_components, init='random',
                             random_state=0, perplexity=perplexity)
        Y = tsne.fit_transform(X)
        print(Y[0])
        print(Y[0, 0])
        t1 = time()
        print("circles, perplexity=%d in %.2g sec" % (perplexity, t1 - t0))
        ax.set_title("Perplexity=%d" % perplexity)
        #ax.scatter(Y[:, 0], Y[:, 1], c=color)
        for j in range(len(y)):
            plt.text(Y[j, 0], Y[j, 1], str(y[j]), fontdict={'weight': 'bold', 'size': 9})
        #print(y)
        #ax.xaxis.set_major_formatter(NullFormatter())
        #ax.yaxis.set_major_formatter(NullFormatter())
        ax.axis('tight')

def main():
    cell_X = load_dict('cell', cells)
    cell_y = [i for i in cells]
    plot_tsne(cell_X, cell_y, 'r')
    #assay_X = load_dict('assay', assays)

    plt.show()

if __name__ == '__main__':
    main()




