#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def swap_list(thelist):
    size = len(thelist)
    if (size %2) ==0:
        post1 = int (len(thelist)/2-1)
        post2 = int (len(thelist)-1)
        thelist[post1], thelist[post2] = thelist[post2], thelist[post1]
        print(thelist)
    else:
        post1 = int (len(thelist)/2-0.5)
        post2 = int (len(thelist)-1)
        thelist[post1], thelist[post2] = thelist[post2], thelist[post1]
        print (thelist)
        return
firstlist = [1,2,3,4,5]
secondlist = [4,5,6,7,8]
swap_list(firstlist)
swap_list(secondlist)

