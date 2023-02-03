"""Program that generates passwords"""

import random


def rps_rules(player_choice, computer_choice):
    '''Function that define rules for rock paper scissors'''
    if player_choice == computer_choice:
        return 'This round is a tie\n'
    if player_choice == 'r' and computer_choice == 'p':
        return 'You lost this round!\n'
    if player_choice == 'r' and computer_choice == 's':
        return 'You won this round!\n'
    if player_choice == 's' and computer_choice == 'p':
        return 'You lost this round!\n'
    if player_choice == 's' and computer_choice == 'r':
        return 'You won this round!\n'
    if player_choice == 'p' and computer_choice == 's':
        return 'You lost this round!\n'
    if player_choice == 'p' and computer_choice == 'r':
        return 'You won this round!\n'


def score_outcome(player_score, computer_score):
    '''Function that determines who wins all rock paper scissors rounds'''

    if player_score > computer_score:
        print('You won!\n')
    if player_score < computer_score:
        print('The computer won.\n')
    if player_score == computer_score:
        print('It was a tie\n')


def rps_start():
    '''Function that runs rock paper scissors'''
    while True:
        print('''-- Rock Paper Scissors Game --''')
        print("(type 'quit' to exit)")
        data = input('How many rounds would you like to play?: ')

        if data.isnumeric():
            counter = 1
            player_score = 0
            computer_score = 0
            while counter <= int(data):
                print(f'\nRound {counter}:')
                choices = ['r', 'p', 's']
                computer_choice = random.choice(choices)
                player_choice = input('Rock, paper or scissors? [r/p/s] ')
                print(f'Computer choice: {computer_choice}')
                result = rps_rules(player_choice, computer_choice)
                print(result)
                if result == 'You won this round!\n':
                    player_score += 1
                if result == 'You lost this round!\n':
                    computer_score += 1
                counter += 1
            print(
                f'[Game summary] Your points: {player_score}  |  Computer points: {computer_score}\n')
            score_outcome(player_score, computer_score)
        if data == 'quit':
            print('Bye!\n')
            break
        if not data.isnumeric():
            print('\nPlease enter a number\n')
            continue


if __name__ == '__main__':
    rps_start()
