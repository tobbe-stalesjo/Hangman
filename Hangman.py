import pygame
import math
import random

# Setup Display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# Button Variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)  # Where to place the first button
starty = 400
A = 65  # The capital A is equal 65 when programming
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])  # Adding the alphabet to the array

# Fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)

# Load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# Game Variables
hangman_status = 0  # First picture
words = ["DEVELOPER", "PYTHON", "GETACCEPT"]  # The word to guess
word = random.choice(words)
guessed = []

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw():
    win.fill(WHITE)  # Set the background color
    # Draw Title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)  # Printing a Title on your game window
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))  # Deciding where to render the title

    # Draw Word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "  # If you guessed right printing the letter and a space
        else:
            display_word += "_ "  # Printing a _ and a space
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))  # Printing the text on the screen

    # Draw Buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:  # Checking if the letter is visible and printing them
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (
            x - text.get_width() / 2, y - text.get_height() / 2))  # Fixing so the letter is centered on the button

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    global hangman_status

    # Setup Game Loop
    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # Checking where you press your mouse button
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False  # Making the button disappear
                            guessed.append(ltr)  # If the letter is in the word it will add it
                            if ltr not in word:  # If not in the word we add on the hangman
                                hangman_status += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("You Won!")
            break

        if hangman_status == 6:
            display_message("You lost!")
            break


main()
pygame.quit()
