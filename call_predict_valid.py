from __future__ import print_function
import os
import sys
from configure import Valid_file, chrom_list

chrom = sys.argv[1]

# remember to change the model_loc and pred_loc in the Average_predict.py
for file in Valid_file[:1]:
    cell = file[:3]
    assay = file[3:]
    #for chrom in chrom_list[:-1]:
        #job_name = "{}{}{}".format(chrom[3:],cell, assay)
        #command = "sbatch -J " + job_name + " -o " + "./cluster_out/" + job_name + "_out.txt -e" + \
        #  "./cluster_err/" + job_name + "_err.txt -t  20:00:00 --mem  20G --partition=c18m "
    command = "python Average_predict.py -c {} -l {} -a {}".format(chrom, cell, assay)
    os.system(command)





