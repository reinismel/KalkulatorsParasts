import tkinter


from tkinter import*
mansLogs=Tk()
mansLogs.title("kalkulators")
#mansLogs.geometry("300x300")


btn0=Button(mansLogs, text="0", padx="40", pady='20')
btn1=Button(mansLogs, text="1", padx="40", pady='20')
btn2=Button(mansLogs, text="2", padx="40", pady='20')
btn3=Button(mansLogs, text="3", padx="40", pady='20')
btn4=Button(mansLogs, text="4", padx="40", pady='20')
btn5=Button(mansLogs, text="5", padx="40", pady='20')
btn6=Button(mansLogs, text="6", padx="40", pady='20')
btn7=Button(mansLogs, text="7", padx="40", pady='20')
btn8=Button(mansLogs, text="8", padx="40", pady='20')
btn9=Button(mansLogs, text="9", padx="40", pady='20')
btnPunkts=Button(mansLogs, text=".", padx="40", pady='20')
btnPlus=Button(mansLogs, text="+", padx="40", pady='20')
btnEql=Button(mansLogs, text="=", padx="40", pady='20')
btnMinus=Button(mansLogs, text="-", padx="40", pady='20')
btnReiz=Button(mansLogs, text="*", padx="40", pady='20')
btnDal=Button(mansLogs, text="/", padx="40", pady='20')

btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
btnDal.grid(row=1,column=3)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btnReiz.grid(row=2,column=3)
btn7.grid(row=3,column=0)
btn8.grid(row=3,column=1)
btn9.grid(row=3,column=2)
btnMinus.grid(row=3,column=3)
btn0.grid(row=4,column=0)
btnPunkts.grid(row=4,column=1)
btnPlus.grid(row=4,column=2)
btnEql.grid(row=4,column=3)

mansLogs.mainloop()