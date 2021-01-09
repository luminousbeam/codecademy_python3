# List Comprehensions to Dictionaries

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# print(zip(names, heights)) 
# zip creates tuples of items

students = { key:value for key, value in zip(names, heights) }

print(students)

# You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each. First, create a variable called zipped_drinks that is a zipped list of pairs between the drinks list and the caffeine list.

# Create a dictionary called drinks_to_caffeine by using a list comprehension that goes through the zipped_drinks list and turns each pair into a key:value item.

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = { key:value for key, value in zipped_drinks }

print(drinks_to_caffeine)

# Review

# We are building a music streaming service. We have provided two lists, representing songs in a user's library and the amount of times each song has been played.

# Using a list comprehension, create a dictionary called plays that goes through zip(songs, playcounts) and creates a song:playcount pair for each song in songs and each playcount in playcounts.

# After printing plays, add a new entry to it. The entry should be for the song "Purple Haze" and the playcount is 1.

# This user has caught Aretha Franklin fever and listened to "Respect" 5 more times. Update the value for "Respect" to be 94 in the plays dictionary.

# Create a dictionary called library that has two key: value pairs:

# key "The Best Songs" with a value of plays, the dictionary you created
# key "Sunday Feelings" with a value of an empty dictionary

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = { song:playcount for song, playcount in zip(songs, playcounts) }

print(plays)

plays["Purple Haze"] = 1
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)

#One way to avoid getting an Invalid Key error, is to check if key is in dictionary. The if check prints value if found, otherwise returns False but avoids error

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"

if "energy" in zodiac_elements:
  print(zodiac_elements["energy"])

# Try/Except to get key

# Use a try block to try to print the caffeine level of "matcha". If there is a KeyError, print "Unknown Caffeine Level".

# Above the try block, add "matcha" to the dictionary with a value of 30.

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

# caffeine_level["matcha"] = 30

try:
  print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level")

# Safely get a key

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
building_heights.get("Shanghai Tower")

#this line will return None:
building_heights.get("My House")

building_heights.get('Shanghai Tower', 0)
# 632
building_heights.get('Mt Olympus', 0)
# 0
building_heights.get('Kilimanjaro', 'No Value')
# 'No Value'

# Use .get() to get the value of "teraCoder"'s user ID, with 100000 as a default value if the user doesn't exist. Store it in a variable called tc_id. Print tc_id to the console.

# Use .get() to get the value of "superStackSmash"'s user ID, with 100000 as a default value if the user doesn't exist. Store it in a variable called stack_id. Print stack_id to the console.

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)

print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)

print(stack_id)

# Delete a key using pop()

raffle = {
  223842: "Teddy Bear", 
  872921: "Concert Tickets", 
  320291: "Gift Basket", 
  412123: "Necklace", 
  298787: "Pasta Maker"
  }

raffle.pop(320291, "No Prize")
raffle.pop(100000, "No Prize")
print(raffle)

# You are designing the video game Big Rock Adventure. We have provided a dictionary of items that are in the player's inventory which add points to their health meter. In one line, add the corresponding value of the key "stamina grains" to the health_points variable and remove the item "stamina grains" from the dictionary. If the key does not exist, add 0 to health_points.

available_items = {
  "health potion": 10, 
  "cake of the cure": 5, 
  "green elixir": 20, 
  "strength sandwich": 25, 
  "stamina grains": 15, 
  "power stew": 30
  }

health_points = 20

if "stamina grains" in available_items:
  health_points += available_items["stamina grains"]
  available_items.pop("stamina grains")
else:
  health_points += 0

print(available_items)