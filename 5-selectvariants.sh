$JAVA -Xmx12g -jar $GATK \
	-R /mnt/isilon/devoto_lab/GrCh37/hs37d5.fa \
	-T SelectVariants \
	-V ItalianExomes_fb_2-27.hardfilter.biallelic.vcf \
	-sn NA04COAN \
	-sn NA04COVI \
	-sn NA04COGI \
	-sn NA04GIFI \
	-env \
	-o NA04_3-3.vcf