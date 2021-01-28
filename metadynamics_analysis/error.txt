#!/bin/bash




module load plumed/2.5.1/GNU


# First, we will calculate the "un-biasing" weights associated to each conformation sampled during the metadynamics run. In order to calculate these weights, we can use either of these two approaches: Weights are calculated by considering the time-dependence of the metadynamics bias potential; Weights are calculated using the metadynamics bias potential obtained at the end of the simulation and assuming a constant bias during the entire course of the simulation. In this exercise we will use the umbrella-sampling-like reweighting approach (Method 2).To calculate the weights, we need to use the PLUMED driver utility and read the HILLS file along with the GROMACS trajectory file produced during the metadynamics simulation. 

# evaluate bias on the full simulation
srun plumed driver --plumed plumed.dat --mf_xtc abl1_md.xtc

# calculate the un-biasing weights using the umbrella-sampling-like approach

# find maximum value of bias
bmax=$(awk 'BEGIN{max=0.}{if($1!="#!" && $4>max)max=$4}END{print max}' COLVAR)
echo $bmax

# calculate COLVAR values and associated weights
awk '{if($1!="#!") print $2,exp(($4-bmax)/kbt)}' kbt=2.494339 bmax=$bmax COLVAR > sR.weight


# we apply the block-analysis technique to calculate for different block sizes the average free-energy and the error using the do_block_fes.py python script to read the rmsd.weight file and produce the desired output.

# args. to python script: weights, No. of CVs, Grid minimum, Grid maximum, number of bins (in rmsd units), kbt, block size

for i in {1..1010..10} 
do 
 python do_block_fes.py sR.weight 1 1.0 112.0 20 2.494339 $i  
done

# For each value of block length N, you will obtain a separate fes.N.dat file, containing the value of the p1.sss variable on a grid, the average free-energy, and the associated error (in kJ/mol)

# we can calculate the average error along the free-energy profile as a function of the block length

for i in {1..1010..10} 
do 
 a=$(awk '{tot+=$3}END{print tot/NR}' fes.$i.dat)
 echo $i $a >> err.blocks
done

