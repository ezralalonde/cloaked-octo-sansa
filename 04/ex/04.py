# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def convert_to_bits(number, unit):
    power = 10
    if unit[0] == 'M':
        power = 20
    if unit[0] == 'G':
        power = 30
    if unit[0] == 'T':
        power = 40
    multiplier = 1
    if unit[1] == 'B':
        multiplier = 8
    return 2 ** power * multiplier * number

def get_hours(seconds):
    hours = seconds / 3600
    if int(hours) == 1:
        return "1 hour"
    return "%d hours" % (hours)

def get_seconds(seconds):
    seconds = seconds % 60
    out = "%s " % (seconds)
    if out[-3:] == ".0 ":
        out = "%d " % (seconds)
    if out[0:2] == "1 ":
        return "1 second"
    return out + "seconds"

def get_minutes(seconds):
    minutes = (seconds / 60) % 60
    if int(minutes) == 1:
        return "1 minute"
    return "%d minutes" % (minutes)

def download_time(size, size_unit, speed, speed_unit):
    filesize = convert_to_bits(size, size_unit)
    bandwidth = convert_to_bits(speed, speed_unit)
    time = 1.0 * filesize / bandwidth
    return "%s, %s, %s" % (get_hours(time), get_minutes(time), get_seconds(time))

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5,'MB')
#>>> 0 hours, 37 minutes, 32.8 seconds

print download_time(10, 'GB', 2, 'MB')
#>>> 1 hour, 25 minutes, 20 seconds
