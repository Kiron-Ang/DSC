import subprocess

# 1. Use curl to get the VCF file from the FTP site
# subprocess.run("curl -v --output all.vcf.gz ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/supporting/hd_genotype_chip/ALL.chip.omni_broad_sanger_combined.20140818.snps.genotypes.vcf.gz")

# 2. Extract the file on Windows using File Explorer

# 3. Get 101 RS numbers from the first additional file of this paper: https://doi.org/10.1186/1471-2156-10-45
rs_numbers = [
  "rs2230806", "rs2297404", "rs4149272", "rs2575875", "rs363717", "rs4148189", 
  "rs3806471", "rs6720173", "rs4131229", "rs4148211", "rs4148217", "rs11887534", 
  "rs6709904", "rs11216158", "rs670", "rs2727784", "rs613808", "rs5082", "rs1263177", 
  "rs5104", "rs675", "rs5092", "rs5110", "rs5090", "rs662799", "rs3135506", "rs679899", 
  "rs934197", "rs1042031", "rs676210", "rs693", "rs4520", "rs5128", "rs2542051", 
  "rs2542052", "rs2854116", "rs2854117", "rs405509", "rs7412", "rs429358", "rs2499856", 
  "rs1205", "rs1417938", "rs11786580", "rs10957056", "rs2241883", "rs3891700", 
  "rs1799883", "rs6857641", "rs10034661", "rs780094", "rs7169744", "rs6078", "rs6084", 
  "rs8034802", "rs1973028", "rs2276269", "rs6507931", "rs2000813", "rs1801177", "rs268", 
  "rs328", "rs1800590", "rs715948", "rs1799986", "rs1800191", "rs982424", "rs1800591", 
  "rs3811800", "rs11771443", "rs743507", "rs1800783", "rs1799983", "rs1284300", 
  "rs1052700", "rs894160", "rs2289487", "rs2304795", "rs1800206", "rs135549", "rs3856806", 
  "rs10865710", "rs12497191", "rs1801282", "rs4235308", "rs2946385", "rs2970869", 
  "rs3736265", "rs4697046", "rs3774923", "rs5888", "rs4765181", "rs4238001", "rs701106", 
  "rs10846748", "rs3924313", "rs61932577", "rs4460661", "rs3813790", "rs544543", "rs505717"
]

# 4. Get 150 Puerto Rican sample names from the IGSR: https://www.internationalgenome.org/data-portal/sample
sample_names = [
  "HG00554", "HG00733", "HG00738", "HG00555", "HG01243", "HG01248", "HG01286", "HG01301", 
  "HG00637", "HG01104", "HG01109", "HG00732", "HG01111", "HG00737", "HG01242", "HG01247", 
  "HG00740", "HG01053", "HG01058", "HG01103", "HG01060", "HG01108", "HG01161", "HG01110", 
  "HG01173", "HG01178", "HG01192", "HG01197", "HG01200", "HG01305", "HG01205", "HG01312", 
  "HG01072", "HG01324", "HG01077", "HG01084", "HG01089", "HG01096", "HG01064", "HG01414", 
  "HG01069", "HG01071", "HG01083", "HG01088", "HG01090", "HG01095", "HG01172", "HG01177", 
  "HG01325", "HG01184", "HG01189", "HG01191", "HG01204", "HG01052", "HG01394", "HG01402", 
  "HG01393", "HG01398", "HG01413", "HG00553", "HG00551", "HG00638", "HG00640", "HG00731", 
  "HG00736", "HG01102", "HG01107", "HG01162", "HG01167", "HG01174", "HG01198", "HG01206", 
  "HG01302", "HG00743", "HG01326", "HG01049", "HG01051", "HG01056", "HG01063", "HG00734", 
  "HG01068", "HG01100", "HG01070", "HG01105", "HG01075", "HG01082", "HG01087", "HG01094", 
  "HG01099", "HG00739", "HG01241", "HG00741", "HG01047", "HG01054", "HG01061", "HG01066", 
  "HG01164", "HG01073", "HG01169", "HG01080", "HG01171", "HG01085", "HG01176", "HG01092", 
  "HG01183", "HG01097", "HG01188", "HG01249", "HG01190", "HG01195", "HG00642", "HG01311", 
  "HG01323", "HG01392", "HG01397", "HG01395", "HG01403", "HG01415", "HG01405", "HG01412", 
  "HG00552", "HG00742", "HG01048", "HG01050", "HG01055", "HG00735", "HG01303", "HG01308", 
  "HG01322", "HG01327", "HG00639", "HG00641", "HG01396", "HG01168", "HG01170", "HG01175", 
  "HG01182", "HG01187", "HG01199", "HG01062", "HG01067", "HG01074", "HG01079", "HG01081", 
  "HG01086", "HG01098", "HG01101", "HG01106", "HG01404", "HG01411"
]

# 5. Create a smaller VCF file by only keeping rows in the original VCF that correspond to one of the 101 RS numbers
"""
input = open("all.vcf", "r")
output = open("small.vcf", "w")

print("Creating small.vcf. . .")

while rs_numbers:
  vcf_line = next(input).split("\t")
  if vcf_line[0].isdigit():
    if vcf_line[2] in rs_numbers:
      print(vcf_line[2])
      rs_numbers.remove(vcf_line[2])
      output.write("\t".join(vcf_line))
  elif vcf_line[0] == "#CHROM":
    output.write("\t".join(vcf_line))

input.close()
output.close()
"""

# 6. Create two VCF files by separating Puerto Ricans from non-Puerto Ricans using the sample names
input = open("small.vcf", "r")
output_one = open("puerto_ricans.vcf", "w")
output_two = open("others.vcf", "w")

print("Creating puerto_ricans.vcf and others.vcf. . .")

lines = input.readlines()

header = lines[0].strip().split("\t")

puerto_ricans = []
others = []

for value in header[9:]:
  if value in sample_names:
    puerto_ricans.append(header.index(value))
  else:
    others.append(header.index(value))

for line in lines:

  line = line.strip().split("\t")

  output_one.write("\t".join(line[0:9]))
  output_one.write("\t")
  
  output_two.write("\t".join(line[0:9]))
  output_two.write("\t")

  temp = [line[i] for i in puerto_ricans]
  output_one.write("\t".join(temp))
  output_one.write("\n")

  temp = [line[i] for i in others]
  output_two.write("\t".join(temp))
  output_two.write("\n")

input.close()
output_one.close()
output_two.close()