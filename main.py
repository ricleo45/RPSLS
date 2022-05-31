from game import run_game

print('Welcome to RPSLS')
print('')
choice = input('To start game enter: yes or y ')
if choice == 'y' or 'Y' or 'Yes' or 'yes':
    run_game()
else:
    ''