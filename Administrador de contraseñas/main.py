import tkinter
import pyperclip
from tkinter import messagebox
import random
import json
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = 5
nr_symbols = 5
nr_numbers = 5
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password = []
    for i in range(0, nr_letters):
        password.append(random.choice(letters))
    for i in range(0, nr_numbers):
        password.insert(random.randint(0, len(password)), random.choice(numbers))
    for i in range(0, nr_symbols):
        password.insert(random.randint(0, len(password)), random.choice(symbols))
    separador = ""
    password = separador.join(password)
    password_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    email = username_input.get()
    web = website_input.get()
    pssword = password_input.get()
    if pssword == "" or web == "" or email == "":
        messagebox.showerror(message="Please, complete all fields",title="Error")
    else:
        confirmation = messagebox.askyesno(title="Password Saver",message=f"Are you sure to save {pssword} as your new password for {web}?")
        if confirmation:
            data_dicc = {web:{"username":email,"password":pssword}}
            try:
                with open("Data.jason","r") as data:
                    diccs = json.load(data)

            except:
                with open("Data.jason","w") as data:
                    json.dump(diccs,data,indent=4)
            else:
                diccs.update(data_dicc)
                with open("Data.jason","w") as data:
                    json.dump(diccs,data,indent=4)
            finally:
                password_input.delete(0,tkinter.END)
                website_input.delete(0,tkinter.END)

def read_data():
    web = website_input.get()
    with open("Data.jason","r") as data:
        diccs = json.load(data)
    try:
        info = diccs[web]
    except:
        messagebox.showerror(title="Error",message="Information not found")
    else:
        messagebox.showinfo(title="Data",message=f"Username/Email: {info['username']}\n Password: {info['password']}")
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager & Generator")
window.config(bg="white",pady=20,padx=20)

canvas = tkinter.Canvas(width=200,height=200,highlightthickness=0,bg="white")
lock_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(50,100,image=lock_image)
canvas.grid(column=1,row=0)

website = tkinter.Label(text="Website:",bg="white")
website.grid(column=0,row=1)
website.config(padx=20)

website_input = tkinter.Entry(width=21)
website_input.grid(column=1,row=1,sticky="EW")
website_input.focus()

search_button = tkinter.Button(text="Search",font=("Arial",8,"normal"),command=read_data)
search_button.grid(column=2,row=1,sticky="EW")

username = tkinter.Label(text="Email/Username: ",bg="white")
username.grid(column=0,row=2)

username_input = tkinter.Entry(width=35)
username_input.grid(column=1,row=2,columnspan=2,sticky="EW")
username_input.insert(0,"dial_99_11@hotmail.com")
password = tkinter.Label(text="Password:",bg="white",)
password.grid(column=0,row=3)

password_input = tkinter.Entry(width=21)
password_input.grid(column=1,row=3,sticky="EW")

password_button = tkinter.Button(text="Generate Password",font=("Arial",8,"normal"),command=password_generator)
password_button.grid(column=2,row=3,sticky="EW")

add_button = tkinter.Button(text="Add",font=("Arial",8,"normal"),width=36,command=save_data)
add_button.grid(column=1,row=4,columnspan=2,sticky="EW")
window.mainloop()
