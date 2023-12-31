from tkinter import *
from tkinter import messagebox
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card={}

# ---------------------------- CHOOSE A FILE ------------------------------- #
try:
    data=pandas.read_csv("data/words_to_learn.csv")
    df_dict=data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    data=pandas.read_csv("data/french_words.csv")
    df_dict=data.to_dict(orient="records")
except FileNotFoundError:
    data=pandas.read_csv("data/french_words.csv")
    df_dict=data.to_dict(orient="records")

# ---------------------------- RANDOM CARD ------------------------------- #
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card,image=front_card)
    try:
        current_card=choice(df_dict)
    except IndexError:
        messagebox.showinfo("Congrats","You now have leared all the words")
        return
    canvas.itemconfig(lang,text="French",fill="black")
    canvas.itemconfig(word,text=f"{current_card["French"]}",fill="black")
    flip_timer=window.after(3000,flip)

# ---------------------------- FLIP CARD ------------------------------- #
def flip():
    canvas.itemconfig(card,image=back_card)
    canvas.itemconfig(lang,text="English",fill="white")
    canvas.itemconfig(word,text=f"{current_card["English"]}",fill="white")

# ---------------------------- KNOWS THE WORD ------------------------------- #
def known_card():
    try:
        df_dict.remove(current_card)
    except ValueError:
        messagebox.showinfo("Congrats","You now know all the words")
        return
    new_data=pandas.DataFrame(df_dict)
    new_data.to_csv("data/words_to_learn.csv",index=False)
    next_card()
       

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,flip)

canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_card=PhotoImage(file="images/card_front.png")
back_card=PhotoImage(file="images/card_back.png")
card=canvas.create_image(400,263,image=front_card)
lang=canvas.create_text(400,150,text="Title",fill="black",font=("Arial",40,"italic"))
word=canvas.create_text(400,263,text="Word",fill="black",font=("Arial",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)


wrong_img=PhotoImage(file="images/wrong.png")
wrong_btn=Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_btn.grid(column=0,row=1)

right_img=PhotoImage(file="images/right.png")
right_btn=Button(image=right_img,highlightthickness=0,command=known_card)
right_btn.grid(column=1,row=1)

next_card()

window.mainloop()