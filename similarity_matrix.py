import numpy as np
import os

loc = '/home/ying/Cluster/izkf/projects/ENCODEImputation/local/NPYFiles/training_data'

chrom_list = ['chr1', 'chr2', 'chr3',
              'chr4', 'chr5', 'chr6',
              'chr7', 'chr8', 'chr9',
              'chr10', 'chr11', 'chr12',
              'chr13', 'chr14', 'chr15',
              'chr16', 'chr17', 'chr18',
              'chr19', 'chr20', 'chr21',
              'chr22', 'chrX']

Train_file=['C02M01', 'C20M01', 'C35M01', 'C45M01', 'C02M02', 'C05M02', 'C06M02', 'C07M02', 'C08M02', 'C11M02', 'C15M02',
            'C16M02', 'C17M02', 'C18M02', 'C19M02', 'C20M02', 'C21M02', 'C22M02', 'C23M02', 'C24M02', 'C27M02', 'C28M02',
            'C30M02', 'C32M02', 'C33M02', 'C35M02', 'C39M02', 'C40M02', 'C41M02', 'C42M02', 'C43M02', 'C44M02', 'C45M02',
            'C46M02', 'C47M02', 'C48M02', 'C49M02', 'C51M02', 'C12M03', 'C17M03', 'C18M03', 'C24M03', 'C25M03', 'C31M03',
            'C34M03', 'C46M03', 'C23M04', 'C27M04', 'C32M04', 'C46M04', 'C23M05', 'C17M06', 'C23M06', 'C27M06', 'C32M06',
            'C46M06', 'C17M07', 'C27M07', 'C32M07', 'C46M07', 'C17M08', 'C23M08', 'C27M08', 'C17M09', 'C23M09', 'C17M10',
            'C23M10', 'C27M10', 'C32M10', 'C31M11', 'C18M12', 'C23M12', 'C27M12', 'C46M12', 'C17M13', 'C18M13', 'C23M13',
            'C32M13', 'C46M13', 'C23M14', 'C27M14', 'C32M14', 'C17M15', 'C18M15', 'C01M16', 'C02M16', 'C03M16', 'C09M16',
            'C10M16', 'C13M16', 'C17M16', 'C18M16', 'C20M16', 'C23M16', 'C24M16', 'C25M16', 'C27M16', 'C32M16', 'C34M16',
            'C36M16', 'C37M16', 'C38M16', 'C46M16', 'C47M16', 'C49M16', 'C50M16', 'C03M17', 'C04M17', 'C07M17', 'C09M17',
            'C12M17', 'C13M17', 'C17M17', 'C18M17', 'C20M17', 'C23M17', 'C25M17', 'C27M17', 'C29M17', 'C32M17', 'C36M17',
            'C46M17', 'C02M18', 'C03M18', 'C04M18', 'C07M18', 'C09M18', 'C10M18', 'C12M18', 'C13M18', 'C14M18', 'C16M18',
            'C17M18', 'C18M18', 'C20M18', 'C23M18', 'C24M18', 'C25M18', 'C27M18', 'C29M18', 'C31M18', 'C32M18', 'C34M18',
            'C48M18', 'C18M19', 'C23M19', 'C27M19', 'C32M19', 'C46M19', 'C02M20', 'C03M20', 'C04M20', 'C10M20', 'C12M20',
            'C14M20', 'C17M20', 'C18M20', 'C20M20', 'C23M20', 'C24M20', 'C25M20', 'C27M20', 'C29M20', 'C31M20', 'C34M20',
            'C36M20', 'C46M20', 'C12M21', 'C17M21', 'C23M21', 'C24M21', 'C27M21', 'C31M21', 'C32M21', 'C34M21', 'C03M22',
            'C04M22', 'C05M22', 'C06M22', 'C07M22', 'C08M22', 'C09M22', 'C10M22', 'C12M22', 'C13M22', 'C16M22', 'C17M22',
            'C18M22', 'C22M22', 'C23M22', 'C24M22', 'C26M22', 'C27M22', 'C29M22', 'C31M22', 'C32M22', 'C34M22', 'C36M22',
            'C37M22', 'C46M22', 'C47M22', 'C48M22', 'C50M22', 'C51M22', 'C17M23', 'C18M23', 'C23M23', 'C17M24', 'C18M24',
            'C23M24', 'C32M24', 'C46M24', 'C12M25', 'C17M25', 'C23M25', 'C25M25', 'C34M25', 'C46M25', 'C12M26', 'C13M26',
            'C14M26', 'C17M26', 'C18M26', 'C24M26', 'C29M26', 'C31M26', 'C32M26', 'C36M26', 'C46M26', 'C23M27', 'C24M27',
            'C34M28', 'C02M29', 'C03M29', 'C04M29', 'C09M29', 'C12M29', 'C13M29', 'C14M29', 'C18M29', 'C20M29', 'C23M29',
            'C24M29', 'C27M29', 'C32M29', 'C34M29', 'C36M29', 'C45M29', 'C46M29', 'C18M30', 'C46M31', 'C23M32', 'C24M32',
            'C25M22', 'C25M32', 'C17M33', 'C18M33', 'C23M33', 'C17M34', 'C18M34', 'C27M34', 'C32M34', 'C46M34', 'C17M35',
            'C23M35', 'C27M35', 'C32M35']

def gwcorr(y_true, y_pred):
    return np.corrcoef(y_true, y_pred)[0, 1]

def dict_to_arr(d, chroms):
    """Concat vectors in d
    """
    result = []
    for c in chroms:
        result.extend(d[c])
    return np.array(result)

def main():

    m = []
    for i in range(len(Train_file)):
        for j in range(i, len(Train_file)):
            file_1_dict = np.load(os.path.join(loc, '{}.npy'.format(Train_file[i])), allow_pickle = True).tolist()
            file_2_dict = np.load(os.path.join(loc, '{}.npy'.format(Train_file[j])), allow_pickle = True).tolist()
            #print(file_1_dict)
            file_1 = dict_to_arr(file_1_dict, chrom_list)
            file_2 = dict_to_arr(file_2_dict, chrom_list)
            #print(file_1)
            corr=gwcorr(file_1, file_2)
            print('the correlation coefficient between {} and {} is {}'.format(Train_file[i], Train_file[j], str(corr)))
            m.append(corr)
        #print('{} is totally compared...'.format(assays[i]))
    print(m)

if __name__ == '__main__':
    main()