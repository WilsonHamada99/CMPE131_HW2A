#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sort_dictionary(thelist):

    out_list = []
    age_list = []
    for k,v in thelist.items():
        out_list.append((k,v[0]))
        age_list.append(v[1])

    output = [x for _, x in sorted(zip(age_list, out_list))]
    print(output)

    return;

Thelist = {'Josh': (5241654, 26), 'Brady': (5748496, 43), 'Patrick': (1659587, 19)}
sort_dictionary(Thelist)

