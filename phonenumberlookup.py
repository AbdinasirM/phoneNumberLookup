import os
import requests
import tkinter as tk
from tkinter import ttk, messagebox
from dotenv import load_dotenv  # Import load_dotenv from python-dotenv

# Load environment variables from .env file
load_dotenv()

# Function to validate the phone number
def validate_phone_number():
    # Read API key from environment variable
    access_key = os.getenv("ACCESS_KEY")
    if access_key is None:
        messagebox.showerror(
            "Error", "API access key not found. Please check your .env file.")
        return

    number = number_entry.get()
    country_code = country_code_entry.get().upper()
    format = country_format_code_entry.get()

    # Make the API request
    response = requests.get("http://apilayer.net/api/validate", params={
        "access_key": access_key,
        "number": number,
        "country_code": country_code,
        "format": format
    })

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Format and display the result as a paragraph
        result_message = "Phone Number Validation Result:\n\n"
        for key, value in data.items():
            result_message += f"{key.capitalize()}: {value}\n"
        messagebox.showinfo("Validation Success", result_message)
    else:
        # Display a user-friendly error message
        messagebox.showerror(
            "Validation Error", "Phone number validation failed. Please check your input and try again.")

# Function to clear input fields


def clear_input_fields():
    number_entry.delete(0, tk.END)
    country_code_entry.delete(0, tk.END)
    country_format_code_entry.delete(0, tk.END)


# Create a Tkinter window
window = tk.Tk()
window.title("Phone Number Validator")

# Create a style for ttk widgets
style = ttk.Style()
style.configure("TButton", padding=10, font=("Helvetica", 14))
style.configure("TEntry", padding=10, font=("Helvetica", 14))

# Create input fields with placeholders using ttk
number_label = ttk.Label(
    window, text="Enter a phone number (e.g., +1234567890):")
number_label.pack(pady=10)  # Add margin at the top
number_entry = ttk.Entry(window)
number_entry.pack(pady=5)  # Add margin at the bottom
number_entry.config(width=30)  # Increase input field width

country_code_label = ttk.Label(window, text="Enter country code (e.g., US):")
country_code_label.pack(pady=10)  # Add margin at the top
country_code_entry = ttk.Entry(window)
country_code_entry.pack(pady=5)  # Add margin at the bottom
country_code_entry.config(width=30)  # Increase input field width

country_format_code_label = ttk.Label(
    window, text="Enter country format code (e.g., +1):")
country_format_code_label.pack(pady=10)  # Add margin at the top
country_format_code_entry = ttk.Entry(window)
country_format_code_entry.pack(pady=5)  # Add margin at the bottom
country_format_code_entry.config(width=30)  # Increase input field width

# Create a "Validate" button using ttk
validate_button = ttk.Button(
    window, text="Validate", command=validate_phone_number)
validate_button.pack(pady=10)  # Add margin at the top
validate_button.config(width=20)  # Increase button width

# Create a "Refresh" button using ttk
refresh_button = ttk.Button(window, text="Refresh", command=clear_input_fields)
refresh_button.pack(pady=10)  # Add margin at the top
refresh_button.config(width=20)  # Increase button width

# Run the Tkinter main loop
window.mainloop()
