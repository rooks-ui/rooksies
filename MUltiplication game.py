c = 0

for i in range(10):
    from random import randint
    r = randint(1,12)
    l = randint(3,20)
    print('Calculate', l, 'X', r)
    start = eval(input('Input your answer: '))
    if start == l*r:
        c = c+1
        print('That is correct')
    else:
       
        print('Wrong! Try again')

print('Good job')
print('You got', c, 'Correct')