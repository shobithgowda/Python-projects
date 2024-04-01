import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_var = tk.StringVar(value="12")
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.punctuation_var = tk.BooleanVar(value=True)
        self.password_var = tk.StringVar(value="")

        # Create widgets
        length_label = ttk.Label(root, text="Password Length:")
        self.length_entry = ttk.Entry(root, textvariable=self.length_var, width=5)
        self.upper_check = ttk.Checkbutton(root, text="Uppercase", variable=self.upper_var)
        self.lower_check = ttk.Checkbutton(root, text="Lowercase", variable=self.lower_var)
        self.digits_check = ttk.Checkbutton(root, text="Digits", variable=self.digits_var)
        self.punctuation_check = ttk.Checkbutton(root, text="Punctuation", variable=self.punctuation_var)
        generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        password_label = ttk.Label(root, text="Generated Password:")
        self.password_entry = ttk.Entry(root, textvariable=self.password_var, state='readonly')

        # Layout widgets
        length_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)
        self.upper_check.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.lower_check.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.digits_check.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.punctuation_check.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        generate_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        password_label.grid(row=6, column=0, padx=5, pady=5, sticky='w')
        self.password_entry.grid(row=6, column=1, padx=5, pady=5)

    def generate_password(self):
        length = int(self.length_var.get())
        uppercase = self.upper_var.get()
        lowercase = self.lower_var.get()
        digits = self.digits_var.get()
        punctuation = self.punctuation_var.get()

        characters = ''
        if uppercase:
            characters += string.ascii_uppercase
        if lowercase:
            characters += string.ascii_lowercase
        if digits:
            characters += string.digits
        if punctuation:
            characters += string.punctuation
        
        if not characters:
            self.password_var.set("Select at least one character set")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
