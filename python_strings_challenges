# Write a function called unique_english_letters that takes the string word as a parameter. 
# The function should return the total number of unique letters in the string. 
# Uppercase and lowercase letters should be counted as different letters. 
# We’ve given you a list of every uppercase and lower case letter in the English alphabet. 
# It will be helpful to include that list in your function.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  counter = 0
  unique_letters = ''
  for letter in letters:
    if (letter in word):
      counter += 1
  return counter

# Tests
print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))


#Write a function named count_char_x that takes a string named word and a single character named x as parameters. 
# The function should return the number of times x appears in word.

# Write your count_char_x function here:
def count_char_x(word, x):
  counter = 0
  for letter in word:
    if letter == x:
      counter += 1
  return counter

# Tests:
print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))

#Write a function named count_multi_char_x that takes a string named word and a string named x. 
# This function should do the same thing as the count_char_x function you just wrote - it should return the number of times x appears in word. 
# However, this time, make sure your function works when x is multiple characters long.

def count_multi_char_x(word, x):
  split_word_len = len(word.split(x)) - 1
  return split_word_len


# Tests:
print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))

#Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. 
# This function should return the substring between the first occurrence of start and end in word. 
# If start or end are not in word, the function should return word.

def substring_between_letters(word, start, end):
  start_idx = word.find(start)
  end_idx = word.find(end)
  if start_idx > -1 and end_idx > -1:
    return word[start_idx+1:end_idx]
  else:
    return word

# Tests:
print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))

#Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. 
# This function should return True if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence, x):
  sentence_splited = sentence.split()
  for word in sentence_splited:
    if len(word) < x:
      return False
  return True

# Tests:
print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))

#Write a function called check_for_name that takes two strings as parameters named sentence and name. 
# The function should return True if name appears in sentence in all lowercase letters, all uppercase letters, or with any mix of uppercase and lowercase letters. 
# The function should return False otherwise.

def check_for_name(sentence, name):
  if name.lower() in sentence.lower():
    return True
  return False

# Tests:
print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))

#Create a function named every_other_letter that takes a string named word as a parameter. 
# The function should return a string containing every other letter in word.

def every_other_letter(word):
  every_other_letter = ""
  for index in range(0,len(word),2):
    every_other_letter += word[index]
  return every_other_letter

# Tests:
print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))

#Write a function named reverse_string that has a string named word as a parameter. 
# The function should return word in reverse.

def reverse_string(word):
  reverse_word = ""
  for index in range((len(word)-1),-1,-1):
    reverse_word += word[index]
  return reverse_word
# Tests:
print(reverse_string("Codecademy"))
print(reverse_string("Hello world!"))
print(reverse_string(""))

#Write a function called make_spoonerism that takes two strings as parameters named word1 and word2.
#Finding the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word. 
#Return the two new words as a single string separated by a space.

def make_spoonerism(word1, word2):
  spoonerism = (word2[0] + word1[1:]) + " " + (word1[0]+ word2[1:])
  return spoonerism


# Tests:
print(make_spoonerism("Codecademy", "Learn"))
print(make_spoonerism("Hello", "world!"))
print(make_spoonerism("a", "b"))

#Create a function named add_exclamation that has one parameter named word. 
# This function should add exclamation points to the end of word until word is 20 characters long. 
# If word is already at least 20 characters long, just return word.

def add_exclamation(word):
  counter = len(word)
  if len(word) >= 20:
    return word
  else:
    while counter < 20:
      word += "!"
      counter += 1
    return word
  
# Tests:
print(add_exclamation("Codecademy"))
print(add_exclamation("Codecademy is the best place to learn"))



