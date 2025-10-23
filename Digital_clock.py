import tkinter as tk
from tkinter import font as tkFont
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x250")
root.configure(bg="black")

# Try to use a custom font; fallback to Arial if unavailable
try:
    custom_font = tkFont.Font(family="Digital-7", size=60)
except:
    custom_font = tkFont.Font(family="Arial", size=60)

# Safe hex color palette for animated pulse
colors = ["#00FFFF", "#FF00FF", "#00FF00", "#FFA500", "#FFFFFF"]

# Time label
time_label = tk.Label(root, font=custom_font, bg="black", fg="#00FFFF")
time_label.pack(pady=20)

# Date label
date_label = tk.Label(root, font=("Arial", 20), bg="black", fg="white")
date_label.pack()

# Function to update time and animate color
def update_time():
    current_time = strftime('%H:%M:%S %p')
    color_index = int(strftime('%S')) % len(colors)
    time_label.config(text=current_time, fg=colors[color_index])
    time_label.after(1000, update_time)

# Function to update date
def update_date():
    current_date = strftime('%A, %d %B %Y')
    date_label.config(text=current_date)
    date_label.after(60000, update_date)

# Initialize clock
update_time()
update_date()

# Bring window to front briefly
root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

# Run the app
root.mainloop()
