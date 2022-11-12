#!/usr/bin/env python
# coding: utf-8

# In[1]:


def swap_list(thelist):
    if len(thelist)%2 ==0 :
        get = thelist[int(len(thelist)/2)-1], thelist[-1]
        thelist[-1],thelist[int(len(thelist)/2)-1] = get
        return thelist
    else:
        get = thelist[int(len(thelist)/2)], thelist[-1]
        thelist[-1],thelist[int(len(thelist)/2)] = get
        return thelist

