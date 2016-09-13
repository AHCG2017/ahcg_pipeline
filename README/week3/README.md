
##Week 3

#Install bedtolls

1.Download bedtools

``` {sh}
wget https://github.com/arq5x/bedtools2/releases/download/v2.25.0/bedtools-2.25.0.tar.gz 
```

2.Untar the file

``` {sh} 
tar -zxvf bedtools-2.25.0.tar.gz
```

3.Install bedtools

``` {sh}
cd bedtools2
make
```
#Adding a file to a repository from the command line

1.Stage the file for commit to your local repository.

```{sh}
git add <file name>
```
####To unstage a file

```{sh} 
git reset HEAD <file name>
```

2.Commit the tracked changes and prepar them to be pushed to a remote repository.

```{sh}
git commit –m ‘comments’
```

3.Push the changes in your local repository to GitHub.

```{sh}
git push origin master
```

#Extract reads mapping to BRCA1 from NA12878 HiSeq Exome dataset

1.Download the NA12878 HiSeq Exome datasets.

```{sh}
wget ftp://ftp-trace.ncbi.nih.gov/giab/ftp/data/NA12878/Garvan_NA12878_HG001_HiSeq_Exome/project.NIST_NIST7035_H7AP8ADXX_TAAGGCGA_2_NA12878.bwa.markDuplicates.bam
wget ftp://ftp-trace.ncbi.nih.gov/giab/ftp/data/NA12878/Garvan_NA12878_HG001_HiSeq_Exome/project.NIST_NIST7086_H7AP8ADXX_CGTACTAG_2_NA12878.bwa.markDuplicates.bam
wget ftp://ftp-trace.ncbi.nih.gov/giab/ftp/data/NA12878/Garvan_NA12878_HG001_HiSeq_Exome/project.NIST_NIST7086_H7AP8ADXX_CGTACTAG_1_NA12878.bwa.markDuplicates.bam
wget ftp://ftp-trace.ncbi.nih.gov/giab/ftp/data/NA12878/Garvan_NA12878_HG001_HiSeq_Exome/project.NIST_NIST7035_H7AP8ADXX_TAAGGCGA_2_NA12878.bwa.markDuplicates.bam
```
2.Use samtools to merge the four bam files.

```{sh}
samtools merge NA12878.bam project.NIST_NIST7035_H7AP8ADXX_TAAGGCGA_2_NA12878.bwa.markDuplicates.bam project.NIST_NIST7035_H7AP8ADXX_TAAGGCGA_2_NA12878.bwa.markDuplicates.bam project.NIST_NIST7086_H7AP8ADXX_CGTACTAG_1_NA12878.bwa.markDuplicates.bam project.NIST_NIST7086_H7AP8ADXX_CGTACTAG_2_NA12878.bwa.markDuplicates.bam
```

3.Use samtools to subset the bam file to the exonic regions corresponding to BRCA1. These regions are saved in BRCA1.bed.

```{sh}
samtools view -L BRCA1.bed -b -o output.bam NA12878.bam
```
4.Use bedtools to convert the bam file to a fastq file (We now extract the reads aligning to the region).

```{sh}
bedtools bamtofastq -i output.bam -fq BRCA1_r1.fq -fq2 BRCA1_r2.fq
```
