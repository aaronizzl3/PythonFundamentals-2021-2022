
import datetime

# Time Deltas - the difference between dates or times
tday = datetime.date.today()
option = int(input("How many days do you want to stay? "))
tdelta = datetime.timedelta(days=option)

print(tday)
print(tdelta)
print(tday + tdelta)

# Birthday
bday = datetime.date(2021, 11, 15) # Inputs a date of our choosing
print(bday - tday) # This prints out the days until our birthday from todays date

date_entry = input("Enter a date in YYYY-MM-DD format")
year, month, day = map(int, date_entry.split('-'))
ourDate = datetime.date(year, month, day)
'''
Create a program which calculates how many days it is until your birthday.

Create a function which takes in a date, calculating how many days it is until Christmas.
'''

def MyFunction(someDate):
    cmas = datetime.date(2021, 12, 25)
    print(cmas - someDate)


MyFunction(datetime.date(2021, 3, 17))
'''
Create a function which takes in days as a parameter. 
It should output the date it will be with those days added on.
'''