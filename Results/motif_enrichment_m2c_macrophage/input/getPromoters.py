
# Import
import os
import sys

# Input
promLength = 1000
il = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment_m2c_macrophage/genes/"
ol = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment_m2c_macrophage/input/"
csFileName = "/home/eg474423/rgtdata/hg19/chrom.sizes"
allPromOriginalFileName = "/work/eg474423/eg474423_Projects/trunk/MesenchymalMethylation/Results/motif_enrichment/DE_genes/input/all_promoters_1000.bed"
inputFileList = ["M2c_macrophage_down", "M2c_macrophage_up"]
outputFileList = ["M2c_macrophage_down", "M2c_macrophage_up"]
outputMissList = ["M2c_macrophage_down_miss", "M2c_macrophage_up_miss"]

# Reading alias dictionary
aliasFileName = "/home/eg474423/rgtdata/hg19/alias.txt"
aliasFile = open(aliasFileName,"r")
aliasDict = dict()
for line in aliasFile:
  ll = line.strip().split("\t")
  for e in [ll[1]]+ll[2].split("&"): aliasDict[e.upper()] = ll[0].upper()
aliasFile.close()

# Reading gene list
geneFileName = "/home/eg474423/rgtdata/hg19/association_file.bed"
geneFile = open(geneFileName,"r")
allGenesDict = dict()
for line in geneFile:
  ll = line.strip().split("\t")
  try: allGenesDict[aliasDict[ll[3].upper()]] = ll
  except Exception: allGenesDict[ll[3].upper()] = ll
geneFile.close()

# Chromosome list
chrList = ["chr"+str(e) for e in range(1,23)+["X"]]

for i in range(0,len(inputFileList)):

  inputFileName = il+inputFileList[i]+".txt"
  outputFileName = ol+outputFileList[i]+".bedT"
  outputMissName = ol+outputMissList[i]+".txt"
  inputFile = open(inputFileName,"r")
  outputFile = open(outputFileName,"w")
  outputMiss = open(outputMissName,"w")
  inputFile.readline()

  for line in inputFile:

    g = line.strip().split(".")[0]
    geneList = [g] + g.split("-")

    for gene in geneList:

      try:
        region = allGenesDict[aliasDict[gene]]
        if(region[0] not in chrList): 1/0
        if(region[5] == "+"):
          p1 = str(int(region[1])-promLength)
          p2 = str(int(region[1])+1)
        else:
          p1 = str(int(region[2])-1)
          p2 = str(int(region[2])+promLength)
        outputFile.write("\t".join([region[0],p1,p2])+"\n")
      except Exception:
        outputMiss.write(gene+"\n")

  inputFile.close()
  outputFile.close()
  outputMiss.close()

  # Correcting output
  outputFileNameSort = ol+outputFileList[i]+"_sort.bed"
  outputFileNameFinal = ol+outputFileList[i]+".bed"
  outputFileNameFinalBB = ol+outputFileList[i]+".bb"
  os.system("sort -k1,1 -k2,2n "+outputFileName+" > "+outputFileNameSort)
  os.system("mergeBed -i "+outputFileNameSort+" > "+outputFileNameFinal)
  os.system("rm "+outputFileName+" "+outputFileNameSort)
  os.system("bedToBigBed "+outputFileNameFinal+" "+csFileName+" "+outputFileNameFinalBB)

  # Creating all_promoter
  allPromoterFileName = ol+outputFileList[i]+"_allprom.bed"
  allPromoterFileNameBB = ol+outputFileList[i]+"_allprom.bb"
  os.system("subtractBed -A -a "+allPromOriginalFileName+" -b "+outputFileNameFinal+" > "+allPromoterFileName)
  os.system("bedToBigBed "+allPromoterFileName+" "+csFileName+" "+allPromoterFileNameBB)


