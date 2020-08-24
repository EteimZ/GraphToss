import tkinter as tk
from random import randint
import matplotlib.pyplot as plt
import numpy as np

window = tk.Tk()
window.wm_title("GraphToss")

frm = tk.Frame()
frm_1 = tk.Frame()
frm_2 = tk.Frame()

def plot():
    roll = ["head", "tail"]
    times = [m,n]
    plt.bar(roll,times)
    plt.show()

def reset():
    lbl_value1["text"] = "Head: 0"
    lbl_value2["text"] = "Tail: 0"

def toss():
    global m,n;
    m = 0
    n = 0
    
    randy = randint(0,1)
    
    for _ in range(int(entry.get())):
        randy = randint(0,1)
        
        if randy == 0:
            m += 1
        if randy == 1:
            n += 1
    
    lbl_value1["text"] = f"Head: {m}"
    lbl_value2["text"] = f"Tail: {n}"
    

 
frm.rowconfigure(0, minsize=60, weight=1)
frm.columnconfigure([0,1], minsize=30, weight=1)

frm_1.rowconfigure(0, minsize=20, weight=1)
frm_1.columnconfigure([0,1], minsize=50, weight=1)

frm_2.rowconfigure(0, minsize=20, weight=1)
frm_2.columnconfigure([0,1,2], minsize=50, weight=1)

lbl_value1 = tk.Label(master=frm, text="Head: 0")
lbl_value1.grid(row=0, column=0)

lbl_value2 = tk.Label(master=frm, text="Tail: 0")
lbl_value2.grid(row=0, column=1)

# Frame 2
lbl_value3 = tk.Label(master=frm_1, text="# Toss")
lbl_value3.grid(row=0, column=0)

entry = tk.Entry(master=frm_1, text = "")
entry.grid(row=0, column=1)


# Toss Button.
btn = tk.Button(master=frm_2, text="Toss", command = toss)
btn.grid(row=0, column=0)

# Plot Button.
btn_1 = tk.Button(master=frm_2, text="Plot", command= plot)
btn_1.grid(row=0, column=1)

# Reset Button.
btn_2 = tk.Button(master=frm_2, text="Reset", command= reset)
btn_2.grid(row=0, column=2)


frm.pack()
frm_1.pack()
frm_2.pack()

window.mainloop()
