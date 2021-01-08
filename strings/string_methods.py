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