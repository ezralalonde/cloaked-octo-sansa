#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

fibs = {0:0, 1:1}
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        if n not in fibs:
            fibs[n] = fibonacci(n-1) + fibonacci(n-2)
        return fibs[n]
        
print fibonacci(36)
#>>> 14930352
