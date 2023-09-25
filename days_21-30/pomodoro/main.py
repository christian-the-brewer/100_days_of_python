# Pomodoro Timer App by Christian Brewer

from tkinter import *
import math

# Constants
PINK = "#e2979c"
RED = "#D80032"
GREEN = "#9bdeac"
BG_COLOR = "#F9DEC9"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark_count = 0
CHECKMARK = "✔"
timer = None

# Timer Reset
def reset_timer():
  global reps, checkmark_count, timer
  window.after_cancel(timer)
  label_1.config(text="Timer", fg=RED)
  canvas.itemconfig(timer_text, text="00:00")
  reps = 0
  checkmark_count = 0
  checkmark_update()
  
# Timer Mechanism
def start_timer():
  global reps, checkmark_count 
  print(reps)
  
  if reps == 7:
    print("long break")
    checkmark_update()
    label_1.config(text="Long Break", fg="#F78CA2")
    count_down(LONG_BREAK_MIN * 60)
    reps = 0
    checkmark_count = 0
    checkmark_update()
  elif reps % 2 == 0:
    label_1.config(text="Focus Time", fg="#D80032")
    print("work")
    count_down(WORK_MIN * 60)
    reps += 1
    checkmark_count += 1
  else:
    label_1.config(text="Break Time", fg="#F78CA2")
    checkmark_update()
    print("short break")
    count_down(SHORT_BREAK_MIN * 60)
    reps += 1

# Countdown
def checkmark_update():
  check_mark.config(text=f"{CHECKMARK * checkmark_count}")

def count_down(count):

  count_min = math.floor(count / 60)
  count_sec = count % 60
  if count_min < 10:
    count_min = f"0{count_min}"
  if count_sec < 10:
    count_sec = f"0{count_sec}"
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    

# UI
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BG_COLOR)

canvas = Canvas(width=200, height=224, bg=BG_COLOR, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

#Timer Label
label_1 = Label(text="Timer", bg=BG_COLOR, fg=RED, font=(FONT_NAME,35,"bold"))
label_1.grid(row=1,column=2)
#Start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3,column=1)
#Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=3,column=3)
#checkmark
check_mark = Label(bg=BG_COLOR, fg=GREEN)
check_mark.grid(row=4,column=2)


window.mainloop()
