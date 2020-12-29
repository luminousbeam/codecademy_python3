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
    greetings.append("Hello, " + name)
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
#One way to do it
# def odd_indices(lst):
#     new_lst = []
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             new_lst.append(lst[i])
#     return new_lst

#Second way to do it
# def odd_indices(lst):
#     new_lst = []
#     for index in range(1, len(lst), 2):
#         new_lst.append(lst[index])
#     return new_lst

#Third way to do it
def odd_indices(lst):
    new_lst = [lst[index] for index in range(1, len(lst), 2)]
    return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))

#Exponents
# Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

# For example, consider the following code.

# exponents([2, 3, 4], [1, 2, 3])
# the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. Then two to the third, and so on.

#One way to do it
# def exponents(bases, powers):
#   exponential = []
#   for base in bases:
#     for power in powers:
#       exponential.append(base ** power)
#   return exponential

#Second way to do it
def exponents(bases, powers):
    exponential = [ base ** power for base in bases for power in powers]
    return exponential

print(exponents([2, 3, 4], [1, 2, 3]))

#Larger Sum
# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for x in lst1:
        sum1 += x
    for y in lst2:
        sum2 += y
    if sum1 > sum2:
        return lst1
    elif sum1== sum2:
        return lst1
    else:
        return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))

# Over 9000

# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.

# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

def over_nine_thousand(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]   
        if sum > 9000:
            return sum
    return sum

print(over_nine_thousand([8000, 900, 120, 5000]))

#Max Num
# Create a function named max_num() that takes a list of numbers named nums as a parameter.

# The function should return the largest number in nums

def max_num(nums):
    max = nums[0]
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]
    return max

print(max_num([50, -10, 0, 75, 20]))

# Same Values
# Write a function named same_values() that takes two lists of numbers of equal size as parameters.

# The function should return a list of the indices where the values were equal in lst1 and lst2.

# For example, the following code should return [0, 2, 3]
