alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_str = ' '.join(alphabet).lower()
alphabet = alphabet_str.split()

guessed = []
input_words = []
subset_words = []

words = open('words.txt', 'r').read().lower()
words = words.split()

word_length = 6
s = [set() for i in range(word_length)]

letter = 's'
remaining_letters = alphabet_str.replace(letter, '')
students = [remaining_letters]
students = [letter, '*', 'a']
appearance_count = 2        #loop over appearance_count from i to word_length -- find max of all including case with o

possible_pairings = [(s1, s2, s3, s4, s5, s6, ) for s1 in students for s2 in students for s3 in students for s4 in students for s5 in students for s6 in students]
#possible_pairings = [(s1, s2, s3, s4) for s1 in students for s2 in students for s3 in students for s4 in students]

pair_pattern = []
for pair in possible_pairings:
  if pair.count(letter)==appearance_count:
    #print(pair)
    pair = ''.join(pair)
    #print(pair)
    pair_pattern.append(pair)
#print(pair_pattern)

# -------------------------------------------------------------------------------------------------------------------- #
#                         Python3 program to print all the strings that match the given pattern                        #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
#               where every character in the pattern is uniquely mapped to a character in the dictionary               #
# -------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------ Function to encode given string ----------------------------------------- #

def encodeString(Str):
  map = {}
  res = ""
  i = 0
    
  for ch in Str:                              # For each character in given string 
    if ch == '*':                             # If the character is not set give it an incremental value
      map[ch] = i
      i += 1
        #If the character is not the key letter - assign it an incremental value number to that char - no uniqueness necessary
    #if ch not in map:
    elif ch not in map:                       # If the character is set and not yet in map assign it a value
      map[ch] = i
      i += 1                                    
    res += str(map[ch])                       # Append the number associate with current character into the output string 
  return res

# Function to print all the strings that match the given pattern where every character in the pattern is uniquely mapped to a character in the dictionary 
def find_matched_words(dict, pattern):
    # len is length of the pattern 
    Len = len(pattern)
    # Encode the string
    hash = encodeString(pattern)
    # For each word in the dictionary  
    counter = 0
    for word in dict:
        # If size of pattern is same as size of current dictionary word and both pattern and the word has same hash, append (or print) the word 
      if(len(word) == Len and
        encodeString(word) == hash):
          print(hash, word, end = " ")
          counter += 1
    #print(counter)

working_list = []
for word in words:
  if len(word)==word_length and word.count(letter)==appearance_count and word not in working_list:
    working_list.append(word)

dict = working_list    #this will contain all words of set length containing at least 1, 2, 3, appearences etc.

for i in range(len(pair_pattern)):
  #print(pair_pattern[i])
  find_matched_words(dict, pair_pattern[i])
  #print(i, pair_pattern[i])
  #print('')

# This code for findMatchedWords is contributed by avanitrachhadiya2155









#   for word in words
#   if guess in word
#     add to dictionary if count of letter in words is 1, 2, 3, ... length
#     so, for a guess of letter 'o', create dictionary dict1, dict2, dict3, etc up to length of word
#     with each dictionary can then track patterns and find sub-dict1a, sub-dict1b, etc that match patterns
#     for a word of length 4, this would be for dict2 (with 2 occurences of 'o') pattern-a (oo##, o##o, o#o#, #o#o, #oo#, ##oo)
#     patterns could be defined with functions above where the set is 'o' and '*'




# def printAllKLength(set, k): 
#     n = len(set)  
#     printAllKLengthRec(set, "", n, k) 
  
# # The main recursive method 
# # to print all possible  
# # strings of length k 

# def printAllKLengthRec(set, prefix, n, k): 
#   # Base case: k is 0, 
#   # print prefix 
#   if (k == 0): 
#     print(prefix)
#     # One by one add all characters  
#     # from set and recursively  
#     # call for k equals to k-1 
#   for i in range(n): 
  
#     # Next character of input added 
#     newPrefix = prefix + set[i] 
#     #print(newPrefix)

#     # k is decreased, because  
#     # we have added a new character 

#     printAllKLengthRec(set, newPrefix, n, k - 1) 

# #printAllKLength(set4, 4)
