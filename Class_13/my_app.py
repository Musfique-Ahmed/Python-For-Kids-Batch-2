import tkinter as tk


root = tk.Tk()
root.title("My First GUI")
root.geometry("600x400")

label = tk.Label(root, text= " Hello, How are you? ")
label.pack()

title_label = tk.Label(
            root,
            text="Retail Billing System",
            bd=12,
            relief=tk.GROOVE,
            bg="white",
            fg="red",
            font=("Arial", 30, "bold"),
            pady=2
        )
title_label.pack(fill=tk.X)


root.mainloop()


