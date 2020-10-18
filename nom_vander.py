#!/usr/bin/env python

"""This script takes a xyz file and a list of atoms in upper half and lower half in the fjord region and calculates steric factor Sxy"""


# Loads the sys to additional input in the line
# Loads the re(regualr expression) search function

import sys
import re

def nom_vanderwaals():
 
# list of nominal van der waals radii and van der Waals distances (global variables)

 C_ali=1.70
 C_aro=1.77
 H_ali=1.20
 H_aro=1.00
 N=1.55
 O=1.52
 O_dou=1.65
 S=1.80

 list1=[C_ali,C_aro,H_ali,H_aro,N,O,O_dou,S]
 list2=[C_ali,C_aro,H_ali,H_aro,N,O,O_dou,S]
 list3=[]
 list4=['C_ali','C_aro','H_ali','H_aro','N','O','O_dou','S']
 list5=['C_ali','C_aro','H_ali','H_aro','N','O','O_dou','S']
 list6=[]
 nominal_van_der={}

 for i in list1:
  for j in list2:
    n=round(i+j,2)
    list3.append(n)

 for x in list4:
  for y in list5:
   list6.append(str(x)+'-'+str(y))

 k=0
 for a in list6:
  nominal_van_der[a]=round(list3[k],2)
  k+=1
 return nominal_van_der




