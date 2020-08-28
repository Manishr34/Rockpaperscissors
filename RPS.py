from tkinter import *
import random
main = Tk()
main.title("Rock Paper Scissors Game")
Font =("times")
title = Label(text="Rock Paper Scissors",font=("times",20),fg="grey")
title.pack()

winner = Label(text="Lets Play The Game...",fg="green",font=("times",13),pady=8)
winner.pack()

frame = Frame(main)
frame.pack()

options = Label(frame,text="Your Options : ",font=Font,fg="grey")
options.grid(row=0,column=0,pady=8)

rock = Button(frame, text = 'Rock', width = 15, bd = 0, bg = 'pink', pady = 5, command = lambda: choice(options[0]))
rock.grid(row = 1, column = 1, padx = 8, pady = 5)

paper = Button(frame, text = 'Paper', width = 15, bd = 0, bg = 'silver', pady = 5, command = lambda: choice(options[1]))
paper.grid(row = 1, column = 2, padx = 8, pady = 5)

scissors = Button(frame, text = 'Scissors', width = 15, bd = 0, bg = 'light blue', pady = 5, command = lambda: choice(options[2]))
scissors.grid(row = 1, column = 3, padx = 8, pady = 5)

score = Label(frame,text="Score : ",font=Font,fg="grey")
score.grid(row=2,column=0)

player_choice_label = Label(frame, text = 'You Selected : ---', font = Font)
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(frame, text = 'Your Score : -', font = Font)
player_score_label.grid(row = 3, column = 2, pady = 5)

computer_choice_label = Label(frame, text = 'Computer Selected : ---', font=Font, fg = 'black')
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(frame, text = 'Computer Score : -', font = Font, fg = 'black')
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('scissors',2)]
def choice(player_input):
    global player_score, computer_score
    computer_input = get_computer_choice()
    player_choice_label.config(text = 'Your Selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])
    if(player_input == computer_input):
        winner.config(text = "Tie")
    elif((player_input[1] - computer_input[1]) % 3 == 1):
        player_score += 1
        winner.config(text="You Won!!!")
        player_score_label.config(text = 'Your Score : ' + str(player_score))
    else:
        computer_score += 1
        winner.config(text="Computer Won!!!")
        computer_score_label.config(text='Your Score : ' + str(computer_score))
#Function to Randomly Select Computer Choice
def get_computer_choice():
    return random.choice(options)

main.geometry('700x300')
main.mainloop()


