#!/usr/bin/env python
# coding: utf-8

# # Assignment - 1

# # 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# 
# * 
# 
# 'hello'
# 
# -87.8
# 
# - 
# 
# / 
# 
# +	
# 
# 6 

# 
# 
# 
# Ans:- 
# 
# Values      - 'hello', -87.8 and 6.
# 
# Expressions - *, -, / and +.

# # 2. What is the difference between string and variable?

# 
# 
# Ans:- 
# 
# String - String is a data value of sequenced character data which is written in single quotes or double quotes.
# 
# Variable - Name of a container for storing data values or Named location which holds value (pointer to a loc). Variable name can be given anything except the words which are python Keywords. Variable name can be started by alphabets or underscore but not with a number. Type casting can also be done.
# 
# 

# # 3. Describe three different data types.

# 
# 
# Ans:- 
# 
# 1. Lists
# 
# -- Ordered collection which is enclosed in square brackets.
# 
# -- similar to arrays in other languages but with additional functionalities.
# 
# -- Mutable.
# 
# -- Created by placing elements inside "[]" brackets.
# 
# -- Heterogeneous Elements: List can contain elements of different data types.
# 
# -- Indexing and Slicing can be performed on lists to access or modify elements.

# In[10]:


fruits = ["Apples", 1, ["List in list"]]
print(fruits)


# 2. Tuple
# 
# -- Similar to list.
# 
# -- Immutable
# 
# -- enclosed in "()"
# 
# -- Heterogeneous elements supported
# 
# -- Indexing and Slicing can be performed to access data but cannot be modified.

# In[12]:


my_tuple = (1,2,3,4)
print(my_tuple)

tuple_heterogenous = ("abc", 2, True, 40, "male")
print(tuple_heterogenous)


# 3. Dictionaries
# 
# -- Unordered collection
# 
# -- key value pairs - item stored in key and value format
# 
# --Mutable
# 
# --Adding elements in form of key-value pairs under "{}".
# 
# --key value pairs are made up with ":" between them for assigning value for the key.
# 
# --Heterogeneous elements supported

# In[14]:


dict = {
  "Apple": "Fruit",
  "Delhi": "Capital",
  "year": 2023,
  "southIndia": ["Andhrapradesh", "Tamilnadu", "Karnataka"]
}
print(dict)


# # 4. What is an expression made up of? What do all expressions do?
# 

# Ans:
# 
# An expression is the combination of an operator and operands which gives some value in result when interpreted.
# 

# # 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# 

# spam = 10
# 
# Statement :- A block of code which runs on login for specific operation.
# 
# Expression :- which produces a result after the operation.
# 

# # 6. After running the following code, what does the variable bacon contain?
# bacon = 22
# 
# bacon + 1
# 
# 

# In[6]:


# 1 will be added to the bacon variable value which is in int datatype.

bacon = 22 
bacon = bacon + 1

print(bacon) 



# # 7. What should the values of the following two terms be?
# 'spam' + 'spamspam'
# 
# 'spam' * 3
# 
# 

# In[11]:


result_1 = 'spam' + 'spamspam'

print(result_1) # result will be additon of both the strings.

result_2 = 'spam' * 3

print(result_2) # result will be the multiplication of the string by three times.


# # 8. Why is eggs a valid variable name while 100 is invalid?
# 

# Ans :  Because variable name can be started by alphabets or underscore but not with a number.

# # 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
# 

# Ans: int(), float() and str().

# # 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'

# In[19]:


# result = 'I have eaten ' + 99 + ' burritos.' 

# python can concatenate only the same datatype. Ex:- int + int , str + str.

# if we want to concatenate str to int, we need to typecast int value as string and concatenate.

result = 'I have eaten' + str(99) + 'burritos.'

print(result)

result_1 = 'I have eaten' + ' ' + '99' + ' ' + 'burritos.'

print(result_1)


# In[ ]:




