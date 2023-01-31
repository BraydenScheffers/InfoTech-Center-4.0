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


# Create a Gas Level Function

def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter","Half","Three Quarter", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

print (gasLevelGauge())

def listOfGasStations():
    gasStations = ["Shell","Costco","Bucc-ee's","Speedway","7/11","Circle-K","Meijer","Marathon"]
    gasStationNearby =random.choice(gasStations)
    return gasStationNearby
    
 print (listofGasStations())
