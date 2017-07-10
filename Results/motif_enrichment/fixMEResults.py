
# Import
import os
import sys
from glob import glob

# Parameters
rLoc = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/extra/random_background/"
aLoc = "/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/extra/all_promoter_background/"

# Moving random background out
os.system("mv "+rLoc+"ME_random_background/*/ "+rLoc)
os.system("rm "+rLoc+"ME_random_background/")

# Moving all prom out
os.system("mkdir -p "+aLoc+"Match/")
os.system("mv "+aLoc+"*/ "+aLoc+"Match/")
os.system("mv "+aLoc+"*/*/*/*/ "+aLoc)

# Fixing HTML logo
for inFileName in glob(rLoc+"*/*.html")+glob(aLoc+"*/*.html"):
  os.system("sed -i 's/\/home\/eg474423\/rgtdata\/logos\/jaspar_vertebrates\//..\/..\/jaspar_logo\//g' "+inFileName)
  os.system("sed -i 's/..\/fig\//..\/..\/jaspar_logo\//g' "+inFileName)

# Fixing HTML link
for inFileName in glob(rLoc+"*/*.html"):
  os.system("sed -i 's/file:\/\/\/work\/eg474423\/eg474423_Projects\/trunk\/Tlf4Erythroid\/Results\/motif_enrichment\/results_jaspar\/random_background\/ME_random_background\//..\//g' "+inFileName)


# Fixing HTML link
#for inFileName in glob(aLoc+"*/*.html"):
#  os.system("sed -i 's/<a class=\"pure-button\".*<\/a>/<a class=\"pure-button\" href=\"..\/LPS_n_UP\/randtest_statistics.html\">LPS_n_UP<\/a>\\n<a class=\"pure-button\" href=\"..\/n_LPS_DOWN\/randtest_statistics.html\">n_LPS_DOWN<\/a>\\n<a class=\"pure-button\" href=\"..\/LPS_LPS_UP\/randtest_statistics.html\">LPS_LPS_UP<\/a>\\n<a class=\"pure-button\" href=\"..\/LPS_LPS_DOWN\/randtest_statistics.html\">LPS_LPS_DOWN<\/a>\\n<a class=\"pure-button\" href=\"..\/n_LPS_UP\/randtest_statistics.html\">n_LPS_UP<\/a>\\n<a class=\"pure-button\" href=\"..\/LPS_n_DOWN\/randtest_statistics.html\">LPS_n_DOWN<\/a>\\n/g' "+inFileName)

# Fixing GO ontology
for inFileName in glob(rLoc+"*/*.html")+glob(aLoc+"*/*.html"):
  os.system("sed -i 's/,/+/g' "+inFileName)


