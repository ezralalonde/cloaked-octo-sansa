# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(nn):
    ii = 0
    result = 1
    while ii < nn:
        ii = ii + 1
        result = result * ii
    return result

#print factorial(4)
#>>> 24
#print factorial(5)
#>>> 120
#print factorial(6)
#>>> 720

