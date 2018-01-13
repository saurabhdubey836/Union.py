from tkinter import *
a = Tk()


def mfileopen():
            from tkinter import filedialog
            file1 =filedialog.askopenfile()
            label = Label(text=file1).pack()
            file2 = file1.name #get file name
            f = open(file2)
            label2 = Label(text = f.read(), font=('arial',10,'bold')).pack()
            

button = Button(text = "openfile",width=30,command=mfileopen).pack()

a.mainloop()
