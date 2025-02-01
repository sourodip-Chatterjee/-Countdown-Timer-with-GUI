import time
import tkinter as tk
from tkinter import simpledialog

def start_countdown(seconds):
    """Updates the countdown label every second."""
    def update_timer():
        nonlocal seconds
        if seconds >= 0:
            mins, secs = divmod(seconds, 60)
            countdown_label.config(text=f"{mins:02}:{secs:02}")
            root.update()
            seconds -= 1
            root.after(1000, update_timer)  # Calls update_timer every second
        else:
            countdown_label.config(text="Time's up! 🚀")

    update_timer()

# Ask user for countdown time
root = tk.Tk()
root.withdraw()  # Hide the main window

try:
    countdown_time = simpledialog.askinteger("Countdown Timer", "Enter countdown time in seconds:")
    if countdown_time is None:
        exit()

    # Create a new window for countdown
    root = tk.Tk()
    root.title("Countdown Timer")
    root.geometry("300x200")
    
    countdown_label = tk.Label(root, text="", font=("Arial", 30))
    countdown_label.pack(expand=True)

    start_countdown(countdown_time)
    root.mainloop()

except ValueError:
    print("Please enter a valid number!")
