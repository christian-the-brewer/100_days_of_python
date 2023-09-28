# Language Learning flash card app by Christian Brewer

import tkinter
import pandas as pd
import random


# word data
try:
    df = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    df = pd.read_csv("data/it_to_en_1000_word_list.csv")
finally:
    words_to_learn = df.to_dict(orient="records")


started = False
current_card = ""
# colors

BG_COLOR = "#B1DDC6"
Font = "#26577C"


language_1 = "Italian"
language_2 = "English"


# random_word func


def random_word():
    global flip_timer, current_card, started
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card, image=front_image)
    canvas.itemconfig(
        shown_word, text=current_card[language_1], font=("Ariel", 60, "bold"), fill="black")
    canvas.itemconfig(language, text=language_1, fill="black")
    flip_timer = window.after(3000, func=flip_card)
    if not started:
        started = True


def flip_card():
    global current_card
    canvas.itemconfig(card, image=back_image)
    canvas.itemconfig(
        shown_word, text=current_card[language_2], font=("Ariel", 60, "bold"), fill="white")
    canvas.itemconfig(language, text=language_2, fill="white")

# known_word


def known_word():
    global current_card
    if started:
        # remove word
        print(len(words_to_learn))
        words_to_learn.remove(current_card)
        print(f"{current_card[language_1]} removed")
        print(len(words_to_learn))
        data = pd.DataFrame(words_to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)

        random_word()
    else:
        random_word()


window = tkinter.Tk()
window.minsize(width=600, height=600)
window.config(padx=50, pady=50, bg=BG_COLOR)
window.title("Language Flash Cards")

flip_timer = window.after(3000, func=flip_card)
window.after_cancel(flip_timer)

canvas = tkinter.Canvas(width=800, height=526,
                        highlightthickness=0, bg=BG_COLOR)

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
right_image = tkinter.PhotoImage(file="images/right.png")
back_image = tkinter.PhotoImage(file="images/card_back.png")
front_image = tkinter.PhotoImage(file="images/card_front.png")

card = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)


# text on canvas
language = canvas.create_text(
    400, 150, text="Italian Flashcards", font=("Ariel", 40, "italic"),)
shown_word = canvas.create_text(
    400, 263, text="Click a button to start", font=("Ariel", 20, "bold"), )

# buttons
wrong_button = tkinter.Button(
    image=wrong_image, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=1)
right_button = tkinter.Button(
    image=right_image, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=0)


window.mainloop()
