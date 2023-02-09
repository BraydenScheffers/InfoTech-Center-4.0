# Programmer: Brayden Scheffers
# Date: 8.2.2023
# Program: Weather System Updates

# Import Libraries Here
import random

# Create Weather conditions in a list and choose it randomnly 
def weather():
    weatherForecast = ["Snowing","Blizzard","Raining","Foggy","Windy","Icy","Sunny"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

# Variable to call weather function once in out VRS system 
weatherAlert = weather()

print (weatherAlert) 
# VRS function to respond to the weather conditions 
def vRS():
    print 