import os
import time
import random
import atexit

# Python 2 should use `raw_input` instead of `input`
atexit.register(input, 'Press Enter to continue...')

# CONSTS
DICTIONARY_FILENAME = 'dictionary.txt'
GAME_TIME_LIMIT = 10

if __name__ == '__main__':
    print('TYPERACER SPEEDRUN...')


    #wczytaj plik
    #wczytaj slowa
    # losuj slowo
    # startuj czas
    # input
    # stop czas

    # sprawdz poprawnosc


    # gui?
    t0 = time.time()

    file = open(DICTIONARY_FILENAME, 'r')
    
    dict = []
    word = 'x'
    while word != '':
        word = file.readline()
        word = word[:-2]
        if len(word) > 2:
            dict.append(word)

    print('Loaded {} with {} words inside in {:.2f}s.'.format(DICTIONARY_FILENAME, len(dict), time.time()-t0))
    #print(dict)


    # GAME LOOP

    score = 0
    time_gamestart = time.time()
    while time.time() - time_gamestart < GAME_TIME_LIMIT:
        current_word = random.choice(dict)

        time_left = GAME_TIME_LIMIT-(time.time()-time_gamestart)
        print('TIME LEFT: {:.2f}s'.format(time_left))
        print('TYPE: {}'.format(current_word))
        user_word = input()

        if user_word == current_word:
            score += 1

    print('TIME IS OVER ({:.2f}s).'.format(GAME_TIME_LIMIT))
    print('Your score: {}'.format(score))









else:
    print('wtf why arent you in main..')

