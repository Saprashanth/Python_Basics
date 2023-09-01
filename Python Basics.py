#!/usr/bin/env python
# coding: utf-8

# # Python Basics Variable
# 

# 
# 1. Declare two variables, `x` and `y`, and assign them integer values. Swap the values of these variables without using any temporary variable.

# In[1]:


x = 8
y = 10
print(x,y)


# In[2]:


x=x+y     # 8+10 = 18
y=x-y     # 18-10= 8 which means x value assigning to y
x=x-y     # 18-8 = 10 which means y value assigning to x 
print(x,y)


# 2. Create a program that calculates the area of a rectangle. Take the length and width as inputs from the user and store them in variables. Calculate and display the area.

# In[4]:


le=int(input())
wi=int(input())
Ar=le*wi
print(Ar)


# 3. Write a Python program that converts temperatures from Celsius to Fahrenheit. Take the temperature in Celsius as input, store it in a variable, convert it to Fahrenheit, and display the result.
# 

# In[5]:


Ce=int(input())
Fa=Ce*(9/5)+32  
print(Fa)


# ## String Based Questions

# 1. Write a Python program that takes a string as input and prints the length of the string.
# 

# In[1]:


st=input()
print(len(st))


# 2. Create a program that takes a sentence from the user and counts the number of vowels (a, e, i, o, u) in the string.
# 

# In[2]:


na = input()
vo = "aeiouAEIOU"

count = sum(na.count(v) for v in vo)  
print(count)


# 3. Given a string, reverse the order of characters using string slicing and print the reversed string.

# In[5]:


a="prashanth"
print(a[::-1])


# 4. Write a program that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards).

# In[4]:


pa=input()
if pa[::-1]==pa:
    print(pa + " is a palindrome")
else:
    print(pa + " is not a palindrome")


# 5. Create a program that takes a string as input and removes all the spaces from it. Print the modified string without spaces.

# In[3]:


sp=input()
print(sp.strip())

