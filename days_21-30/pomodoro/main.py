# Pomodoro Timer App by Christian Brewer

from tkinter import *

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BG_COLOR = "#F9DEC9"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Timer Reset

# Timer Mechanism


# Countdown


# UI
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BG_COLOR)

canvas = Canvas(width=200, height=224, bg=BG_COLOR, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


window.mainloop()
