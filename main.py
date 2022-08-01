from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

email_username_field = Entry(width=35)
email_username_field.grid(column=1, row=2, columnspan=2, sticky="W")

password_field = Entry(width=21)
password_field.grid(column=1, row=3, sticky="W")

# BUTTONS

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="W")

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")

windows.mainloop()
