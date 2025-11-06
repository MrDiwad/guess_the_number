import random

def diff_lvl():
    diff_level=input("Please choose level of difficulty(1=easy[1-50] 2=medium[1-100] 3=hard[1-1000])\n")
    try:
        diff_level=int(diff_level)
    except:
        print("Error! Provide a correct number!")
        diff_lvl()
    if (diff_level>0 and diff_level<=3):
        return diff_level
    else:
        print("Error! Provide a correct number!")
        diff_lvl()

difficulty_level=diff_lvl()

def rangeOfSecretNumber():
    if difficulty_level==1:
        return 50
    elif difficulty_level==2:
        return 100
    else:
        return 1000

def menu():
    print("Welcome to game called Guess the number!")
    print("Choose what do you want to do (1-play the game 2-save best score to file 3-quit)")
    answer=int(input())

best_score=None
def game():
    secret_number=random.randint(1,rangeOfSecretNumber())
    number_of_tries=0
    while True:
        guess_of_user=input("Guess a number!\n")
        try:
            guess_of_user=int(guess_of_user)
        except:
            print("Provide number!")
            continue
        guess_of_user=int(guess_of_user)
        number_of_tries+=1
        if guess_of_user==secret_number:
            print(f"Congratulation! You guessed the number! Your number of tries: {number_of_tries}")
        elif guess_of_user<secret_number:
            print("Wrong! Try bigger number!")
        else:
            print("Wrong! Try lower number!")
        if number_of_tries==7:
            print("You lost! You reached maximum of tries (7). Try again!")
            break

# dokończyć menu, zapetlic gre