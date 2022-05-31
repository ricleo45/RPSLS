from ai import AI
from human import Human

class Game:
    def __init__(self):
        pass

player1 = Human('Player 1')
player2 = AI('Player 2')
player1.name = input('Please enter your name: ')
# player one rules
def game_rutine(): 
    if player1.picked_gesture == player2.picked_gesture:
        print('We have an tie')
    elif player1.picked_gesture == 'Rock' and player2.picked_gesture == 'Scissors':
        print(f'Rock smashes {player2.picked_gesture}')
        player1.score = player1.score + 1
    elif player1.picked_gesture == 'Rock' and player2.picked_gesture == 'Lizard':
        print(f'Rock smashes {player2.picked_gesture}')
        player1.score = player1.score + 1
    elif player1.picked_gesture == 'Paper' and player2.picked_gesture == 'Rock':
        print(f'Paper covers {player2.picked_gesture}')
        player1.score = player1.score + 1
    elif player1.picked_gesture == 'Paper' and player2.picked_gesture == 'Spock':
        print(f'Paper disposes {player2.picked_gesture}')
        player1.score = player1.score + 1
    elif player1.picked_gesture == 'Scissors' and player2.picked_gesture == 'Paper':
        print(f'Scissors cuts {player2.picked_gesture}')
        player1.score = player1.score + 1
    elif player1.picked_gesture == 'Scissors' and player2.picked_gesture == 'Lizard':
        print(f'Scissors decapitates {player2.picked_gesture}')
        player1.score = player1.score + 1
    elif player1.picked_gesture == 'Spock' and player2.picked_gesture == 'Scissors':
        print(f'Spock smashes {player2.picked_gesture}')
        player1.score = player1.score + 1
    elif player1.picked_gesture == 'Spock' and player2.picked_gesture == 'Rock':
        print(f'Spock vaporizes {player2.picked_gesture}')
        player1.score = player1.score + 1
    elif player1.picked_gesture == 'Lizard' and player2.picked_gesture == 'Spock':
        print(f'Lizard poisons {player2.picked_gesture}')
        player1.score = player1.score + 1
    elif player1.picked_gesture == 'Lizard' and player2.picked_gesture == 'Paper':
        print(f'Lizard eats {player2.picked_gesture}')
        player1.score = player1.score + 1

# player 2 rules 
    elif player2.picked_gesture == player1.picked_gesture:
        print('We have an tie')
    elif player2.picked_gesture == 'Rock' and player1.picked_gesture == 'Scissors':
        print(f'Rock smashes {player1.picked_gesture}')
        player2.score = player2.score + 1
    elif player2.picked_gesture == 'Rock' and player1.picked_gesture == 'Lizard':
        print(f'Rock smashes {player1.picked_gesture}')
        player2.score = player2.score + 1
    elif player2.picked_gesture == 'Paper' and player1.picked_gesture == 'Rock':
        print(f'Paper covers {player1.picked_gesture}')
        player2.score = player2.score + 1
    elif player2.picked_gesture == 'Paper' and player1.picked_gesture == 'Spock':
        print(f'Paper disposes {player1.picked_gesture}')
        player2.score = player2.score + 1
    elif player2.picked_gesture == 'Scissors' and player1.picked_gesture == 'Paper':
        print(f'Scissors cuts {player1.picked_gesture}')
        player2.score = player2.score + 1
    elif player2.picked_gesture == 'Scissors' and player1.picked_gesture == 'Lizard':
        print(f'Scissors decapitates {player1.picked_gesture}')
        player2.score = player2.score + 1
    elif player2.picked_gesture == 'Spock' and player1.picked_gesture == 'Scissors':
        print(f'Spock smashes {player1.picked_gesture}')
        player2.score = player2.score + 1
    elif player2.picked_gesture == 'Spock' and player1.picked_gesture == 'Rock':
        print(f'Spock vaporizes {player1.picked_gesture}')
        player2.score = player2.score + 1
    elif player2.picked_gesture == 'Lizard' and player1.picked_gesture == 'Spock':
        print(f'Lizard poisons {player1.picked_gesture}')
        player2.score = player2.score + 1
    elif player2.picked_gesture == 'Lizard' and player1.picked_gesture == 'Paper':
        print(f'Lizard eats {player1.picked_gesture}')
        player2.score = player2.score + 1
    else:
        print('A choice has to be made')

def run_game():
    while player1.score or player2.score != 3:
        player1.choose_gesture()
        player2.choose_gesture()
        game_rutine()
        if player1.score == 3:
            print(f'{player1.name} Wins best {player1.score} of 3')
            break
        elif player2.score == 3:
            print(f'AI Wins best {player2.score} of 3')
            break
        else:
            continue
