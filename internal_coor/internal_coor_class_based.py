
# # Import relevant modules

# In[1]:


import sys
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:



# # Load the Cartesian coordinates into a Pandas DataFrame

# In[21]:

class Molecule:

    def __init__(self,filename):
        self.df=pd.read_csv(filename,sep="\s+",header=None,skiprows=2)
        self.df.columns=['Atom','x','y','z']
        self.df.index=[i+1 for i in range(len(self.df))]


# # Calculation of bond length
# Bond length between two atoms defined by Cartesian coordinates $\vec{a}=(x_1,y_1,z_1)$ and $\vec{b}=(x_2,y_2,z_2)$ is $\newline$
# $$\sqrt{{(x_2-x_1)}^2+{(y_2-y_1)}^2+{(z_2-z_1)}^2}$$ 
# i.e., norm of the vector connecting two points

# In[17]:


    def bond_length(self,p,q):
    
        a=self.df.loc[int(p)][1:]
        b=self.df.loc[int(q)][1:]
    
        return round(np.linalg.norm(b-a),2)

# In[19]:

# # Calculation of bond angle
# Bond angle between three atoms defined by Cartesian coordinates $\vec{a}=(x_1,y_1,z_1)$, $\vec{b}=(x_2,y_2,z_2)$ and $\vec{c}=(x_3,y_3,z_3)$: $\newline$
# (i) We first define two vectors $\vec{ab}$ and $\vec{bc}$ as: $$\vec{ab}=\vec{b}-\vec{a}$$ and $$\vec{bc}=\vec{c}-\vec{b}$$ $\newline$ 
# (ii) Cosine of the angle between the two vectors calculated as: $$\frac{\vec{ab}.\vec{bc}}{||\vec{ab}||.||\vec{bc}||}$$

# In[15]:


    def bond_angle(self,p,q,r):
   
        a=self.df.loc[int(p)][1:]
        b=self.df.loc[int(q)][1:]
        c=self.df.loc[int(r)][1:]
        # step (i)
        ab=np.array(b-a).astype(float)
        bc=np.array(c-b).astype(float)
        # step (ii)
        cos_teta=np.dot(ab,bc)/(np.linalg.norm(ab)*np.linalg.norm(bc))
    
        return round(np.degrees(np.arccos(cos_teta)),1)


# In[16]:

# # Calculation of dihedral angle 
# Dihedral angle between the four atoms defined by Cartesian coordinates $\vec{a}=(x_1,y_1,z_1)$, $\vec{b}=(x_2,y_2,z_2)$, $\vec{c}=(x_3,y_3,z_3)$ and $\vec{d}=(x_4,y_4,z_4)$:  $\newline$
# (i) We first define three vectors $\vec{ab}$ , $\vec{bc}$ and $\vec{cd}$ $\newline$
# (ii) Then we calculate normal vector to the plane containing $\vec{a}, \vec{b}$ and $\vec{c}$ as well as for the plane containg $\vec{b}$, $\vec{c}$ and $\vec{d}$ as: $\newline$ $$\vec{n1}=\vec{ab}\times\vec{bc}$$ $$\vec{n2}=\vec{bc}\times\vec{cd}$$ $\newline$
# (ii) Cosine of the angle between the two normal vectors calculated as: $$\frac{\vec{n1}.\vec{n2}}{||\vec{n1}||.||\vec{n2}||}$$

# In[11]:


    def dihedral_angle(self,p,q,r,s):
    
        a=self.df.loc[int(p)][1:]
        b=self.df.loc[int(q)][1:]
        c=self.df.loc[int(r)][1:]
        d=self.df.loc[int(s)][1:]
        # step (i)
        ab=np.array(b-a).astype(float)
        bc=np.array(c-b).astype(float)
        cd=np.array(d-c).astype(float)
        # step (ii)
        nor1=np.cross(ab,bc)
        nor2=np.cross(bc,cd)
        # step (iii)
        cos_teta=np.dot(nor1,nor2)/(np.linalg.norm(nor1)*np.linalg.norm(nor2))
    
        return round(np.degrees(np.arccos(cos_teta)),1)


# In[14]:




# # References
# 1. https://sites.math.washington.edu/~king/coursedir/m445w04/notes/vector/equations.html $\newline$
# 2. https://sites.math.washington.edu/~king/coursedir/m445w04/notes/vector/normals-planes.html#cross

# In[ ]:




