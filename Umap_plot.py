print(__doc__)
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold
from matplotlib.ticker import NullFormatter
from time import time
from matplotlib import offsetbox
import umap

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

CELL_NAME = {
    'C02': 'adrenal_gland',
    'C20': 'heart_left_ventricle',
    'C35': 'omental_fat_pad',
    'C45': 'testis',
    'C05': 'BE2C',
    'C06': 'brain_microvascular_endothelial_cell',
    'C07': 'Caco-2',
    'C08': 'cardiac_fibroblast',
    'C11': 'dermis_microvascular_lymphatic_vessel_endothelial_cell',
    'C15': 'G401',
    'C16': 'GM06990',
    'C17': 'H1-hESC',
    'C18': 'H9',
    'C19': 'HAP-1',
    'C21': 'hematopoietic_multipotent_progenitor_cell',
    'C22': 'HL-60',
    'C23': 'IMR-90',
    'C24': 'K562',
    'C27': 'mesenchymal_stem_cell',
    'C28': 'MG63',
    'C30': 'NCI-H460',
    'C32': 'neural_stem_progenitor_cell',
    'C33': 'occipital_lobe',
    'C39': 'SJCRH30',
    'C40': 'SJSA1',
    'C41': 'SK-MEL-5',
    'C42': 'skin_fibroblast',
    'C43': 'skin_of_body',
    'C44': 'T47D',
    'C46': 'trophoblast_cell',
    'C47': 'upper_lobe_of_left_lung',
    'C48': 'urinary_bladder',
    'C49': 'uterus',
    'C51': 'WERI-Rb-1',
    'C12': 'DND-41',
    'C25': 'KMS-11',
    'C31': 'NCI-H929',
    'C34': 'OCI-LY7',
    'C01': 'adipose_tissue',
    'C03': 'adrenal_gland_embryonic',
    'C09': 'CD4-positive_alpha-beta_memory_T_cell',
    'C10': 'chorion',
    'C13': 'endocrine_pancreas',
    'C36': 'peripheral_blood_mononuclear_cell',
    'C37': 'prostate',
    'C38': 'RWPE2',
    'C50': 'vagina',
    'C04': 'amnion',
    'C29': 'myoepithelial_cell_of_mammary_gland',
    'C14': 'ES-I3',
    'C26': 'lower_leg_skin'
}
ASSAY_NAME = {
    'M01': 'ATAC-seq',
    'M02': 'DNase-seq',
    'M03': 'H2AFZ',
    'M04': 'H2AK5ac',
    'M05': 'H2AK9ac',
    'M06': 'H2BK120ac',
    'M07': 'H2BK12ac',
    'M08': 'H2BK15ac',
    'M09': 'H2BK20ac',
    'M10': 'H2BK5ac',
    'M11': 'H3F3A',
    'M12': 'H3K14ac',
    'M13': 'H3K18ac',
    'M14': 'H3K23ac',
    'M15': 'H3K23me2',
    'M16': 'H3K27ac',
    'M17': 'H3K27me3',
    'M18': 'H3K36me3',
    'M19': 'H3K4ac',
    'M20': 'H3K4me1',
    'M21': 'H3K4me2',
    'M22': 'H3K4me3',
    'M23': 'H3K56ac',
    'M24': 'H3K79me1',
    'M25': 'H3K79me2',
    'M26': 'H3K9ac',
    'M27': 'H3K9me1',
    'M28': 'H3K9me2',
    'M29': 'H3K9me3',
    'M30': 'H3T11ph',
    'M31': 'H4K12ac',
    'M32': 'H4K20me1',
    'M33': 'H4K5ac',
    'M34': 'H4K8ac',
    'M35': 'H4K91ac'
}

#parameter set
#n_components = 2

#(fig, subplots) = plt.subplots(2, 4, figsize=(25, 10))
#perplexities = [5, 30, 50, 100]

loc = '/home/ying/Cluster/izkf/projects/ENCODEImputation/exp/Ying/Embedding_weights/EmbeddingRegression'
save_loc = '/home/ying/Cluster/izkf/projects/ENCODEImputation/report/Visualization/EmbeddingRegression'


def load_dict(type, lst):
    result_dict = {}
    for j in lst:
        result_dict[j] = []
    for i in chrom_list[:-1]:
        para = np.load(os.path.join(loc, '{}_{}.npy'.format(type, i)), allow_pickle=True)
        para_dict = para.tolist()
        for j in lst:
            result_dict[j].extend(para_dict[j])
    result_array = []
    for i in result_dict:
        result_array.append(result_dict[i])
    return np.array(result_array)

def plot_tsne(dic, data, type,lst):
    y = [i  for i in lst]
    embedding = umap.UMAP()
    Y = embedding.fit_transform(data)
    f = open(os.path.join(save_loc, '{}_umap.txt'.format(type)), 'a')
    for i in Y:
        #print(i)
        f.write(str(i[0]) + '\t' + str(i[1]) + '\n')
    f.close()
    print('{} file is saved...'.format(type))
    plt.figure(figsize=(12, 12), dpi=80)
    plt.scatter(Y[:, 0], Y[:, 1], c='r')
    for j in range(len(lst)):
        plt.text(Y[j, 0], Y[j, 1], dic[y[j]], fontdict={'weight': 'bold', 'size': 9})
    plt.savefig(os.path.join(save_loc, '{}_embedding_umap.pdf'.format(type)), format='pdf')
    print('{} plot is saved...'.format(type))
    #plt.show()

def main():
    print('load files...')
    cell_X = load_dict('cell', cells)
    plot_tsne(CELL_NAME, cell_X, 'cell', cells)
    #y = [i for i in cells]
    assay_X = load_dict('assay', assays)
    plot_tsne(ASSAY_NAME, assay_X, 'assay', assays)
    #y = [i for i in assays]



if __name__ == '__main__':
    main()