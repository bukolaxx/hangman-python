import random
import string
from words import words
from hangman_drawing import user_lives

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word=random.choice(words)

    return word.upper()

def hangman():

        lives =6

        word = get_valid_word(words)
        word_letters = set(word) #letters in the word
        alphabet = set(string.ascii_uppercase)
        used_letters = set() #what the user has guessed

        while len(word_letters)>0 and lives>0:
            print('You have', lives, ' lives and you have used these letter: ', ' '.join(used_letters))
            word_list=[letter if letter in used_letters else '-' for letter in word]
            print('Current word:  ', ' '.join(word_list))

            #getting user input
            user_letter = input('Guess a letter: ').upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    lives-=1
                    print('Letter is not in word')
                    user_lives(lives)

            elif user_letter in used_letters:
                print('You have already guessed that charcter, try again')

            else:
                print('Invalid character')

            #gets here when len(word_letter) == 0 or when lives ==0
        if lives == 0:
            print('Too bad, you lose the word was',word)
        else:
            print('You have guessed the word', word, ' !!')


hangman()
