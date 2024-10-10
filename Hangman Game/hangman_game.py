import pygame
from math import sqrt
import random
import sys

pygame.init()

WIDTH, HEIGHT = 1200, 850
score = 0
score_incremented = False
lives = 3
lives_decrement = False

def draw():

    global hint_text, hint_Rect, hint_message, won
    won = all(letter in guessed_letters for letter in word)

    window.fill((background))

    window.blit(hint_text, hint_Rect)

    # Display score and lives
    score_text = big_font.render(f'Score: {score}', 1, BLACK)
    score_rect = score_text.get_rect()
    score_rect.center = (980, 70)
    window.blit(score_text, score_rect)

    lives_text = big_font.render(f'Lives: {lives}', 1, BLACK)
    lives_rect = lives_text.get_rect()
    lives_rect.center = (650, 70)
    window.blit(lives_text, lives_rect)

    #Display word
    answer = ""
    for letter in word:
        if letter in guessed_letters:
            answer += letter + " "
        else:
            answer += "_ "
    
    answer_blank = big_font.render(answer, 1, BLACK)
    window.blit(answer_blank, (550,200))

    #Unpack list to draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(window, BLACK, (x,y), RAD, 3)
            text = small_font.render(ltr, 1, BLACK)
            window.blit(text, (x-text.get_width()/2, y-text.get_height()/2))

    if hint_message:
        answer_hint = medium_font.render(hint_message, 1, BLACK)
        window.blit(answer_hint, (550, 400))

    # Display image from images at position x, y
    try:
        if not (won or hangman_stage == 6):
            window.blit(images[hangman_stage], (35, 50)) 
            pygame.display.update()
        else:
            pass
            
    except IndexError:
        win_lose()
  

def compare_lists(words, used_words):

    global lives, score

    remaining_words = set(words) - set(used_words)
    if not remaining_words:
        window.fill(background)
        winner20_text = big_font.render("Well Done! YOU BEAT THE HANGMAN!", 1, BLACK)
        window.blit(winner20_text, (WIDTH / 2 - winner20_text.get_width() / 2,
                                (HEIGHT / 2 - winner20_text.get_height() / 2) - 100))
        
        total_score_text = big_font.render(F"YOU SCORED: {score}/{len(words)}", 1, BLACK)
        window.blit(total_score_text, (WIDTH / 2 - total_score_text.get_width() / 2,
                                       HEIGHT / 2 - total_score_text.get_height() + 100 / 2))
        
        pygame.display.update()
        pygame.time.delay(3000)
        
        run = False
        sys.exit()

    elif lives == 0:

        window.fill(background)
        major_loser_text = big_font.render("THE GALLOWS HAVE CLAIMED YOU!", 1, BLACK)
        window.blit(major_loser_text, (WIDTH / 2 - major_loser_text.get_width() / 2,
                                 (HEIGHT / 2 - major_loser_text.get_height() / 2) - 100))

        total_score_text = big_font.render(F"YOU SCORED: {score}/{len(words)}", 1, BLACK)
        window.blit(total_score_text, (WIDTH / 2 - total_score_text.get_width() / 2,
                                       HEIGHT / 2 - total_score_text.get_height() + 100 / 2))
                    
        pygame.display.update()
        pygame.time.delay(3000)
                    
        run = False
        sys.exit()

    elif (len(used_words) == 20) and not (lives == 0):
        window.fill(background)
        winner20_text = big_font.render("Well Done! YOU BEAT THE HANGMAN!", 1, BLACK)
        window.blit(winner20_text, (WIDTH / 2 - winner20_text.get_width() / 2,
                                (HEIGHT / 2 - winner20_text.get_height() / 2) - 100))
        
        total_score_text = big_font.render(F"YOU SCORED: {score}/{len(words)}", 1, BLACK)
        window.blit(total_score_text, (WIDTH / 2 - total_score_text.get_width() / 2,
                                       HEIGHT / 2 - total_score_text.get_height() + 100 / 2))
        
        pygame.display.update()
        pygame.time.delay(3000)
        
        run = False
        sys.exit()


    else:
        word = random.choice(list(remaining_words))
        used_words_list.append(word)
        return word



def win_lose():

    global won, hangman_stage, score, score_incremented, lives, lives_decrement, run, guessed_letters, letters, word, hint_message
    won = all(letter in guessed_letters for letter in word)
    run = True

    if won and not score_incremented:  # Check if the player won and the score has not been incremented yet
        score += 1
        score_incremented = True  # Set flag to indicate that score has been incremented
        window.fill(background)
        winner_text = big_font.render("YOU WON!", 1, BLACK)
        window.blit(winner_text, (WIDTH / 2 - winner_text.get_width() / 2,
                                (HEIGHT / 2 - winner_text.get_height() / 2) - 100))


    if hangman_stage == 6:
        lives -= 1
        lives_decrement = True
        window.fill(background)
        loser_text = big_font.render("YOU LOSE!", 1, BLACK)
        window.blit(loser_text, (WIDTH / 2 - loser_text.get_width() / 2,
                                (HEIGHT / 2 - loser_text.get_height() / 2) - 100))
        
    play_again_text = big_font.render('Wanna play again?', 1, BLACK)
    window.blit(play_again_text, ((WIDTH / 2 - play_again_text.get_width() / 2,
                                                HEIGHT / 2 - play_again_text.get_height() / 2)))
    window.blit(yes_text, yes_rect)
    window.blit(no_text, no_rect)
    pygame.display.update()

    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_pos2 = pygame.mouse.get_pos()
                
                if no_rect.collidepoint(m_pos2):
                    window.fill(background)
                    major_loser_text = big_font.render("THE GALLOWS HAVE CLAIMED YOU!", 1, BLACK)
                    window.blit(major_loser_text, ((WIDTH / 2 - major_loser_text.get_width() / 2,
                                (HEIGHT / 2 - major_loser_text.get_height() / 2) - 100)))
                    total_score_text = big_font.render(F"YOU SCORED: {score}/{len(words)}", 1, BLACK)
                    window.blit(total_score_text, ((WIDTH / 2 - total_score_text.get_width() / 2,
                                       HEIGHT / 2 - total_score_text.get_height() + 100 / 2)))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    run = False
                    sys.exit()


                if yes_rect.collidepoint(m_pos2):
                    run = False
                    guessed_letters = [""]
                    hint_message = ""
                    score_incremented = False
                    lives_decrement = False
                    word = compare_lists(words, used_words)
                    for letter in letters:
                        letter[3] = True
                    main()

                break



def main():

    global hangman_stage, hint_message, won

    won = all(letter in guessed_letters for letter in word)

    hangman_stage = 0
    global hint_text, event, m_pos
    global run
    run = True

    used_words.append(word)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN and not (won or hangman_stage == 6):
                m_pos = pygame.mouse.get_pos()
                m_x, m_y = m_pos
                if hint_Rect.collidepoint(m_pos):
                    hint_message = hint(word)
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dist = sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dist < RAD:
                            letter[3] = False
                            guessed_letters.append(ltr)
                            if ltr not in word:
                                hangman_stage += 1


        draw()
        if won or hangman_stage == 6:
            win_lose()




def hint(word):
    hints = {
        "APPLE": "Keeps doctors away.",
        "CHAIR": "Furniture.",
        "WATER": "Air, Earth, Fire and?",
        "KING": "A ruler or monarch.",
        "FOREIGN": "Not from here.",
        "SNITCHES": "You'll get stitches.",
        "PIZZA": "A Ninja Turtles' Favourite food",
        "CLOUD": "Where does rain come from?",
        "APOTHECARY": "Potions maker.",
        "XYLOPHONE": "X Musical instrument.",
        "QUASAR": "Brightest objects in the universe.",
        "JINX": "Bad luck.",
        "ZEPHYR": "A gentle, mild breeze.",
        "LABYRINTH": "The minatour lurks within a giant maze.",
        "MEMENTO": "Latin: Remember you must die.",
        "WYVERN": "A dragon, but with 2 wings & 2 legs.",
        "QUEUED": "To have already stood in line",
        "EPIPHANY": "Ureka moment!",
        "PHOENIX": "Dumbledores pet.",
        "PENGUIN": "Happy feet.",
        "LIGHTSABER": "Jedi = Green/Blue, Sith = Red.",
        "CAMOUFLAGE": "Blending into the environment.",
        "COSMONAUT": "Russian astronaut.",
        "EQUINOX": "When day and night are equal length.",
        "SYNOPSIS": "A brief summary of a story.",
        "PARADOX" : "Contradicts itself.",
        "MASQUERADE": 'To hide your identity.',
        "WHALE": "Largest animal on Earth.",
        "GHOST": "Casper.",
        "RENDEZVOUS": "Meet at the agreed time & place"

    }

    return hints.get(word)


# Game variables
words = [ "APPLE", "CHAIR", "WATER", "KING",
          "FOREIGN", "SNITCHES", "PIZZA", "CLOUD", 
          "APOTHECARY", "XYLOPHONE", "QUASAR", "JINX", 
          "ZEPHYR", "LABYRINTH", "MEMENTO", "WYVERN", 
          "QUEUED", "EPIPHANY", "PHOENIX", "PENGUIN", 
          "LIGHTSABER", "CAMOUFLAGE", "COSMONAUT", "EQUINOX", 
          "SYNOPSIS", "PARADOX", "MASQUERADE", "WHALE", "GHOST", "RENDEZVOUS"]

guessed_letters = [""]
used_words_list = []
used_words = list(set(used_words_list))
word = compare_lists(words, used_words)
score = 0
lives = 3

# Create window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Name")
icon = pygame.image.load('deadguy.png')
pygame.display.set_icon(icon)

# Colours
background = (170, 175, 180)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Button variables
RAD = 20
GAP = 15
letters = []
startx = 60
starty = 735
hintx = 960
hinty = 760

# Keyboard value of A
A = 65

# Fonts
small_font = pygame.font.SysFont("comicsans", 20)
medium_font = pygame.font.SysFont("comicsans", 30)
big_font = pygame.font.SysFont("comicsans", 60)

hint_text = big_font.render('Hint', True, BLACK, background)
hint_Rect = hint_text.get_rect()
hint_Rect.center = (hintx, hinty)
hint_message = ""



yes_text = big_font.render('YES', True, BLACK, background)
yes_rect = yes_text.get_rect()
yes_rect.center = (500, 600)
no_text =  big_font.render('NO', True, BLACK, background)
no_rect = no_text.get_rect()
no_rect.center = (700, 600)

# Letter Maker

for j in range(2):
    for i in range(13):
        x = startx + ((RAD*2 + GAP) * (i % 13))
        y = starty + ((1 // 13) * (GAP + RAD *2))
        letters.append([x, y, chr(A+i), True])
    A = 78
    starty += 60

# Images
images = []

for i in range(6):
    stage = pygame.image.load("hangman"+ str(i) +".png")
    images.append(stage)     

if __name__ == "__main__":
    main()
