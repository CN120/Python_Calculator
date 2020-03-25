#!/usr/bin/env python

import tkinter as tk
from tkinter import ttk
#setting up window
root = tk.Tk()
main = ttk.Frame(root)
main.pack(fill='both', expand=1)


#GLOBAL CONSTANTS
NUM_ROWS = 6
NUM_COLUMNS = 4

#Global Variables
Display_Num = tk.StringVar()
Display_Num.set('0')
stored_num = 0
Equation = [0,'+',0]









#window configuration
ttk.Style().configure("Num.TButton", font = ('Calibri',14, 'normal'))  
ttk.Style().configure("Bold.TLabel",font = ('Calibri',15, 'bold'))  #Highligting Active Record Number
for i in range(3):
    main.grid_columnconfigure(i,weight=3)
main.grid_columnconfigure(3,weight=1)
for j in range(NUM_ROWS):
    main.grid_rowconfigure(j,weight=1)



def clear():
    global stored_num
    Display_Num.set('0')
    stored_num = 0
    clear_but_text.set('AC')
    root.update()

def negate():
    global stored_num
    if stored_num==0:
        return
    elif stored_num>0:
        Display_Num.set('-'+Display_Num.get())
        stored_num=-stored_num
    else:
        Display_Num.set(Display_Num.get()[1:])
        stored_num=-stored_num
    root.update()
        

def point():
    global stored_num
    if Display_Num.get().find('.')==-1:
        Display_Num.set(Display_Num.get()+'.')
        stored_num = float(stored_num)

def percent():
    global stored_num
    stored_num*=100
    Display_Num.set(str(stored_num))

def NumberPressed(number):
    global stored_num
    if Display_Num.get() == '0' or Display_Num.get()=="Error":
        Display_Num.set(str(number))
        root.update()
        clear_but_text.set('C')
        stored_num = int(number)
    else:
        Display_Num.set(Display_Num.get()+str(number))
        root.update()
        new_num = Display_Num.get()
        if new_num.find('.')==-1:
            stored_num=int(new_num)
        else:
            stored_num=float(new_num)



def operation(opChar):
    global Equation, stored_num
    Display_Num.set('0')
    root.update()
    Equation[0] = stored_num
    Equation[1] = opChar
    stored_num = 0

def add():
    operation('+')

def subtract():
    operation('-')

def multiply():
    operation('*')

def divide():
    operation('/')

 
def equals():
    global Equation, stored_num
    Equation[2] = stored_num
    EqString = f'{Equation[0]}{Equation[1]}{Equation[2]}'
    try:
        result = eval(EqString)
        Equation[0] = result
        stored_num = result
        Display_Num.set(str(result))
    except:
        Display_Num.set("Error")
        root.update()
        Equation = [0,'+',0]
        stored_num = 0

    


#Widget creation
ttk.Label(main,textvariable=Display_Num,style="Bold.TLabel").grid(row=0,column=0,columnspan=4,padx=10, sticky='E')

# B_Text = (None,('AC', '+/-','%','÷'), ('7','8','9','x'),('4','5','6','−'),('1','2','3','+'),('0','0','.','='))


lcn = 0 #lcn = left column number
clear_but_text = tk.StringVar()
clear_but_text.set('AC')
ttk.Button(main,textvariable=clear_but_text,style="Num.TButton",command=clear).grid(row=1,column=lcn+0,sticky="NSEW")
ttk.Button(main,text='+/-',style="Num.TButton",command=negate).grid(row=1,column=lcn+1,sticky="NSEW")
ttk.Button(main,text='%',style="Num.TButton",command=percent).grid(row=1,column=lcn+2,sticky="NSEW")
ttk.Button(main,text='÷',style="Num.TButton",command=divide).grid(row=1,column=lcn+3,columnspan=2,sticky="NSEW")
#button row 2
ttk.Button(main,text='7',style="Num.TButton",command=lambda:NumberPressed('7')).grid(row=2,column=lcn+0,sticky="NSEW")
ttk.Button(main,text='8',style="Num.TButton",command=lambda:NumberPressed('8')).grid(row=2,column=lcn+1,sticky="NSEW")
ttk.Button(main,text='9',style="Num.TButton",command=lambda:NumberPressed('9')).grid(row=2,column=lcn+2,sticky="NSEW")
ttk.Button(main,text='x',style="Num.TButton",command=multiply).grid(row=2,column=lcn+3,sticky="NSEW")
#button row 3
ttk.Button(main,text='4',style="Num.TButton",command=lambda:NumberPressed('4')).grid(row=3,column=lcn+0,sticky="NSEW")
ttk.Button(main,text='5',style="Num.TButton",command=lambda:NumberPressed('5')).grid(row=3,column=lcn+1,sticky="NSEW")
ttk.Button(main,text='6',style="Num.TButton",command=lambda:NumberPressed('6')).grid(row=3,column=lcn+2,sticky="NSEW")
ttk.Button(main,text='−',style="Num.TButton",command=subtract).grid(row=3,column=lcn+3,sticky="NSEW")
#button row 4
ttk.Button(main,text='1',style="Num.TButton",command=lambda:NumberPressed('1')).grid(row=4,column=lcn+0,sticky="NSEW")
ttk.Button(main,text='2',style="Num.TButton",command=lambda:NumberPressed('2')).grid(row=4,column=lcn+1,sticky="NSEW")
ttk.Button(main,text='3',style="Num.TButton",command=lambda:NumberPressed('3')).grid(row=4,column=lcn+2,sticky="NSEW")
ttk.Button(main,text='+',style="Num.TButton",command=add).grid(row=4,column=lcn+3,sticky="NSEW")
#button row 5
ttk.Button(main,text='0',style="Num.TButton",command=lambda:NumberPressed('0')).grid(row=5,column=lcn+0,sticky="NSEW",columnspan=2)
ttk.Button(main,text='.',style="Num.TButton",command=point).grid(row=5,column=lcn+2,sticky="NSEW")
ttk.Button(main,text='=',style="Num.TButton",command=equals).grid(row=5,column=lcn+3,sticky="NSEW")




root.geometry("240x320+20+20")
root.minsize(240,320)
root.title("My Calculator")
root.mainloop()
