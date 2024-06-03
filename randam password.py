import tkinter as tk
from tkinter import messagebox
import random
import string
import tkinter.simpledialog

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.length_entry = tk.Entry(master)
        self.length_entry.insert(tk.END, "12")  # Default length
        self.length_entry.grid(row=0, column=1, padx=10, pady=5)

        self.lower_var = tk.IntVar()
        self.lower_checkbox = tk.Checkbutton(master, text="Include Lowercase", variable=self.lower_var)
        self.lower_checkbox.select()
        self.lower_checkbox.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        self.upper_var = tk.IntVar()
        self.upper_checkbox = tk.Checkbutton(master, text="Include Uppercase", variable=self.upper_var)
        self.upper_checkbox.select()
        self.upper_checkbox.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        self.digits_var = tk.IntVar()
        self.digits_checkbox = tk.Checkbutton(master, text="Include Digits", variable=self.digits_var)
        self.digits_checkbox.select()
        self.digits_checkbox.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        self.symbols_var = tk.IntVar()
        self.symbols_checkbox = tk.Checkbutton(master, text="Include Symbols", variable=self.symbols_var)
        self.symbols_checkbox.select()
        self.symbols_checkbox.grid(row=4, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        length = int(self.length_entry.get())
        use_lower = self.lower_var.get()
        use_upper = self.upper_var.get()
        use_digits = self.digits_var.get()
        use_symbols = self.symbols_var.get()

        if not (use_lower or use_upper or use_digits or use_symbols):
            messagebox.showwarning("Warning", "Please select at least one option.")
            return

        characters = ''
        if use_lower:
            characters += string.ascii_lowercase
        if use_upper:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.copy_to_clipboard(password)
        messagebox.showinfo("Password Generated", "Password copied to clipboard:\n{}".format(password))

    @staticmethod
    def copy_to_clipboard(text):
        root = tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
