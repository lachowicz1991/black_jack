from black_jack import BlackJack
from replit import clear
from art import logo

if __name__ == '__main__':
    print(logo)
    run = True
    game = BlackJack()
    while True:
        clear()
        start = input("Would you like to start the game of Black Jack? (y/n): ")
        if start == 'y':
            game.play_game()
        else:
            break

print('Thank you for playing!')