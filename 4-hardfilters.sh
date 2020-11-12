$JAVA -Xmx24g -jar $GATK \
	-R /mnt/isilon/devoto_lab/GrCh37/hs37d5.fa \
	-T VariantFiltration \
	-V NA04_GATK3_Calls.vcf \
	-o NA04_GATK3_Calls.hardFilters.vcf  \
	--clusterWindowSize 10 \
	--filterExpression "QD < 4.0 || DP < 11 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0" \
	--filterName "LowQual"  \
	--genotypeFilterExpression "DP<11 " \
	--genotypeFilterName "LowDP"