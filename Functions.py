#!/usr/bin/env python
# coding: utf-8

# In[20]:


def fib(N, a=0, b=1):  # named parameters must come last in the parameter list
    L = []
    #a, b = 0, 1
    while len(L) < N:
        L.append(a)
        a, b = b, a+b
    return L, a, b  # return a tuple, list and the values of a and b


# In[24]:


print(fib(5))


# In[25]:


x, y, z = fib(5)


# In[28]:


x


# In[29]:


y


# In[30]:


z


# In[5]:


def findMaxPrime(n):
    result = -1
    while n % 2 == 0:
        n >>= 1
        
    if n == 1:
        result = 2
        
    for odd in range(3, n + 1, 2):
        while n % odd == 0:
            n = n // odd
        if n == 1:
            result = odd
            break
            
    return result


# In[6]:


findMaxPrime(1323)


# In[33]:


def catch_all(*args, **kwargs):  # keyword arguments
    print('args = ', args)
    print('kwargs = ', kwargs)


# In[32]:


catch_all([1, 2, 3], {2, 4, 5, 6})


# In[34]:


catch_all(2, 3, 4, a=7, b=8, c=9)


# In[36]:


catch_all(d=2, 3, 4, a=7, b=8, c=9, 5)  # default args must come first


# In[37]:


inputs = (1, 2, 3, 4)


# In[38]:


keywords = {'a':1, 'b':2, 'c':3}


# In[43]:


catch_all(*inputs, **keywords)  
# * means you remove the outer parentheses of the tuple, ** means you want to expand the dictionary


# In[40]:


catch_all(inputs, keywords)


# In[41]:


catch_all(inputs, **keywords)


# lambda is an anonyomous function

# In[58]:


add = lambda x, y: x + y


# In[47]:


type(add)  # add is just a name pointing to that function


# In[59]:


add(1, 2)


# In[60]:


add2 = add


# In[61]:


add2(2, 3)


# In[56]:


def nonamefunc(x, y):
    return x + y

add3 = nonamefunc


# In[62]:


add3(4, 5)


# In[64]:


data = [{'first': 'Guido', 'last': 'Van Rossum', 'YOB': 1956},
       {'first': 'Grace', 'last': 'Hopper', 'YOB': 1906},
       {'first': 'Alan', 'last': 'Turing', 'YOB': 1912}]


# In[65]:


data


# In[66]:


sorted([3, 2, 1, 5])


# In[68]:


sorted(data)  # custom key function is missing


# In[71]:


sorted(data, key = lambda item: item['YOB'])


# In[72]:


def myfunc(item):
    return item['YOB']


# In[73]:


sorted(data, key = myfunc)


# Exceptions

# In[74]:


1/0


# In[115]:


''' try and except is equivalent to try/catch'''
def div(a, b):
    try:
        return a / b
    except:
        print('cannot be divided by zero!')


# In[116]:


div(1, 0)


# In[94]:


div(4, 2)


# In[123]:


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError as error1:
        print('cannot be divided by zero!', error1)  # custom message and system message
    except NameError:
        print('variable undefined')


# In[122]:


div(1, 0)


# In[110]:


a = 1
a / c


# In[125]:


raise ZeroDivisionError("Hey, you cannot do this!")  # like 'throw' exception in c#


# In[176]:


class MySpecialError(ZeroDivisionError):
    pass

def div(a, b):
    try:
        return a/b
    except ZeroDivisionError as error1:
        print('cannot be divided by zero!', error1)
        raise MySpecialError("hey!");
    except NameError:
        print('variable undefined')
        


# In[179]:


try:
    div(1, 0)
except MySpecialError:
    print('my special error.')
except ZeroDivisionError:
    print('function div failed.')


# try... catch... else... finally = Try catch and finally in C#

# In[184]:


try:
    #messed up your data
    1 / 0
    print("try something here")
except:
    print("this happens only if it fails")
else:
    print("this happens only if it succeeds")
finally:
    # clean up your data
    print("this happens no matter what")


# In python theres no such thing has memory management so you dont need to release memory

# In[ ]:




