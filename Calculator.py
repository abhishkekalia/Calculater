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

# s_vars = []
# for i in range(5):
#     print i
for row in range(6):
    for col in range(7):
        if(row==0 and col %3!=0 ) or (row==1 and col%3==0) or(row-col==2 ) or(row+col==8):
            print "*",
        else:
            print " "
            print

root.mainloop()

# root.title("Sandwich")
# tk.Button(root, text="hello abhsihek kalia").pack()
# tk.mainloop()
