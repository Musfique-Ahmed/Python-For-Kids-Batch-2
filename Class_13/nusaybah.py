import tkinter as tk

root = tk.Tk()
root.title("conversation")
root.geometry("500x800")
label=tk.Label(root,text="this is how u should mak a short convo")
label.pack()
def say():
    print("hii")
button=tk.Button(root, text="start convo", command=say)
button.pack()

def end():
    print("bye")
button2=tk.Button(root, text="end convo", command=end)
button2.pack()
root.mainloop()