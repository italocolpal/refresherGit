import random 
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
         print('hello lets play')
         word_completion = '_'*len(word)
         guessed = False
         guessed_letters = []
         guessed_words = []
         tries = 6
         print('Lets play hangman')
         print(display_hangman(tries))
         print(word_completion)
         print('\n')
         while not guessed and tries > 0 : 
            guess = input('Please guess a letter or word').upper()
            # length has to be equal to one (char) and it has to a letter--> isalpha()
            if len(guess) == 1  and guess.isalpha():
               #char already in list of guessed letters
                  if guess in guessed_letters:
                     print('You are ready guess the letter' , guess)
                     # if (char) not in the character of the word 
                  elif guess not in word: 
                     print(guess, ' is not in the word')
                     tries -= 1
                     guessed_letters.append(guess)
                  else: 
                     print('Good job', guess , 'is in the word!')
                     guessed_letters.append (guess)
                     word_as_list = list(word_completion)

      

        




def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]



def main():
    word = get_word()
    play(word)


if __name__ == '__main__':
    main()
