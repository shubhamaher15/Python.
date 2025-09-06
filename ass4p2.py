#Write a Python script to display datetime in various formats using datetime module 
#a. Current date and time 
#b. Current year 
#c. Month of year 
#d. Week number of the year 
#e. Weekday of the week 
#f. Day of year 
#g. Day of the month 
#h. Day of week

import datetime
now = datetime.datetime.now()
print("a. Current date and time:", now)
print("b. Current year:", now.year)
print("c. Month of year:", now.month)
print("d. Week number of the year:", now.strftime("%U"))
print("e. Weekday of the week:", now.weekday())
print("f. Day of year:", now.strftime("%j"))
print("g. Day of the month:", now.day)
print("h. Day of week:", now.strftime("%A"))
