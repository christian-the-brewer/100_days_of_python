# Password manager app by Christian Brewer
import tkinter
from tkinter import messagebox
import random
import pyperclip

# Constants
BG_Color = "#E5CFF7"
PRIMARY_COLOR = "#5B0888"
SECONDARY_COLOR = "#713ABE"
TERTIARY_COLOR = "#9D76C1"

# password generator


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    pw_entry.delete(0, "end")
    pw_entry.insert(0, password)
    pyperclip.copy(password)

# add password


def add_password():
    email = email_entry.get()
    website = web_entry.get()
    password = pw_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo(
            title="Error", message="Please complete all fields.")
        return
    confirm = tkinter.messagebox.askokcancel(
        title=website, message=f"Email/Username: {email}\nPassword: {password}\nIs this correct?")

    if confirm:
        data = f"{website} | {email} | {password}\n"
        file = open("data.txt", "a")
        file.write(data)
        file.close()
        print(data)
        web_entry.delete(0, 'end')
        pw_entry.delete(0, 'end')
        tkinter.messagebox.showinfo(
            title="Success", message="Account added for {website}")


# UI
window = tkinter.Tk()
window.title("Password Manager")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg=BG_Color)

canvas = tkinter.Canvas(width=200, height=200,
                        highlightthickness=0, bg=BG_Color)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
web_label = tkinter.Label(text="Website:", background=BG_Color)
web_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username:", background=BG_Color)
email_label.grid(row=2, column=0)
pw_label = tkinter.Label(text="Password:", background=BG_Color)
pw_label.grid(row=3, column=0)

# entries
website_data = tkinter.StringVar()
web_entry = tkinter.Entry(textvariable=website_data, width=40)
web_entry.grid(row=1, column=1, columnspan=2)
email_data = tkinter.StringVar()
email_entry = tkinter.Entry(textvariable=email_data, width=40)
email_entry.insert(0, "email@email.com")
email_entry.grid(row=2, column=1, columnspan=2)
pw_data = tkinter.StringVar()
pw_entry = tkinter.Entry(textvariable=pw_data, width=21)
pw_entry.grid(row=3, column=1)

# buttons
generate_pw_button = tkinter.Button(
    text="Generate Password", command=generate_password, width=15)
generate_pw_button.grid(row=3, column=2)
add_pw_button = tkinter.Button(
    text="Add", command=add_password, width=37)
add_pw_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
