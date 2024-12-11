# 06.12.2024, 09.12.2024

# https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-time-calculator-project/build-a-time-calculator-project
# Build a Time Calculator Project (Scientific Computing with Python 2/5)
# Write a function named add_time that takes in two required parameters and one optional parameter:

#     1) a start time in the 12-hour clock format (ending in AM or PM)
#     2) a duration time that indicates the number of hours and minutes
#     3) (optional) a starting day of the week, case insensitive

# The function should add the duration time to the start time and return the result.
# If the result will be the next day, it should show (next day) after the time. 
# If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.
# If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. 
# The day of the week in the output should appear after the time and before the number of days later.

# Do not import any Python libraries. Assume that the start times are valid times. 
# The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

def am_pm(ap):
    if ap == "AM":
        ap = "PM"
    else:
        ap = "AM"
    return ap

def add_time(start,duration,day=None):
    start = start.split(":")
    start[1] = start[1].split(" ")
    shour = int(start[0]) # starting hour
    smin = int(start[1][0]) # starting minutes
    duration = duration.split(":") 
    durh = int(duration[0]) # duration hours
    durmin = int(duration[1]) # duration minutes
    ap = start[1][1] # AM or PM at start
    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    days = 0
    new_time = ""
    
    totmin = smin + durmin
    toth = shour + durh
        
    # adding another hour, if minutes sum up to that
    if totmin > 59:
        totmin = totmin - 60
        toth += 1
    
    # counting days and adjusting time 
    while toth > 12:
        ap = am_pm(ap)
        if ap == "AM":
            days += 1
        toth -= 12
    if toth == 12:
        ap = am_pm(ap)
        if ap == "AM":
            days += 1
            
    # stringifying calculated time
    if totmin < 10:
        new_time = f"{toth}:0{totmin} {ap}"
    else:
        new_time = f"{toth}:{totmin} {ap}"

    # calculates end weekday
    if day:
        dex = weekdays.index(day.capitalize()) + days
        # makes weekdays loop by stopping index from going out of range
        while dex > 6:
            dex -= 7
        new_time += f", {weekdays[dex]}"
        
    # setting up daycounter string for final return
    if days == 1:
        daycounter = " (next day)"
    elif days > 1:
        daycounter = f" ({days} days later)"
    else:
        daycounter = ""
    
    new_time += daycounter  
    
    return new_time  
        
# test    
tests = [     
        add_time('3:30 PM', '2:12'),                     
        add_time('11:55 AM', '3:12'),                  
        add_time('2:59 AM', '24:00'),                   
        add_time('11:59 PM', '24:05'),                  
        add_time('8:16 PM', '466:02'),                  
        add_time('3:30 PM', '2:12', 'Monday'),          
        add_time('2:59 AM', '24:00', 'saturDay'),       
        add_time('11:59 PM', '24:05', 'Wednesday'),      
        add_time('8:16 PM', '466:02', 'tuesday')]

for t in tests:
    print(t)

 
    
#1 '5:42 PM'
#2 '3:07 PM'
#3 '2:59 AM (next day)'
#4 '12:04 AM (2 days later)'
#5 '6:18 AM (20 days later)'
#6 '5:42 PM, Monday'
#7 '2:59 AM, Sunday (next day)'
#8 '12:04 AM, Friday (2 days later)'
#9 '6:18 AM, Monday (20 days later)'
















