
import os
import sys

il = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/input/"
al = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/results_jaspar/all_promoter_background/"
rl = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/results_jaspar/random_background/"
aml = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/results_jaspar/all_promoter_background/Match/"
rml = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/results_jaspar/random_background/Match/"
inList = ["LPS_LPS_DOWN", "LPS_LPS_UP", "LPS_n_DOWN", "LPS_n_UP", "n_LPS_DOWN", "n_LPS_UP"]

al = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/extra/all_promoter_background/"
rl = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/extra/random_background/"
aml = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/extra/all_promoter_background/Match/"
rml = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/extra/random_background/Match/"
inList = ["LPS_LPS_LPS_n_DOWN", "LPS_LPS_LPS_n_UP"]

for inName in inList:
  fml = al+inName+"/Match/"
  os.system("mkdir -p "+fml)
  os.system("cp "+il+inName+"_allprom.bb "+fml+"random_regions.bb") # Random regions
  os.system("cp "+aml+inName+"_mpbs.bb "+fml+"random_regions_mpbs.bb") # Random regions MPBS
  os.system("cp "+rml+inName+"_mpbs.bb "+fml+inName+"_mpbs.bb") # Foreground MPBS

#os.system("rm -rf "+aml)


