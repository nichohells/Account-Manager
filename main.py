from tkinter import *
from tkinter import messagebox
import time
import math
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = box_website.get()
    email = email_box.get()
    password = password_box.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Error", message="You need to fill all spaces")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Char: {website} "
                                                              f"\nAccount: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("accounts.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
                box_website.delete(0, END)
                password_box.delete(0, END)
                email_box.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password")
window.config(padx=50, pady=50)


canvas = Canvas(width=500, height=333, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Char", width=20)
website_label.grid(column=0, row=1)

email_label = Label(text="Account", width=20)
email_label.grid(column=0, row=2)

password_label = Label(text="Password", width=20)
password_label.grid(column=0, row=3)

box_website = Entry(width=35)
box_website.grid(column=1, row=1, columnspan=2)
box_website.focus()

email_box = Entry(width=35)
email_box.grid(column=1, row=2, columnspan=2)
email_box.insert(0, "")


password_box = Entry(width=35)
password_box.grid(column=1, row=3, columnspan=2)


add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
