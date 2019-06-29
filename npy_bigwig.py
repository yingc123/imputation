import argparse
import numpy as np
import os
from configure import blacklist_dict, chrom_list

'''
python npy_bigwig.py -c chr18 -n C03M02
remember to change npy_loc, big_loc and bed_loc each time
'''

npy_loc = '/home/ying/Cluster/izkf/projects/ENCODEImputation/local/NPYFiles/var_cross_cell'
big_loc = '/home/ying/Cluster/izkf/projects/ENCODEImputation/local/BigWigFiles/var_cross_cell'
bed_loc = '/home/ying/Cluster/izkf/projects/ENCODEImputation/local/BigWigFiles/var_cross_cell'

def parse_arguments():
    parser = argparse.ArgumentParser()
    #parser.add_argument('-c', '--chrom', type=str)
    parser.add_argument('-n', '--name', type=str)

    return parser.parse_args()

# read params
args = parse_arguments()

def writefile(fsub, fwrite, fnpy, chrom):
    step = 0
    for line in fsub:
        l = line.split('\t')
        if l[0] == chrom:
            fwrite.write(l[0] + '\t' + l[1] + '\t' + l[2] + '\t' + str(fnpy[step]) + '\n')
            step += 1
        else:
            pass
    print(step)

def writeblack(fsub, fwrite, fnpy, blackpart, chrom):
    #blackpart is a list, the corresponding chrom with blacklist part, * 25 is needed
    step = 0
    for line in fsub:
        l = line.split('\t')
        c = l[0]
        s = l[1]
        e = l[2]
        if c == chrom:
            if (int(s)//25 in blackpart) & (int(s)//25 in blackpart):
                # if the same, keep the original value 0
                fwrite.write(line)

            else:
                # else append the value from npy
                fwrite.write(c + '\t' + s + '\t' + e + '\t' + str(fnpy[step]) + '\n')
                step += 1
        else:
            pass
    print(step)

def dict_to_arr(d, chroms):
    """Concat vectors in d
    """
    result = []
    for c in chroms:
        result.extend(d[c])
    return np.array(result)

def main():
    #read template.bedgraph
    for chrom in chrom_list:
        fsub = open('submission_template.bedgraph', 'r')
        fwrite = open(os.path.join(bed_loc, '{}_{}.bedgraph'.format(args.name, chrom)), 'w')
        fnpy_dict = np.load(os.path.join(npy_loc, '{}.npy'.format(args.name)), allow_pickle=True).tolist()
        fnpy_arr = fnpy_dict[chrom]
        if chrom in blacklist_dict:
            writeblack(fsub, fwrite, fnpy_arr, blacklist_dict[chrom],chrom)
            print('{} is writed to bed...'.format(chrom))
        else:
            writefile(fsub, fwrite, fnpy_arr, chrom)
            print('{} is writed to bed...'.format(chrom))

if __name__ == '__main__':
    main()
