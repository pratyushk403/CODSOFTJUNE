import tkinter as tk
from tkinter import messagebox
import pyperclip

def copy_to_clipboard(link):
    pyperclip.copy(link)
    messagebox.showinfo("Copied", "Link copied to clipboard!")


def show_custom_popup():
    popup = tk.Toplevel(root)
    popup.title("Social Links")
    popup.geometry("300x200+600+300")
    popup.config(bg='#223441')
    
    social_links = [
        ("",""),
        ("Twitter", "https://twitter.com/pratyushkashy11"),
        ("Instagram", "https://www.instagram.com/pratyushkashyap__/"),
        ("LinkedIn", "https://www.linkedin.com/in/pratyush-kashyap-1a73b7253")
    ]
    
    for label, link in social_links:
        link_label = tk.Label(popup, text=label, fg="red", cursor="hand2", font=("Times", 14), bg='#223441')
        link_label.pack(padx=10, pady=5)
        link_label.bind("<Button-1>", lambda event, link=link: copy_to_clipboard(link))


def add_task(event=None):
    task = task_entry.get()
    if task:
        lb.insert("end", task)
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning","Please Enter any Task ! ")


def delete_task(event=None):
    selected_task_index = lb.curselection()
    if not selected_task_index:
        result = messagebox.askyesno("Delete All Tasks", "No task selected. Do you want to delete all tasks?")
        if result:
            lb.delete(0, "end")
    else:
        lb.delete(selected_task_index)


root = tk.Tk()
# root.iconbitmap("to-do-list.ico")
root.geometry('500x500+500+150')
root.title('To-Do List')
root.config(bg='#223441')
root.resizable(width=False, height=False)


frame = tk.Frame(root)
frame.pack(pady=10)


task_entry = tk.Entry(frame, font=('Times', 14))
task_entry.pack(side="left", fill="both")
task_entry.bind("<Return>",add_task)
task_entry.bind("<Delete>",delete_task)


add_task_button = tk.Button(frame, text="Add Task", command=add_task)
add_task_button.pack(side="left")


delete_button = tk.Button(frame, text="Delete", command=delete_task)
delete_button.pack(side="left")


listbox_frame = tk.Frame(root)
listbox_frame.pack()


lb = tk.Listbox(listbox_frame, width=40, height=15, font=('Times', 14), bd=0, fg='#464646', highlightthickness=0, selectbackground='#a6a6a6', activestyle="none")
lb.pack(side="left",fill="both")


social_popup_button = tk.Button(root, text="Connect to ME ", command=show_custom_popup)
social_popup_button.place(x=200, y=450)


scrollbar = tk.Scrollbar(listbox_frame, command=lb.yview)
scrollbar.pack(side="right", fill="y")
lb.config(yscrollcommand=scrollbar.set)


root.mainloop()