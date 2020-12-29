# You are adding students to a Poetry class, the size of which is capped at 6. While the length of the students_in_poetry list is less than 6, use .pop() to take a student off the all_students list and add it to the students_in_poetry list. Print the students_in_poetry list .

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

index = 0
while index < 6:
  students_in_poetry.append(all_students.pop())
  print(students_in_poetry)
  index +=1

# We have provided the list sales_data that shows the numbers of different flavors of ice cream sold at three different locations of the fictional shop, Gilbert and Ilbert's Scoop Shop. We want to sum up the total number of scoops sold. Start by defining a variable scoops_sold and set it to zero.

# Go through the sales_data list. Call each inner list location, and print out each location list.

# Within the sales_data loop, go through each location list and add the element to your scoops_sold variable.

# By the end, you should have the sum of every number in the sales_data nested list.

# Print out the value of scoops_sold.

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  for scoops in location:
    scoops_sold += scoops
print(scoops_sold) 

# We have defined a list heights of visitors to a theme park. In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters. Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.
# Print can_ride_coaster.

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

#One way to do it
# can_ride_coaster = []
# for height in heights:
#   if height > 161:
#     can_ride_coaster.append(height)
# print(can_ride_coaster)

#List comprehension way to do it
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

# We have provided a list of temperatures in celsius. Using a list comprehension, create a new list called fahrenheit that converts each element in the celsius list to fahrenheit.

# *Note: * To convert, use the formula:
# temperature_in_fahrenheit = temperature_in_celsius * 9/5 + 32

# Print fahrenheit.

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp_in_cel * 9/5 + 32 for temp_in_cel in celsius ]
print(fahrenheit)

# List comprehension example
desired_list = [i-1 for i in range(5)]
print(desired_list)

# Divisible by Ten
# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

# Return the count of how many numbers in the list are divisible by 10.

def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

# Greetings

# Create a function named add_greetings() which takes a list of strings named names as a parameter.

# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.

# Return the new list containing the greetings.

def add_greetings(names):
  greetings = []
  for name in names:
    greetings.append(f"Hello, {name}")
  return greetings

print(add_greetings(["Owen", "Max", "Sophie"]))

# Delete Starting Even Numbers

# Write a function called delete_starting_evens() that has a parameter named lst.

# The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.

# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

# Make sure your function works even if every element in the list is even!

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
print(delete_starting_evens([4, 5, 13]))


# Odd Indices

# Create a function named odd_indices() that has one parameter named lst.

# The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].