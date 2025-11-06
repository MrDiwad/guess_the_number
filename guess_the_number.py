import random
import sys

def menu():
    print("==============================")
    print("Welcome to game called Guess the number!")
    print("Choose what do you want to do (1-play the game 2-save best score to file 3-quit)")
    try:
        answer = int(input())
    except ValueError:
        print("Provide correct number")
        return menu()
    if answer==1:
        game()
    elif answer==2:
        with open("score.txt","w") as file:
            file.write(f"Best score: {best_score}")
        print("Best score saved to score.txt")
        menu()
    elif answer==3:
        print("Thanks for playing! Goodbye!")
        sys.exit()
    else:
        print("Provide correct number")

best_score=None

def game():
    global best_score
    diff_level=input("Please choose level of difficulty(1=easy[1-50] 2=medium[1-100] 3=hard[1-1000])\n")
    upper_range=0
    try:
        diff_level=int(diff_level)
    except:
        print("Error! Provide a correct number!")
        game()
    if (diff_level>0 and diff_level<=3):
        diff_level=int(diff_level)
    else:
        print("Error! Provide a correct number!")
        game()
    if diff_level==1:
        upper_range=50
    elif diff_level==2:
        upper_range=100
    else:
        upper_range=1000
    secret_number=random.randint(1,upper_range)
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
            if best_score is None or number_of_tries<best_score:
                best_score=number_of_tries
            menu()
        elif guess_of_user<secret_number:
            print("Wrong! Try bigger number!")
        else:
            print("Wrong! Try lower number!")
        if number_of_tries==7:
            print("You lost! You reached maximum of tries (7). Try again!")
            menu()
menu()