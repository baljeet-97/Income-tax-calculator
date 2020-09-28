from tkinter import *
from tkinter import ttk

exp = " "
def press(num):
    global exp
    exp+=str(num)
    equation.set(exp)
    
def clear ():
    global exp
    exp = " "
    equation.set(" ")

def taxamount(income):
    totalamount=0
    tax=0
    if income <= 500000:
        tax = 0
        
    elif income <= 1000000:
        tax = 12500 + (income) * 0.20
        
    elif income >= 1000001:
        tax = 112500 + (income) * 0.30
    else:
        tax = 12500+100000+(income - 1000000)* 0.3
    
    totalamount=tax
    return totalamount

def butter():
    income=IntVar()
    income=incomefield.get()
    entryField.delete(0,'end')
    amount = taxamount(int(income))
    print(amount)
    entry.set(str(amount))
    


root=Tk() 



root.configure(background="lightgrey")
root.resizable(width=None,height=None)
root.geometry('300x420')
root.title("income Tax Calculator")

entry= StringVar()
equation = StringVar()



labelincome = Label(root,text="Your Income",background="royalblue",foreground="White")
labelincome.place(x=110,y=0)
incomefield = Entry(root,textvariable = equation, width = 40,background="SkyBlue2",foreground="black")
incomefield.place(x=25,y=21)


totaltax = Label(root,text="Total Tax",background="royalblue",foreground="white")
totaltax.place(x=120,y=60)
entryField = Entry(root,textvariable = entry, width = 40,background="Yellowgreen",foreground="black",justify=CENTER)
entryField.place(x=27,y=80)



button = Button(root,text="find income tax", width = 40, command=butter)
button.place(x=5,y=260)




btn9 = ttk.Button(root, text = '9' , width = 15 ,  command = lambda : press(9) )
btn9.place(x=0,y=290 )

btn8 = ttk.Button(root, text = '8' , width = 15 ,  command = lambda : press(8) )
btn8.place(x=100,y=290)

btn7 = ttk.Button(root, text = '7' , width = 15 ,  command = lambda : press(7) )
btn7.place(x=200,y=290)

btn6 = ttk.Button(root, text = '6' , width = 15 ,  command = lambda : press(6) )
btn6.place(x=0,y=315 )

btn5 = ttk.Button(root, text = '5' , width = 15 ,  command = lambda : press(5) )
btn5.place(x=101,y=315)

btn4 = ttk.Button(root, text = '4' , width = 15 ,  command = lambda : press(4) )
btn4.place(x=200,y=315)

btn3 = ttk.Button(root, text = '3' , width = 15,  command = lambda : press(3)  )
btn3.place(x=2,y=340)

btn2 = ttk.Button(root, text = '2' , width = 15,  command = lambda : press(2)  )
btn2.place(x=101,y=340)

btn1 = ttk.Button(root, text = '1' , width = 15 ,  command = lambda : press(1) )
btn1.place(x=200,y=340)

btn0= ttk.Button(root, text = '0' , width = 48,  command = lambda : press(0)  )
btn0.place(x=0,y=368)

btnclr = ttk.Button(root, text = 'Clear' , width = 48,  command = clear )
btnclr.place(x=0,y=392)


root.mainloop()