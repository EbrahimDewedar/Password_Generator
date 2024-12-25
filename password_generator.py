
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters= [choice(letters) for letter in range(randint(8,10))]
    password_numbers= [choice(numbers) for number in range(randint(1,2))]
    password_symbols= [choice(symbols) for symbol in range(randint(1,2))]

    password_list= password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password= ''.join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    web= web_entry.get()
    email= email_entry.get()
    password= password_entry.get()
    if len(web)== 0 or len(password)== 0:
        messagebox.showinfo(title= 'Oops', message= "please make sure you haven't left any fields empty")
    else:
        is_ok= messagebox.askokcancel(title= 'web', message= f'these are entered details\nemail:'
                                f'{email}\npassword: {password}\nLs it ok to save?')
        if is_ok:
            with open('hima_data.txt', 'a') as file:
                file.write(f'{web} | {email} | {password}\n')
                web_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title('Password Generator')
window.config(padx= 50, pady= 50)

canvas= Canvas(width= 200, height= 200)
my_logo= PhotoImage(file= 'logo.png')
canvas.create_image(100,100, image= my_logo)
canvas.grid(column= 1, row= 0)

# labels
web_label= Label(text= 'Website')
web_label.grid(column= 0, row= 1)
email_label= Label(text= 'Email/Username')
email_label.grid(column= 0, row= 2)
password_label= Label(text= 'Password')
password_label.grid(column= 0, row= 3)

# Entries
web_entry= Entry(width= 35)
web_entry.focus()
web_entry.grid(column= 1, row= 1, columnspan= 2)
email_entry= Entry(width= 35)
email_entry.insert(END, 'ebrahim_dewedar@gmail.com')
email_entry.grid(column= 1, row= 2, columnspan= 2)
password_entry= Entry(width= 21)
password_entry.grid(column= 1, row= 3)

# Buttons
generate_password_button= Button(text= 'Generate Password', command= generate_password)
generate_password_button.grid(column= 2, row= 3)
add_button= Button(text= 'Add', command= save_password, width= 36)
add_button.grid(column= 1, row= 4, columnspan= 2)

window.mainloop()