# Programmer: Brayden Scheffers
# Date: 20.1.2023
# Program: InfoTech Center Upgrades

"""
Our Welcome Screen will start our Program letting
drivers know that the InfoTech Center 4.0 OS is loading.
"""

# Import Libraries Here
import time
import sys  # I imported the system library for further use in code.

"""
import time
time.sleep (secs) 
"""

x = 0
a = 0

print ("\n\nWelcome - InfoTech Center 4.0")

time.sleep (2)
print (" ")
while x != 20:
    x += 1
    b = ("Operation Fury OS is Loading " + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print(' Done')


