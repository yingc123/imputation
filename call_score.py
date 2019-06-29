import os
import numpy as np


Valid_file = ['C03M02', 'C34M02', 'C50M02', 'C23M03', 'C27M03', 'C17M04', 'C23M07', 'C32M08', 'C46M10', 'C32M12',
              'C27M13', 'C04M16', 'C12M16', 'C48M16', 'C10M17', 'C16M17', 'C24M17', 'C36M18', 'C46M18', 'C47M18',
              'C17M19', 'C09M20', 'C13M20', 'C32M20', 'C18M21', 'C25M21', 'C46M21', 'C02M22', 'C20M22', 'C45M22',
              'C27M24', 'C18M25', 'C24M25', 'C31M25', 'C23M26', 'C25M26', 'C27M26', 'C17M29', 'C29M29', 'C37M29',
              'C12M32', 'C17M32', 'C34M32', 'C23M34', 'C46M35']



#bootstrapped_label = np.load('bootstrapped_label.npy', allow_pickle = True)
#bootstrapped_label_dict = bootstrapped_label[0]



Bootstrap1 ='chr10,chr11,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr3,chr4,chr5,chr6,chr7,chr8,chr9,chrX'
Bootstrap2 ='chr1,chr10,chr11,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr20,chr21,chr22,chr3,chr4,chr5,chr6,chr7,chr8,chr9,chrX'
Bootstrap3 ='chr1,chr10,chr11,chr12,chr13,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr22,chr4,chr5,chr6,chr7,chr8,chr9,chrX'
Bootstrap4 ='chr1,chr10,chr11,chr12,chr14,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr22,chr3,chr5,chr6,chr7,chr8,chr9,chrX'
Bootstrap5 ='chr1,chr10,chr11,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr22,chr3,chr4,chr6,chr7,chr8,chr9,chrX'
Bootstrap6 ='chr1,chr11,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr22,chr3,chr4,chr5,chr7,chr8,chr9,chrX'
Bootstrap7 ='chr1,chr10,chr11,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr22,chr3,chr4,chr5,chr6,chr9,chrX'
Bootstrap8 ='chr1,chr10,chr11,chr12,chr13,chr14,chr16,chr17,chr18,chr19,chr2,chr21,chr22,chr3,chr4,chr5,chr6,chr7,chr8,chrX'
Bootstrap9 ='chr1,chr10,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr22,chr3,chr4,chr5,chr6,chr7,chr8,chr9'
Bootstrap10 ='chr1,chr10,chr11,chr12,chr13,chr14,chr15,chr19,chr2,chr20,chr22,chr3,chr4,chr5,chr6,chr7,chr8,chr9,chrX'

team = 'Average'
submission_id = 20
for file in Valid_file:

    myCmd = 'python score.py /home/ying/Cluster/izkf/projects/ENCODEImputation/local/NPYFiles/evaluation_data/average_activity/{}.npy /home/ying/Cluster/izkf/projects/ENCODEImputation/local/NPYFiles/validation_data/{}.npy  ' \
        '--bootstrap-chrom  {} {} {} {} {} {} {} {} {} {}   ' \
        '--var-npy /home/ying/Cluster/izkf/projects/ENCODEImputation/local/NPYFiles/var_cross_cell/{}.npy  ' \
        '--out-file  /home/ying/Cluster/izkf/projects/ENCODEImputation/report/Round1Score/Average/{}_output_Average.tsv ' \
            ' --cell  {}  --assay  {}  -t {}  -s {}'\
    .format(file, file, Bootstrap1, Bootstrap2, Bootstrap3, Bootstrap4, Bootstrap5, Bootstrap6, Bootstrap7, Bootstrap8, Bootstrap9, Bootstrap10, file[3:], file, file[:3], file[3:], team, submission_id)
    os.system(myCmd)