"""
1 Jan 1900 was a Monday.
Thirty days has September, April, June and November.
All the rest have thirty-one, 
Saving February alone, Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


def days_in(year, month):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28
    else:
        return 31 

def is_sunday(days_post_jan_1_1901):
    # 1st sunday in 1901 is Jan 6
    return days_post_jan_1_1901 % 7 == 6

def sunday_as_first_of_month_from_1901_2000():
    total_days = 1
    sundays = 0
    for year in xrange(1901, 2001):
        for month in xrange(1, 13):
            total_days += days_in(year, month)
            if is_sunday(total_days):
                sundays +=1

    return sundays
