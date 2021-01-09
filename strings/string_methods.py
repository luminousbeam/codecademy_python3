# Count Letters
# Write a function called unique_english_letters that takes the string word as a parameter. The function should return the total number of unique letters in the string. Uppercase and lowercase letters should be counted as different letters.

# We've given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to include that list in your function.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  count = 0
  for i in range(len(letters)):
    if letters[i] in word:
      count += 1
  return count

print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# Count X
# Write a function named count_char_x that takes a string named word and a single character named x as parameters. The function should return the number of times x appears in word.

def count_char_x(word, x):
  count = 0
  for letter in word:
    if x == letter:
      count += 1
  return count

print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

# Count Multi X
# Write a function named count_multi_char_x that takes a string named word and a string named x. This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. However, this time, make sure your function works when x is multiple characters long.

# For example, count_multi_char_x("Mississippi", "iss") should return 2

def count_multi_char_x(word, x):
  split_word = word.split(x)
  print(split_word)
  joined = "".join(split_word)
  print(joined)
  return (len(word) - len(joined))//len(x)

print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

# Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.

# For example, substring_between_letters("apple", "p", "e") should return "pl".

def substring_between_letters(word, start, end):
  if start not in word or end not in word:
    return word
  else:
    start_index = word.find(start)
    end_index = word.find(end)
    return word[start_index + 1:end_index]

print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# X Length
# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. This function should return True if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence, x):
  sentence_split = sentence.split()
  for word in sentence_split:
    if len(word) >= x:
      return True
    else:
      return False

print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

# Check name
# Write a function called check_for_name that takes two strings as parameters named sentence and name. The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. The function should return False otherwise.

# For example, the following three calls should all return True:

# check_for_name("My name is Jamie", "Jamie")
# check_for_name("My name is jamie", "Jamie")
# check_for_name("My name is JAMIE", "Jamie")

def check_for_name(sentence, name):
  if name.lower() in sentence.lower():
    return True
  else:
    return False

print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

#Every other letter
# Create a function named every_other_letter that takes a string named word as a parameter. The function should return a string containing every other letter in word.

def every_other_letter(word):
  new_word = ""
  for i in range(0, len(word), 2):
    new_word += word[i]
    print(word[i])
  return new_word

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

# Reverse
# Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

def reverse_string(word):
  reversed_word = ""
  for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
  return reversed_word

print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# Make Spoonerism
# A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism is made when someone says "Belly Jeans" instead of "Jelly Beans".

# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. Finding the first syllable of a word is a difficult task, so for our function, we're going to switch the first letters of each word. Return the two new words as a single string separated by a space.

def make_spoonerism(word1, word2):
  new_word1 = word2[0]  + word1[1:]
  new_word2 = word1[0] + word2[1:] 
  return "{} {}".format(new_word1, new_word2)

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

# Add Exclamation
# Create a function named add_exclamation that has one parameter named word. This function should add exclamation points to the end of word until word is 20 characters long. If word is already at least 20 characters long, just return word.

def add_exclamation(word):
  word_length = len(word)
  if word_length < 20:
    exclamation = 20 - word_length
    return word + ("!" * exclamation)
  else:
    return word

print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn