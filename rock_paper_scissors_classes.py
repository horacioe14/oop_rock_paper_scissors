"""Program that plays rock paper scissors with classes"""

import random


class Player:
    '''Function that keeps player scores'''

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0


class HumanPlayer:
    def __init__(self):
        self.player_choice = input('Rock, paper or scissors? [r/p/s]')

    def choose(self):
        while True:
            if self.player_choice in ['r', 'p', 's']:
                return self.player_choice


class ComputerPlayer:
    choices = ['r', 'p', 's']

    def __init__(self):
        self.computer_choice = random.choice(ComputerPlayer.choices)


class Game(Player):

    def __init__(self, rounds):
        self.rounds = rounds
        Player.__init__(self)

    def rules(self, player_choice, computer_choice):
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

    def score_outcome(self):
        '''Function that determines who wins all rock paper scissors rounds'''
        print(
            f'[Game summary] Your points: {self.player_score}  |  Computer points: {self.computer_score}\n')

        if self.player_score > self.computer_score:
            print('You won!\n')
        if self.player_score < self.computer_score:
            print('The computer won.\n')
        if self.player_score == self.computer_score:
            print('It was a tie\n')

    def start_game(self):
        counter = 1
        while counter <= int(self.rounds):
            print(f'\nRound {counter}:')
            cc = ComputerPlayer().computer_choice
            pc = HumanPlayer()
            print(f'Computer choice: {cc}')
            result = self.rules(HumanPlayer.choose(pc), cc)
            print(result)
            if result == 'You won this round!\n':
                self.player_score += 1
            if result == 'You lost this round!\n':
                self.computer_score += 1
            counter += 1
        self.score_outcome()


if __name__ == '__main__':
    while True:
        print('--- Rock Paper Scissors Game ---')
        print("(type 'quit' to exit)")
        round_c = input('How many rounds would you like to play?: ')
        if round_c.isnumeric():
            Game(round_c).start_game()
        if round_c == 'quit':
            print('Bye!\n')
            break
        if not round_c.isnumeric():
            print('\nPlease enter a number\n')
            continue
