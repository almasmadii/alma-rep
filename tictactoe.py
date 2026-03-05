import tkinter as tk
from operator import truediv
from optparse import check_choice

from PIL import Image,ImageTk
window=tk.Tk()

x_img=Image.open("images/x.png",)
x_img=x_img.resize((25,25))
o_img=Image.open("images/o.png")
o_img=o_img.resize((25,25))
x_photo=ImageTk.PhotoImage(x_img)
o_photo=ImageTk.PhotoImage(o_img)
grid_img = Image.open("images/image.png")
grid_img=grid_img.resize((300, 300))
grid_photo = ImageTk.PhotoImage(grid_img)

grid_label=tk.Label(window,image=grid_photo)
grid_label.grid(row=0,column=0,columnspan=3)
x_label=tk.Label(window,image=x_photo)
current_player = "X"
board=[None]*9
def handle_click(btn,i):
    board[i]=current_player
winning_combos = [
    [0, 1, 2],  # top row
    [3, 4, 5],  # middle row
    [6, 7, 8],  # bottom row
    [0, 3, 6],# left column
    [1, 4, 7],
    [2, 5, 8],
    [0 ,4 ,8],
    [2, 4, 6],
    # 👈 can you fill in the remaining 4?
]

result_label = tk.Label(window, text="", font=("Arial", 16))
result_label.grid(row=1, column=0, columnspan=3)

def check_winner():
    for combo in winning_combos:
        a,b,c=combo
        if board[a]==board[b]==board[c] and board[a] is not None:
            return board[a]
    return None

def handle_click(btn,i):
    global current_player
    board[i]=current_player
    if current_player == "X":
        btn.config(image=x_photo)
        btn.image = x_photo
    else:
        btn.config(image=o_photo)
        btn.image=o_photo
    winner=check_winner()
    if winner:
        result_label.config(text=f"{winner} Wins!")
    current_player="O" if current_player =="X" else "X"
for i in range (0,9):
    btn=tk.Button(window,bg="white",bd=0)
    btn.config(command=lambda b=btn ,idx=i: handle_click(b,idx))
    x=(i%3)*100 +50
    y=(i//3) *100 +50
    btn.place(x=x,y=y)


window.mainloop()
