import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.expression = ""

        # Display entry
        self.entry = tk.Entry(root, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button layout
        button_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0, 4)
        ]

        for (text, row, col, *span) in button_texts:
            span = span[0] if span else 1
            button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=span)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid expression")
                self.entry.delete(0, tk.END)
                self.expression = ""
        elif char == "C":
            self.entry.delete(0, tk.END)
            self.expression = ""
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
