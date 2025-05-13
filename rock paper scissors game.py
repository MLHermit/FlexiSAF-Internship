import random

scoreline = {'Player' : 0, 'Tie': 0, 'AI': 0}

'getting the input from user'
while True:
        player_input = input('Enter your input: ')
        player_input.strip().lower()
        if player_input in ['rock', 'paper', 'scissors']:
            print('....')
            'getting the AI input'
            AI_input = random.choice(['rock', 'paper', 'scissors'])

            'displaying the AI choice'
            print(f'AI input: {AI_input}')

            'comparing inputs and deciding the winner'
            if (player_input == AI_input):
                print('It\'s a tie!')
                scoreline['Tie'] += 1
                print(scoreline)

            elif (player_input == 'rock' and AI_input == 'scissors')\
            or (player_input == 'scissors' and AI_input == 'paper') or (player_input == 'paper' and AI_input == 'rock'):
                print('Player wins!')
                scoreline['Player'] += 1
                print(scoreline)
            else:
                print('AI wins!')
                scoreline['AI'] += 1
                print(scoreline)
        else:   
             print('invalid input, enter correct input')