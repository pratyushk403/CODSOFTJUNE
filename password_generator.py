import tkinter as tk
import tkinter.messagebox
import pyperclip
import random
import string

def copy_to_clipboard(password):
    pyperclip.copy(password)
    tk.messagebox.showinfo("Copied", "Password copied to clipboard!")

def password_generate(password_length):
    password_len = int(password_length/2)
    rnd = string.ascii_letters + string.digits 
    special_character = ['@','#','!']
    f_psd = ''.join(random.choices(rnd, k=password_length))
    s_psd = ''.join(random.choices(rnd, k=password_len))
    special = ''.join(random.choices(special_character))
    psd = f_psd + special + s_psd

    entry.delete(0, tk.END)
    entry.insert(0, psd)

root = tk.Tk()
root.title('Password Generator')
root.geometry('500x200+600+300')
root.config(bg='#507996')

Random_password = tk.Label(root, text="Password")

Random_password.pack()

entry = tk.Entry(root)
entry.pack()

password_length_label = tk.Label(root, text="Password Length:")

password_length_label.pack()

password_length_spinbox = tk.Spinbox(root, from_=8, to=50)
password_length_spinbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=lambda: password_generate(int(password_length_spinbox.get())))
generate_button.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=lambda: copy_to_clipboard(entry.get()))
copy_button.pack()

root.mainloop()
