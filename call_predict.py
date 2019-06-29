from __future__ import print_function

import os
from configure import Valid_file, Train_file, chrom_list

for file in Valid_file:
    cell = file[:3]
    assay = file[3:]
    for chr in chrom_list:
        chrom = chr
        job_name = "{}{}{}".format(chrom[3:],cell, assay)
        command1 = 'cd /home/ying/PycharmProjects/test/imputation_challenge'
        command2 =  'python Avocado_predict.py -c {} -l {}  -a {}'.format(chrom, cell, assay)
        #command = "sbatch -J " + job_name + " -o " + "./cluster_out/" + job_name + "_out.txt -e " + \
          #"./cluster_err/" + job_name + "_err.txt -t 120:00:00 --mem 100G -c 48 --partition=c18m -A rwth0233 "
        #command += "./avocado1.zsh "
        #os.system(command+" "+chrom+cell+assay)
        os.system(command1)
        print('Now is doing the {}{} for {}...'.format(cell, assay, chrom))
        os.system(command2)
