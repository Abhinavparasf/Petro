from tkinter import *

root = Tk()
root.geometry("700x500")
root.maxsize(700, 500)
root.title("Permeability calculator")
root.wm_iconbitmap("icon.ico")

lbl = Label(text="Klinkenberg effect", fg="#2e1e42", bg="#f2edf7", relief="groove", font="Arial 20 bold")
lbl.grid(row=0, ipadx=60, ipady=10)

l1 = Label(text="Kg (air permeability in mD):", font="Arial 14 bold")
l1.grid(row=1, pady=15)

l2 = Label(text="Ki (Initial guess of Kl in mD):", font="Arial 14 bold")
l2.grid(row=2, pady=15)

l3 = Label(text="Pm (Mean pressure in Psi):", font="Arial 14 bold")
l3.grid(row=3, pady=15)

l4 = Label(text="Tolerable Error:", font="Arial 14 bold")
l4.grid(row=4, pady=15)

l5 = Label(text="Final permeability (in mD):", font="Arial 14 bold")
l5.grid(row=6, pady=15)

l6 = Label(text="Iterations performed:", font="Arial 14 bold")
l6.grid(row=7, pady=15)

val1 = DoubleVar()
val2 = DoubleVar()
val3 = DoubleVar()
val4 = DoubleVar()
val5 = StringVar()
val6 = StringVar()

entry1 = Entry(root, textvariable=val1, font="Arial 14 bold")
entry1.grid(row=1, column=2)

entry2 = Entry(root, textvariable=val2, font="Arial 14 bold")
entry2.grid(row=2, column=2)

entry3 = Entry(root, textvariable=val3, font="Arial 14 bold")
entry3.grid(row=3, column=2)

entry4 = Entry(root, textvariable=val4, font="Arial 14 bold")
entry4.grid(row=4, column=2)

entry5 = Entry(root, textvariable=val5, font="Arial 14 bold")
entry5.grid(row=6, column=2)

entry6 = Entry(root, textvariable=val6, font="Arial 14 bold")
entry6.grid(row=7, column=2)


def calculate():
    kg = float(val1.get())
    ki = float(val2.get())
    pm = float(val3.get())
    er = float(val4.get())
    c = 1
    while abs((6.9*(ki**0.64)+(pm*ki)-(pm*kg))/(4.416*(ki**(-0.36))+pm)) >= er:
        ki = ki - ((6.9*(ki**0.64)+(pm*ki)-(pm*kg))/(4.416*(ki**(-0.36))+pm))
        c = c + 1
    val5.set(str(ki.real))
    val6.set(str(c))


b1 = Button(text="Calculate", width=20, relief="raised", font="Arial 14 bold", command=calculate)
b1.grid(row=5, pady=10, padx=100)

root.mainloop()


