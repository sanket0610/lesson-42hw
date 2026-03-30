from tkinter import *
window=Tk()
window.title("INTEREST CALCULATOR")
window.configure(bg="black")
window.geometry("600x230")

n1=Label(text="ENTER PRINCIPAL", fg="white", bg="blue", height=2, width=100)
pr=Entry(width=60)
n2=Label(text="ENTER RATE OF INTEREST", fg="white", bg="blue", height=2, width=100)
rt=Entry(width=60)
n3=Label(text="ENTER TIME", fg="white", bg="blue", height=2, width=100)
tm=Entry(width=60)

def SI():
    p=int(pr.get())
    r=int(rt.get())
    t=int(tm.get())
    si=p*r*t/100
    tx.insert(1.0,"INTEREST=")
    tx.insert(1.17,si)

tx=Text(height=2, width=100)

b=Button(text="CALCULATE", command=SI, bg="red", fg="white")


n1.pack()
pr.pack()
n2.pack()
rt.pack()
n3.pack()
tm.pack()
b.pack()
tx.pack()
window.mainloop()



