BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")  #it gives the values to list in dict [{'French': 'partie', 'English': 'part'}, {'French': 'histoire',


window = Tk()
window.title("French to Eng Leaner")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_loc = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 262, image=image_loc)
canvas.grid(column=0, row=0, columnspan=2)
#--------------------------next_card--------------------------
def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    print(current_card["French"])
    canvas.itemconfig(words, text=current_card["French"])

#----------------------------------------------------------------------
# label

words = canvas.create_text(400, 250, text="Words", fill="black", font=("Ariel", 60, 'bold'))
card_title = canvas.create_text(400, 128, text="shuhaib", fill="black", font=("Ariel", 40, 'bold'))

# Button
Button_r_img = PhotoImage(file="./images/right.png")
Button_right = Button(image=Button_r_img, highlightthickness=0,command=next_card)
Button_right.grid(column=1, row=1)

Button_w_img = PhotoImage(file="./images/wrong.png")
Button_left = Button(image=Button_w_img, highlightthickness=0,command=next_card)
Button_left.grid(column=0, row=1)
window.mainloop()


#-----------------------------------------------random_F_word----------------------------------------------


