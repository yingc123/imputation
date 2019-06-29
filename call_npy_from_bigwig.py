import os


Valid_file = ['C03M02', 'C34M02', 'C50M02', 'C23M03', 'C27M03', 'C17M04', 'C23M07', 'C32M08', 'C46M10', 'C32M12',
              'C27M13', 'C04M16', 'C12M16', 'C48M16', 'C10M17', 'C16M17', 'C24M17', 'C36M18', 'C46M18', 'C47M18',
              'C17M19', 'C09M20', 'C13M20', 'C32M20', 'C18M21', 'C25M21', 'C46M21', 'C02M22', 'C20M22', 'C45M22',
              'C27M24', 'C18M25', 'C24M25', 'C31M25', 'C23M26', 'C25M26', 'C27M26', 'C17M29', 'C29M29', 'C37M29',
              'C12M32', 'C17M32', 'C34M32', 'C23M34', 'C46M35']

for file in Valid_file:
    myCmd = 'python build_npy_from_bigwig.py ' \
            '/home/ying/Cluster/izkf/projects/ENCODEImputation/data_true/validation_data/{}.bigwig ' \
            '--out-npy-prefix /home/ying/Cluster/home/true_npy/{}'.format(file, file)
    os.system(myCmd)