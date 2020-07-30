import random
import string


def menu():
    print('Type "play" to play the game, "exit" to quit: ', end='')
    while True:
        answer = input()
        if answer == 'play':
            start_game()
        elif answer == 'exit':
            exit()
        else:
            print('Type "play" to play the game, "exit" to quit: ', end='')
            continue


def start_game():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    secret = random.choice(word_list)
    guess = list('-' * len(secret))
    letters = set()
    count = 1

    while count <= 8:
        print()
        print(''.join(guess))
        print('Input a letter: ', end='')
        letter = input()
        if letter in secret and letter not in guess and bool(letter) is True and letter not in letters:
            for j in range(len(list(secret))):
                if list(secret)[j] == letter:
                    guess[j] = letter
            if ''.join(guess) == secret:
                break
        elif len(letter) != 1:
            print('You should input a single letter')
        elif letter not in string.ascii_letters or letter.islower() is False:
            print('It is not an ASCII lowercase letter')
        elif letter not in secret and letter not in letters or not bool(letter):
            print('No such letter in the word')
            count += 1
        elif letter in letters and ''.join(guess) != secret:
            print('You already typed this letter')
        elif ''.join(guess) == secret:
            break
        else:
            break
        letters.add(letter)

    if ''.join(guess) != secret:
        print('You are hanged!\n')
        menu()
    elif ''.join(guess) == secret:
        print('You guessed the word!', 'You survived!', sep='\n')
        menu()


print('H A N G M A N')
menu()
