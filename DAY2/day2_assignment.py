#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
d=int(input("Enter 4th number:"))
e=int(input("Enter 5th number:"))
avg=(a+b+c+d+e)/5
print("Average of the five numbers is: ",avg)


# In[4]:


num1=int(input("Enter 1st Number:"))
num2=int(input("Enter 2nd Number:"))
print("Sum of this two number is: ",num1+num2)
print("Subtraction of this two number is: ",num1-num2)
print("Multiplication of this two number is: ",num1*num2)
print("Division of this two number is: ",num1/num2)
print("Modulus of this two number is: ",num1%num2)


# In[5]:


M,X,C=0.1,3,2
Y=(M*X)+C
print("Value of Y is:",Y)


# In[8]:


a=int(input("Enter the value of A:"))
b=int(input("Enter the value of B:"))
c=int(input("Enter the value of C:"))
k=int(input("Enter the value of K:"))

y=a*b*c+11+k
print("Value of y is: ",y)


# In[16]:


name=input("Enter user's name: ")
age=input("Enter user's age: ")
dob=input("Enter user's DOB in (DD/MM/YYYY) form: ")
email=input("Enter user's Email address: ")
contNumber=input("Enter user's Contact number: ")
bio_data="Name: {name}\nAge: {age}\nDOB: {dob}\nEmail: {email}\nContact Number: {contNumber}"
print("\n\nBio Data of User's: ")
print(bio_data.format(name=name,age=age,dob=dob,email=email,contNumber=contNumber))


# In[ ]:




