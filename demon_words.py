alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
not_guessed = []
guessed = []
rounds_remaining = 8
import curses, sys 

# Setup: capture control sequence 
curses.setupterm() 
clear = str(curses.tigetstr('clear'), 'ascii') 

words = open('words.txt', 'r').read().lower()
import random
words = words.split()
subset_words = []
set_word_length = 4
#guessed = ['a', 'b', 'c']
guess=''
position = []
subber_words= []
for word in words:
  if len(word) == set_word_length:
    subset_words.append(word)
#print(subset_words)
counter=0
in_sub = False
true_count = 0
while len(guessed) < 25:

  #guessed.append(guess)
  # for x in subset_words:
  #   for guesses in guessed:
  #     if guesses in x:
  #      #print('hello', word)
  #       subset_words.remove(x)

  #print('before entered letter', subset_words)
  new_subset_words = []
  new_subset_words_alt = []
  guess = input('enter a guess')
  for sub in subset_words:
    if guess in sub:
      new_subset_words.append(sub)
    else:
      new_subset_words_alt.append(sub)
  if len(new_subset_words)>len(new_subset_words_alt):
    subset_words = new_subset_words
    print(f'{guess} is in word')
    position.append(guess)
    in_sub = True
    
    
    for subber in subset_words:
      if guess in subber[true_count]:
        print('I am HERE', subber)
        subber_words.append(subber)
        #subber_words.append(subber)
      #else:
        
    print(subber_words)
    true_count +=1

  else:
    subset_words = new_subset_words_alt
    print(f'{guess} is not in word')
  #guessed.append(guess)
  if in_sub == True:
    subset_words = subber_words
    subber_words = []
  print('after entered letter', subset_words)

  counter += 1
  in_sub = False
  print(counter)
  print(in_sub)
  print(true_count)
  #print('removing e words', new_subset_words)

# Next step is to fix the position of guess when "it is in word". start with fixing it to first position available

# candidates =[[],[],[],[]]

# for word in subset_words:
#   for spot in range(len(word)):
#     if guess == list(word)[spot]:
#       print(candidates[spot])
#       candidates[spot].append(word)
# print(len(candidates[0]), len(candidates[1]), len(candidates[2]))


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

