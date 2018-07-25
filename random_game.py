import inquirer
import itertools
from random import randint
import string
import math

orders=[
    inquirer.Text('player_number',message='Please enter your number',validate=lambda _,x: isinstance(int(x),int) )
]
do_you_want_to_con=[inquirer.Text('con',message='Do you want to play next stage?') ]
number_generator=(randint(1,101) for j in range(5))
users_points=0
attempts_count=0
target_number=next(number_generator)
for i in itertools.count(start=0):
    attempts_count=0
    for j in range(5):    
        player_answer=inquirer.prompt(orders)
        player_answer['player_number']=int(player_answer['player_number'])
        print(target_number)
        if player_answer['player_number']==target_number:
            print('You won!!!!!!!!!!!!!!!')
            users_points+=1
            target_number=next(number_generator)
            continue
        elif player_answer['player_number']> target_number and abs(player_answer['player_number']-target_number)>30:
            attempts_count+=1
            print('Your answer is much more bigger than target number')
        elif player_answer['player_number']< target_number and abs(player_answer['player_number']-target_number)>30:
            attempts_count+=1
            print('Your answer is much less than target number')
        elif player_answer['player_number']>target_number and abs(player_answer['player_number']-target_number)>15:
            attempts_count+=1
            print('you\'re answer a little bit bigger')
        elif player_answer['player_number']<target_number and abs(player_answer['player_number']-target_number)>15:
            attempts_count+=1
            print('you\'re answer a little bit less')
        elif player_answer['player_number']>target_number and abs(player_answer['player_number']-target_number)<15:
            attempts_count+=1
            print('you\'re too close but your answer a little bigger')
        elif player_answer['player_number']<target_number and abs(player_answer['player_number']-target_number)<15:
            attempts_count+=1
            print('you\'re close but your answer a little less')
        if attempts_count==5:
            print('You lost fucking sore loser!!')
            break
        else:
            print('You have left only',5-attempts_count)
    print('your points',users_points)
    ans=inquirer.prompt(do_you_want_to_con)
    if ans['con']=='yes':
        continue
    else:
        break
    