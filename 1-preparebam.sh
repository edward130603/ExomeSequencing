#!/bin/bash
#$ -cwd
#$ -l mem_free=50G
#$ -l h_vmem=50G
#$ -V

/mnt/isilon/cbmi/variome/bin/Novoalign/3.03.01/novoalign \
         -d /mnt/isilon/cbmi/variome/reference/human/g1k_v37/human_g1k_v37.nix \
         -f /mnt/isilon/devoto_lab/ItalianExomes/Nov2016/FASTQ/Sample_NA04COAN/Sample_NA04COAN_r1.fastq.gz /mnt/isilon/devoto_lab/ItalianExomes/Nov2016/FASTQ/Sample_NA04COAN/Sample_NA04COAN_r2.fastq.gz \
         -i PE 220,80 -c 24 -k -t 15,4 -H 20 --softclip 20 --hlimit 7 -p 5,20 \
         -o SAM '@RG	ID:NA04COAN	PU:platform	LB:bar	PL:illumina	SM:NA04COAN' | $SAMBLASTER --addMateTags | $SAMTOOLS view -Sb - > NA04COAN.mdup.bam
/mnt/isilon/cbmi/variome/bin/Novoalign/3.03.01/novosort \
        -m 16G \
        -t /mnt/lustre/users/zhaoe/ \
        -i \
        -o NA04COAN.sorted.mdup.bam \
        -c 16 NA04COAN.mdup.bam