from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def password_generator():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_entries.delete(0, "end")
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_list += [choice(letters) for _ in range(nr_letters)]
    password_list += [choice(symbols) for _ in range(nr_symbols)]
    password_list += [choice(numbers) for _ in range(nr_numbers)]

    shuffle(password_list)

    password = "".join(password_list)

    password_entries.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entries.get()
    password_entries.delete(0, "end")

    try:
        with open("data.json", mode="r") as file:
            # Reading Old data
            data = json.load(file)
            target_website = None
            for key in data:
                if str(key) == website:
                    target_website = key
                    target_email = data[target_website]["email"]
                    target_password = data[target_website]["password"]
                    pyperclip.copy(target_password)
                    messagebox.showinfo(
                        target_website,
                        message=f"Email: {target_email}\nPassword: {target_password}",
                    )
            if target_website == None:
                messagebox.showinfo(
                    title="Sorry", message="No details for the website exists."
                )

    except FileNotFoundError:
        messagebox.showerror("Error", message="No Data File Found!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entries.get()
    email_username = email_username_entries.get()
    password = password_entries.get()

    new_data = {website: {"email": email_username, "password": password}}

    if website == "" or email_username == "" or password == "":
        fields_ok = False
        messagebox.showerror("OOPS", message="Please don't leave any fields empty!")
    else:
        fields_ok = True

    if fields_ok:
        are_details_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email_username}\nPassword: {password}\nIs it ok to save? ",
        )

        if are_details_ok:
            pyperclip.copy(password)
            try:
                with open("data.json", mode="r") as file:
                    # Reading Old data
                    data = json.load(file)
                    # updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                # updating data
                data = new_data
            finally:
                with open("data.json", mode="w") as file:
                    # saving updated data
                    json.dump(data, file, indent=4)
                    website_entries.delete(0, "end")
                    password_entries.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(
    width=200,
    height=200,
    highlightthickness=0,
)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(row=0, column=1)

# LABELS
website_label = Label(
    text="Website:",
)
website_label.grid(
    row=1,
    column=0,
)
# -----------------------------------------------
email_username_label = Label(
    text="Email/Username:",
)
email_username_label.grid(row=2, column=0)
# -----------------------------------------------
password_label = Label(
    text="Password:",
)
password_label.grid(row=3, column=0)

# ENTRIES
website_entries = Entry(
    width=25,
)
website_entries.grid(
    row=1,
    column=1,
)
website_entries.focus()
# -----------------------------------------------
email_username_entries = Entry(
    width=35,
)
email_username_entries.grid(row=2, column=1, columnspan=2)
email_username_entries.insert(0, "YOUR EMAIL GOES HERE")
# -----------------------------------------------
password_entries = Entry(
    width=25,
)
password_entries.grid(row=3, column=1)

# BUTTONS
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)
# -----------------------------------------------
generate_password_button = Button(
    text="Generate Password", width=15, command=password_generator
)
generate_password_button.grid(
    row=3,
    column=2,
)
# -----------------------------------------------
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
