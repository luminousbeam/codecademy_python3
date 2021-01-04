#Strings and Conditionals
# Write a function called letter_check that takes two inputs, word and letter.
# This function should return True if the word contains the letter and False if it does not.

def letter_check(word, letter):
  for char in word:
    print(char)
    if char == letter:
      return True
  else:
    return False

print(letter_check("strawberry", "a"))

# Write a function called contains that takes two arguments, big_string and little_string and returns True if big_string contains little_string.
# For example contains("watermelon", "melon") should return True and contains("watermelon", "berry") should return False.
# Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.
# The letters in the returned list should be unique. For example:
# common_letters("banana", "cream") should return ['a'].

def common_letters(string_one, string_two):
    same = []
    for x in string_one:
        for y in string_two:
            if x == y:
                if x in same:
                    continue
                else:
                    same.append(x)
    return same


print(common_letters("strawberry", "banana"))
