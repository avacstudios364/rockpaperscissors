from tkinter import *
import tkinter.font as font
import random

game_window = Tk()
game_window.title('Rock, paper, scissors')


player_score = 0
computer_score = 0

options = [('rock', 0),('paper', 1),('scissors', 2)]

def computer_win():
    global computer_score, player_score
    computer_score = computer_score + 1
    winner_label.config(text = 'Computer wins!')
    computer_score_label.config(text = 'Computer score: ' +str(computer_score))
    player_score_label.config(text = 'Player score: ' +str(player_score))

def player_win():
    global computer_score, player_score
    player_score = player_score + 1
    winner_label.config(text = 'Player wins!')
    computer_score_label.config(text = 'Computer score: ' +str(computer_score))
    player_score_label.config(text = 'Player score: ' +str(player_score))

def tie():
    global computer_score, player_score
    winner_label.config(text = 'Its a tie!')
    computer_score_label.config(text = 'Computer score: ' +str(computer_score))
    player_score_label.config(text = 'Player score: ' +str(player_score))

def get_computer_choice():
    return random.choice(options)

def get_player_choice(player_input):
    global computer_score, player_score
    print(player_input)
    computer_input = get_computer_choice()
    print(computer_input)
    player_choice_label.config(text = 'You selected: ' +player_input[0])
    computer_choice_label.config(text = 'Computer selected: ' +computer_input[0])
    
    if (player_input == computer_input):
        tie()
    
    # if player selected rock
    if (player_input[1] == 0): # 0 = rock
        if (computer_input[1] == 1): #1 = paper
            computer_win()
        elif (computer_input[1] == 2): #2 = scissors
            player_win()
   
    #if player selected paper
    elif(player_input[1] == 1):
        if(computer_input[1] == 0):
            player_win()
        elif(computer_input[1] == 2):
            computer_win() 
    
    #if player selected scissors
    elif(player_input[1] == 2):
        if(computer_input[1] == 0):
            computer_win()
        if(computer_input[1] == 1):
            player_win()

app_font = font.Font(size = 12)#

game_title = Label(text = 'Lets play rock, paper, scissors!', font = font.Font(size = 20), fg = 'Purple')
game_title.pack()

winner_label = Label(text = 'Lets start the game!', font = font.Font(size = 15), fg = 'Green')
winner_label.pack(pady = 2)

input_frame = Frame(game_window)
input_frame.pack()

player_options_text = Label(input_frame, text = 'Your options: ', font = app_font, fg = 'green')
player_options_text.grid(row = 0, column = 0, pady = 7)

rock_button = Button(input_frame, text = 'Rock', width = 15, bg = 'salmon', fg = 'white', command = lambda: get_player_choice(options[0]))
rock_button.grid(row = 1, column = 1, pady = 5, padx = 5)

paper_button = Button(input_frame, text = 'Paper', width = 15, bg = 'gray', fg = 'white', command = lambda: get_player_choice(options[0]))
paper_button = Button(row = 3,)

game_window.mainloop()
