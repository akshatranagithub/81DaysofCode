import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open("passwords.json", 'r') as data_file:
            data = json.load(data_file)
            website_name = website_entry.get()
            values = data[website_name]
            messagebox.showinfo(title=website_name,
                                message=f"Email: {values['Email']} \nPassword: {values['Password']}")
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No password saved yet!')

    except KeyError:
        messagebox.showerror(title="Error", message=f"No password with the website: {website_name}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    data = {
        website: {
            "Email": email,
            "Password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='Error', message="Please do not leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=f"{website}",
                                       message=f"Entered details: \nEmail: {email} \nPassword: {password} \nDo you want to save?")

        if is_ok:
            try:
                with open("passwords.json", 'r') as data_file:
                    new_data = json.load(data_file)
            except FileNotFoundError:
                with open("passwords.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            else:
                new_data[website] = data[website]
                with open("passwords.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website", pady=5)
website_label.grid(row=1)
email_label = Label(text="Email", pady=5)
email_label.grid(row=2)
password_label = Label(text="Password", pady=5)
password_label.grid(row=3)

website_entry = Entry(text="", width=25)
website_entry.focus()
website_entry.grid(row=1, column=1, padx=2)
email_entry = Entry(text="", width=35)
email_entry.insert(0, "akshat@gmail.com")
email_entry.grid(row=2, column=1, columnspan=3)
password_entry = Entry(text="", width=25)
password_entry.grid(row=3, column=1, padx=2)

search_button = Button(text="Search", command=find_password, width=7)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate", command=generate_password, width=7)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save_password, pady=5)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
