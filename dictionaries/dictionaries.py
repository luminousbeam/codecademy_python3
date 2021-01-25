# List Comprehensions to Dictionaries

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# print(zip(names, heights)) 
# zip creates tuples of items

students = { key:value for key, value in zip(names, heights) }

# print(students)

# You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each. First, create a variable called zipped_drinks that is a zipped list of pairs between the drinks list and the caffeine list.

# Create a dictionary called drinks_to_caffeine by using a list comprehension that goes through the zipped_drinks list and turns each pair into a key:value item.

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = { key:value for key, value in zipped_drinks }

# print(drinks_to_caffeine)

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

# print(plays)

plays["Purple Haze"] = 1
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}

# print(library)