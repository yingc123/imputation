python build_var_npy.py  /home/ying/Cluster/izkf/projects/ENCODEImputation/local/NPYFiles/training_data/C46M31.npy   --out-npy-prefix /home/ying/Cluster/izkf/projects/ENCODEImputation/local/NPYFiles/var_cross_cell/M31


python build_npy_from_bigwig.py  /home/ying/Cluster/izkf/projects/ENCODEImputation/local/BigWigFiles/evaluation_data/average_activity/C23M07.bigwig --out-npy-prefix /home/ying/Cluster/home/average_npy/C23M07_average  --blacklist-file  /home/ying/PycharmProjects/test/imputation_challenge/annot/hg38/hg38.blacklist.bed.gz


python score.py /home/ying/Cluster/home/average_npy/C02M22.npy [TRUTH_NPY] \
    --bootstrapped-label-npy [BOOTSTRAP_LABEL_NPY] \
    --var-npy var_[ASSAY_OR_MARK_ID].npy
	--out-db-file [SCORE_DB_FILE] \
	--cell [CELL_ID] --assay [ASSAY_OR_MARK_ID] \
	-t [TEAM_ID_INT] -s [SUBMISSION_ID_INT] \
	--validated


python score.py /home/ying/Cluster/izkf/projects/ENCODEImputation/exp/Ying/Preditions/avocado/NPY_whole/C03M02.npy  /home/ying/Cluster/izkf/projects/ENCODEImputation/local/NPYFiles/validation_data/C03M02.npy  --var-npy /home/ying/Cluster/izkf/projects/ENCODEImputation/local/NPYFiles/var_cross_cell/M02.npy  --out-file /home/ying/Cluster/home/average_npy/out.txt  --cell  C03  --assay  M02  -t avocado_li  -s 0


python rank_cy.py /home/ying/PycharmProjects/test/imputation_challenge/round1.csv

python rank_cy.py  -c /hpcwork/izkf/projects/ENCODEImputation/report/Round1Rank/round1.csv -r /hpcwork/izkf/projects/ENCODEImputation/report/Round1Rank/rank.txt -a /hpcwork/izkf/projects/ENCODEImputation/report/Round1Rank/rank_all.txt

python score.py /hpcwork/izkf/projects/ENCODEImputation/exp/Ying/Preditions/avocado/NPY_whole/C03M02.npy \
                /hpcwork/izkf/projects/ENCODEImputation/local/NPYFiles/validation_data/C03M02.npy \
        --bootstrap-chrom   \
        chr10,chr11,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr3,chr4,chr5,chr6,chr7,chr8,chr9,chrX \
        chr1,chr10,chr11,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr20,chr21,chr22,chr3,chr4,chr5,chr6,chr7,chr8,chr9,chrX \
        chr1,chr10,chr11,chr12,chr13,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr22,chr4,chr5,chr6,chr7,chr8,chr9,chrX \
        chr1,chr10,chr11,chr12,chr14,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr22,chr3,chr5,chr6,chr7,chr8,chr9,chrX \
        chr1,chr10,chr11,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr22,chr3,chr4,chr6,chr7,chr8,chr9,chrX \
        chr1,chr11,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr22,chr3,chr4,chr5,chr7,chr8,chr9,chrX \
        chr1,chr10,chr11,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr22,chr3,chr4,chr5,chr6,chr9,chrX \
        chr1,chr10,chr11,chr12,chr13,chr14,chr16,chr17,chr18,chr19,chr2,chr21,chr22,chr3,chr4,chr5,chr6,chr7,chr8,chrX \
        chr1,chr10,chr12,chr13,chr14,chr15,chr16,chr17,chr18,chr19,chr2,chr20,chr21,chr22,chr3,chr4,chr5,chr6,chr7,chr8,chr9 \
        chr1,chr10,chr11,chr12,chr13,chr14,chr15,chr19,chr2,chr20,chr22,chr3,chr4,chr5,chr6,chr7,chr8,chr9,chrX \
        --var-npy /hpcwork/izkf/projects/ENCODEImputation/local/NPYFiles/var_cross_cell/M02.npy \
        --out-file  /hpcwork/izkf/projects/ENCODEImputation/report/Round1Score/Avo_embedding_pred/$1_output.tsv \
        --cell C03 --assay  M02  -t Avo_embedding_pred  -s 1070