# Import the required library
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the geometry
win.geometry("700x350")

# Sample list of objects (you can replace this with your actual objects)
objects = [
    {"name": "Object 1", "description": "This is object 1."},
    {"name": "Object 2", "description": "This is object 2."},
    {"name": "Object 3", "description": "This is object 3."},
    # Add more objects as needed
]

def display_objects():
    for obj in objects:
        # Insert each object into the table (Treeview)
        tree.insert('', 'end', values=(obj['name'], obj['description']))

# Create a Treeview widget for the table
tree = ttk.Treeview(win, columns=("Name", "Description"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Description", text="Description")
tree.pack()

# Add a text widget
text = Text(win, width=30, height=2)
text.insert(END, "")
text.pack(side=TOP, pady=(30, 0))

# Create a button to display the objects in the table
b = ttk.Button(win, text="Print", command=display_objects)
b.pack(side=TOP)

win.mainloop()
