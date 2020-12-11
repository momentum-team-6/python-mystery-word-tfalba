import curses, sys 
curses.setupterm() 
clear = str(curses.tigetstr('clear'), 'ascii') 

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
guessed = []
input_words = []
subset_words = []

words = open('words.txt', 'r').read().lower()
words = words.split()
set_word_length = int(input('Choose number of letters in word: '))

# new list with only words with set_word_length letters and removing dups
[subset_words.append(word) for word in words if len(word) == set_word_length and word not in subset_words]

# this code removes any word with multiple occurences of a letter and saves it in new list input_words
# it is ugly but it works
counter = 0
for word in subset_words:
  for letter in word:
    if word.count(letter) > 1:
      word = word.replace(letter, '?')
  # [word.replace(letter, '?') for letter in word if word.count(letter) > 1]
  # why doesn't the above work?
  if '?' not in word:
    input_words.append(word)
# new_input_words = []
# #[input_words.remove(word) for word in input_words if '?' in word]
# # why doesn't the above work??
# [new_input_words.append(word) for word in input_words if '?' not in word]
# input_words = new_input_words

## add set split to choose max over position of letter 
## for instance if a is selected, compare all a in first position, all a in secon
## and so on... see if the max of those sets is greater than alt set
display = '_ '*set_word_length
display = display.split()

guess=''
while len(guessed) < 27:
  input_words_dict = {letter: input_words.count(letter) for letter in input_words}
  input_words_dict_alt = []
  for word in input_words:
    input_words_dict_alt.append({letter: word.count(letter) for letter in word})

  alt_sub_input_words = []
  guess = input('enter a guess: ').lower()
  #create empty list of lists for each possible position
  sub_input_words=[ [] for i in range(set_word_length)]
  position = [ [] for i in range(set_word_length)]
  

  for sub in input_words:
    if guess in sub:
      [sub_input_words[i].append(sub) for i in range(set_word_length) if guess == sub[i]]
      [position[i].append(i) for i in range(set_word_length) if guess == sub[i]]
    else:
      alt_sub_input_words.append(sub)
  max_length = max([len(sub_input_words[i]) for i in range(set_word_length)])
  #input_words = [alt_sub_input_words if len(alt_sub_input_words)>max_length else max(sub_input_words, key=len)]
  # why doesn't the above work?
  input_dict = {}
  if len(alt_sub_input_words)>max_length:
    print(len(input_words))
    input_words = alt_sub_input_words
    print(f'{guess.upper()} is not in word')
  else:
    print(len(input_words))
    input_words = max(sub_input_words, key=len)
    input_position = max(position, key=len)
    display[input_position[0]] = guess
    input_dict = {input_words[i]: input_position[i] for i in range(len(input_words))}
    #here is where I want to set a position identifier -- need to mark it when generate set_input_words[i]
    #think of possibility of using classes after reading more from notebook
    print(f'{guess.upper()} is in word')

  guessed.append(guess)
  counter += 1
  
  guessed = ' '.join(guessed)
  guessed = guessed.upper().split()
  
  guessed.sort()
  print(f'These are the letters you have guessed: {guessed}')
  print(f'You have guessed {counter} times.')
  disp = ' '.join(display)
  disp = disp.upper()
  print(disp)
  print('')
  if '_' not in display:
    print('You win!!')







