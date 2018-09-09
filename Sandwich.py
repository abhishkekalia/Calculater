import sys
if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk

def startgame():
    pass

root = tk.Tk()

root.option_add("*Button.Background", "black")
root.option_add("*Button.Foreground", "red")

root.title('Amazing Calculator')
root.geometry("500x500")
root.resizable(0, 0)

back = tk.Frame(master=root,bg='white')
back.pack_propagate(0)
back.pack(fill=tk.BOTH, expand=1)

go = tk.Button(master=back, text='Start Game', command=startgame)
go.pack()
close = tk.Button(master=back, text='Quit', command=root.destroy)
close.pack()
info = tk.Label(master=back, text='Made by me!', bg='#009933', fg='black')
info.pack()

root.mainloop()

# root.title("Sandwich")
# tk.Button(root, text="hello abhsihek kalia").pack()
# tk.mainloop()
