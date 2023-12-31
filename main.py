from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_card=PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=front_card)
canvas.create_text(400,150,text="Title",fill="black",font=("Arial",40,"italic"))
canvas.create_text(400,263,text="Word",fill="black",font=("Arial",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)


wrong_img=PhotoImage(file="images/wrong.png")
wrong_btn=Button(image=wrong_img,highlightthickness=0)
wrong_btn.grid(column=0,row=1)

right_img=PhotoImage(file="images/right.png")
right_btn=Button(image=right_img,highlightthickness=0)
right_btn.grid(column=1,row=1)


window.mainloop()