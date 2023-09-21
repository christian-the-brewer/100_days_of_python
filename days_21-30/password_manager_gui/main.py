# Password manager app by Christian Brewer
import tkinter


# Constants
BG_Color = "#E5CFF7"
PRIMARY_COLOR = "#5B0888"
SECONDARY_COLOR = "#713ABE"
TERTIARY_COLOR = "#9D76C1"

# password generator


def generate_password():
    pass

#add password
def add_password():
  email = email_entry.get()
  website = web_entry.get()
  password = pw_entry.get()
  data = f"{website} | {email} | {password}\n"
  file = open("data.txt", "a")
  file.write(data)
  file.close()
  print(data)
  web_entry.delete(0, 'end')
  pw_entry.delete(0, 'end')
  

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
pw_entry = tkinter.Entry(textvariable=pw_data, width=24)
pw_entry.grid(row=3, column=1)

# buttons
generate_pw_button = tkinter.Button(
    text="Generate Password", command=generate_password, width=13)
generate_pw_button.grid(row=3, column=2)
add_pw_button = tkinter.Button(
    text="Add", command=add_password, width=38)
add_pw_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
