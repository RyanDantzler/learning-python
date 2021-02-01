#!/usr/bin/env python
# coding: utf-8

# Data Structures: list (array), tuple (list you cannot modify), dict (hashmap or hashtable), set (only unique elements "Hashset in C#")

# In[2]:


x = [1, 2, 3]
len(x)


# In[11]:


x = [1, 2, 3, 1, 2, 3]
x


# In[6]:


x.append(5)
x


# In[12]:


x.remove(1)
x


# In[17]:


x.remove(5)
x


# In[18]:


x.insert(4, 5)
x


# In[21]:


x += [6]
x


# In[22]:


x + [7]


# In[23]:


[0] + x


# In[25]:


y = [0] + x
y


# In[26]:


x.count(6)


# In[28]:


x = [1, 2, [2, 3]]
x.count(2)


# In[29]:


x.count([2, 3])


# In[31]:


x = [1, 4, 5, 3, 2]
x.sort()
x


# Sort changes original object

# In[32]:


x = [5, 2.0, 1, 4.0]
x.sort()
x


# In[33]:


x = [5, 2, 'a', 4, 'ab', 'aa']
x.sort()


# In[34]:


x = ['bc', 'ab', 'aa', 'da']
x.sort()
x


# In[35]:


x = [[2, 3], [2, 2], [1, 3], [1, 2]]
x.sort()
x


# In[36]:


x = [[3, 2, 3], [2, 2], [1, 2, 3], [1, 2]]
x.sort()
x


# In[38]:


type(3*'abc')


# In[39]:


int('3')


# In[40]:


int('a')


# No way to convert char to int

# In[41]:


x = [1, 2, 3, 4]
x


# In[42]:


x[0]


# In[43]:


x[4]


# In[44]:


x[-1]


# In[45]:


x[-5]


# In[46]:


x[1-len(x)]


# In[47]:


x = "hello world!"
x.strip()


# In[61]:


x = [1, 2, 3, 4, 5, 6, 7]
x


# In[51]:


x[0:3]  # first number is inclusive, second number is not inclusive


# In[52]:


x[:3]


# In[53]:


x[3:]


# In[54]:


x[-1:]


# In[55]:


x[-3:]


# In[56]:


x[1:-3]


# In[58]:


x[-3:-1]


# In[62]:


x[:]


# In[63]:


x[::2]


# In[64]:


x = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
x[::2]


# In[68]:


x[::-1]  # negative step size reverses the list


# In[66]:


x[::-2]


# In[70]:


x = [1, 2, 3, 4, 5, 6, 7]
x[2:5:2]


# In[71]:


x[2:5:-1]


# In[74]:


x[5:2:-1]  # you need to reverse your start and end indexes if you reverse the list by step size


# In[75]:


x


# In[76]:


x[2:4] = ['a', 'b', 'c'] 
x


# In[77]:


x[2:5] = ['d']
x


# tuple is immutable list

# In[79]:


t = (1, 2, 3)
t


# In[80]:


t.append(4)


# In[81]:


t.count(2)


# In[83]:


t = (1, 1, 2, 2, 3, 3)  # can contain duplicate values
t


# In[84]:


t.count(2)


# In[85]:


t[:4]


# In[86]:


t[2:4] = [4, 5]


# In[89]:


t = (1)
t


# In[91]:


type(t)


# In[92]:


t = (1,)
type(t)


# In[93]:


t


# In[94]:


t = 1,
type(t)


# In[95]:


t


# In[98]:


t = 1, 2, 3
t


# In[97]:


type(t)


# In[99]:


t[::-1]


# In[102]:


x = 0.125
x.as_integer_ratio()  # returns a tuple


# In[101]:


1/8


# In[103]:


type(x.as_integer_ratio())


# In[104]:


a, b = x.as_integer_ratio()


# In[105]:


a


# In[106]:


b


# In[107]:


(a, b) = x.as_integer_ratio()


# In[108]:


a


# In[109]:


b

