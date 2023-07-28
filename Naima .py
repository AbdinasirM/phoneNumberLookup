# Import the required library
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the geometry
win.geometry("700x350")

def get_input():
    label.config(text="" + text.get(1.0, "end-1c"))

# Create a frame to hold the widgets and center it within the window
frame = Frame(win)
frame.pack(expand=True, pady=(30, 0))  # Set pady to (30, 0) for 30 pixels padding at the top

# Add a text widget
text = Text(frame, width=30, height=2)
text.insert(END, "")
text.pack(side=LEFT)  # Set the side option to LEFT to place it on the left side

# Create a button to get the text input
b = ttk.Button(frame, text="Print", command=get_input)
b.pack(side=LEFT)  # Set the side option to LEFT to place it on the left side

# Create a Label widget
label = Label(win, text="", font=('Calibri 15'))
label.pack()

win.mainloop()
