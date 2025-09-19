import tkinter as tk

def update_lable():
    user_text = entry.get()
    label.config(text = "You wrote: " + user_text)

root = tk.Tk()
root.title("MY 2nd APP")
root.geometry("600x400")

label = tk.Label(root, text="Hello! Type sometning bellow", font=('Arial', 25))
label.pack(pady=10)


entry = tk.Entry(root, width=50)
entry.pack(pady=5)


button = tk.Button(root, text="Update", command=update_lable)
button.pack()

root.mainloop()