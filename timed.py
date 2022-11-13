#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time

def timeme(func):
    def innertime():
        start = time.time()
        func()
        end = time.time()
        total = end - start
        print("Total time: ", total)
    return innertime

