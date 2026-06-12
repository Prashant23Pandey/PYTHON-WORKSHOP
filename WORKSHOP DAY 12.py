from tkinter import *
root = Tk()
root.title("Registration Form")
root.geometry("350x250")
Label(root, text="Registration Form", font=("Arial", 14, "bold")).pack(pady=10)
Label(root, text="Email").pack()
email_entry = Entry(root, width=30)
email_entry.pack(pady=5)
Label(root, text="Password").pack()
password_entry = Entry(root, width=30, show="*")
password_entry.pack(pady=5)
def register():
    email = email_entry.get()
    password = password_entry.get()
    result_label.config(
        text=f"Email: {email}\nPassword: {password}"
    )
    email_entry.delete(0, END)
    password_entry.delete(0, END)
Button(root, text="Register", command=register).pack(pady=10)
result_label = Label(root, text="", fg="blue")
result_label.pack()
root.mainloop()
