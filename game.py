# TYPE GAME and GUESS GAME
from string import *
from math import *
import random
import sys, select
import time
from threading import Thread
import threading
import sys
import os
import termios, fcntl
import colorsys



# -------GLOBAL  VARIABLES
answer = "None"
x= False
is_run=True


# -------------TYPE GAME -----------
def type():
    global answer
    string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = random.choice(string) + (random.choice(string)) + (random.choice(string)) + (random.choice(string))
    print("You have 10 Seconds to Type the below word:")
    print("Type : ",s)
    #time.sleep(10)
    input_usr()
    for i in range(0, 9):

        if answer=="None":
            time.sleep(1)
        else:
            time.sleep(1)
            break
    if answer==s:
        print("**** Great, You WIN !")
    elif answer == "None":
        print("\033[91m {}\033[00m".format("# TIME OUT ...."))

    else:
        print("\033[91m {}\033[00m".format("WRONG...."))
# -------------END OF TYPE GAME -----------






#--------------MATH GAME ------------------
def math():
    global answer
    print("You have 10 seconds to solve this math problem:")
    a=random.randint(0,101)
    b=random.randint(0,51)
    operator ={0:"*", 1:"/", 2:"+",3:"-"}
    c= random.randint(0,3)
    print(c)
    if c==0:
        print(a,operator[c],b, " = ")
        cal=a*b
    elif c==1:
        t=max(a,b)
        b=min(a,b)
        a=t
        print(a,operator[c],b, " = ")
        cal=a/b
    elif c==2:
        print(a,operator[c],b, " = ")
        cal=a+b
    elif c==3:
        print(a,operator[c],b, " = ")
        cal=a-b
    #time.sleep(10)
    input_usr()
    for i in range(0, 9):

        if answer=="None":
            time.sleep(1)
        else:
            time.sleep(1)
            break
    if answer != "None":
        ans = float(answer)
        if ans==cal:
            print("**** Great, You WIN !")
        else:
            print("\033[91m {}\033[00m".format("# Incorrect"))
    else:
        print("\033[91m {}\033[00m".format("# TIME OUT ...."))
#--------------MATH GAME ENDs here------------------






#--------------GUESS THE NUMBER --------------------
def guess():
    print ("We just taken one random number between 1 to 100 in mind, you have to guess the Number  in 6 guesses:")
    number = random.randint(1, 99)
    print("Number is: ", number)
    guesses = 1
    while guesses <= 6:
        print ("\n\n#This is your guess no :  %d" %guesses)
        guess = int(input("Enter an integer from 1 to 100: "))
        guesses +=1

        if guess < number:
            print ("*hint: guess is low, try a big number")
            if (guesses == 4):
                print("*hint: number lies between", number + 4, " - ", number - 4)
        elif guess > number:
            print ("*hint: guess is high, try a low number")
            if (guesses == 4):
                print("*hint: number lies between", number + 4, " - ", number - 4)
        elif guess == number:
            break


    if guess == number:
        guesses = str(guesses)
    print ("\nHurray!\nYou guessed it right in : ", guesses ," guesses")

    if guess != number:
        number = str(number)
    print ("The secret number was: ", number)
#--------------Guess THE NUMBER ENDs here --------------------






# -------------INPUT FROM THE USER-----------
def input_usr():
    global answer
    answer =input("")


# ------------INPUT ENDS HERE ----------------
#------------- Calling THREADS ---------------
def main_call():
    print("Choose the Game You Want to Play:")
    print("1. Typing Game")
    print("2. Number Guess game")
    print("3. Math Game")
    print("4. Exit the Game")
    game_select=input("\n\n Enter your choice: ")
    if game_select=='1':
        #Thread(target=type).start()
        game = threading.Thread(target=type)
        game.daemon = True
        game.start()
        game.join()
    elif game_select=='2':
        #Thread(target = guess).start()
        game = threading.Thread(target=guess)
        game.daemon = True
        game.start()
        game.join()

    elif game_select=='3':
        game = threading.Thread(target=math)
        game.daemon = True
        game.start()
        game.join()
    elif game_select == '4':
        exit()
    else:
        print("Invalid Choice Entered")

# ------------WELCOME SCREEN START
print("### Quick GAMES by HSK ####")
name=str(input("Enter your name: "))
os.system("clear")
print("\nWelcome "+name+" ! ")

loading = "..............................#"
print("# Loading Games for you .")
for l in loading:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.1)

while is_run:
    os.system('clear')
    main_call()
    if input("\n#Game Over#\nTry again ? Y/N : ")=="Y":
        is_run=True
    else:
        is_run=False






# ------ WElcome Screen END -------



#time.sleep(2)
# LINUX
#os.system('clear')

