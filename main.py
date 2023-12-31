from tkinter import *
from random import choice
import pandas
BACKGROUND_COLOR = "#B1DDC6"
words_known=[]
data=pandas.read_csv("data/french_words.csv")
df_dict=data.to_dict(orient="records")

def random_word():
    random_word=choice(df_dict)
    french_word=random_word["French"]
    english_word=random_word["English"]

    while True:
        if len(words_known)==len(df_dict) :
            return
        elif french_word in words_known:
            random_word=choice(df_dict)
            french_word=random_word["French"]
            english_word=random_word["English"]
        else:
            break
    words_known.append(french_word)
    canvas.itemconfig(lang,text="French")
    canvas.itemconfig(word,text=french_word)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_card=PhotoImage(file="images/card_front.png")
card=canvas.create_image(400,263,image=front_card)
lang=canvas.create_text(400,150,text="Title",fill="black",font=("Arial",40,"italic"))
word=canvas.create_text(400,263,text="Word",fill="black",font=("Arial",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)


wrong_img=PhotoImage(file="images/wrong.png")
wrong_btn=Button(image=wrong_img,highlightthickness=0,command=random_word)
wrong_btn.grid(column=0,row=1)

right_img=PhotoImage(file="images/right.png")
right_btn=Button(image=right_img,highlightthickness=0,command=random_word)
right_btn.grid(column=1,row=1)

random_word()

window.mainloop()