import tkinter as tkinter

window = tkinter.Tk()
window.geometry("500x500")

window.title("login page")


lbl1 = tkinter.Label(window, text="username:", font=("new roman", 15))
entry1 = tkinter.Entry(window)


lbl2 = tkinter.Label(window, text="password:", font=("new roman", 15))
entry2 = tkinter.Entry(window)

btn = tkinter.Button(window, text="Button")
lbl1.pack()
entry1.pack()

lbl2.pack()
entry2.pack()

btn.pack()

window.mainloop()
