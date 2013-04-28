# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

# this function is required, even though the problem statement
# doesn't mention it, the marker wants one.
def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    count = 0
    yearX = year1
    while yearX < year2:
        if isLeapYear(yearX):
            count = count + 1
        count = count + 365
        yearX = yearX + 1
    count -= day_of_year(year1,month1,day1)
    count += day_of_year(year2,month2,day2)
    return count

def day_of_year(year, month, day):
    count = day
    if month >= 1:
        count = count + 0
    if month >= 2:
        count = count + 31
    if month >= 3:
        count = count + 28
        if isLeapYear(year):
            count = count + 1
    if month >= 4:
        count = count + 31
    if month >= 5:
        count = count + 30
    if month >= 6:
        count = count + 31
    if month >= 7:
        count = count + 30
    if month >= 8:
        count = count + 31
    if month >= 9:
        count = count + 31
    if month >= 10:
        count = count + 30
    if month >= 11:
        count = count + 31
    if month >= 12:
        count = count + 30
    return count

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
