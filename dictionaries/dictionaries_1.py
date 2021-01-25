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

# print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)

# print(stack_id)

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
# print(raffle)

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

#Get all keys using list() and keys() on dictionary
#list() creates a new list of student names, once you loop over disctionary using .keys() you can print out student names
# .values() prints all of the dictionary's values

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

print(list(test_scores))

for student in test_scores.keys():
  print(student)

#if you would like to create a list of values, do it this way
print(list(test_scores.values()))

# for score_list in test_scores.values():
#   print(score_list)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

users = user_ids.keys()
print(users)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

lessons = num_exercises.keys()
print(lessons)

# Get all items by using .items() on a dictionary, it outputs a tuple (key, value)

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
 
for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")


pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, num_women in pct_women_in_occupation.items():
  print(f'Women make up {num_women} percent of {occupation}s.')

#Review
#We have provided a pack of tarot cards, tarot. You are going to do a three card spread of your past, present, and future.

# Create an empty dictionary called spread.

# The first card you draw is card 13. Pop the value assigned to the key 13 out of the tarot dictionary and assign it as the value of the "past" key of spread.

# The second card you draw is card 22. Pop the value assigned to the key 22 out of the tarot dictionary and assign it as the value of the "present" key of spread.

# The third card you draw is card 10. Pop the value assigned to the key 10 out of the tarot dictionary and assign it as the value of the "future" key of spread.

# Iterate through the items in the spread dictionary and for each key: value pair, print out a string that says:

# Your {key} is the {value} card.

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread['past'] = tarot.pop(13)

spread['present'] = tarot.pop(22)

spread['future'] = tarot.pop(10)

for key, value in spread.items():
  print(f'Your {key} is the {value} card.')