# Programmer: Brayden Scheffers
# Date: 30.1.2023
# Program: InfoTech Center 4.0 - Gasoline

"""
We will create a Function that will tell us our Fuel Gauge level
    -Create a List with Gas Levels
    -Randomize and choose from the List to determine our gas lever

Create a Function to determine our closest Gas Station
    -Create a List of Gas Stations
    -Randomly choose a Gas Station from the List

    Create a Function to determine our Gas Level and closest Gas Station
    -Print Gas Level
    -Print Closest Gas Station
"""

# Import Libraries Here
import random
from time import sleep

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

gasLevelAlert()