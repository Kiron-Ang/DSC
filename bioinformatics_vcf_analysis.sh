#!/bin/bash

puerto_rican_ids="HG00554 HG00733 HG00738 HG00555 HG01243 HG01248 HG01286 HG01301 HG00637 HG01104 HG01109 HG00732 HG01111 HG00737 HG01242 HG01247 HG00740 HG01053 HG01058 HG01103 HG01060 HG01108 HG01161 HG01110 HG01173 HG01178 HG01192 HG01197 HG01200 HG01305 HG01205 HG01312 HG01072 HG01324 HG01077 HG01084 HG01089 HG01096 HG01064 HG01414 HG01069 HG01071 HG01083 HG01088 HG01090 HG01095 HG01172 HG01177 HG01325 HG01184 HG01189 HG01191 HG01204 HG01052 HG01394 HG01402 HG01393 HG01398 HG01413 HG00553 HG00551 HG00638 HG00640 HG00731 HG00736 HG01102 HG01107 HG01162 HG01167 HG01174 HG01198 HG01206 HG01302 HG00743 HG01326 HG01049 HG01051 HG01056 HG01063 HG00734 HG01068 HG01100 HG01070 HG01105 HG01075 HG01082 HG01087 HG01094 HG01099 HG00739 HG01241 HG00741 HG01047 HG01054 HG01061 HG01066 HG01164 HG01073 HG01169 HG01080 HG01171 HG01085 HG01176 HG01092 HG01183 HG01097 HG01188 HG01249 HG01190 HG01195 HG00642 HG01311 HG01323 HG01327 HG00639 HG00641 HG01396 HG01168 HG01170 HG01175 HG01182 HG01187 HG01199 HG01062 HG01067 HG01074 HG01079 HG01081 HG01086 HG01098 HG01101 HG01106 HG01404 HG01411"

header=$(grep -m 1 '^#CHROM' all.vcf)

pr_col="1,2,3,4,5,6,7,8,9"
other_col=""
seen_columns=()  # Array to keep track of columns already added to other_col

# Convert puerto_rican_ids into a hash set for faster lookup
declare -A puerto_rican_ids_set
for id in $puerto_rican_ids; do
  puerto_rican_ids_set[$id]=1
done

for label in $header; do
  ((num_col++))
  # Check if the label is in the puerto_rican_ids_set
  if [[ ${puerto_rican_ids_set[$label]} ]]; then
    pr_col="$pr_col,$num_col"
    echo PR: $num_col
    # Remove the matched ID from the set to avoid reprocessing
    unset puerto_rican_ids_set[$label]
  else
    # Add to other_col if it's not already there
    if [[ ! " ${seen_columns[@]} " =~ " ${num_col} " ]]; then
      other_col="$other_col,$num_col"
      seen_columns+=($num_col)  # Add the column number to the seen_columns array
      echo NOT PR: $num_col
    fi
  fi
done

other_col=${other_col:1}  # Remove the initial comma

echo "$header" > header.txt

cut -f "$pr_col" header.txt > pr.vcf
cut -f "$pr_col" small.vcf >> pr.vcf

cut -f "$other_col" header.txt > not_pr.vcf
cut -f "$other_col" small.vcf >> not_pr.vcf

echo SCRIPT END