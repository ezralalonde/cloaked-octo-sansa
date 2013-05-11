# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

# this function is required, even though the problem statement doesn't mention it, the marker wants one.
def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    count = day_of_year(year2,month2,day2)
    count -= day_of_year(year1,month1,day1)
    while year1 < year2:
        count += day_of_year(year1, 12, 31)
        year1 = year1 + 1
    return count

def day_of_year(year, month, day):
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year):
        month_length[1] += 1
    return day + sum(month_length[:month-1])

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
