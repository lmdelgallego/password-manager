import json
from secrets import choice
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """
    Generates a password based on the user's input.
    """
    password_field.delete(0, END)
    password_list = []

    password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_field.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """
    Saves the password to a file.
    """

    website = website_field.get()
    password = password_field.get()
    email = email_username_field.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(
            "Oops", "Please make sure you haven't left any fields empty.")
    else:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            print(data)
            data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        website_field.delete(0, END)
        password_field.delete(0, END)

        print("Password saved.")

    # ---------------------------- UI SETUP ------------------------------- #


windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# LABELS

website_label = Label(text="Website:", font=(FONT_NAME, 12))
website_label.grid(column=0, row=1, sticky="W")

email_username_label = Label(text="Email/Username:", font=(FONT_NAME, 12))
email_username_label.grid(column=0, row=2, sticky="W")

password_label = Label(text="Password:", font=(FONT_NAME, 12))
password_label.grid(column=0, row=3, sticky="W")

# ENTRY FIELDS
website_field = Entry(width=35)
website_field.grid(column=1, row=1, columnspan=2, sticky="W")
website_field.focus()

email_username_field = Entry(width=35)
email_username_field.grid(column=1, row=2, columnspan=2, sticky="W")
email_username_field.insert(END, "alucardluis@gmail.com")

password_field = Entry(width=21)
password_field.grid(column=1, row=3, sticky="W")

# BUTTONS

generate_password_button = Button(
    text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="W")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")

windows.mainloop()
