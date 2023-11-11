from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
   data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
   orginal_data = pandas.read_csv("./data/french_words.csv")
   print(orginal_data)
   to_learn = orginal_data.to_dict(orient="records")
else:
   to_learn = data.to_dict(orient="records")  #it gives the values to list in dict [{'French': 'partie', 'English': 'part'}, {'French': 'histoire',

def next_card():
    global current_card,flip_timmer
    window.after_cancel(flip_timmer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(words, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timmer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(words, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background,image=back_image)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()


window = Tk()
window.title("French to Eng Leaner")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timmer = window.after(3000,func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 262, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)
words = canvas.create_text(400, 250, text="", fill="black", font=("Ariel", 60, 'bold'))
card_title = canvas.create_text(400, 128, text="", fill="black", font=("Ariel", 40, 'bold'))

# Button
Button_r_img = PhotoImage(file="./images/right.png")
Button_right = Button(image=Button_r_img, highlightthickness=0,command=is_known)
Button_right.grid(column=1, row=1)

Button_w_img = PhotoImage(file="./images/wrong.png")
Button_left = Button(image=Button_w_img, highlightthickness=0,command=next_card)
Button_left.grid(column=0, row=1)

next_card()  # avoiding the inital opening empty words and card-tilt





window.mainloop()
#-----------------------------------------------random_F_word----------------------------------------------


