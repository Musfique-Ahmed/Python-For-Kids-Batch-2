import tkinter as tk


root = tk.Tk()
root.title("My First GUI")
root.geometry("600x400")

label = tk.Label(root, text= " Hello, How are you? ")
label.pack()

def say_hello():
    print("I am good how are you?")
    label2 = tk.Label(root, text= " I am good how are you? ")
    label2.pack()

button = tk.Button(root, text= "I dare you to click me", command=say_hello)
button.pack()


root.mainloop()


