
# coding: utf-8

# In[ ]:


import time as t

time = t.time()

s = int(time%60)
ms = int((s-int(s))*1000)
m = int((time)//60%60)             #60 seconds in a minute
h = int((time)//3600%24)          #3600 seconds in an hour
d = int((time)//86400%365.25)     #86400 seconds in a day
y = int((time)//31536000)         #31536000 seconds in a year

print("Mill:",ms, "\nSeconds:", s, "\nMinutes:", m, "\nHours:", h, "\nDays:",d, "\nYears",y, "\nSince Jan 1, 1970")

