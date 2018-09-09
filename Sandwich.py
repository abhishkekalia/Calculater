import sys
if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk

class Sandwhich(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Submit", command=self.on_button)
        self.button.pack()
        self.entry.pack()

    def on_button(self):
        print(self.entry.get())

app = Sandwhich()
app.mainloop()

# root.title("Sandwich")
# tk.Button(root, text="hello abhsihek kalia").pack()
# tk.mainloop()
