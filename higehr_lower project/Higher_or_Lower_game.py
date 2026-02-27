import random
import art
import game_data
import os
max=0
random_choiceA_original=random.choice(game_data.data)
a=random_choiceA_original['follower_count']

random_choiceB_original=random.choice(game_data.data)
b=random_choiceB_original['follower_count']#for just printing

check=[a,b]
flag=True
score=0

def random_compare_for_a():
    print("Choice A",end=" : ")
    for _ in range(0,1) :
        print(f"name :{random_choiceA_original['name']}  a {random_choiceA_original['description']}   from  {random_choiceA_original['country']}")

def random_compare_for_b():
    print("Choice B",end=": ")
    for _ in range(0,1) :
        print(f"name :{random_choiceB_original['name']}  a {random_choiceB_original['description']}   from  {random_choiceB_original['country']}")

def check_user_choice(user_choice_):
    global flag
    global score
    if user_choice_=='a':
        if a>b:
            print("You win!... try again")
            score += 1
            print(f"Your score is: {score}")
        else:
                print("You lost!... try again")
                flag=False
    elif user_choice_=='b':
         if b>a:
            print("You win!... try again")
            score+=1
            print(f"Your score is: {score}")
         else:
            print("You lose!... try again")
            flag=False

def cls():
        print('\n'*50)

while flag:
    random_compare_for_a()
    print(art.logo)
    random_compare_for_b()
    user_choice=input("\nwho has the most followers? ").lower()#####         A
    check_user_choice(user_choice)
    random_choiceA_original=random_choiceB_original
    random_choiceB_original=random.choice(game_data.data)
    a=random_choiceA_original['follower_count']
    b=random_choiceB_original['follower_count']
    cls()














