#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
def timeme(deco):
    def inner():
        begin =time.time()
        deco()
        end = time.time()
        total = end-begin
        print ("Total Time: ", end - begin)
    return inner1

