# You must always instantiate a class
# Class methods w/arguments

class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile
 
converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"


# It’s March 14th (known in some places as Pi day) at Jan van High, and you’re feeling awfully festive. You decide to create a program that calculates the area of a circle.
# Create a Circle class with class variable pi. Set pi to the approximation 3.14.
# Give Circle an area method that takes two parameters: self and radius.
# Return the area as given by this formula: area = pi * radius ** 2
# Create an instance of Circle. Save it into the variable circle.
# You go to measure several circles you happen to find around.
# A medium pizza that is 12 inches across.
# Your teaching table which is 36 inches across.
# The Round Room auditorium, which is 11,460 inches across.
# You save the areas of these three things into pizza_area, teaching_table_area, and round_room_area.
# *Remember that the radius of a circle is half the diameter. We gave three diameters here, so halve them before you calculate the given circle’s area.

class Circle:
  pi = 3.14

  def area(self, radius):
    return self.pi * radius ** 2

circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)
print(pizza_area)
print(teaching_table_area)
print(round_room_area)

# Constructors
class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:
      # then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"
shout2 = Shouter("shout")
# prints "SHOUT"
shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

class Circled:
  pi = 3.14
  # Add constructor here:
  def __init__(self, diameter):
    print(f"New circle with diameter: {diameter}")

teaching_table = Circled(36)

# Instance variables
class FakeDict:
  pass

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()
 
fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"
# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"

class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

# Attribute functions
class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()
try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")
# prints "This text gets printed!"

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")
'''
<class 'dict'> does not have the count attribute :(
<class 'str'> has the count attribute!
<class 'int'> does not have the count attribute :(
<class 'list'> has the count attribute!
'''