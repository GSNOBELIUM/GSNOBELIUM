import time
import random

def clear_screen():
    print("\033[H\033[J")

def draw_dinosaur():
    print('''
             __
            / _)
     .-^^^-/ /
  __/       /
 /__.|_|-|_|
''')

def draw_cactus():
    print('''
   _
 /' \\
|    |
 \\___/
''')

def jump():
    clear_screen()
    draw_dinosaur()
    time.sleep(0.5)
    clear_screen()

def play_game():
    score = 0
    while True:
        obstacle = random.choice(['cactus', ''])
        if obstacle == 'cactus':
            clear_screen()
            draw_dinosaur()
            draw_cactus()
            print("Game Over! Your score:", score)
            break
        else:
            jump()
            score += 1
            print("Score:", score)
            time.sleep(0.1)

if __name__ == "__main__":
    print("Welcome to the Mini Dinosaur Game!")
    print("Press Enter to jump.")
    input("Press Enter to start the game...")
    play_game()
