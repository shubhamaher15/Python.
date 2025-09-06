#Write a Python program to print Calendar of specific month of input year using calendar module
import calendar
year = int(input("Enter year"))
month = int(input("Enter month (1-12) "))
print("\n", calendar.month(year, month))
