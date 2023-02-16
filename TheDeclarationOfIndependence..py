# Programmer: Brayden Scheffers
# Date:  1.28.2023
# Program: InfoTech Center Upgrades

"""
Our Welcome Screen will start our Program letting
drivers know that the InfoTech Center 4.0 OS is loading.

"""

# Import Libraries Here
import time
import sys
import random
from time import sleep

# I imported the system library for further use in code.

"""
import time
time.sleep (secs) 
"""

x = 0
a = 0

#print ("\n\n\033[31mWelcome - InfoTech Center 4.0")

time.sleep (2)
while x != 20:
    x += 1
    b = ("Declaration of Independance OS is Loading " + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.1)
    if a == 4:
        a = 0
    if x == 20:
        print('\nDone\n\n')
        
sleep (1)
    
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
    
sleep (1)    

if current_time >= "18:00:00":
    print ("Your headlights have been automatically turned on and your speed has been limited to 45 MPH, due to limited vison.\n")
elif current_time <= "06:00:00":
    print ("Your headlights have been automatically turned on and your speed has been limited to 45 MPH, due to limited vison.\n")

# Programmer: Brayden Scheffers
# Date: 2.6.2023
# Merged Welcome Screen and Gasoline Branches - Stable

"""
We will create a Function that will tell us our Fuel Gauge level
    -Create a List with Gas Levels
    -Randomize and choose from the List to determine our gas lever
"""


# Programmer: Brayden Scheffers
# Date: 30.1.2023
# Program: InfoTech Center 4.0 - Gasoline

"""
Create a Function to determine our closest Gas Station
    -Create a List of Gas Stations
    -Randomly choose a Gas Station from the List

    Create a Function to determine our Gas Level and closest Gas Station
    -Print Gas Level
    -Print Closest Gas Station
"""


# Create a Gas Level Function

def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter","Half","Three Quarter", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calling gasLevelGauge Function to store its value
gasLevelIndicator = gasLevelGauge()

# List of Gas Stations

def listOfGasStations():
    gasStations = ["Shell","Costco","Bucc-ee's","Speedway","7/11","Circle-K","Meijer","Marathon"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby
    
# Determine Gas Level and Closest Gas Station

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),2)
    milesToGasStationQuarter = round(random.uniform(26,50),2)
    if gasLevelIndicator == "Empty":
        print("***WARNING YOUR VEHICLE IS EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***WARNING***")
        sleep(1)
        print("Your gas tank is depleting, checking for closest gas station.")
        sleep(1)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter":
        print("***WARNING***")
        sleep(1)
        print("Your tank is at a Quarter, and the closest Gas Station is",listOfGasStations(),"which is",milesToGasStationQuarter, "miles away.")
    elif gasLevelIndicator == "Half":
        print("Your Gas Tank is Half full")
    elif gasLevelIndicator == "Three Quarter":
        print("Your Gas Tank is at Three Quarters, you have enough Gas to travel today.")
    else:
        print("You Gas Tank is Full, you have enough Gas to travel today.")


# Programmer: Brayden Scheffers
# Date: 8.2.2023
# Program: Weather System Updates

# Create Weather conditions in a list and choose it randomnly 
def weather():
    weatherForecast = ["Snow","Blizzard","Rain","Fog","Wind","Ice","Sunny"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

# Variable to call weather function once in out VRS system 
weatherAlert = weather()

# VRS function to respond to the weather conditions 
def vRS():
    if weatherAlert == "Snow":
        print ("National Weather Service has changed your Alarm by 15 minuites due to the harsh conditions and weather forecast of", weatherAlert,"\n")
        print ("VRS has been engaged, only allowing your vecihle to travel at 45 MPH")
    elif weatherAlert == "Blizzard":
        print ("National Weather Service has changed your Alarm by 35 minuites due to the harsh conditions and weather forecast of", weatherAlert,"\n")
        print ("VRS has been engaged, only allowing your vecihle to travel at 30 MPH")
    elif weatherAlert == "Rain":
        print ("National Weather Service is recommending slower speeds and more caution, due to the harsh conditions and weather forecast of", weatherAlert,"\n")
    elif weatherAlert == "Fog":
        print ("National Weather Service is recommending slower speeds and more caution, due to the harsh conditions, reduced vision and a weather forecast of", weatherAlert,"\n")
    elif weatherAlert == "Wind":
        print ("National Weather Service is recommending slower speeds and more caution, due to the harsh conditions, reduced vision and a weather forecast of", weatherAlert,"\n")  
    elif weatherAlert == "Ice":
        print ("National Weather Service has changed your Alarm by 20 minuites and is recommending slower speeds and more caution, due to the harsh conditions, reduced traction and a weather forecast of", weatherAlert)        
        print ("VRS has been engaged, only allowing your vecihle to travel at 30 MPH\n")      
    else:
        print ("The weather is", weatherAlert,", although there are no harsh weather conditions, still drive safely and responsibily.\n")       
    
# Call Function Here  
while x != 30:
    x += 1
    b = ("National Weather Service is checking conditions " + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.1)
    if a == 4:
        a = 0
    if x == 30:
        print('\n')
sleep (1)
vRS()
while x != 40:
    x += 1
    b = ("Checking Gas Levels " + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.1)
    if a == 4:
        a = 0
    if x == 40:
        print('\n')
        
sleep (1)
gasLevelAlert()
