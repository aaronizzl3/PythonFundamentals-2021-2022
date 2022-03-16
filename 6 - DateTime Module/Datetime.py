
# Dates, Times, DateTimes

import datetime

# Naive - don't have information on daylight savings, timezones, etc, but easier to work with
# Aware - used for more accuracy

# Year, Month, Day
d = datetime.date(2016, 7, 24)
print(d)

# Today's Date
tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)

# 0 Monday, 6 Sunday, we can use this to equate to a specific day
print(tday.weekday())

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"The day is {days[tday.weekday()]}.")

# Time Deltas - the difference between dates or times
tdelta = datetime.timedelta(days=7)
print(f"Original Date: {tday}\nTime Delta Added: {tday + tdelta}")

# Birthday
bday = datetime.date(2021, 11, 15)
timeUntil = bday - tday
print(timeUntil)

# Formatting
print(tday.strftime('%B %d, %Y'))
