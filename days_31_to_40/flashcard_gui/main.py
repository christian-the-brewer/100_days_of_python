# Language Learning flash card app by Christian Brewer

import tkinter
import pandas as pd
import random
import time

# word data
df = pd.read_csv("it_to_en_1000_word_list.csv")


# colors

BG_COLOR = "#B1DDC6"
Font = "#26577C"
window = tkinter.Tk()
window.minsize(width=600, height=600)
window.config(padx=50, pady=50, bg=BG_COLOR)
window.title("Language Flash Cards")

language_1 = "Italian"
language_2 = "English"

global num

# random_word func


def random_word():
  num = random.randint(0, len(df))
  canvas.itemconfig(shown_word,text=df.loc[num][language_1])
  time.sleep(3)
  
  


word = "test"

canvas = tkinter.Canvas(width=800, height=526,
                        highlightthickness=0, bg=BG_COLOR)

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
right_image = tkinter.PhotoImage(file="images/right.png")
back_image = tkinter.PhotoImage(file="images/card_back.png")
front_image = tkinter.PhotoImage(file="images/card_front.png")

canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

# text on canvas
language = canvas.create_text(
    400, 150, text=language_1, font=("Ariel", 40, "italic"),)
shown_word = canvas.create_text(
    400, 263, text=word, font=("Ariel", 60, "bold"), )

# buttons
wrong_button = tkinter.Button(
    image=wrong_image, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=1)
right_button = tkinter.Button(
    image=right_image, highlightthickness=0, command=random_word)
right_button.grid(row=1, column=0)


window.mainloop()
