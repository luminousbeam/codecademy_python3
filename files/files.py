# Reading file
with open('files/test_files/welcome.txt') as text_file:
  text_data = text_file.read()
  print(text_data)

# Iterating through lines
with open('files/test_files/how_many_lines.txt') as lines_doc:
  for line in lines_doc:
    print(line)

# Reading a line
with open('files/test_files/just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)

# Writing a file
with open('files/test_files/bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write("Nickelback")

# Appending to a file
with open('files/test_files/cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write("Air Buddy")

# Older way of writing and appending files, have to close() them after
fun_cities_file = open('files/test_files/fun_cities.txt', 'a')
fun_cities_file.write("Montréal")
fun_cities_file.close()