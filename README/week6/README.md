#Assignment5
## Variant Quality Score Recalibration (VQSR)

###VariantRecalibrator 
Create a Gaussian mixture model by looking at the distribution of annotation values over a high quality subset of the input call set, and then scoring all input variants according to the model.

1.Check the recalibrating SNPs in exome data at [GATK Variant Recalibrator] (https://software.broadinstitute.org/gatk/gatkdocs/org_broadinstitute_gatk_tools_walkers_variantrecalibration_VariantRecalibrator.php). 

2.Download the resource files: 
[Hapmap]
(http://vannberg.biology.gatech.edu/data/ahcg2016/gatk/hapmap_3.3.hg19.sites.vcf.gz)
[Hapmap Index]
(http://vannberg.biology.gatech.edu/data/ahcg2016/gatk/hapmap_3.3.hg19.sites.vcf.gz.tbi)
[Omni]
(http://vannberg.biology.gatech.edu/data/ahcg2016/gatk/1000G_omni2.5.hg19.sites.vcf.gz)
[Omni Index]
(http://vannberg.biology.gatech.edu/data/ahcg2016/gatk/1000G_omni2.5.hg19.sites.vcf.gz.tbi)
[1000G Phase I]
(http://vannberg.biology.gatech.edu/data/ahcg2016/gatk/1000G_phase1.snps.high_confidence.hg19.sites.vcf.gz)
[1000G Phase I Index]
(http://vannberg.biology.gatech.edu/data/ahcg2016/gatk/1000G_phase1.snps.high_confidence.hg19.sites.vcf.gz.tbi)
[dbSNP]
(http://vannberg.biology.gatech.edu/data/ahcg2016/gatk/dbsnp.vcf.gz)
[dbSNP Index]
(http://vannberg.biology.gatech.edu/data/ahcg2016/gatk/dbsnp.vcf.gz.tbi).


3.Download the variants file.

```{sh}
wget http://vannberglab.biology.gatech.edu/data/ahcg2016/vcf/NA12878_variants.vcf
```

4.Run the [GATK Variant Recalibrator] (https://software.broadinstitute.org/gatk/gatkdocs/org_broadinstitute_gatk_tools_walkers_variantrecalibration_VariantRecalibrator.php)

```{sh}
../pipeline/jre1.8.0_101/bin/java -jar ../pipeline/GenomeAnalysisTK.jar \
   -T VariantRecalibrator \
   -R ../pipeline/resources/hg19.fa \
   -input NA12878_variants.vcf \
   -resource:hapmap,known=false,training=true,truth=true,prior=15.0 hapmap_3.3.hg19.sites.vcf.gz \
   -resource:1000G,known=false,training=true,truth=false,prior=12.0 1000G_omni2.5.hg19.sites.vcf.gz \
   -resource:1000G,known=false,training=true,truth=false,prior=10.0 1000G_phase1.snps.high_confidence.hg19.sites.vcf.gz \
   -resource:dbsnp,known=true,training=false,truth=false,prior=2.0 dbsnp.vcf.gz \
   -an DP -an QD -an MQ -an FS -an SOR\
   -mode SNP \
   -recalFile output.recal \
   -tranchesFile output.tranches 

```
The options for -an match the fields in the vcf file, never exclude DP= depth coverage. 

###ApplyRecalibration
 
The second step is filtering variants based on score cutoffs identified in the first pass.
 
1.Check example for filtering SNPs [GATK ApplyRecalibration] (https://software.broadinstitute.org/gatk/gatkdocs/org_broadinstitute_gatk_tools_walkers_variantrecalibration_ApplyRecalibration.php)

2.Use the ApplyRecalibration on the output.recal obtained in 3.

```{sh}
../pipeline/jre1.8.0_101/bin/java -jar ../pipeline/GenomeAnalysisTK.jar \
   -T ApplyRecalibration \
   -R  ../pipeline/resources/genome/hg19.fa \
   -input output.recal \
	 -tranchesFile output.tranches \
   -recalFile output.recal \
   -mode SNP \
   -o output.recalibrated.filtered.vcf
```
 
 The output of the assignment is output.recalibrated.filtered.vcf 

 
