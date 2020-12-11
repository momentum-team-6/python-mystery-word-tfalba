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

