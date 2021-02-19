#!/usr/bin/env python
# coding: utf-8

# In[126]:


#!/usr/bin/env python
# coding: utf-8


# In[70]:


import sys
import numpy as np
import pandas as pd


# ### Read the .xyz file and make atomic symbol as index

# In[90]:


coor=pd.read_csv("1.xyz",sep="\s+",skiprows=2,header=None)
coor.columns=['Atom label', 'x', 'y', 'z']
coor.set_index('Atom label',inplace=True)


# ### Save number of atoms, atomic masses, Boltzmann constant, Temperature and masses; convert everything to atomic units

# In[108]:


number_of_atoms=len(coor); kb=1; temp_au=300*0.00000316683
atomic_mass_amu={'H':1.0078,'C':12.0107,'N':14.0067,'O':15.9990,
               'F':18.9984,'P':30.9738,'S':32.0650, 'Cl':35.4530}
mass_amu=np.array([atomic_mass_amu[item] for item in coor.index])
coor['mass_a.u.']=mass_amu*1822.888


# ### Calculate Gaussian width $\sigma_i =\sqrt \frac{k_bT}{m_i}$  where i is atom index, m is mass of atom in a.u.

# In[116]:


coor['sigma_i']=np.sqrt(kb*temp_au/coor['mass_a.u.'])
coor['label']=coor.index.str.lower()
coor.to_csv("coor.xyz",sep="\t",header=None,columns=['x','y','z','label'],
            float_format="%2.7f",index=None)


# ### Generate 3N random numbers from a standard normal distribution (mean=0, stdev=1)

# In[122]:


rand_xyz = np.random.normal(0, 1, size=(number_of_atoms, 3))


# ### Calculate velocities as $ vel(x,y,z) = rand(x,y,z) * \sigma_i $

# In[117]:


sigmas=np.array(coor['sigma_i']).reshape(-1,1)
vel_xyz=rand_xyz*sigmas
vel_df=pd.DataFrame(vel_xyz,index=coor.index,columns=['x','y','z'])
vel_df['label']=vel_df.index.str.lower()
np.savetxt("velocity.txt", vel_df[['label','x','y','z']], fmt=["%s","%.10f","%.10f","%.10f"])


# ### Write positions, time step and start time, and velocities to mdlog.1 in TURBOMOLE prescribed format

# In[118]:


with open("velocity.txt",'a') as vfile:
    vfile.write("$end")


# In[121]:


time_step=41.5
time_start=0.0
with open("mdlog.1", 'w') as logfile, open('coor.xyz') as coorf, open('velocity.txt') as velf:
    logfile.write("# AIMD log file\n")
    logfile.write("$log\n")
    logfile.write("$current\n")
    logfile.write("t=   0.0000\n")
    logfile.write(coorf.read())  # write positions
    logfile.write(f'{time_step:.6f} \t {time_start:.6f}\n') # write timestep and starttime in a.u.
    logfile.write(velf.read()) # write velocities


# ### Notes: Maxwell-Boltzmann distrbiution of velocities $$\sqrt{\frac{m}{2\pi{k_bT}}} \exp({\frac{-mv^2}{2k_bT}})$$ is a Gaussian distrbution with width $$\sigma^2 =\sqrt \frac{k_bT}{m_i}$$ which turns to
# ### $$\frac{1}{\sqrt{2\pi\sigma^2}} \exp({\frac{-v^2}{2\sigma^2}}) $$
