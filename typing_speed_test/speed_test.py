import tkinter as tk
from tkinter import messagebox
import time

# Sample text for the typing test
SAMPLE_TEXT = """The quick brown fox jumps over the lazy dog. 
This sentence contains every letter of the English alphabet."""

# Function to calculate typing speed
def calculate_speed():
    global start_time
    
    if start_time is None:
        messagebox.showwarning("Error", "Please start typing first!")
        return
    
    typed_text = typing_area.get("1.0", tk.END).strip()  # Get text from typing area
    end_time = time.time()
    
    # Calculate the time taken in seconds and convert to minutes
    time_taken = (end_time - start_time) / 60
    word_count = len(typed_text.split())
    
    if time_taken > 0:
        wpm = word_count / time_taken
        result_label.config(text=f"Your typing speed: {int(wpm)} WPM")
    else:
        result_label.config(text="Invalid time taken")

# Start the timer when typing starts
def start_typing(event):
    global start_time
    if start_time is None:
        start_time = time.time()

# Reset the typing area and timer
def reset_test():
    global start_time
    typing_area.delete("1.0", tk.END)
    result_label.config(text="")
    start_time = None

# Initialize the Tkinter window
root = tk.Tk()
root.title("Typing Speed Test")

start_time = None

# Display the sample text
sample_label = tk.Label(root, text="Type the following text as fast as you can:")
sample_label.pack(pady=10)

sample_text_label = tk.Label(root, text=SAMPLE_TEXT, wraplength=400, justify="left")
sample_text_label.pack(pady=10)

# Text area for the user to type
typing_area = tk.Text(root, height=8, width=50)
typing_area.pack(pady=10)
typing_area.bind("<KeyPress>", start_typing)  # Start the timer on first key press

# Button to submit and calculate typing speed
submit_button = tk.Button(root, text="Submit", command=calculate_speed)
submit_button.pack(pady=10)

# Button to reset the test
reset_button = tk.Button(root, text="Reset", command=reset_test)
reset_button.pack(pady=5)

# Label to display the typing speed result
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()