import tkinter as tk
from tkinter import messagebox
import random

BLUE = "#3b82f6"

#Window
window = tk.Tk()
window.title("Password Manager")
window.config(
    padx=50,
    pady=40
)

#Canvas and Image
canvas = tk.Canvas(
    window,
    width=200,
    height=200,
    highlightthickness=0
)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(
    row=0,
    column=1,
    pady=(0, 20)
)

#Labels
website_label = tk.Label(
    window,
    text="Website:",
    font=("Courier New", 12)
)
website_label.grid(
    row=1,
    column=0,
    padx=(0, 20),
    pady=5
)

email_label = tk.Label(
    window,
    text="Email/Username:",
    font=("Courier New", 12)
)
email_label.grid(
    row=2,
    column=0,
    padx=(0, 20),
    pady=5
)

password_label = tk.Label(
    window,
    text="Password:",
    font=("Courier New", 12)
)
password_label.grid(
    row=3,
    column=0,
    padx=(0, 20),
    pady=5
)

#Entries
website_entry = tk.Entry(
    window,
    width=40
)
website_entry.grid(
    row=1,
    column=1,
    columnspan=2,
    sticky="ew",
    pady=5
)
website_entry.focus()

email_entry = tk.Entry(
    window,
    width=40
)
email_entry.grid(
    row=2,
    column=1,
    columnspan=2,
    sticky="ew",
    pady=5
)

password_entry = tk.Entry(
    window,
    width=27
)
password_entry.grid(
    row=3,
    column=1,
    sticky="w",
    pady=5
)

#Buttons and Their Functions
def generate_password():
    password_entry.delete(0, tk.END)

    lower_case = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    upper_case = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    number = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    symbol = ("-", "_", ".", ":", "!", "?", ",", ";", "+", "*", "/", "=", "%", "@", "#", "$", "&", "*", "(", ")", "'", "^")

    pass_char_list = []

    pass_char_list.append(random.choice(lower_case))
    pass_char_list.append(random.choice(upper_case))
    pass_char_list.append(random.choice(number))
    pass_char_list.append(random.choice(symbol))

    all_char = (*upper_case, *lower_case, *number, *symbol)

    number_of_char = random.randint(8, 12)
    for _ in range(number_of_char):
        random_char = random.choice(all_char)
        pass_char_list.append(random_char)

    random.shuffle(pass_char_list)
    password = "".join(pass_char_list)

    password_entry.insert(0, password)

password_generate_button = tk.Button(
    window,
    text="Generate Password",
    font=("Courier New", 10),
    relief="ridge",
    width=20,
    command=generate_password
)
password_generate_button.grid(
    row=3,
    column=2,
    sticky="e",
    pady=5
)

def add_to_file():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not email or not password:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")
    else:
        save_or_not = messagebox.askokcancel(title="Confirmation", 
                                            message=f"These are details that are entered: "
                                            f"\nWebsite: {website}"
                                            f"\nEmail: {email}" 
                                            f"\nPassword: {password}" 
                                            "\nIs it okay to save?")

        text = f"{website} | {email} | {password}\n"

        if save_or_not:
            with open("data.txt", mode="a", encoding="utf-8") as file:
                file.write(text)

            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

            website_entry.focus()

add_button = tk.Button(
    window,
    text="Add",
    font=("Courier New", 10),
    relief="ridge",
    width=40,
    bg=BLUE,
    command=add_to_file
)
add_button.grid(
    row=4,
    column=1,
    columnspan=2,
    sticky="ew",
    pady=(10, 0)
)

window.mainloop()