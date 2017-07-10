
import os
import sys

il = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment_m2c_macrophage/input/"
al = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment_m2c_macrophage/results/all_promoter_background/"
rl = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment_m2c_macrophage/results/random_background/"
aml = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment_m2c_macrophage/results/all_promoter_background/Match/"
rml = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment_m2c_macrophage/results/random_background/Match/"
inList = ["M2c_macrophage_down", "M2c_macrophage_up"]

for inName in inList:
  fml = al+inName+"/Match/"
  os.system("mkdir -p "+fml)
  os.system("cp "+il+inName+"_allprom.bb "+fml+"random_regions.bb") # Random regions
  os.system("cp "+aml+inName+"_mpbs.bb "+fml+"random_regions_mpbs.bb") # Random regions MPBS
  os.system("cp "+rml+inName+"_mpbs.bb "+fml+inName+"_mpbs.bb") # Foreground MPBS

#os.system("rm -rf "+aml)


