#!/usr/bin/env python

"""This script changes gaussian output files to xyz format"""


# Loads the sys to additional input in the line
# Loads the re(regualr expression) search function

import sys
import re

# Set global variables
start = 0
end = 0

# This comes from the input files
# Gives names to possible new files

for i in sys.argv[1:]:
  filename = i
  new = filename.split('.')[0]
  newfile = str(new) + ".xyz"

  # Open the original file in read mode
  # Create a new file with writing rights

  openold = open(filename,"r")
  opennew = open(newfile,"w")

  # Read the entire original file

  rline = openold.readlines()

  for i in range (len(rline)):
    if "Standard orientation:" in rline[i]:
        start = i

  for m in range (start + 5, len(rline)):
    if "---" in rline[m]:
        end = m
	break
  number_of_atoms=abs(end-start-5)
  print >>opennew, number_of_atoms
  print >>opennew

  # Conversion section

  for line in rline[start+5 : end] :
    words = line.split()
    word1 = int(words[1])
    word3 = str(words[3])
    if word1 == 17 :
        word1 = "Cl"
    elif word1 == 9 :
        word1 = "F "
    elif word1 == 35 :
        word1 = "Br"
    elif word1 == 5 :
        word1 = "B "
    elif word1 == 46 :
        word1 = "Pd"
    elif word1 == 6 :
        word1 = "C "
    elif word1 == 1:
        word1 = "H "
    elif word1 == 7:
        word1 = "N "
    elif word1 == 8:
        word1 = "O "
    elif word1 == 16:
	word1 = "S "
    print >>opennew, "%s%s" % (word1,line[30:-1])
  opennew.close()
  openold.close()
