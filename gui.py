# gui.py
import tkinter as tk
from recognition import start_recognition

def on_start():
    start_recognition()

def on_exit():
    root.destroy()

root = tk.Tk()
root.title("Vision-Based Attendance System")
root.geometry("400x200")
root.resizable(False, False)

title = tk.Label(root, text="Attendance System", font=("Arial", 20))
title.pack(pady=20)

start_btn = tk.Button(root, text="Start Attendance", font=("Arial", 14), bg="green", fg="white", command=on_start)
start_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", font=("Arial", 14), bg="red", fg="white", command=on_exit)
exit_btn.pack(pady=10)

root.mainloop()
