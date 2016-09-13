##Week4

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