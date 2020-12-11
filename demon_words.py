alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

guessed = []
import curses, sys 

# Setup: capture control sequence 
curses.setupterm() 
clear = str(curses.tigetstr('clear'), 'ascii') 

words = open('words.txt', 'r').read().lower()
import random
words = words.split()
input_words = []
subset_words = []
set_word_length = int(input('Choose number of letters in word: '))

# new list with only words with set_word_length letters and removing dups
[subset_words.append(word) for word in words if len(word) == set_word_length and word not in subset_words]

# this code removes any word with multiple occurences of a letter and saves it in new list input_words
# it is ugly but it works
for word in subset_words:
  for letter in word:
    if word.count(letter) > 1:
      word = word.replace(letter, '?')
  # [word.replace(letter, '?') for letter in word if word.count(letter) > 1]
  # why doesn't the above work?
  input_words.append(word)
new_input_words = []
#[input_words.remove(word) for word in input_words if '?' in word]
# why doesn't the above work??
[new_input_words.append(word) for word in input_words if '?' not in word]
input_words = new_input_words

## call subset_words output_words instead
## add set split to choose max over position of letter 
## for instance if a is selected, compare all a in first position, all a in secon
## and so on... see if the max of those sets is greater than alt set

guess=''
while len(guessed) < 25:

  alt_sub_input_words = []
  guess = input('enter a guess: ')
  #create empty list of lists for each possible position
  sub_input_words=[ [] for i in range(set_word_length)]
  for sub in input_words:
    if guess in sub:
      [sub_input_words[i].append(sub) for i in range(set_word_length) if guess == sub[i]]
    else:
      alt_sub_input_words.append(sub)
  max_length = max([len(sub_input_words[i]) for i in range(set_word_length)])
  if len(alt_sub_input_words)>max_length:
    input_words = alt_sub_input_words
    print(f'{guess} is not in word')
  else:
    input_words = max(sub_input_words, key=len)
    #here is where I want to set a position identifier -- need to mark it when generate set_input_words[i]
    #think of possibility of using classes after reading more from notebook
    print(f'{guess} is in word')

  guessed.append(guess)
  #saving guesses for later and for tracking while loop
  print(sub_input_words)
  print([len(sub_input_words[i]) for i in range(set_word_length)])
  print(max_length)
  print('after entered letter', input_words)



# def new_round():
#   game_mode = input("Please enter '1' for easy mode, '2' for normal mode, or '3' for hard mode: ")
#   get_word(game_mode)

# def get_word(game_mode):
#   words = open('words.txt', 'r').read()
#   import random
#   words = words.split()
#   word = random.choice(words)
#   check_word(word, game_mode)

# def check_word(word_option, game_mode):
#   if game_mode == '1':
#     if len(word_option) <7 and len(word_option)>3:
#       start_round(word_option)
#     else:
#       get_word(game_mode)
#   elif game_mode == '2':
#     if len(word_option) <9 and len(word_option)>5:
#       start_round(word_option)
#     else:
#       get_word(game_mode)
#   else:
#     if len(word_option) > 7:
#       start_round(word_option)
#     else:
#       get_word(game_mode)

# def show_display(list_not_guessed, list_guessed, last_guess, word_letters):
#   new_display = word_letters

#   for i in range(len(list_not_guessed)):
#     new_display = [letter.replace(list_not_guessed[i], '_') for letter in new_display]
#   disp = ' '.join(new_display)
#   print(disp)

# def start_play(iter, word_letters, word):
#   #sys.stdout.write(clear)
#   print(f'You have {iter} rounds remaining')
#   if iter == 8:
#     show_display(not_guessed, guessed, '', word_letters)
#   if iter >0:
#     new_guess = input('Enter a new letter: ')
#     new_guess = new_guess.capitalize()
#     if len(new_guess) != 1 or new_guess not in alphabet:
#       print('Invalid response, please enter a new letter')
#       start_play(iter, word_letters, word)
#     else:
#       if new_guess in not_guessed and new_guess not in guessed:
#         not_guessed.remove(new_guess)
#         show_display(not_guessed, guessed, new_guess, word_letters)
#         if len(not_guessed) == 0:
#           print(f'You win! The word is {word}! Play again?  ')
#           play_again()
#         else:
#           guessed.append(new_guess)
#           start_play(iter, word_letters, word)
#           print('You found a letter!')
#       elif new_guess in guessed:
#         print('You already guessed that letter')
#         start_play(iter, word_letters, word)
#       else:
#         print('Sorry- that letter is not present')
#         show_display(not_guessed, guessed, new_guess, word_letters)
#         iter = iter - 1
#         guessed.append(new_guess)
#         start_play(iter, word_letters, word)
#   else:
#     print(f'Sorry - you are out of guesses! The word is {word} Play again?  ')
#     play_again()
#   return

# def start_round(word):
#   word = word.upper()
#   word_letters = []
#   word_letters = list(word)
#   #how to turn the following into a comprehension?
#   for letter in word_letters:
#     if letter not in not_guessed:
#       not_guessed.append(letter)
#   print(f'The word contains {len(word)} letters.')
#   start_play(rounds_remaining, word_letters, word)

# def play_again():
  
#   keep_going = input("Enter 'y' to play again or 'n' to quit.  ")
#   if keep_going == 'y':
#     sys.stdout.write(clear)
#     new_round()
#   else:
#     print('Thanks for playing mystery word!')

# new_round()

