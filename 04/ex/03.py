# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3

def convert_seconds(seconds):
    hour = int(seconds / 3600)
    minute = int(seconds / 60) % 60
    seconds = seconds * 10 - 10 * (hour * 3600 + minute * 60)
    ss, sh, sm = "seconds", "hours", "minutes"
    if hour == 1:
        sh = "hour"
    if minute == 1:
        sm = "minute"
    if seconds == 10:
        ss = "second"
    if seconds % 10 == 0:
        seconds = seconds / 10
        outseconds = "%d %s" % (seconds, ss)
    else:
        seconds = seconds / 10.
        outseconds = "%.1f %s" % (seconds, ss)
    
    return "%d %s, %d %s, %s" % (hour, sh, minute, sm, outseconds)


print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
