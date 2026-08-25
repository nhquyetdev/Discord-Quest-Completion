import tkinter as tk
import sys
from pathlib import Path

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown")
        self.root.geometry("350x180")
        self.root.resizable(False, False)

        self.remaining = 15 * 60

        self.label = tk.Label(
            root,
            text="15:00",
            font=("Arial", 48, "bold")
        )
        self.label.pack(pady=40)

        self.countdown()

    def countdown(self):
        minutes, seconds = divmod(self.remaining, 60)
        self.label.config(text=f"{minutes:02d}:{seconds:02d}")

        if self.remaining > 0:
            self.remaining -= 1
            self.root.after(1000, self.countdown)
        else:
            self.root.destroy()

def resource_path(filename):
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS) / filename
    return Path(__file__).parent / filename


root = tk.Tk()
root.iconbitmap(resource_path("icon.ico"))
app = CountdownApp(root)
root.mainloop()