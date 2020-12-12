alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet = ' '.join(alphabet).lower()
alphabet = alphabet.split()

guessed = []
input_words = []
subset_words = []

words = open('words.txt', 'r').read().lower()
words = words.split()
#set_word_length = int(input('Choose number of letters in word: '))

def printAllKLength(set, k): 
    n = len(set)  
    printAllKLengthRec(set, "", n, k) 
  
# The main recursive method 
# to print all possible  
# strings of length k 

def printAllKLengthRec(set, prefix, n, k): 
  # Base case: k is 0, 
  # print prefix 
  if (k == 0) : 
    print(prefix)
    return
  
    # One by one add all characters  
    # from set and recursively  
    # call for k equals to k-1 
  for i in range(n): 
  
    # Next character of input added 
    newPrefix = prefix + set[i] 
    #print(newPrefix)

    # k is decreased, because  
    # we have added a new character 

    printAllKLengthRec(set, newPrefix, n, k - 1) 

set1 = ['a', 'b']
set2 = ['a', 'b', 'c', 'd']
set3 = ['a', 'b', 'c', 'd', 'o']
k = 3
print(printAllKLength(set3, 3))
#printAllKLength(set1, 4)
