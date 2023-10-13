import tkinter as tk


class SimpleForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Form")

        self.label = tk.Label(root, text="Name:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        name = self.entry.get()
        if name:
            result_label = tk.Label(self.root, text=f"Hello, {name}!")
            result_label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    form = SimpleForm(root)
    root.mainloop()
