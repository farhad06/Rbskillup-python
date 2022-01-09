#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1.Sum of three number
m= int(input())
n = int(input())
p=int(input())
print(m+n+p)


# In[ ]:


#Q2.Write a program that greets the person by printing the word "Hi" and the name of the person
name=input()
print("Hi ",name)


# In[ ]:


#Q3.Write a program that takes a number and print its square.
number=int(input())
sq=number ** 2
print(sq)


# In[ ]:


#Q4.Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. Every number is given on a separate line
a=int(input())
b=int(input())
area=a*b/2
print(area)


# In[ ]:


#Q5.Write a program that greets the user by printing the word "Hello", a comma, the name of the user and an exclamation mark after it
name = input()
print('Hello, '+name+'!')


# In[ ]:


#Q6.N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?
n = int(input())
k = int(input())
print(k // n)
print(k % n)


# In[ ]:


#Q7.Write a program that reads an integer number and prints its previous and next numbers.
num=int(input())
next_num=num+1
pre_num=num-1
print('The next number for the number '+str(num)+' is '+str(next_num)+'.')
print('The previous number for the number '+str(num)+' is '+str(pre_num)+'.')


# In[ ]:


#Q8.A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them
timespan1_hour=int(input())
timespan1_min=int(input())
timespan1_sec=int(input())
timespan2_hour=int(input())
timespan2_min=int(input())
timespan2_sec=int(input())
timespan1_total_sec=timespan1_hour*3600+timespan1_min*60+timespan1_sec
timespan2_total_sec=timespan2_hour*3600+timespan2_min*60+timespan2_sec
total_sec=timespan2_total_sec-timespan1_total_sec
print(total_sec)


# In[ ]:


#Q9.A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
class1=int(input())
class2=int(input())
class3=int(input())
no_of_desk=(class1//2+class2//2+class3//2+class1%2+class2%2+class3%2)
print(no_of_desk)

