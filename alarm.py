import sys
import tkinter as tk
from pathlib import Path

running = True
img = None


def resource_path(relative_path):
    """Get the absolute path to a resource, works for PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = Path(__file__).parent
    return Path(base_path) / relative_path


def show_reminder(root):
    """
    Create and show the reminder window.
    """
    global img
    reminder_window = tk.Toplevel(root)
    reminder_window.title("It's time to reat your eyes ~ ~ ~")
    reminder_window.geometry("1600x1600")

    image_path = resource_path("Eta6.png")
    img = tk.PhotoImage(file=image_path)

    label = tk.Label(reminder_window, image=img)
    label.pack(padx=10, pady=10)

    text_label = tk.Label(
        reminder_window, text="Let's relax! Rest your eyes for 1 minute ~", font=("Arial", 16)
    )
    text_label.pack(padx=10, pady=10)

    # Bind click to close the reminder window
    reminder_window.bind("<Button-1>", lambda e: reminder_window.destroy())


def schedule_reminder(root, interval):
    """
    Schedule the reminder to show periodically.
    """
    if running:
        show_reminder(root)
        root.after(int(interval * 1000), schedule_reminder, root, interval)


def stop_program(event=None):
    """
    Stop the program when Ctrl+Q is pressed.
    """
    global running
    running = False
    print("Program has been stopped.")
    sys.exit(0)


if __name__ == "__main__":
    interval_minutes = 1
    interval_seconds = interval_minutes * 60

    root = tk.Tk()
    root.withdraw()

    root.bind("<Control-q>", stop_program)

    root.after(int(interval_seconds * 1000), schedule_reminder, root, interval_seconds)

    print("Reminder program is running. Press Ctrl+Q to stop.")
    root.mainloop()
