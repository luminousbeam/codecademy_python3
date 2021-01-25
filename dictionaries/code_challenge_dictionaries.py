# Sum Values
# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return the sum of the values of the dictionary

def sum_values(my_dictionary):
  sum = 0
  for value in my_dictionary.values():
    sum += value
  return sum


print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

# Even Keys
# Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter. This function should return the sum of the values of all even keys.

def sum_even_keys(my_dictionary):
  sum = 0
  for key, val in my_dictionary.items():
    if key % 2 == 0:
      sum += val
  return sum

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

# Add Ten
# Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. The function should add 10 to every value in my_dictionary and return my_dictionary

def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

# Values that are keys
# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. This function should return a list of all values in the dictionary that are also keys.

def values_that_are_keys(my_dictionary):
  same = []
  for val in my_dictionary.values():
    for key in my_dictionary.keys():
      if val == key:
        same.append(val)
  return same

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# Largest Value
# Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary.

def max_key(my_dictionary):
  max = 0
  max_key = 0
  for key, val in my_dictionary.items():
    if val > max:
      max = val
      max_key = key
  return max_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

# Word length dict
# Write a function named word_length_dictionary that takes a list of strings named words as a parameter. The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.

def word_length_dictionary(words):
  word_len = []
  for word in words:
    word_len.append(len(word))
  word_and_len = {key:val for key, val in zip(words, word_len)}
  return word_and_len

print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

#Frequency count
# Write a function named frequency_dictionary that takes a list of elements named words as a parameter. The function should return a dictionary containing the frequency of each element in words.

def frequency_dictionary(words):
  unique_words = []
  word_count = []
  for word in words:
    if word not in unique_words:
      unique_words.append(word)
  for unique in unique_words:
    word_count.append(words.count(unique))
  freq_dict = {key:val for key, val in zip(unique_words, word_count)}
  return freq_dict

print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

#Unique values
# Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. The function should return the number of unique values in the dictionary.

def unique_values(my_dictionary):
  dict_values = []
  special_values = []
  for val in my_dictionary.values():
    dict_values.append(val)
  for item in dict_values:
    if item not in special_values:
      special_values.append(item)
  return len(special_values)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

#Count first letter
# Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might look like this:
# names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
# The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.

# So in example above, the function would return:
# {"S" : 4, "L": 3}

def count_first_letter(names):
  result = {}
  for key,value in names.items():
    # dictionary.get(keyname, value)
    #keyname -	Required. The keyname of the item you want to return the value from
    #value -	Optional. A value to return if the specified key does not exist. Default value 'None'
    result[key[0]]=len(value)+result.get(key[0],0)
  return result

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
