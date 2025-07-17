import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox

def run_retrieve_db():
    db = simpledialog.askstring("Database", "Enter database name:")
    if db is None:
        return

    master = simpledialog.askstring("Master Password", "Enter master password:", show='*')
    if master is None:
        return

    stdin_data = f"{db}\n{master}\n"

    try:
        result = subprocess.run(
            ['python', 'retrieve_db.py', '--simple'],
            input=stdin_data.encode(),
            capture_output=True,
            check=True
        )
        output = result.stdout.decode().strip()
        messagebox.showinfo("Output", output)
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode().strip()
        messagebox.showerror("Error", f"Error occurred:\n{error_msg}")

root = tk.Tk()
root.withdraw()
run_retrieve_db()
