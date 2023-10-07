from tkinter import *
import time
from csv import *
import os

global number
number = 1
class appWindow:
    def __init__(self,root):
        # root = Tk()
        self.root = root
        self.root.geometry("1200x700+0+0")
        self.root.resizable(1,1)
        self.root.title("Restaurant Management System")

        Tops = Frame(self.root,bg="white",width = 1000,height=50,relief=SUNKEN)
        Tops.pack(side=TOP)

        f1 = Frame(self.root,width = 900,height=700,relief=SUNKEN)
        f1.pack(side=LEFT)

        f2 = Frame(self.root ,width = 400,height=700,relief=SUNKEN)
        f2.pack(side=RIGHT)
        #------------------TIME---------------
        localtime=time.asctime(time.localtime(time.time()))
        #-----------------INFO TOP------------
        lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Restaurant Management System",fg="steel blue",bd=10,anchor='w')
        lblinfo.grid(row=0,column=0)
        lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
        lblinfo.grid(row=1,column=0)

        #---------------Calculator------------------
        text_Input=StringVar()
        operator =""

        txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
        txtdisplay.grid(columnspan=4)

        def  btnclick(numbers):
            global operator
            operator=operator + str(numbers)
            text_Input.set(operator)

        def clrdisplay():
            global operator
            operator=""
            text_Input.set("")

        def eqals():
            global operator
            sumup=str(eval(operator))

            text_Input.set(sumup)
            operator = ""
            
        def Ref():
            contFJ =float(FJ.get())
            contGT= float(GT.get())
            contPT= float(PT.get())
            contST= float(ST.get())
            contLassi= float(Lassi.get())
            contDrink= float(Drink.get())

            costofFJ = contFJ*100
            costofGT = contGT*110
            costofPT = contPT*130
            costofST = contST*150
            costofLassi = contLassi*70
            costofdrinks = contDrink*20

            #********* TYPE OF COSTS ***************************************************
            cstmeal = (costofFJ +  costofGT + costofPT + costofST + costofLassi + costofdrinks) 
            costofmeal = "Rs.",str('%.2f'% cstmeal) 

            PayTax=((costofFJ +  costofGT + costofPT + costofST +  costofLassi + costofdrinks)*0.33) # 33% GST
            PaidTax="Rs.",str('%.2f'% PayTax)

            Totalcost=(costofFJ +  costofGT + costofPT + costofST  + costofLassi + costofdrinks) 
            Ser_Charge=((costofFJ +  costofGT + costofPT + costofST + costofLassi + costofdrinks)/99)
            Service="Rs.",str('%.2f'% Ser_Charge)
            ovrcst = PayTax + Totalcost + Ser_Charge
            OverAllCost="Rs.",str('%.2f'% ovrcst)

            Service_Charge.set(Service)
            cost.set(costofmeal)
            Tax.set(PaidTax)
            Subtotal.set(costofmeal)
            Total.set(OverAllCost)

            global Header,dict
            
            Header = [ 'Order No' , 'Fafda-Jalebi (500gm)' , 'Gujarati Thali' , 'Punjabi Thali', 'SouthIndian Tadka' ,'Lassi (400ml)' , 'Drink (200ml)',
                      'Cost Of Meal' , 'Tax(GST)', 'Total cost', 'Service charge' , 'Final Cost'] 
            dict = {'Order No' : number, 
                    'Fafda-Jalebi (500gm)': contFJ,
                    'Gujarati Thali':contGT , 
                    'Punjabi Thali':contPT,                    
                    'SouthIndian Tadka':contST ,
                    'Lassi (400ml)': contLassi, 
                    'Drink (200ml)': contDrink,
                    'Cost Of Meal': cstmeal, 
                    'Tax(GST)': PayTax , 
                    'Total cost':Totalcost, 
                    'Service charge': Ser_Charge , 
                    'Final Cost': ovrcst}

        def qexit():
            self.root.destroy()

        def reset():
            FJ.set("")
            GT.set("")
            PT.set("")
            ST.set("")
            Lassi.set("")
            Drink.set("")
            Subtotal.set("")
            Total.set("")
            Service_Charge.set("")
            Tax.set("")
            cost.set("")

        
        def csv_inc():
            fname = 'Sample.csv'
            IsExist = os.path.exists(fname)
            print(IsExist)

            if IsExist:
                with open('Sample.csv','a',newline = '') as csvfile:
                    my_writer = DictWriter(csvfile,fieldnames=Header)
                    my_writer.writerow(dict)
                    global number
                    number += 1
                    lblreference.config(text=number)
                    reset()
            else:
                with open('Sample.csv','a',newline = '') as csvfile:
                    my_writer = writer(csvfile)
                    my_writer.writerow(Header)
                    writer1 = DictWriter(csvfile,fieldnames=Header)
                    writer1.writerow(dict)
                    number += 1
                    lblreference.config(text=number)
                    reset()

            

        #***********************Buttons Of calculator*****************************************************************************************
        btn7=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="7",bg="powder blue", command=lambda: btnclick(7) )
        btn7.grid(row=2,column=0)

        btn8=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="8",bg="powder blue", command=lambda: btnclick(8) )
        btn8.grid(row=2,column=1)

        btn9=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="9",bg="powder blue", command=lambda: btnclick(9) )
        btn9.grid(row=2,column=2)

        Addition=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="+",bg="powder blue", command=lambda: btnclick("+") )
        Addition.grid(row=2,column=3)
        #---------------------------------------------------------------------------------------------
        btn4=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="4",bg="powder blue", command=lambda: btnclick(4) )
        btn4.grid(row=3,column=0)

        btn5=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="5",bg="powder blue", command=lambda: btnclick(5) )
        btn5.grid(row=3,column=1)

        btn6=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="6",bg="powder blue", command=lambda: btnclick(6) )
        btn6.grid(row=3,column=2)

        Substraction=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="-",bg="powder blue", command=lambda: btnclick("-") )
        Substraction.grid(row=3,column=3)
        #-----------------------------------------------------------------------------------------------
        btn1=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="1",bg="powder blue", command=lambda: btnclick(1) )
        btn1.grid(row=4,column=0)

        btn2=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="2",bg="powder blue", command=lambda: btnclick(2) )
        btn2.grid(row=4,column=1)

        btn3=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="3",bg="powder blue", command=lambda: btnclick(3) )
        btn3.grid(row=4,column=2)

        multiply=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="*",bg="powder blue", command=lambda: btnclick("*") )
        multiply.grid(row=4,column=3)
        #------------------------------------------------------------------------------------------------
        btn0=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="0",bg="powder blue", command=lambda: btnclick(0) )
        btn0.grid(row=5,column=0)

        btnc=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="c",bg="powder blue", command=clrdisplay)
        btnc.grid(row=5,column=1)

        btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="black", font=('ariel', 20 ,'bold'),text="=",bg="powder blue",command=eqals)
        btnequal.grid(columnspan=4)

        Decimal=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text=".",bg="powder blue", command=lambda: btnclick(".") )
        Decimal.grid(row=5,column=2)

        Division=Button(f2,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="/",bg="powder blue", command=lambda: btnclick("/") )
        Division.grid(row=5,column=3)
        

        #---------------------------------------------------------------------------------------
        FJ = StringVar()
        GT = StringVar()
        PT = StringVar()
        ST = StringVar()
        Lassi = StringVar()
        Drink = StringVar()
        Subtotal = StringVar()
        Total = StringVar()
        Service_Charge = StringVar()
        Tax = StringVar()
        cost = StringVar()


        lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10,anchor='w')
        lblreference.grid(row=0,column=0)
        lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text=str(number),fg="steel blue",bd=10,anchor='w')
        lblreference.grid(row=0,column=1)


        lblFJ = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fafda-Jalebi (500gm)",fg="steel blue",bd=10,anchor='w')
        lblFJ.grid(row=1,column=0)
        qFJ = Entry(f1,font=('ariel' ,16,'bold'), textvariable=FJ , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
        qFJ.grid(row=1,column=1)

        lblGT = Label(f1, font=( 'aria' ,16, 'bold' ),text="Gujarati Thali",fg="steel blue",bd=10,anchor='w')
        lblGT.grid(row=2,column=0)
        qGT = Entry(f1,font=('ariel' ,16,'bold'), textvariable=GT , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
        qGT.grid(row=2,column=1)


        lblPT = Label(f1, font=( 'aria' ,16, 'bold' ),text="Punjabi Thali",fg="steel blue",bd=10,anchor='w')
        lblPT.grid(row=3,column=0)
        qPT = Entry(f1,font=('ariel' ,16,'bold'), textvariable=PT , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
        qPT.grid(row=3,column=1)

        lblST = Label(f1, font=( 'aria' ,16, 'bold' ),text="SouthIndian Tadka",fg="steel blue",bd=10,anchor='w')
        lblST.grid(row=4,column=0)
        qST = Entry(f1,font=('ariel' ,16,'bold'), textvariable=ST , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
        qST.grid(row=4,column=1)

        lblLassi = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lassi (400ml)",fg="steel blue",bd=10,anchor='w')
        lblLassi.grid(row=5,column=0)
        qLassi = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Lassi , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
        qLassi.grid(row=5,column=1)

        #--------------------------------------------------------------------------------------
        lblDrink = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drink (200ml)",fg="steel blue",bd=10,anchor='w')
        lblDrink.grid(row=0,column=2)
        qDrink = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drink , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
        qDrink.grid(row=0,column=3)

        lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="steel blue",bd=10,anchor='w')
        lblcost.grid(row=1,column=2)
        txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
        txtcost.grid(row=1,column=3)

        lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="steel blue",bd=10,anchor='w')
        lblService_Charge.grid(row=2,column=2)
        txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
        txtService_Charge.grid(row=2,column=3)

        lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10,anchor='w')
        lblTax.grid(row=3,column=2)
        txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
        txtTax.grid(row=3,column=3)

        lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="steel blue",bd=10,anchor='w')
        lblSubtotal.grid(row=4,column=2)
        txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
        txtSubtotal.grid(row=4,column=3)

        lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
        lblTotal.grid(row=5,column=2)
        txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='right')
        txtTotal.grid(row=5,column=3)

        btnprint=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Print", bg="powder blue",command=csv_inc)
        btnprint.grid(row=8, column=0)

        #-----------------------------------------Buttons------------------------------------------
        lblTotal = Label(f1,text="---------------------",fg="white")
        lblTotal.grid(row=6,columnspan=3)

        btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
        btnTotal.grid(row=7, column=1)

        btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
        btnreset.grid(row=7, column=2)

        btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
        btnexit.grid(row=7, column=3)

        def price():
            roo = Tk()
            roo.geometry("600x220+0+0")
            roo.title("Price List")
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
            lblinfo.grid(row=0, column=0)
            lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
            lblinfo.grid(row=0, column=2)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
            lblinfo.grid(row=0, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fafda-Jalebi (500gm)", fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="100", fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Gujarati Thali", fg="steel blue", anchor=W)
            lblinfo.grid(row=2, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="110", fg="steel blue", anchor=W)
            lblinfo.grid(row=2, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Punjabi Thali", fg="steel blue", anchor=W)
            lblinfo.grid(row=3, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="130", fg="steel blue", anchor=W)
            lblinfo.grid(row=3, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SouthIndian Tadka", fg="steel blue", anchor=W)
            lblinfo.grid(row=4, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="150", fg="steel blue", anchor=W)
            lblinfo.grid(row=4, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lassi (400ml)", fg="steel blue", anchor=W)
            lblinfo.grid(row=5, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="70", fg="steel blue", anchor=W)
            lblinfo.grid(row=5, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drink (200ml)", fg="steel blue", anchor=W)
            lblinfo.grid(row=6, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20", fg="steel blue", anchor=W)
            lblinfo.grid(row=6, column=3)


        btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Menu", bg="powder blue",command=price)
        btnprice.grid(row=7, column=0)

def main():
    # ==== create tkinter window
    root = Tk()

    # === creating object for class InvoiceGenerator
    obj = appWindow(root)
    
    # ==== start the gui
    root.mainloop()

if __name__ == "__main__":
    main()
