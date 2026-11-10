
#! Project Name - Tic Tac Toe Game

import tkinter
from tkinter import messagebox
def set_tile(row, column):
    global current_player

    # btn text not change after game over
    if game_over:
        return

    if board[row][column]["text"] != '':
        # already marked Box
        return

    # switching turns
    board[row][column]["text"] = current_player
    if current_player == playerX:
        current_player = playerO
    else:
        current_player = playerX
    # update label
    label["text"] = current_player+"'s turn"

    # check winner after every btn click
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1
    # check winner horizontally, 3 row
    for row in range(3):
        if (board[row][0]["text"] != '') and (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]):
            label.config(text=board[row][0]["text"]+" is Winner..!!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(background=color_light_gray, foreground=color_yellow)

            messagebox.showinfo("Tic Tac Toe", f"Player {board[row][0]["text"]} Wins..!!")
            game_over = True
            return

    # check winner vertically, 3 column
    for column in range(3):
        if (board[0][column]["text"] != '') and (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]):
            label.config(text=board[0][column]["text"]+" is Winner..!!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)

            messagebox.showinfo("Tic Tac Toe", f"Player {board[0][column]["text"]} Wins..!!")
            game_over = True
            return

    # check winner diagonally, 2 diagonals
    # left diagonal
    if (board[0][0]["text"] != '') and (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]):
        label.config(text=board[1][1]["text"]+" is Winner..!!", foreground=color_yellow)
        board[0][0].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][2].config(foreground=color_yellow, background=color_light_gray)

        messagebox.showinfo("Tic Tac Toe", f"Player {board[0][0]["text"]} Wins..!!")
        game_over = True
        return

    # Right diagonal
    if (board[0][2]["text"] != '') and (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]):
        label.config(text=board[1][1]["text"]+" is Winner..!!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)

        messagebox.showinfo("Tic Tac Toe", f"Player {board[0][2]["text"]} Wins..!!")
        game_over = True
        return

    # Check Tie 
    if turns == 9:
        game_over = True
        label.config(text="Oops, It's Tie..!!", foreground=color_yellow)
        messagebox.showinfo("Tic Tac Toe", f"Oops, It's Tie..!!")
        return


def new_game():
    global turns, game_over
    turns = 0
    game_over = False
    label.config(text=current_player+"'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text='', background=color_gray, foreground=color_blue)

# game setup
playerX = 'X'
playerO = 'O'
current_player = 'X'
turns = 0
game_over = False
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# colors
color_blue = '#4584b6'
color_yellow = '#ffde57'
color_gray = '#343434'
color_light_gray = '#646464'

game_window = tkinter.Tk()
game_window.title("Tic Tac Toe Game")
game_window.resizable(False, False)

frame = tkinter.Frame(game_window)

label = tkinter.Label(frame, text=current_player+"'s turn", 
                      font=('consolas', 20), 
                      background=color_gray, 
                      foreground="White"
                      )
label.grid(row=0, column=0, columnspan=3, sticky='we')

for row in range(3):
    for column in range(3):

        board[row][column] = tkinter.Button(frame, text='',
                                            font=('consolas', 50, 'bold'),
                                            background=color_gray,
                                            foreground=color_blue,
                                            width=4, height=1,
                                            command = lambda row=row, column=column: set_tile(row, column)
                                            )
        
        board[row][column].grid(row=row+1, column=column)

restart_btn = tkinter.Button(frame, text='Restart',
                             font=('consolas', 20),
                             background=color_gray,
                             foreground='White',
                             command=new_game
                             )
restart_btn.grid(row=4, column=0, columnspan=3, sticky='we')

frame.pack()

# center the game_window
game_window.update()
window_width = game_window.winfo_width()
window_height = game_window.winfo_height()
screen_width = game_window.winfo_screenwidth()
screen_height = game_window.winfo_screenheight()

window_x = int((screen_width/2)-(window_width/2))
window_y = int((screen_height/2)-(window_height/2))

# format "(w)x(h)+(x)+(y)"
game_window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

game_window.mainloop()