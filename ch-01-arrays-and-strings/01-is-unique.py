# Determine whether or not a given string contains no duplicate characters.

def contains_no_duplicates(string):
  letters = {}
  for letter in string:
    if letter in letters:
      return False
    letters[letter] = True
  return True

if __name__ == "__main__":
  import sys
  print(contains_no_duplicates(sys.argv[-1]))
    
contains_no_duplicates('fo')


letters={}

letters['f'] = True
