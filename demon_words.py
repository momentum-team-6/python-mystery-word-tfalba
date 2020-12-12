import curses, sys 
curses.setupterm() 
clear = str(curses.tigetstr('clear'), 'ascii') 

alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet = ' '.join(alphabet_upper)
alphabet = alphabet.lower()
alphabet_lower = alphabet.split()

def play_demon_words():
  guessed = []

  counter = 0
  attempts = 24
  game_over = False

  words = open('words.txt', 'r').read().lower()
  words = words.split()
  
  set_word_length = input('Choose number of letters in word: ')          #Have user input the length of the word and add error exception
  while type(set_word_length) == str:
    if set_word_length in alphabet_lower or set_word_length in alphabet_upper or len(set_word_length) >= 2:
        set_word_length = input('Invalid entry. Please choose a number less than 10: ')
    else:
      set_word_length = int(set_word_length)
  set_word_length = int(set_word_length)
  
  subset_words = []                                                                                                                    # new list with only words with set_word_length letters and removing dups
  [subset_words.append(word) for word in words if len(word) == set_word_length and word not in subset_words]    
  remove_words = []                                                                                                                   #identify list of words with repeated chars
  [remove_words.append(word) for word in subset_words for letter in word if word.count(letter) > 1 and word not in remove_words]    
  input_words = []                                                                                                                     #append to input list only words that have no repeat chars
  [input_words.append(word) for word in subset_words if word not in remove_words]               

  display = '_ '*set_word_length
  display = display.split()

  while len(guessed) < attempts and game_over == False:
    guess = input('Enter a guess: ').lower()
    
    if guess not in alphabet_lower or len(guess)>1:                     #Handle invalid choices or repeat guess
      print('\n' + 'Input not valid. Please enter letter again: ' + '\n')
      continue
    if guess in guessed:
      print('\n' + 'You already tried that letter. Please pick a new one: ' + '\n')
      continue

    alt_sub_input_words = []                                              #holder sublist for cases without guessed letter
    sub_input_words=[ [] for i in range(set_word_length)]                 #create empty list of lists for each possible wordlist with letter and position placeholder
    position = [ [] for i in range(set_word_length)]
    
    for sub in input_words:
      if guess in sub:                                                                            ## create sublists to choose max over position of letter 
        [sub_input_words[i].append(sub) for i in range(set_word_length) if guess == sub[i]]       ## for instance if a is selected, compare all a in first position, all a in secon
        [position[i].append(i) for i in range(set_word_length) if guess == sub[i]]                ## and so on... see if the max of those sets is greater than alt set
      else:
        alt_sub_input_words.append(sub)
    max_length = max([len(sub_input_words[i]) for i in range(set_word_length)])

    if len(alt_sub_input_words)>max_length:
      input_words = alt_sub_input_words
    else:
      input_words = max(sub_input_words, key=len)                                               #If a sublist with the letter is the max size, set the new input list to it
      input_position = max(position, key=len)                                                   #Also set the position identifier for that list ***Caution - two unordered lists
      display[input_position[0]] = guess                                                        #Set proper position of display to the letter guessed
    
    guessed.append(guess)                                                     #add to list of guessed letters & increment game-play
    counter += 1

    [print('\n' + f'{guess.upper()} is not in word' + '\n') if len(alt_sub_input_words)>max_length else print('\n' + f'{guess.upper()} is in word' + '\n') ]      #print display info (reformatting as well)
    print('Words Remaining: ' + str(len(input_words))+ '\n')                  
    
    guessed_disp = ' '.join(guessed)
    guessed_disp = guessed_disp.upper().split()
    guessed_disp.sort()

    print(f'These are the letters you have guessed: {guessed_disp}')
    print('\n' + f'You have {attempts - counter} guesses remaining.' + '\n')
    disp = ' '.join(display)
    disp = disp.upper()
    print(' '*4 + disp + '\n')
    
    if '_' not in disp:                                                       #If guess word - offer replay option
      print('\n' + 'You win!!')
      game_over = True
      continue
  [print('\n' + 'Thanks for playing!' + '\n') if game_over == True else print('\n' + 'You are out of guesses.' + '\n')]
  play_again = input('Play again? y/n: ')
  if play_again == 'y' or play_again == 'Y':
    play_demon_words()
  else:
    print('\n' + 'See you next time!')

play_demon_words()



  #input_words = [alt_sub_input_words if len(alt_sub_input_words)>max_length else max(sub_input_words, key=len)]
  ## why doesn't the above work to do:

  ## think it needs to be [input_words = alt_sub.... if len(...)>max... else max(sub_input....)]

  # if len(alt_sub_input_words)>max_length:
  #   input_words = alt_sub_input_words
  # else:
  #   input_words = max(sub_input_words, key=len)



    # input_words_dict = {letter: input_words.count(letter) for letter in input_words}        #Save this for later
    # input_words_dict_alt = []
    # for word in input_words:
    #   input_words_dict_alt.append({letter: word.count(letter) for letter in word})

 #input_dict = {input_words[i]: input_position[i] for i in range(len(input_words))}        #need to think about how I can use this
     #input_dict = {}



