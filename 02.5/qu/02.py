# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Compensate for leap days. 
# Assume that the birthday and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 2 Jan 2012 
# you are 1 day old.
#
# Hint
# A whole year is 365 days, 366 if a leap year. 
    
def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gergorian calendar, and the first date is not after
       the second."""
        
    # YOUR CODE HERE!
    day_count = 0
    while(dateLessThan(year1, month1, day1, year2, month2, day2)):
          day_count += 1
          year1, month1, day1 = nextDay(year1, month1, day1)
    return day_count

def dateLessThan(year1, month1, day1, year2, month2, day2):
    """Checks that the firt date is less than the second"""
    is_less = year1 < year2
    is_less = is_less or year1 == year2 and month1 < month2
    is_less = is_less or year1 == year2 and month1 == month2 and day1 < day2
    return is_less

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
    
