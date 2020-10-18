#!/usr/bin/env python

"""This program calculates the net charges on lowerhalf and upperhalf from the inputs
of mulliken charges on individual atoms in a xyz file and explicitly providing the atom numbers in lower half and upper half"""


import sys
import re

# Set global variables
initial = 0
final = 0

inputfile=open(sys.argv[1],'r')
new = sys.argv[1].split('.')[0]
newfile = str(new) + ".txt"
outputfile = open(newfile,"w")

# Read the entire original file

readline = inputfile.readlines()

# Extracting the required data

for i in range (len(readline)):
    if "Mulliken population Analysis for root number: 1" in readline[i]:
        initial = i
    elif "Mulliken population Analysis for root number: 2" in readline[i]:
        initial = i
    elif "Mulliken population Analysis for root number: 3" in readline[i]:
        initial = i
for m in range (initial, len(readline)):
    if "Total electronic charge=" in readline[m]:
        final = m
        break
for line in readline[initial+10:final-1]: 
   # if line=="\n":
   #         pass
    if line[0:13]==[]:
            print >>outputfile, "%s" % (line[13:-1])
    if "N-E" in line:
            print >>outputfile, "%s" % (line)
inputfile.close()
outputfile.close()
