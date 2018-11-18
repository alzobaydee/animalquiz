# -*- coding: utf-8 -*-
def guessing_controller(guess, answer):
    global points
    is_still_guessing = True
    tries = 0

    while is_still_guessing and tries < 3:
        if guess.lower() == answer.lower():
            print('Right on!')
            points = points + 3 - tries
            is_still_guessing = False
        else:
            if tries < 2:
                guess = input('Nope, try again ')
            tries = tries + 1
    if tries == 3:
        print("Whaaat? you couldn't get this one? it's: " + answer)
        
points = 0
print('Guess the animal')
answer1 = input('What bear lives in the north pole? ')
guessing_controller(answer1, 'ice bear')

answer2 = input('what animal is the fastest? ')
guessing_controller(answer2, 'cheetah')

answer3 = input('which animal is the BIGGEST? ')
guessing_controller(answer3, 'blue whale')

answer4 = input('which of these choices is a fish? \n \
A) Whale\n B) Something\n C) Shark\n \
Write A, B or C ')
guessing_controller(answer4, 'c')

print('yo points aa: ' + str(points) + ' of total: 12')
