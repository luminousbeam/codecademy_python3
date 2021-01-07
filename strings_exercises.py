#Strings and Conditionals
# Write a function called letter_check that takes two inputs, word and letter.
# This function should return True if the word contains the letter and False if it does not.

def letter_check(word, letter):
  for char in word:
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

first_name = "Jocelyn"
print(first_name[:3])

# Username & Password Generator
# Copeland's Corporate Company has finalized what they want their username and temporary password creation to be and have enlisted your help, once again, to build the function to generate them. In this exercise, you will create two functions, username_generator and password_generator.

# Let's start with username_generator. Create a function called username_generator take two inputs, first_name and last_name and returns a username. The username should be a slice of the first three letters of their first name and the first four letters of their last name. If their first name is less than three letters or their last name is less than four letters it should use their entire names.

# For example, if the employee's name is Abe Simpson the function should generate the username AbeSimp.


def username_generator(first_name, last_name):
  username = ""
  if len(first_name) < 3:
    username += first_name
  else:
    username += first_name[:3]

  if len(last_name) < 4:
    username += last_name
  else:
    username += last_name[:4]
  return username

print(username_generator("Abe", "Simpson"))

# Great work! Now for the temporary password, they want the function to take the input user name and shift all of the letters by one to the right, so the last letter of the username ends up as the first letter and so forth. For example, if the username is AbeSimp, then the temporary password generated should be pAbeSim.

# Start by defining the function password_generator so that it takes one input, username and in it define an empty string named password.

# Inside password_generator create a for loop that iterates through the indices username by going from 0 to len(username).

# To shift the letters right, at each letter the for loop should add the previous letter to the string password.


def password_generator(username):
  password = ""
  for i in range(len(username)):
    password += username[i - 1]
  return password

print(password_generator("AbeSimp"))


# Your boss at the Poetry organization sent over a bunch of author names that he wants you to prepare for importing into the database. Annoyingly, he sent them over as a long string with the names separated by commas.

# Using .split() and the provided string, create a list called author_names containing each individual author name as it's own string.

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

# print(author_names)
# ['Audre Lorde', 'Gabriela Mistral', 'Jean Toomer', 'An Qi', 'Walt Whitman', 'Shel Silverstein', 'Carmen Boullosa', 'Kamala Suraiyya', 'Langston Hughes', 'Adrienne Rich', 'Nikki Giovanni']

author_last_names = []
for author in author_names:
  author_name = author.split()
  author_last_names.append(author_name[1])

# print(author_last_names)
# ['Lorde', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya', 'Hughes', 'Rich', 'Giovanni']

# The organization has sent you over the full text for William Carlos Williams poem Spring Storm. They want you to break the poem up into its individual lines.

# Create a list called spring_storm_lines that contains a string for each line of Spring Storm.
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
# print(spring_storm_lines)

# You've been given a list, winter_trees_lines, that contains all the lines to William Carlos Williams poem, Winter Trees. You've been asked to join together the strings in the list together into a single string that can be used to display the full poem. Name this string winter_trees_full.

# Print your result to the terminal. Make sure that each line of the poem appears on a new line in your string.

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
# print(winter_trees_full)


# They sent over another list containing all the lines to the Audre Lorde poem, Love, Maybe. They want you to join together all of the lines into a single string that can be used to display the poem again, but this time, you've noticed that the list contains a ton of unnecessary whitespace that doesn't appear in the actual poem.

# First, use .strip() on each line in the list to remove the unnecessary whitespace and save it as a new list love_maybe_lines_stripped.

# .join() the lines in love_maybe_lines_stripped together into one large multi-line string, love_maybe_full, that can be printed to display the poem.

# Each line of the poem should show up on its own line.

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())

love_maybe_full = "\n".join(love_maybe_lines_stripped)

print(love_maybe_full)

# Review
# Preserve the Verse has one final task for you. They have delivered you a string that contains a list of poems, titled highlighted_poems, they want to highlight on the site, but they need your help to parse the string into something that can display the name, title, and publication date of the highlighted poems on the site.

# First, start by printing highlighted_poems to the terminal and see how it displays.

# The information for each poem is separated by commas, and within this information is the title of the poem, the author, and the date of publication.

# Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list.

# Print highlighted_poems_list, how does the structure of the data look now?

# Notice that there is inconsistent whitespace in highlighted_poems_list. Let's clean that up.

# Start by creating a new empty list, highlighted_poems_stripped.

# Then, iterate through highlighted_poems_list using a for loop and for each poem strip away the whitespace and append it to your new list, highlighted_poems_stripped.

# Print highlighted_poems_stripped.

# Looks good! All the whitespace is cleaned up.

# Next we want to break up all the information for each poem into it's own list, so we end up with a list of lists.

# Create a new empty list called highlighted_poems_details.

# Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into highlighted_poems_details.

# Great! Now we want to separate out all of the titles, the poets, and the publication dates into their own lists.

# Create three new empty lists, titles, poets, and dates.

# Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the lists titles, poets, and dates.

# For example, for the poem The Shadow (1915) by William Carlos Williams your code should be adding "The Shadow" to titles, "William Carlos Williams" to poets, and "1915" to dates.

# Finally, write a for loop that uses .format() to print out the following string for each poem:

# The poem TITLE was published by POET in DATE.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

# print(highlighted_poems_list)

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())

# print(highlighted_poems_stripped)

highlighted_poems_details = []

for details in highlighted_poems_stripped:
  highlighted_poems_details.append(details.split(':'))

# print(highlighted_poems_details)
titles = []
poets = []
dates = []

for item in highlighted_poems_details:
  titles.append(item[0])
  poets.append(item[1])
  dates.append(item[2])

# print(titles)
# print(poets)
# print(dates)

for i in range(len(titles)):
  title, poet, date = titles[i], poets[i], dates[i]
  print("The poem {} was published by {} in {}.".format(title, poet, date))
