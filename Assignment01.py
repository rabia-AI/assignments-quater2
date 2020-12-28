#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


nl = np.zeros(10)
print(nl)


# In[3]:


rng = np.arange(10,49)
print(rng)


# In[4]:


print(rng.shape)


# In[5]:


print(rng.dtype)


# In[6]:


print(np.__version__)
print(np.show_config())


# In[7]:


dm = np.array([10,49])
print(dm)


# In[8]:


bol = np.ones(10, dtype = bool)
print(bol)


# In[13]:


dmary2 = np.ndarray((10,49))
print("dimension:",dmary2.ndim)


# In[14]:


dmary3 = np.ndarray((10,49,69))
print("dimensional:",dmary3.ndim)


# In[15]:


rng = np.arange(10,49)
print(rng[::-1])


# In[21]:


nll = np.zeros(10)
nll[5] = 1
print(nll)

