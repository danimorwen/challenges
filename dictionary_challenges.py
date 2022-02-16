#Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. 
# The function should return the sum of the values of the dictionary

def sum_values(my_dictionary):
  sum_values = 0
  for value in my_dictionary.values():
    sum_values += value
  return sum_values

#Tests:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
print(sum_values({10:1, 100:2, 1000:3}))

#Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter. 
#This function should return the sum of the values of all even keys.

def sum_even_keys(my_dictionary):
  total_sum = 0
  for key, value in my_dictionary.items():
    if key % 2 == 0:
      total_sum += value
  return total_sum

#Tests:
print(sum_even_keys({1:5, 2:2, 3:3}))
print(sum_even_keys({10:1, 100:2, 1000:3}))

#Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. 
#The function should add 10 to every value in my_dictionary and return my_dictionary

def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

#Tests:
print(add_ten({1:5, 2:2, 3:3}))
print(add_ten({10:1, 100:2, 1000:3}))

#Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
#This function should return a list of all values in the dictionary that are also keys.

def values_that_are_keys(my_dictionary):
  values_that_are_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      values_that_are_keys.append(value)
  return values_that_are_keys

#Tests:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))

#Write a function named max_key that takes a dictionary named my_dictionary as a parameter. 
#The function should return the key associated with the largest value in the dictionary.

def max_key(my_dictionary):
  max_value = 0
  largest_key = 0
  for key, value in my_dictionary.items():
    if value > max_value:
      max_value = value
      largest_key = key
  return largest_key

#Tests:
print(max_key({1:100, 2:1, 3:4, 4:10}))
print(max_key({"a":100, "b":10, "c":1000}))

#Write a function named word_length_dictionary that takes a list of strings named words as a parameter. 
#The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.

def word_length_dictionary(words):
  my_dictionary = {}
  for word in words:
    my_dictionary[word] = len(word)
  return my_dictionary

#Tests:
print(word_length_dictionary(["apple", "dog", "cat"]))
print(word_length_dictionary(["a", ""]))

#Write a function named frequency_dictionary that takes a list of elements named words as a parameter. 
#The function should return a dictionary containing the frequency of each element in words.

def frequency_dictionary(words):
  my_dictionary = {}
  for word in words:
    if word not in my_dictionary.keys():
      my_dictionary[word] = 1
    elif word in my_dictionary.keys():
      my_dictionary[word] += 1
  return my_dictionary

#Tests:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0,0,0,0,0]))

#Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. 
#The function should return the number of unique values in the dictionary.

def unique_values(my_dictionary):
  unique_values = []
  for value in my_dictionary.values():
    if value not in unique_values:
      unique_values.append(value)
  return len(unique_values)


#Tests:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
print(unique_values({0:3, 1:3, 4:3, 5:3}))

#Create a function named count_first_letter that takes a dictionary named names as a parameter. 
#names should be a dictionary where the key is a last name and the value is a list of first names. 
# For example, the dictionary might look like this:
#names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
#The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.
#So in example above, the function would return:
#{"S" : 4, "L": 3}

def count_first_letter(names):
  new_dictionary = {}
  for key in names.keys():
    if key[0] not in new_dictionary:
      new_dictionary[key[0]] = len(names[key])
    elif key[0] in new_dictionary:
      new_dictionary[key[0]] += len(names[key])
  return new_dictionary
#Tests:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))