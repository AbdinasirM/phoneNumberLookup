import tkinter as tk
from tkinter import ttk

def display_text():
    text = entry.get()
    label.config(text=text)

# Create the main Tkinter instance
win = tk.Tk()
win.title("Simple Text Display")

# Create and pack the Label widget
label = ttk.Label(win, text="", font=("Courier", 22, "bold"))
label.pack()

# Create and pack the Entry widget
entry = ttk.Entry(win, width=40)
entry.pack()
entry.focus_set()

# Create and pack the Button widget
ttk.Button(win, text="Okay", width=20, command=display_text).pack(pady=20)

win.mainloop()
