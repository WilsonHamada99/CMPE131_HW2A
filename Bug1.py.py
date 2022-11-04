#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Base:
    def __init__(self, x, y, size):
# TODO: will need to fill this in
        self.x = x
        self.y = y
        self.size = size
#
    def draw(self):
        return ""
class Circle(Base):
    def __init__(self,x, y, size):
        super().__init__(x,y,size)
    def draw(self):
        return f"""
({self.x}, {self.y})
{self.size}
        , - ~ ~ ~ - ,
    , '               ' ,
  ,                      ,
 ,                        ,
,                          ,
,                          ,
,                          ,
 ,                        ,
  ,                      ,
    ,                 , '
      ' - , _ _ _ , '
"""
class Square(Base):
    def __init__(self, x, y, size):
        super().__init__(x,y,size)
    def draw(self):
        return f"""
({self.x}, {self.y})
{self.size}
--------------------
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
--------------------
"""

