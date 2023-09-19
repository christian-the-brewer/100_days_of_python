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


# spinbox field function


def spinbox_used():
    print(spinbox.get())

# submit button


def calculate():
    if radio_state.get() == 1:
        result_label.config(text=str(float(spinbox.get()) * 1.609344))
        print("converting miles")
    elif radio_state.get() == 2:
        result_label.config(text=str(float(spinbox.get()) * 0.6213712))
        print("converting kilometers")
    else:
        print("cannot get radio state")


# label
title_label = tkinter.Label(text="Miles / Kilometer Converter")
title_label.grid(row=1, column=1)

# radio button for selecting miles or km
radio_state = tkinter.IntVar()
radio_miles = tkinter.Radiobutton(
    text="Miles to Kilometers", value=1, variable=radio_state, command=radio_select)
radio_kms = tkinter.Radiobutton(
    text="Kilometers to Miles", value=2, variable=radio_state, command=radio_select)
radio_miles.grid(row=2, column=1)
radio_kms.grid(row=3, column=1)

# spinbox for units
spinbox = tkinter.Spinbox(width=15, from_=0, command=spinbox_used)
spinbox.grid(row=4, column=1)

# submit button
submit_button = tkinter.Button(text="Convert", command=calculate)
submit_button.grid(row=5, column=1)

# display
result_label = tkinter.Label(text="Result")
result_label.grid(row=6, column=1)

window.mainloop()
