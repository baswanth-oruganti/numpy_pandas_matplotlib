#!/usr/bin/env python

"""This script changes gaussian output files to xyz format"""

# importing nominal vanderWaals distcances using the module nom_vander

from nom_vander import *
import sys
import re
import string

# Loads the sys to additional input in the line
# Loads the re(regualr expression) search function

#variable declaration: upperhalf data,lower half data, interaction,interatomic dist

uhalf=[]
lhalf=[]
atom_distance=[]
interaction_type=[]
atom_number=[]


# This comes from the input files


filename = sys.argv[1]

  # Open the original file in read mode
  # Create a new file with writing rights

file=open(filename,"r")

  # Read the entire original file

rline = file.readlines()

# Obtaining the cartesian coordiantes of upper half and lower half atoms

for i in range (len(rline)):
    if "Atoms in upper half" in rline[i]:
        pass
    elif "Atoms in lower half" in rline[i]:
	break
    else:
          uhalf.append(rline[i].split())
	  j=i

for k in range(len(rline)):
    if "Atoms in lower half" in rline[k]:
        pass
    elif k>j:
          lhalf.append(rline[k].split())

# Calculating interatomic distances between upper half and lower half atoms

for i in uhalf:
  for j in lhalf:
    distance=((float(i[2])-float(j[2]))**2+(float(i[3])-float(j[3]))**2+(float(i[4])-float(j[4]))**2)**0.5
    atom_distance.append(distance) 
    interaction_type.append(i[1]+"-"+j[1])
    atom_number.append(i[1]+i[0]+"-"+j[1]+j[0])       

# Creating a dictionary with interaction type and corresponding interatomic diatnces 

inter_atomic={}
l=0
for a in interaction_type:
   if a not in inter_atomic.keys() and atom_distance[l]<3.80:
    inter_atomic[a]=[atom_distance[l]]
   elif atom_distance[l]<3.80:
    inter_atomic[a].append(atom_distance[l])
   l+=1

# for printing atom numbers

duplicate={}
k=0
z=''
list1=[]
for a in atom_number:
   if  atom_distance[k]<3.55:
    duplicate[a]=round(atom_distance[k],2)
   k+=1 
 



# calling the module to obtain nominal vanderWaals distances

vander=nom_vanderwaals().copy()


# Now calculating steric factor by consdiering interatomic distances that are less than nominal vanderWaals distances

steric=[]
Total_steric=0.0
for i in inter_atomic:
  for j in inter_atomic[i]:
    if j<vander[i]:
     steric.append(round(vander[i]-j,2))
     Total_steric+=vander[i]-j
     continue

Total_steric=round(Total_steric,2)
print vander
print
print steric
print
print Total_steric
print
print duplicate
