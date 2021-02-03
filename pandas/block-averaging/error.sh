#!/bin/bash

# 
for blocksize in {1..1010..10} 
do 
 python error.py 1 1.0 112.0 20 $blocksize
done


for i in {1..1010..10} 
do 
 a=$(awk '{tot+=$3}END{print tot/NR}' fes$i.dat)
 echo $i $a >> err.blocks
done

