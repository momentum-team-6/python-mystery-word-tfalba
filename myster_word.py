
not_guessed = []
guessed = []

def clear_display(list_not_guessed, list_guessed, last_guess):
  new_display = word_letters
  #list_guessed = list_guessed.append(last_guess)

  for i in range(len(list_not_guessed)):
    new_display = [letter.replace(list_not_guessed[i], '_') for letter in new_display]
  print(new_display)

def start_play(iter):
  print(f'You have {iter} rounds remaining')
  clear_display(not_guessed, guessed, '')
  #print(iter)
  #print(len(not_guessed))
  if iter >0:
    new_guess = input('Enter a new letter: ')
    if len(new_guess) != 1:
      print('invalid response, please enter a new letter')
      start_play(iter)
    else:
      new_guess = new_guess.capitalize()
      guessed.append(new_guess)
      if new_guess in not_guessed:
        not_guessed.remove(new_guess)
        clear_display(not_guessed, guessed, new_guess)
        if len(not_guessed) == 0:
          print(f'You win! The word is {word}!')
        else:
          print('You found a letter!')
          print(f'You have {iter} rounds remaining')
          print(guessed)
          start_play(iter)
      else:
        print('Sorry- that letter is not present')
        iter = iter - 1
        print(f'You have {iter} rounds remaining')
        start_play(iter)
  else:
    print('Sorry - you are out of guesses! Play again?')
  return

round = 8
#word = input('Please enter a word for the game:  ')
word = 'fortitude'


if len(word) > 0:
  word = word.upper()
  word_letters =[]
  word_letters += word
  for letter in word_letters:
    if letter not in not_guessed:
      not_guessed.append(letter)
  print(f'The word contains {len(word)} letters.')
  start_play(round)

# Add a list that keeps track of guessed letters and notifies if used again
# track what is happening when the letter that is already up doesn't show up in 
# not_guessed 
# can handle that by checking all guessed letters since no penalty for that
# figure out how to pull a random word from the text file
# figure out how to choose a word of a specified length randomly
# what is devil mode?
# make display more exciting!!
# handle error cases better
# add options to restart play if don't get word in 8 rounds or if win

 