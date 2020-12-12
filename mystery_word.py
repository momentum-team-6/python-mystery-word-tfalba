alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import random
import curses, sys 
curses.setupterm() 
clear = str(curses.tigetstr('clear'), 'ascii') 

# -------------------------------------------------------------------------------------------------------------------- #
#                                     new_round sets off game and calls start_play                                     #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
#             start_play toggles back and forth to show_display unless game ending when call to play_again             #
# -------------------------------------------------------------------------------------------------------------------- #

def new_round():                           #Sets up new round -- initialize play-level, select word, and set inital values and top display
  game_mode = input("Please enter '1' for easy mode, '2' for normal mode, or '3' for hard mode: ")
  words = open('words.txt', 'r').read()
  words = words.split()

  if game_mode == '1':                                                            #Define word set based on play-level selected
    play_words = [word for word in words if len(word) <7 and len(word) >3]
  elif game_mode == '2':
    play_words = [word for word in words if len(word) <9 and len(word) >5]
  elif game_mode == '3':
    play_words = [word for word in words if len(word) >7]
  else:
    print('Invalid selection. Please select again.')
    new_round()

  play_word = random.choice(play_words)                     #choose random word, set initial values including not_guessed as unique letters appearing
  word = play_word.upper()
  word_letters = list(word)
  guessed = []
  not_guessed = []
  rounds_remaining = 8
  [not_guessed.append(letter) for letter in word_letters if letter not in not_guessed]

  print(f'The word contains {len(word)} letters.')          #Top display
  print('_ '*len(word))

  start_play(rounds_remaining, word_letters, word, guessed, not_guessed)      #Begin play

def start_play(iter, word_letters, word, guessed, not_guessed):     #Collects input letter, validates, and checks result // updating display and prompting and moving to next letter or ending game
  if iter >0:                                            #When rounds still remain
    guessed.sort()
    print(f'Guessed letters: {guessed}')
    print('')
    new_guess = input('Enter a new letter: ')
    new_guess = new_guess.upper()
    
    if len(new_guess) != 1 or new_guess not in alphabet:      #Invalid entry return to start
      print('Invalid response, please enter a new letter.')
      start_play(iter, word_letters, word, guessed, not_guessed)
    else:                                                         #Is valid entry - 3 options
      if new_guess in not_guessed and new_guess not in guessed:   #opt1 -- newly revealed letter -- show_display & check cases a & b
        not_guessed.remove(new_guess)
        show_display(iter, word_letters, word, new_guess, guessed, not_guessed)
        if len(not_guessed) == 0:                                                   #case_a -- round is won -- play again option
          print('')
          print(f'You win! The word is {word}! Play again?')
          play_again()
        else:                                                                       #case_b -- restart and append guess
          guessed.append(new_guess)
          print('You found a letter!')
          start_play(iter, word_letters, word, guessed, not_guessed)
      elif new_guess in guessed:                                  #opt2 -- previously guessed letter (in word or not), start_play
        print('')
        print('You already guessed that letter')
        print('')
        start_play(iter, word_letters, word, guessed, not_guessed)
      else:                                                       #opt3 -- new guess that is not in word // show_display, append, and start_play
        print('')
        print('Sorry - that letter is not present.')
        show_display(iter, word_letters, word, new_guess, guessed, not_guessed)     #could test not re-showing display here
        iter -= 1
        guessed.append(new_guess)
        start_play(iter, word_letters, word, guessed, not_guessed)
  else:                                                     #No rounds remaining
    print('')
    print(f'Sorry - you are out of guesses! The word is {word} Play again?')
    play_again()
  return

def show_display(iter, word_letters, word, last_guess, guessed, not_guessed):   #Shows display and updates appropriately based on guessed letters
  new_display = word_letters

  for i in range(len(not_guessed)):
    new_display = [letter.replace(not_guessed[i], '_') for letter in new_display]
  disp = ' '.join(new_display)

  print('')
  print(f'You have {iter} rounds remaining')
  print('')
  print(disp)
  print('')

def play_again():                            #Provides option to restart game and resets if y
  print('')
  keep_going = input("Enter 'y' to play again or 'n' to quit.  ")
  if keep_going == 'y':
    sys.stdout.write(clear)
    new_round()
  else:
    print('')
    print('Thanks for playing mystery word!')
    return

new_round()                                   #Initial call of function to play

#Find out how to add a break line to a print statement

