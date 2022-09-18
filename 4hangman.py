import random
from words4handman import words
import string

def valid_word(words) :
    word = random.choice(words)
    while "-" in word or " " in word :
        word = random.choice(words)
    
    return word.upper()

def hangman() :
    word = valid_word(words)
    # string function
    alphabets = set(string.ascii_uppercase)
    # use of set for easy handling of duplicates, set.add, set.remove
    letters_in_word = set(word)
    # used letters here used for display purposes, see LC below
    used_letters = set()
    
    lives = 6

    while len(letters_in_word) > 0 and lives > 0 :
        # LC one liner cool stuffs
        hanger = [letter if letter in used_letters else '-' for letter in word]
        print("\nRemaining lives:", lives, "| Used letters: ", ' '.join(used_letters))
        print("\n\n\n",' '.join(hanger)) 
        user_guess = input("\nGuess the word, or one letter: ").upper()
        print("\n%-----------------------------------%")
       
        if user_guess == word :
            break

        if user_guess in letters_in_word :
            used_letters.add(user_guess)
            letters_in_word.remove(user_guess)
        elif user_guess in used_letters :
            if lives != 1 :
                print("\nLetter", user_guess, "already used, try another!")
            lives -= 1
        elif user_guess not in alphabets :
            if lives != 1 :
                print ("\nInvalid guess, try again!")
            lives -= 1
        else :
            if lives != 1 :
                print("\nLetter", user_guess, "not in word, try again!")
            used_letters.add(user_guess)
            lives -= 1

    
    print("%-----------------------------------%")
    word_display = ' '.join(list(word))
    if lives == 0 :
        print("\nBoo hoo, the word is.. ", word_display)
        print("Remaining lives: ", lives)
    else :
        print("\n", word_display)
        print("\n\nYou got it! Well done!")
        print("Remaining lives: ", lives)
    print("%-----------------------------------%\n\n")


if __name__ == '__main__':
    hangman()

# pending add hang visuals