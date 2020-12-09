word = 'Barbados'
word = word.upper()
word_letters = ['B', 'A', 'R', 'B', 'A', 'D', 'O', 'S']
guesses = ['B', 'A', 'D', 'C']
not_guessed = ['B', 'A', 'R', 'D', 'O', 'S']

def clear_display(list_not_guessed):
  
  new_display = word_letters
  for i in range(len(list_not_guessed)):
    new_display = [letter.replace(list_not_guessed[i], '_') for letter in new_display]
  print(new_display)


def start_play():
  clear_display(not_guessed)
  new_guess = input('Enter a new letter: ')
  #print(new_guess)
  not_guessed.remove(new_guess)
  #print(not_guessed)
  clear_display(not_guessed)
  if len(not_guessed) > 1:
    again = input('guess the word? ')
    if again == 'y':
      checker = input('what is the word?  ')
      if checker == word:
        print('You win')
      else: 
        print('Keep guessing... ')
        start_play()
    else:
      start_play()
  else:
    checker = input('what is the word?  ')
    if checker == word:
      print('you win')
  return

start_play()


 