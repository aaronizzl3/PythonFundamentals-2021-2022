
"""
Calculate Cost of Stay
"""

# Imports
import datetime

# Data
hotel_room = {
    "costPerDay": 110,
    "cardFee": 4.40
}


# Functions
def calculate_stay(nd):
    cost = (hotel_room["costPerDay"] * nd) + hotel_room["cardFee"]
    return cost


def calculate_end_date(nd):
    today = datetime.date.today()
    time_delta = datetime.timedelta(days=nd)
    end_date = today + time_delta
    return today, end_date


# Main Logic
num_days = int(input("How long would you like to stay? "))
hotel_cost = calculate_stay(num_days)
start, end = calculate_end_date(num_days)
print(f"£{hotel_cost}")
print(f"Start Date: {start}")
print(f"End Date: {end}")
