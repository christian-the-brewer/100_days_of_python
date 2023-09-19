# day_27
# from tkinter import *

# # Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
# window.config(padx=20, pady=20)

# # Labels
# label = Label(text="This is old text")
# label.config(text="This is new text", padx=100, pady=100)
# label.pack()

# # Buttons


# def action():
#     print("Do something")


# # calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()

# # Entries
# entry = Entry(width=30)
# # Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# # Gets text in entry
# print(entry.get())
# entry.pack()

# # Text
# text = Text(height=5, width=30)
# # Puts cursor in textbox.
# text.focus()
# # Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# # Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()

# # Spinbox


# def spinbox_used():
#     # gets the current value in spinbox.
#     print(spinbox.get())


# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# # Scale
# # Called with current scale value.


# def scale_used(value):
#     print(value)


# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# # Checkbutton


# def checkbutton_used():
#     # Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())


# # variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(
#     text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

# # Radiobutton


# def radio_used():
#     print(radio_state.get())


# # Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1,
#                            variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2,
#                            variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()


# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))


# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()


# Mile to Kilometer Converter Project
import tkinter

# set up window with button for selecting unit entry, button for submit, entry field for miles or km to be converted. Some output. A label

window = tkinter.Tk()
window.title("Mile/Kilometer Converter")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# radio button function


def radio_select():
    print(radio_state.get())


# submit button


def calculate():
    if check_entry():
        pass
    else:
        result_label.config(text="Error")
        return

    if mode.state == 1:
        result_label.config(text=str(float(entry.get()) * 1.609344))
        print("converting miles")
    elif mode.state == -1:
        result_label.config(text=str(float(entry.get()) * 0.6213712))
        print("converting kilometers")
    else:
        print("cannot get radio state")


def check_entry():
    string = entry.get()

    if string.isdecimal():
        return True

    else:
        return False

# convert state


class Game_mode:
    def __init__(self, state):
        self.state = 1

    def change_mode(self):
        change_mode()
        self.state *= -1


mode = Game_mode(1)

# function to change conversion mode and labels


def change_mode():

    if mode.state == 1:
        label_1.config(text="Km")
        label_2.config(text="Miles")

    elif mode.state == -1:
        label_1.config(text="Miles")
        label_2.config(text="Km")


# button to swap conversion
swap_button = tkinter.Button(text="Swap", command=mode.change_mode)
swap_button.grid(row=1, column=1)

# entry for units
entry = tkinter.Entry(width=15)
entry.grid(row=1, column=2)

# submit button
submit_button = tkinter.Button(text="Convert", command=calculate)
submit_button.grid(row=3, column=2)

# display
result_label = tkinter.Label(text="Result")
result_label.grid(row=2, column=2)
is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=2, column=1)
label_1 = tkinter.Label(text="Miles")
label_1.grid(row=1, column=3)
label_2 = tkinter.Label(text="Km")
label_2.grid(row=2, column=3)

window.mainloop()
