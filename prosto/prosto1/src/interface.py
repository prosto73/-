import tkinter as tk

number=0

def start():
    global number, counter
    number  += 1
    view(counter, number)

def view(counter, _number):
    counter.config(text=_number)


root = tk.Tk()
root.geometry('500x500')
root.title('Task Manager')

counter = tk.Label(text=f"{number}")
counter.pack()
tk.Button(root,text="start", background="light blue", width=18, height=6, command=start) .pack()

root.mainloop()
