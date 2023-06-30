#!/usr/bin/env python
# coding: utf-8

# # Assignment - 2

# # 1. What are the two values of the Boolean data type? How do you write them?
# 

# 
# 
# 
# Ans:- 
# 
# 2 Boolean Values      - TRUE and FALSE / 1 and 0 / T and F 
# 
# 1. True will be written when a condition specified becomes true / passes . 
# 
# 2. False will be written when a condition specified becomes fails . 
# 
# Ex:- 
# * 1 == 1 is True.
# * 1 != 1 is False
# * 1 != 2 is True
# * 1 == 2 is False

# # 2. What are the three different types of Boolean operators?

# 
# 
# Ans:- Logical Operators: AND, OR and NOT.
# 
# 1. AND operator: Provides result TRUE if both the operands are true. And can be represented as 'AND' or '&&'
# 2. OR operator : Provides result TRUE if one of the operands is true. And can be represented as 'OR' or '||'
# 3. Not operator: Provides result opposite to the result of operand. And can be represented as 'NOT' or '!'
# 
# 
# 
# * A && B => True if both operands are true. or else returns false.
# * A || B => True if both operands are true and even if either one of the operands is true. If No one is true, then it retuurns False.
# * NOT A => returns True if A if False , Returns False if A is true.
# 
# 
# Ex: 
# 
# If ((a == b) OR (a != b)) = True ( one is true)
# 
# If ((a < b) AND (a != b)) = True (both are true)
# 
# If ( Not (a == b)) = True. ( because a == b gives false)

# # 3.  Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

# 
# 
# Ans:- 
# 
# AND Truth Table:
# 
#     A       AND      B      Returns
#     True    AND     True     True
#     True    AND     False    False
#     False   AND     True     False
#     False   AND     False    False
#     
#  OR Truth Table:
#  
#      A       OR      B      Returns
#     True    OR     True     True
#     True    OR     False    True
#     False   OR     True     True
#     False   OR     False    False
#     
#  NOT Truth Table:
#  
#      A      NOT     Returns
#     True    NOT      FALSE
#     FALSE   NOT      TRUE

# # 4 . What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# 
# not (5 > 4)
# 
# (5 > 4) or (3 == 5)
# 
# not ((5 > 4) or (3 == 5))
# 
# (True and True) and (True == False)
# 
# (not False) or (not True)
# 
# 

# Ans:
# 
# (5 > 4) and (3 == 5) = FALSE
# 
# not (5 > 4) = FALSE
# 
# (5 > 4) or (3 == 5) = TRUE
# 
# not ((5 > 4) or (3 == 5)) = FALSE
# 
# (True and True) and (True == False) = FALSE
# 
# (not False) or (not True) = TRUE
# 

# # 5. What are the six comparison operators?
# 

# Comparision Operators:
# 
# '==' (EQUAL TO),
# 
# '!=' = (NOT EQUAL TO),
# 
# '>' and '<' =  (Greater and less thanoperator) , 
# 
# '<=' and '>=' = (Greater than or equal to / lesser than or equal to).
# 
# Ex: 
# 
# a = 10
# b = 20
# c = 10
# 
# a == b : False
# 
# a != b : True
# 
# a > b  : False
# 
# b < a  : True
# 
# a >= c : True
# 
# c <= b : True

# # 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
# 
# 

# Ans: 
#     1. "=" is an assignment operator. 
#     2. "==" is an equality operator
# 
#     Ex: 
#        1.  a = 10 (Value '10' is assigned to 'a' variable)
#            a == b (Comparing if the both 'a' and 'b' variable are equal). 
#         
#        2. x = 1 -- assigned the value
#           x == 2 -- returns false (comapring values)
#           2 == 2 -- returns true (both are wqual)

# # 7. Identify the three blocks in this code:
# spam = 0
# 
# if spam == 10:
# 
# print('eggs')
# 
# if spam > 5:
# 
# print('bacon')
# 
# else:
# 
# print('ham')
# 
# print('spam')
# 
# print('spam')
# 
# 

# In[6]:


spam = 10

# 1st block
if spam == 10:
    print('eggs')
    
# 2nd Block
if spam > 5:
    print('bacon')

# 3rd block    
else:
    print('ham')

print('spam')
print('spam')


# # 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
# 

# In[24]:


spam = 2
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
   print("Greetings!")


# ## 9.If your programme is stuck in an endless loop, what keys you’ll press?
# 

# Ans: Ctrl + c

# # 10. How can you tell the difference between break and continue?
# 

# Ans: Both keywords are used in loops but, 
# 
#     1. Break - stops the flow/execution completely on that condition itself.
#     2. Continue - skips the current condition/statement and conitnues with next.

# # 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# Ans: Range syntax - range(start, stop step)
# 
#     range(10) - returns the sequence of the numbers in the specified range one by one. 
#     
#     range(0, 10) - Here, start and stop are specified. '0' is the start positions and '10' is the end position. This function will return this sequence from 0 to 9.
#     
#     range(0, 10, 1) - All three specified - start, stop and step. Step defines the difference between the first and next element.Here step value = 1 i.e., range functions consider jump of 1 value each time.

# # 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[25]:


# using for loop
x = 10
    
print("Numbers from 1 to 10 using for loop:")
for j in range(1, 11):
    print(j)  #prints 1 to 10
    
a = 1
print("Numbers from 1 to 10 using while loop:")
while a <= 10:
    print(a)
    a += 1  #prints 1 to 10


# # 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

# from spam import bacon
# 
# #or 
# 
# import spam
# 
# spam.bacon() 

# In[ ]:





# In[ ]:




