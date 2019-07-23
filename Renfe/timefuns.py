####################### Time Functions ########################
# These functions extract information from a time string.
# The format of the string must be like '2019-05-29 06:20:00'
#
# - getHour returns the hour as an integer
# - getHourFloat returns the hour and minutes as a float
#                (1 minute is 1/60 hours)
# - getMonth returns the month as an integer
# - weekday returns the weekday as a string
#                (only works for dates in 2019)
# - weekdayNum returns the weekday as a float between 0 and 1
# - daysNum returns the day of the year as a float between 0 and 1
#                (Jan 1 is about 0 and Dec 31 is about 1)
###############################################################

def getHour(date):
    return int(date[11:13])

def getHourFloat(date):
    return float(date[11:13]) + float(date[14:16])/60

def getMonth(date):
    return int(date[5:7])

def getDate(date):
    return date[:10]

def weekday(date):
    month = int(date[5:7])
    day = int(date[8:10])
    
    daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    weekdays = ['tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'monday']
    
    daysSince = day - 1
    i = month - 1
    while i > 0:
        daysSince = daysSince + daysPerMonth[i-1]
        i = i - 1
        
    return weekdays[daysSince % 7]

def weekdayNum(wd):
    if wd == 'monday':
        return 1.0/7.0
    elif wd == 'tuesday':
        return 2.0/7.0
    elif wd == 'wednesday':
        return 3.0/7.0
    elif wd == 'thursday':
        return 4.0/7.0
    elif wd == 'friday':
        return 5.0/7.0
    elif wd == 'saturday':
        return 6.0/7.0
    elif wd == 'sunday':
        return 7.0/7.0
    
def daysNum(date):
    month = int(date[5:7])
    day = int(date[8:10])
    
    daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    weekdays = ['tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'monday']
    
    daysSince = day - 1
    i = month - 1
    while i > 0:
        daysSince = daysSince + daysPerMonth[i-1]
        i = i - 1
        
    return daysSince/365.0