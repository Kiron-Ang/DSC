#!/bin/bash
# This Bash script contains code for
# analyzing a VCF file from the 1000 genomes project.
# This script was authored by Kiron Ang on
# December 2, 2024 for a bioinformatics final project.
# This script is intended for usage on a Windows
# operating system with Git Bash by running
# bash bioinformatics_vcf_analysis.sh

<<'COMMENT'
echo COUNTING LINES. . .
wc -l *.vcf

echo PRINTING HEAD. . .
head *.vcf

echo PRINTING TAIL. . .
tail *.vcf

echo PRINTING HEADER LINE. . .
grep "^#CHROM" *.vcf

COMMENT

echo COUNTING NUMBER OF INDIVIDUALS. . .
grep "^#CHROM" *.vcf | awk '{print NF-9}'

echo SCRIPT END