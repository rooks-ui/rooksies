print('Let us play a game of Rock, Paper, Scissors')
print('Input 1 for Rock, 2 for Paper, 3 for Scissors')
for i in range(5):
    from random import randint
    comp = randint(1,3)
    player = eval(input('Rock, Paper, Scisssors! : '))
    if player==3 and comp==1:
        print('You lose')
    elif player>comp:
        print('You win')
    elif player==1 and comp==3:
        print('You win')
    else:
        print('You lose')
print('The end')

