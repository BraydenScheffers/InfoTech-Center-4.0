# Programmer: Brayden Scheffers
# Date: 8.2.2023
# Program: Weather System Updates

# Import Libraries Here
import random

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
        print ("\nNational Weather Service has changed your Alarm by 15 minuites due to the harsh conditions and weather forecast of", weatherAlert)
        print ("VRS has been engaged, only allowing your vecihle to travel at 45 MPH")
    elif weatherAlert == "Blizzard":
        print ("\nNational Weather Service has changed your Alarm by 35 minuites due to the harsh conditions and weather forecast of", weatherAlert)
        print ("VRS has been engaged, only allowing your vecihle to travel at 30 MPH")
    elif weatherAlert == "Rain":
        print ("\nNational Weather Service is recommending slower speeds and more caution, due to the harsh conditions and weather forecast of", weatherAlert)
    elif weatherAlert == "Fog":
        print ("\nNational Weather Service is recommending slower speeds and more caution, due to the harsh conditions, reduced vision and a weather forecast of", weatherAlert)
    elif weatherAlert == "Wind":
        print ("\nNational Weather Service is recommending slower speeds and more caution, due to the harsh conditions, reduced vision and a weather forecast of", weatherAlert)  
    elif weatherAlert == "Ice":
        print ("\nNational Weather Service has changed your Alarm by 20 minuites and is recommending slower speeds and more caution, due to the harsh conditions, reduced traction and a weather forecast of", weatherAlert)        
        print ("VRS has been engaged, only allowing your vecihle to travel at 30 MPH")      
    else:
        print ("\nThe weather is", weatherAlert,", although there are no harsh weather conditions, still drive safely and responsibily.")       
        
vRS()