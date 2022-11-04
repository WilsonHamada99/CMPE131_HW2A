#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
def timeme(deco):
    def inner1(*a,**b):
        begin =time.time()
        deco(*a,**b)
        end = time.time()
        print ("Total Time", end - begin)
    return inner1

@timeme
def decoused():
    time.sleep(2)
decoused()

