#DICTIONARIES
import math

# Lab 3 - Road Trip
# Program determines the time it takes to complete a road trip from Chicago to other cities in the US
# and how many podcasts you can listen to on the road trip

# TODO: Add your name and the names of your team members
#Akio Pancho, Isaac, Justin 


# Get input from user of what city they would like to visit
city = input("What city would you like to visit? ")

distance_to_city = {
  'Chicago': 0,
  'Minneapolis': 410,
  'Columbus': 350, 
  'Nashville': 475,
  'Denver': 1005,
  'Portland': 2125,
  'Tampa': 1170
}

speed = 70 # miles per hour
hours_per_day = 8 # hours you can travel per day
podcast_length = 25 # minutes

# TODO: finish the code here
days = math.ceil((distance_to_city[city] / speed) / hours_per_day)
print('It will take ' + str(days) + ' day(s) to road trip from Chicago to', city)

time = (((distance_to_city[city] / speed) * 60) / 25)
print('Number of podcasts you can listen to:', int(time))




# NO CODE WRITING HERE. YOU ARE TO USE THE CONSOLE/TERMINAL FOR THIS SECTION

# We are going to use the following dictionary:

# # Dictionary of <city> paired with <distance> in miles to city
# # distances are from Chicago
# distance_to_city = {
#   'Chicago': 0,
#   'Minneapolis': 410,
#   'Columbus': 350, 
#   'Nashville': 475,
#   'Denver': 1005
# }

# A dictionary is a structure we can write in Python to keep a list of pairs linked together. In this case, we want to store a list of cities with their distances from Chicago. You’ll noticed the syntax includes:

# Curly brackets around the items
# Colon between each item in the pair
# Commas between each pair

# Below is where you can run python in the terminal. 
# Type and enter
# python3 
# into the terminal.

# If you see the >>> in the terminal, you have opened Python. Copy and paste the code above the defines the distance_to_city dictionary. Now, try a few things in the terminal to explore how the dictionary works.

# 1. Try printing the dictionary:
# print(distance_to_city)

# 2. Look up the distance to Minneapolis:
# distance_to_city['Minneapolis']

# 3. Look up the distance to Denver:
# distance_to_city['Denver']
