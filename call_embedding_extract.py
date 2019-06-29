from __future__ import print_function


import os

chrom_list = ['chr1', 'chr2', 'chr3',
              'chr4', 'chr5', 'chr6',
              'chr7', 'chr8', 'chr9',
              'chr10', 'chr11', 'chr12',
              'chr13', 'chr14', 'chr15',
              'chr16', 'chr17', 'chr18',
              'chr19', 'chr20', 'chr21',
              'chr22', 'chrX']

for chrom in chrom_list[:-1]:
    #job_name = "{}_extract".format(chrom)
    #command = "sbatch -J " + job_name + " -o " + "./cluster_out/" + job_name + "_out.txt -e" + \
          #"./cluster_err/" + job_name + "_err.txt -t 120:00:00 --mem 100G --partition=c18m -A rwth 0233 "
    command = "python embedding_extract.py -c {}".format(chrom)
    os.system(command)
