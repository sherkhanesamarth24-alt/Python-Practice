# Python DateTime Module

from datetime import datetime, date

current_time = datetime.now()
today = date.today()

print("Current Date and Time:", current_time)
print("Today's Date:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
