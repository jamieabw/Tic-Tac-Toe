from tkinter import Button, Label, Frame, Tk, messagebox
import random
# Player contains import variables and methods which need to be accessed anywhere
class Player:
    players = ["x", "o"]
    player = random.choice(players)
    end = False # this variable is a bit messy being here, but is used to test if the game has ended
    winner = None # will be set to either 'x' or 'o' depending on the winner

    @classmethod # basically hard coded in, switches the player after every go
    def change_player(cls):
        if cls.player == "x":
            cls.player = cls.players[1]
        else:
            cls.player = cls.players[0]
        player_label.config(text=f"Current player: {Player.player}")

        # function activated if the game is finished, displays the winner

def end_game_win(player):
        Player.end = True
        Player.winner = player
        message = messagebox.showinfo(title="Winner!", message=f"PLAYER {Player.winner} won!")

# checks through all win conditions each turn to determine if the game has been won

def check_win(row, column):
    if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
        end_game_win(Player.player)
    elif buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
        end_game_win(Player.player)
    elif buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        end_game_win(Player.player)
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        end_game_win(Player.player)


# functions for when the game is finished, displays it is a draw
def end_game_draw():
    Player.end = True
    messagebox.showinfo(title="Draw", message="This game was a draw.")

# loops through each button to check if they have been used, if all are used and theres no winner then it is a draw
def check_draw():
    if Player.end == True:
        return
    draw = True
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                draw = False
    if draw:
        end_game_draw()      

# function to test if a player has already placed there, if not then it places itself there

def place(player, row, column):
    if buttons[row][column]['text'] != "" or Player.end is True:
        return
    buttons[row][column]['text'] = f"{player}"
    check_win(row, column)
    check_draw()
    Player.change_player()

# a simple loop to generate the buttons (the grid), you can change size by editing the row range value or column range value
def create_board(buttons, frame):
    for row in range(3):
        for column in range(3):
            buttons[row][column] =\
            Button(frame, width=20, height=10, text="",command= lambda row=row, column=column : place(Player.player, row, column))
            buttons[row][column].grid(row=row, column=column)

# a button function used to restart the game and clear the board whenever, completely resets game

def restart():
    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""
    Player.end = False

window = Tk()
window.title("Tic-Tac-Toe")
player_label = Label(window, text=f"Current player: {Player.player}")
player_label.pack()
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
frame = Frame(window) # frame used here to grid the buttons together to make the iconic grid look
frame.pack()
create_board(buttons, frame)
restart_button = Button(text="Restart", command=restart) # button to restart the game whenever
restart_button.pack()
window.mainloop()
