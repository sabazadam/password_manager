from tkinter import *
from tkinter import messagebox
import random
import json
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' , '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+']
random.shuffle(letters)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def passwordGenarator():
    password = ""
    password_entry.delete(first=0,last=END)
    for i in range(12):
        password += random.choice(letters)
    password_entry.insert(string = password,index=END)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def savePassword():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Oops", message="Hey, you missed some of the blanks.")
        return

    is_ok = messagebox.askyesno(message="You fill: "
                        f"\nwebsite name: {website}"
                        f"\nemail: {email}"
                        f"\npassword: {password}"
                        f"\nAre you accept to save data?",title="Make sure your data.")
    if is_ok:
        data = new_data
        try:
            with open("data.json", "r") as data_file:
                #Read the data
                data = json.load(data_file)
                #Update the data
                data.update(new_data)
        except:
            open("data.json", "w")


        with open("data.json", "w") as data_file:
            json.dump(data,data_file,indent=4)


            website_entry.delete(first=0,last=END)
            password_entry.delete(first=0,last=END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50,pady=50)
window.title("Password Manager")


imagefile = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100,100,image =imagefile)
canvas.grid(row=0,column=1)

website = Label(text="Website:")
website.grid(row=1,column = 0)

email_username = Label(text="Email/username: ")
email_username.grid(row = 2, column=0)

password = Label(text="Password: ")
password.grid(row=3,column=0)

website_entry = Entry(width=35)
website_entry.focus()
password_entry = Entry(width=35)
email_username_entry = Entry(width=35)
email_username_entry.insert(string="kerem@gmail.com",index=END)

website_entry.grid(row= 1, column=1, columnspan=2)
email_username_entry.grid(row=2,column=1,columnspan = 2)
password_entry.grid(row = 3, column = 1, columnspan = 2)

generatePassword = Button(text="Generate Password", command=passwordGenarator)
generatePassword.grid(row=3,column=2)

add_button = Button(width=36,text="Add",command=savePassword)
add_button.grid(row=4,column=1,columnspan =2)

window.mainloop()