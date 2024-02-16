import tkinter
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
window = tkinter.Tk()
current_word = ""
data = pd.read_csv("data/words.csv")
dicc = {row.English: row.Spanish for (_, row) in data.iterrows()}
words_list = [row.English for (_, row) in data.iterrows()]
df = pd.DataFrame(data)

#=============== FLIP THE CARD ======================
def flip(picked):
    #window.after_cancel(timer)
    canvas.itemconfig(bg_image,image=back)
    canvas.itemconfig(lenguage,text="Spanish")
    canvas.itemconfig(word,text=picked)
#=============== PICK A RANDOM WORD ======================
def pick_a_word():
    global current_word
    pick = choice(words_list)
    current_word = pick
    canvas.itemconfig(bg_image,image=front)
    canvas.itemconfig(lenguage,text="English")
    canvas.itemconfig(word,text=pick)
    window.after(3000, flip, dicc[pick])

#================= REMOVE CARD ======================
def remove_word():
    global current_word,df
    i = df[df["English"] == current_word].index
    df = df.drop(i)
    df.to_csv("data/words.csv",index=False)
    words_list.remove(current_word)
    pick_a_word()
#================ UI ======================================
window.title("Learning English Program")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

canvas = tkinter.Canvas(width=800,height=526,highlightthickness=0, bg=BACKGROUND_COLOR)
front = tkinter.PhotoImage(file="images\card_front.png")
back = tkinter.PhotoImage(file="images/card_back.png")
bg_image = canvas.create_image(400,263,image=front)
lenguage = canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
word = canvas.create_text(400,256,text="",font=("Arial",60,"bold"))
canvas.grid(columnspan=2,column=0,row=0)

red_image = tkinter.PhotoImage(file="images\wrong.png")
wrong_button = tkinter.Button(image=red_image,highlightthickness=0,command=pick_a_word)
wrong_button.grid(column=0,row=1)

green_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=green_image,highlightthickness=0,command=remove_word)
right_button.grid(column=1,row=1)

pick_a_word()

window.mainloop()
