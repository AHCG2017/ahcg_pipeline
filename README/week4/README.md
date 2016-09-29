s ##Week4

#VCF for BRCA1 sample test

1.Go to the repository folder

2.Download and gunzip reads files

```{sh}
cd files
wget http://vannberg.biology.gatech.edu/data/reads_B1_27000x150bp_0S_0I_0D_0U_0N_1.fq.gz 
wget http://vannberg.biology.gatech.edu/data/reads_B1_27000x150bp_0S_0I_0D_0U_0N_2.fq.gz 
gunzip reads_B1_27000x150bp_0S_0I_0D_0U_0N_1.fq.gz 
gunzip reads_B1_27000x150bp_0S_0I_0D_0U_0N_2.fq.gz
rm reads_B1_27000x150bp_0S_0I_0D_0U_0N_1.fq.gz 
rm reads_B1_27000x150bp_0S_0I_0D_0U_0N_2.fq.gz 
```

2.Download the regerence genome

```{sh}
cd files 
wget http://vannberg.biology.gatech.edu/data/chr17.fa
```

3.Create dictonary file

```{sh}
cd pipeline
jre1.8.0_101/bin/java -jar picard.jar CreateSequenceDictionary R=../files/chr17.fa O=../files/chr17.dict
```

4.Create Bowtie index

```{sh}
cd pipeline
bowtie2-2.2.9/bowtie2-build ../files/chr17.fa ../files/chr17
```
5.Create Samtools fasta index

```{sh}
samtools index ../files/chr17.fa
```
6.Run the pipeline

```{sh}
cd script
python3 ahcg_pipeline.py -t ../pipeline/Trimmomatic-0.36/trimmomatic-0.36.jar -b  ../pipeline/bowtie2-2.2.9/bowtie2 -p ../pipeline/picard.jar -g ../pipeline/GenomeAnalysisTK.jar -i ../files/reads_B1_27000x150bp_0S_0I_0D_0U_0N_1.fq    ../files/reads_B1_27000x150bp_0S_0I_0D_0U_0N_2.fq -w ../files/chr17 -d ../pipeline/resources/dbsnp/dbsnp_138.hg19.vcf -r ../files/chr17.fa  -a ../pipeline/Trimmomatic-0.36/adapters/NexteraPE-PE.fa -o ../files/BRCA1_pipeline_output
```

#### variants.vcf shasum number: 00ab164b17f1b5150a59e7fa9c5b3f9797aac73a

#Find variants in common between pipeline and Genome in a Bottle project. 

1.Go to the repository folder

2.Download an Illumina kit to capture exomes from Illumuina website. Go to http://support.illumina.com/sequencing/sequencing_kits/nextera-rapid-capture-exome-kit/downloads.html and choose one kit beetween Nextera Rapid Capture Exome v1.2 and Nextera Rapid Capture Exome 

```{sh}
cd files
wget http://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/samplepreps_nextera/nexterarapidcapture/nexterarapidcapture_exome_targetedregions.bed
```

3.Download the variants found with our pipeline

```{sh}
wget http://vannberg.biology.gatech.edu/data/variants.vcf
```

4.Grab only the variants that are in exome regions of the .vcf file

```{sh}
bedtools intersect -wb -a nexterarapidcapture_exome_targetedregions.bed -b variants.vcf > exome_variants.vcf
```

5.Download all the variants found in the Genome in a Bottle project: go to https://github.com/genome-in-a-bottle/giab_latest_release, click on 'latest release for NA12878_HG001' and enter as a guest. Then, download and gunzip the variants file.

```{sh}
wget NA12878_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-Solid-10X_CHROM1-X_v3.3_highconf.vcf.gz
gunzip NA12878_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-Solid-10X_CHROM1-X_v3.3_highconf.vcf.gz
```
6.Run a python script (split_colomns_no_chr.py) to remove 'chr' from variants.vcf and save in exome_variants1.vcf

```{sh}
python split_colomns_no_chr.py ../files/variants.vcf > ../files/exome_variants1.vcf
```
7.Safe the common and not common variants in a file. When you see a '.' this means that the variant is not in common.

```{sh}
bedtools -wao intersect -a NA12878_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-Solid-10X_CHROM1-X_v3.3_highconf.vcf -b exome_variants1.vcf > not_and_common_variants
```
