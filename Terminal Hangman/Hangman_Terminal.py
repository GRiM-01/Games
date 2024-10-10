import random as r
import time

words = ["apple", "chair", "happy"]

count = 5
used_words = []
correct_answers = 0
timestart = time.time()

def guess(hint_message):

    '''
    try and except to make sure user input is only 1 letter
    checks for hint message

    '''

    while True:
        try:
            u_in = input("Guess a letter: ").lower()
            if u_in in ("quit", "exit"):
                print(f"Final time: {time.time()-timestart:.2f}")
                time.sleep(3)
                exit()
            elif u_in == "hint":
                print(hint_message)
                continue
            elif len(u_in) == 1 and u_in.isalpha():
                return u_in 
            else:
                raise ValueError("Type a SINGLE LETTER!")
        except ValueError:
            print("Type a SINGLE LETTER!")


def check(u_in, answer, blank, count, guesses):

    '''
    checks if user's guessed letter is in answer
    if true, replace blank index with user guess
    else decrement count
    display relative messages
    
    '''

    if u_in in answer:
        for index, letter in enumerate(answer):
            if letter == u_in:
                blank[index] = u_in
        print("Attempts left:", count)
        print("Wrong Letters Guessed:", set(guesses))
    else:
        count -= 1
        if count == 0:
            print("GAME OVER!" + "\n" + f"Correct Answer: {answer}")
        else:
            print("Attempts left:", count)
            guesses.append(u_in)
            print("Wrong Letters Guessed:", set(guesses))
    return count


def game(answer, blank, count, guesses, hint_message):

    '''
    play the game
    
    '''

    global correct_answers

    while count > 0 and '_' in blank:
        print('\n' + ' '.join(blank))
        u_in = guess(hint_message)

        count = check(u_in, answer, blank, count, guesses)

    print('\n' + ' '.join(blank)) 

    if count == 0:
        print('You lost...' + '\n' + 'The correct answer was:', answer.upper() + '\n')
    else:
        if correct_answers == len(words)-1:
            print("Wow! Well done! You beat the Hangman!")
            print(f"Final time: {time.time() - timestart:.2f}")
            time.sleep(3)
            exit()
        else: 
            correct_answers += 1
            print("YOU WIN! The answer was:", answer.upper() + '\n' + f'Score: {correct_answers}/{len(words)}' + '\n')
            return correct_answers


def hint():

    """
    dictionary of hints for answers
    returns hints
    
    """

    hints = {
        "apple": "Keeps doctors away.",
        "chair": "Furniture.",
        "happy": "An emotion similar to joy and contentment.",
        "water": "This substance is a transparent and tasteless liquid.",
        "smile": "Used to visually express happiness.",
        "king": "A ruler or monarch.",
        "foreign": "Not from here.",
        "sweet": "Having a taste characteristic of sugar or honey.",
        "cloud": "A visible mass of water droplets or ice crystals suspended in the atmosphere.",
        "laugh": "A sound often associated with joy or amusement.",
        "xylophone": "A musical instrument consisting of wooden bars played with mallets.",
        "quasar": "An astronomical object that emits intense energy.",
        "jigsaw": "A puzzle consisting of small irregularly shaped pieces that fit together.",
        "zephyr": "A gentle, mild breeze.  z _ _ _ _ _",
        "labyrinth": "A complicated and confusing network of passages.",
        "memento": "Remember: _ _ _ _ _ _ _ mori",
        "symphony": "A long musical composition for a full orchestra.",
        "quartz": "A hard mineral often used in jewelry and electronics, ends with z.",
        "epiphany": "A moment of sudden realization or insight.",
        "phoenix": "Dumbedores pet."
    }
    return hints


def compare_lists(words, used_words):
    remaining_words = set(words) - set(used_words)
    if not remaining_words:
        print("Well Done! You completed all the words!")
        exit()
    else:
        answer = r.choice(list(remaining_words))
        used_words.append(answer)
        return answer


def greet():

    '''
    initiate game sequence or quit based on user input
    
    '''

    while True:
            try:

                start = input("Hello... Do you want to play hangman? (Y/N): ").lower()

                if start == 'y':
                                
                    answer = compare_lists(words, used_words)

                    blank = ["_" for letter in answer]
                    guesses = []
                    hints = hint()
                    hint_message = hints.get(answer)

                    correct_answers = game(answer, blank, count, guesses, hint_message)

                    return answer, blank, guesses, hint_message

                elif start == 'n':
                    print(f"Final time: {time.time()-timestart:.2f}")
                    time.sleep(3)
                    exit()


                else:
                    print("Type either y or n.")

            except ValueError:
                print("Type either the LETTER y or n.")


while True:
    answer, blank, guesses, hint_message = greet()
