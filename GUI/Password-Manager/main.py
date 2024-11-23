import os
import sqlite3
import tkinter as tk
from tkinter import ttk

from _sql import add_data, create_table, all_data
from password_generator import password_generator



# CHANGE DIR:
os.chdir(r".\GUI\Password-Manager\data")

# DB CONNECTION:
connection = sqlite3.connect("database.db")
create_table(connection)

# GET ALL DATA:
def get_data(tree):
    global connection

    rows = all_data(connection)
    for item in tree.get_children():
        tree.delete(item)
    
    for title, username, password in rows:
        tree.insert("", "end", values=(title,username,password))


# MAIN WINDOW:
main_window = tk.Tk()
main_window.geometry("645x470")
main_window.resizable(False, False)
main_window.title("Password Manager")
main_window.configure(background='#d5dcda')

# ADD STYLE:
style = ttk.Style()
style.theme_use("clam")

# SHOW DATA FRAME:
display_frame = ttk.LabelFrame(main_window, text="Stored Data", padding=(10, 10))
display_frame.place(x=5, y=180)

tree = ttk.Treeview(display_frame, columns=("Title", "Username", "Password"), show="headings", height=10, padding=5)
tree.heading("Title", text="Title")
tree.heading("Username", text="Username")
tree.heading("Password", text="Password")
tree.pack()

# LOAD DATA:
get_data(tree)

# DATA ENTRY FRAME:
entry_frame = ttk.LabelFrame(
    master = main_window,
    text="Data Entry",
)
entry_frame.place(x=5, y=5, width=410)

# DATA FRAME ITEMS:

# TITLE FIELD:
title = tk.StringVar()
ttk.Label(entry_frame, text="Title:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
title_entry = ttk.Entry(
    master = entry_frame,
    width=32,
    textvariable=title,
).grid(row=2, column=1, pady=5, padx=20)

# USERNAME FIELD:
username = tk.StringVar()
ttk.Label(entry_frame, text="Username:", font=("Arial", 10)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
username_entry = ttk.Entry(
    master = entry_frame,
    width=32,
    textvariable=username,
).grid(row=3, column=1, pady=5, padx=20)

# PASSWORD FIELD:
var_password = tk.StringVar()
ttk.Label(entry_frame, text="Password:", font=("Arial", 10)).grid(row=4, column=0, sticky="w", padx=5, pady=5)
password_entry = ttk.Entry(
    master = entry_frame,
    width=32,
    textvariable = var_password,
).grid(row=4, column=1, pady=5, padx=20)

# SAVE BUTTON:
def save_function():
    global tree
    add_data(
        connection, title=title.get(),
        username=username.get(),
        password=var_password.get()
    )
    get_data(tree)

ttk.Button(entry_frame, text="SAVE", command = lambda: save_function()).grid(row=5, column=2)


# OPTIONS FRAME
options_frame = ttk.LabelFrame(
    master = main_window,
    text="Options",
)
options_frame.place(x=460, y=5, width=183)

# OPTIONS FRAME ITEMS:

# VARS:
length = tk.IntVar(value=8)
number_allow = tk.BooleanVar(value=True)
punctuation = tk.BooleanVar(value=True)

ent_length = ttk.Entry(
    master = options_frame,
    textvariable = length,
    width = 5,
    justify = "center",
).pack()
ttk.Checkbutton(options_frame, text="Number", variable=number_allow).pack(pady=5)
ttk.Checkbutton(options_frame, text="punctuation", variable=punctuation).pack(pady=5)

def pg_function ():
    global var_password

    password = password_generator(length=length.get(),number_allow=number_allow.get(),punctuation=punctuation.get())
    var_password.set(password)

btn_pg = ttk.Button(
    master = options_frame,
    text="Generate Password",
    command = lambda: pg_function()
).pack(padx=5, pady=5)

main_window.mainloop()
connection.close()
