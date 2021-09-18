#!/usr/bin/env python
# coding: utf-8

# In[ ]:


year = int(input("Enter a year:- "))   # Here, you take the input from the user

# step 1 : check if year is eveanly devide by 4 go to step 2   otherwise go to step 4 
if year % 4 ==0:  
# step 2: check if year is not evenly devided by 100 otherwise go to step 3  
    if year %100 !=0: 
        print("{0} is a leap year!!".format(year))
        
# step 3: check if year is evenly devided by 400        
    else: 
        if year %400==0:
            print("{0} is a leap year!!".format(year))
        else:
             print("{0} is not a leap year!!".format(year))
#step 4            
else:
    print("{0} is not a leap year!!".format(year))


# In[ ]:




