import random
import os

correct = 0
incorrect = 0

def scoreboard():
    print("==========================================")
    print("=      \033[91mQuiz Game By Pratyush Kashyap     \033[0m=")
    print("=                                        =")
    print(f"=  \033[94m  Correct Answer: {correct} \t\t\t\033[0m=")
    print(f"=  \033[94m  Incorrect Answer : {incorrect}\t\t\033[0m=")
    print("=                                        =")
    print("==========================================\n\n")

def rules():
    print('''WELCOME TO THE BOLLYWOOD MCQ GAME
The rules of this game are -:
1. You cannot choose multiple options.
2. Your scores will be maintained.
3. You cannot exit the game in between.''')


def question():
    global correct, incorrect
    
    print("The questions are as follows:")
    
    # Question 1
    print("Jhanvi Kapoor is the daughter of which veteran Actress?")
    print("a. Juhi Chawla\nb. Sonali Bendre\nc. Sridevi\nd. Babita Kapoor")
    ans = input("Please choose your answer: ").lower()
    if ans == 'c':
        print("Correct answer")
        correct += 1
    else:
        print("Incorrect answer, the correct answer is option c")
        incorrect += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    scoreboard()
    
    # Question 2
    print("The next question is:")
    print("What is the Name of Nana Patekar’s character in ‘WELCOME’?")
    print("a. Majnu Shetty\nb. Nana Das\nc. Uday Shetty\nd. Santa Singh")
    ans = input("Please choose your answer: ").lower()
    if ans == 'c':
        print("Correct answer")
        correct += 1
    else:
        print("Incorrect answer, the correct answer is option c")
        incorrect += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    scoreboard()

    # Question 3
    print("The next question is:")
    print("Which Following Actress debuted opposite Shahrukh Khan in movie “Om Shanti Om”?")
    print("a. Sonam Kapoor\nb. Deepika Padukone\nc. Anushka Sharma\nd. Priyanka Chopra")
    ans = input("Please choose your answer: ").lower()
    if ans == 'b':
        print("Correct answer")
        correct += 1
    else:
        print("Incorrect answer, the correct answer is option b")
        incorrect += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    scoreboard()

    # Question 4
    print("The next question is:")
    print("Famous Bollywood Actress “Priyanka Chopra” first movie in Hollywood was _________.")
    print("a. Baywatch\nb. Terminator\nc. Force\nd. Women in Black")
    ans = input("Please choose your answer: ").lower()
    if ans == 'a':
        print("Correct answer")
        correct += 1
    else:
        print("Incorrect answer, the correct answer is option a")
        incorrect += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    scoreboard()

rules()
rul = input("Do You accept the rules: (yes/no) ").lower()
if rul == "no":
    print("Accept and play the game ..... ")
    while True:
        rules()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Accept and play the game ..... ")
        rul = input("Do You accept the rules: (yes/no) ").lower()
        if rul == "yes":
            break
    question()
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    question()
