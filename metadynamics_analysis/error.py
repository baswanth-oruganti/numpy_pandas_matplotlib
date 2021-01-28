#!/usr/bin/env python
# coding: utf-8

# ## Import Relevant Modules

import math
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ## Specify all relevant constants

kbt=2.494339
minS=float(sys.argv[1])
maxS=float(sys.argv[2])
nbin=int(sys.argv[3])
block_size = int(sys.argv[4])

# ## Load the COLVAR file containing the CVS and the bias values
data=pd.read_csv("COLVAR",sep="\s+", header=None, skiprows=1,usecols=[1,2,3]) 
data.columns=['s(R)','z(R)','bias']
data['s(R)']=data['s(R)'].round(2)


# ## Calculate Free energy as the negative of bias potential and make minimum free-energy zero
data['energy']=-data['bias'] # free-energy is negative of bias potential
min_energy=data['energy'].min() # minimum bias
data['energy']=data['energy']-min_energy # make minimum bias zero

# ## Normalize s(R)
data['norm s(R)']=(data['s(R)']-minS)/(maxS-minS)

# ## Calculate Maximum bias
bmax=data['bias'].max()


# # Calculate Boltzmann weights for bias and save s(R) and weights info to sR.weight
data['weights']=np.exp((data['bias']-bmax)/kbt)
data.to_csv("sR.weight",index=False,sep="\t",columns=['s(R)','weights'])

# ## calculate number of blocks
nblocks = int(len(data)/block_size)


# ## Binning of data using cut: Create 20 equal-sized bins
data['bins']=pd.cut(data['norm s(R)'], bins=nbin)


# # Calculate mean with in each bin
data2=data.groupby('bins').mean()


# ## Plot free energy vs normalized s(R)
plt.plot(data2['norm s(R)'],data2['energy'])




# # Block averaging: Take one block at a time
bin_size = (maxS-minS)/float(nbin-1)


# ## Binning the data into bins of uniform size
weight_df=pd.read_csv('sR.weight',sep="\t")
weight_df.columns=['s(R)','weights']
weight_df['bin_index'] = (weight_df['s(R)'] - weight_df['s(R)'].min())/ bin_size 
weight_df['bin_index']=weight_df['bin_index'].apply(round).astype(int)

bin_list=list(weight_df['bin_index'].unique())


xbar=pd.Series(index=bin_list,dtype=float,data=[0 for i in range(len(bin_list))])
xbarsq=pd.Series(index=bin_list,dtype=float,data=[0 for i in range(len(bin_list))])
s_series = pd.Series(dtype=float,data=[(minS + (float(i) * bin_size)) for i in range(len(bin_list))])


for iblock in range(0, nblocks):
    start = iblock * block_size 
    end = start + block_size
    weightcopy=weight_df.copy()
    grp=weightcopy[start:end].groupby('bin_index')
    msum=grp['weights'].sum()/float(block_size)
    ind_list=list(msum.index)
    for ind in ind_list:
        xbar[ind]+=msum[ind]
        xbarsq[ind]+=msum[ind]*msum[ind]


result=pd.DataFrame(columns=['s(R)','W','F'],index=bin_list)
result['s(R)']=s_series
result['n-s(R)']=(result['s(R)']-minS)/(maxS-minS)
result['W']=xbar/nblocks
result['F']=(-kbt * np.log(result['W']))/4.184


result['<x**2>']= (xbarsq-result['W']**2)/(nblocks-1)
result['sem']=(np.sqrt(result['<x**2>']/nblocks))
result['error']=(kbt/result['W'])*result['sem']
outdf=result[['n-s(R)','F','error']].round(2)
outdf.to_csv(f'fes{block_size}.dat',sep="\t",index=False)

sns.set_style()
plt.show()
