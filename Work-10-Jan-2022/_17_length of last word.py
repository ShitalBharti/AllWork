def last_word_length(my_string):
   init_val = 0

   processed_str = my_string.strip()

   for i in range(len(processed_str)):
      if processed_str[i] == " ":
         init_val = 0
      else:
         init_val += 1
   return init_val

my_input = "Hi how are you Will"
print("The string is :")
print(my_input)
print("The length of the last word is :")
print(last_word_length(my_input))


'''def length_of_last_word(s):
    words = s.split()
    if len(words) == 0:
        return 0
    return len(words[-1])


print(length_of_last_word("Python  ljlkfjkgjko Exercises "))
print(length_of_last_word("Python"))
print(length_of_last_word(""))
print(length_of_last_word("  "))'''