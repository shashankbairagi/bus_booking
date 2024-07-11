from tkinter import *
import sqlite3
from tkinter.messagebox import *
import random
from datetime import date
from datetime import datetime
import re

class main_fn:
    def front(self):

        root=Tk()

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()

        root.state('zoomed')

        img=PhotoImage(file='Bus.png')

        Label(root,image=img).pack()

        Label(root,text='Online Bus Booking System',fg='Red',bg='bisque',font="Arial 24 bold").pack()

        Label(root,text='Name : SHASHANK BAIRAGI',fg='blue2',font="Arial 11 bold",pady=25).pack()

        Label(root,text='Er : 221B343',fg='blue2',font="Arial 11 bold",pady=25).pack()

        Label(root,text='Mobile :  70244200XX',fg='blue2',font="Arial 11 bold",pady=25).pack()

        Label(root,text='Submitted to : Dr. Mahesh Kumar ',fg='Red',bg='bisque',font="Arial 15 bold").pack()

        Label(root,text='Project Based Learning',fg='Red',font="Arial 13 bold").pack()

        def nex(e=0):
            root.destroy()
            self.menu()
        root.bind("<KeyPress>",nex)
        root.mainloop()

    def menu(self):

        root=Tk()

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()

        root.geometry('%dx%d+0+0'%(w,h))

        img=PhotoImage(file='Bus.png')

        Label(root,image=img).grid(row=0,column=0,padx=w/2.5,columnspan=7)

        Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7,pady=40)

        def booking():
            root.destroy()
            self.booking()
        def check():
            root.destroy()
            ###
            self.ticket()
            ###
            
        def add():
            root.destroy()
            self.loginn()

        Button(root,text='Seat Booking',bg='LightGreen',font="Arial 14 bold",command=booking).grid(row=5,column=1,padx=80,columnspan=2)

        Button(root,text='Check Booked seat',bg='green2',font="Arial 14 bold",command=check).grid(row=5,column=2,padx=60,columnspan=3)

        Button(root,text='Update Database',bg='green4',font="Arial 14 bold",command=add).grid(row=5,column=3,columnspan=4)

        Label(root,text="").grid(row=6,column=2)

        admin=Label(root,text="For Admin Only",fg="red",font="Arial 12 bold").grid(row=7,column=3,columnspan=4)

        root.mainloop()
            

    def booking(self):

        root=Tk()

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()

        root.geometry('%dx%d+0+0'%(w,h))

        img=PhotoImage(file='Bus.png')

        Label(root,image=img).grid(row=0,column=0,padx=w/2.45,columnspan=7)

        Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7,pady=10)

        Label(root,text="Enter Journey Details",bg="light green",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=3,column=0,columnspan=7)

        Label(root,text="").grid(row=4,column=0)

        Frame2=Frame(root)

        Frame3=Frame(root)

        check = 0
            
        def clicked(value):
            global check
            check = value
        def datecheck(test):
            format = "%d/%m/%Y"
            res = True
            try:
                    res = bool(datetime.strptime(test, format))
            except ValueError:
                    res = False
            return res

        def show():

            con = sqlite3.connect('mydatabase.db')

            global check

            check = 0

            cur = con.cursor()

            r=IntVar()
            Frame3.grid_forget()
            Frame2.grid(row=6,column=0,columnspan=10,pady=20)
            
            if(to.get()==""):
                showerror('Field Missing','Please enter your Destination')
                Frame2.grid_forget()
                Frame3.grid_forget()
            elif(frm.get()==""):
                showerror('Field Missing','Please enter your Boarding Location')
                Frame2.grid_forget()
                Frame3.grid_forget()
            elif(jdate.get()==""):
                showerror('Field Missing','Please enter your Journey Date')
                Frame2.grid_forget()
                Frame3.grid_forget()
            else:

                try:
                    int(to.get())
                    showerror('Invalid Input','Destination cannot be a number')
                    to.delete(0,END)
                    return
                    int(frm.get())
                    showerror('Invalid Input','Boarding Location cannot be a number')
                    frm.delete(0,END)
                    return
                except:
                    m=0
                res=datecheck(jdate.get())
                if(res==True):
                    datelist=jdate.get().split("/")
                    d = str(date.today())
                    dlist=d.split("-")
                    print(datelist)
                    print(dlist)
                    if(len(datelist[0])==2):
                        if(len(datelist[1])==2):
                            m=0
                        else:
                            showerror('Invalid month Format','Please enter month in correct format')
                            Frame2.grid_forget()
                            return
                    else:
                        showerror('Invalid date Format','Please enter date in correct format')
                        Frame2.grid_forget()
                        return
                            
                    if(int(datelist[2])>int(dlist[0])):
                        m=0
                    elif(int(datelist[2])==int(dlist[0])):
                        if(int(datelist[1])>int(dlist[1])):
                            m=0
                        elif(int(datelist[1])==int(dlist[1])):
                            if(int(datelist[0])<int(dlist[2])):
                                showerror('Invalid Date','Please enter a valid date')
                                Frame2.grid_forget()
                                return
                        else:
                            showerror('Invalid month','Please enter a valid month')
                            Frame2.grid_forget()
                            return
                    else:
                        showerror('Invalid Year','Please enter a valid Year')
                        Frame2.grid_forget()
                        return
                else:
                    showerror('Wrong Date','Date or Date format incorrect\nTry again')
                    Frame2.grid_forget()
                    return

                tsname = to.get().lower()
                
                cur.execute("SELECT * FROM route where Sname=:to",
                            {
                                'to': tsname
                            }
                            )

                to_records = cur.fetchall()
                print(to_records)

                fname = frm.get().lower()
                
                if(to_records == []):
                    showinfo('No Bus Found','Sorry, No buses are available for this route')
                    to.delete(0,END)
                    frm.delete(0,END)
                    jdate.delete(0,END)
                    Frame2.grid_forget()
                    Frame3.grid_forget()
                    return
                cur.execute("SELECT * FROM route where Sname=:frm",
                            {
                                'frm': fname
                            }
                            )
                
                frm_records = cur.fetchall()
                if(frm_records == []):
                    showinfo('No Bus Found','Sorry, No buses are available for this route')
                    to.delete(0,END)
                    frm.delete(0,END)
                    jdate.delete(0,END)
                    Frame2.grid_forget()
                    Frame3.grid_forget()
                    return
                i=0
                j=0
                tempid=0
                for record in to_records:
                    for rec in frm_records:    
                        if(to_records[i][0]==frm_records[j][0]):
                            if(to_records[i][1]>frm_records[j][1]):
                                tempid = to_records[i][0]
                        j=j+1
                    i=i+1
                    j=0
                if(tempid==0):
                    showinfo('No Bus Found','Sorry, No buses are available')
                    oid.delete(0,END)
                    name.delete(0,END)
                    address.delete(0,END)
                    Frame2.grid_forget()
                    Frame3.grid_forget()
                    return
                cur.execute("SELECT * FROM running where BusID IN(select BusID from BUS where RID=:tempid) and date=:jdate and Available_seats>0",
                            {
                                'tempid': tempid,
                                'jdate': jdate.get()
                            }
                            )
                run_info = cur.fetchall()

                if(run_info==[]):
                    showinfo('No Bus Found','Sorry, No buses are available')
                    to.delete(0,END)
                    frm.delete(0,END)
                    jdate.delete(0,END)
                    Frame2.grid_forget()
                    Frame3.grid_forget()
                    return
                for widget in Frame2.winfo_children():
                    widget.destroy()

                Label(Frame2,text='Select Bus',fg='green3',font='Arial 15 bold').grid(row=0,column=0,padx=20)
                
                Label(Frame2,text='Operator',fg='green3',font='Helvetica 15 bold').grid(row=0,column=2,padx=20)
                
                Label(Frame2,text='Bus Type',fg='green3',font='Helvetica 15 bold').grid(row=0,column=4,padx=20)
                
                Label(Frame2,text='Available/Capacity',fg='green3',font='Helvetica 15 bold').grid(row=0,column=6,padx=20)
                
                Label(Frame2,text='Fare',fg='green3',font='Helvetica 15 bold').grid(row=0,column=8,padx=20)

                Button(Frame2,text='Proceed to Book',fg='black',bg='LightGreen',font='Arial 14 bold',command=book).grid(row=2,column=10,padx=20)

                cur.execute("SELECT count(*) FROM running where BusID IN(select BusID from BUS where RID=:tempid) and date=:jdate and Available_seats>0",
                            {
                                'tempid': tempid,
                                'jdate': jdate.get()
                            }
                            )
                no_of_labels = cur.fetchall()
                enteries = no_of_labels[0][0]
                counter=0
                while(enteries!=0):
                    cur.execute("SELECT * FROM Bus where BusID=:busid",
                                {
                                    'busid': run_info[counter][0]
                                }
                                )
                    bus_info = cur.fetchall()

                    cur.execute("SELECT Name from operator where OID=:oid",
                                {
                                    'oid': bus_info[0][5]
                                }
                                )
                    op_name = cur.fetchall()
                    
                    Radiobutton(Frame2,text='Bus '+str(counter+1),font='Helvetica 11',variable=r,value=counter+1,command=lambda : clicked(r.get())).grid(row=counter+1,column=0,padx=20,pady=5)
                    
                    Label(Frame2,text=op_name[0][0],fg='blue',font='Helvetica 12 italic').grid(row=counter+1,column=2,padx=20,pady=5)

                    Label(Frame2,text=bus_info[0][1],fg='blue',font='Helvetica 12 bold').grid(row=counter+1,column=4,padx=20,pady=5)

                    Label(Frame2,text=str(run_info[counter][2])+'/'+str(bus_info[0][2]),fg='blue',font='Helvetica 12 bold').grid(row=counter+1,column=6,padx=20,pady=5)

                    Label(Frame2,text=bus_info[0][3],fg='blue',font='Helvetica 12 bold').grid(row=counter+1,column=8,padx=20,pady=5)

                    counter=counter+1

                    enteries=enteries-1

        def book():
            global check
            if(check==0):
                showerror('Field Missing','Please select a bus')
                Frame3.grid_forget()
                return

            def confirm():
                con = sqlite3.connect('mydatabase.db')
                
                cur = con.cursor()
                
                if(cname.get()==""):
                    showerror('Field Missing','Please enter Name')
                elif(gender.get()=="Select"):
                    showerror('Field Missing','Please Select Gender')
                elif(mno.get()==""):
                    showerror('Field Missing','Please enter Mobile Number')
                elif(cage.get()==""):
                    showerror('Field Missing','Please enter Age')
                elif(cseat.get()==""):
                    showerror('Field Missing','Please enter No of seats')
                else:
                    try:
                        global check
                        try:
                            int(cname.get())
                            showerror('Invalid Name','Name cannot be numbers')
                            cname.delete(0,END)
                            return
                        except:
                            m=0
                        try:
                            int(mno.get())
                        except:
                            showerror('Invalid Mobile','Please enter valid mobile number')
                            mno.delete(0,END)
                            return
                        try:
                            int(cage.get())
                        except:
                            showerror('Invalid Age','Please enter valid Age')
                            cage.delete(0,END)
                            return
                        try:
                            int(cseat.get())
                        except:
                            showerror('Invalid Seat','Please enter valid number of seats')
                            cseat.delete(0,END)
                            return

                        if(len(mno.get())!=10):
                            showerror('Wrong Input','Please enter a valid 10 digit Mobile number')
                            mno.delete(0,END)
                            return
                        if(int(cage.get())>130 or int(cage.get())<1):
                            showerror('Wrong Input','Please enter a valid Age')
                            cage.delete(0,END)
                            return

                        tsname=to.get().lower()
                        
                        cur.execute("SELECT * FROM route where Sname=:to",
                                {
                                    'to': tsname
                                }
                                )

                        to_records = cur.fetchall()

                        fname = frm.get().lower()
                        
                        cur.execute("SELECT * FROM route where Sname=:frm",
                                    {
                                        'frm': fname
                                    }
                                    )

                        frm_records = cur.fetchall()
                    
                        i=0
                        j=0
                        tempid=0
                        for record in to_records:
                            for rec in frm_records:    
                                if(to_records[i][0]==frm_records[j][0]):
                                    if(to_records[i][1]>frm_records[j][1]):
                                        tempid = to_records[i][0]
                                j=j+1
                            i=i+1
                            j=0

                        cur.execute("SELECT * FROM running where BusID IN(select BusID from BUS where RID=:tempid) and date=:jdate and Available_seats>0",
                                    {
                                        'tempid': tempid,
                                        'jdate': jdate.get()
                                    }
                                    )
                        run_info = cur.fetchall()

                        if(int(cseat.get())>run_info[check-1][2] or int(cseat.get())<1):
                            showerror('Invalid Input','Please enter a valid no. of seats')
                            cseat.delete(0,END)
                            return

                        cur.execute("SELECT * FROM Bus where BusID=:busid",
                                    {
                                        'busid': run_info[check-1][0]
                                    }
                                    )

                        bus_info = cur.fetchall()
                        
                        cur.execute("SELECT ref,phone FROM Bookinghistory")
                        ref = cur.fetchall()
                        h=0

                        cur.execute("SELECT count(*) FROM bookinghistory")

                        lastid = cur.fetchall()

                        reference = lastid[0][0] + 1
                        
                        for ph in ref:
                            if(ref[h][1]==int(mno.get())):
                                showinfo('Record exist','Booking from this number already exist..')
                                return
                            h=h+1
                            
                        choice=askyesno('Confimation','Your fare is '+str(int(cseat.get())*bus_info[0][3])+'\nConfirm booking?')
                        

                        cur.execute("INSERT INTO Bookinghistory(pname,ref,phone,travel_on,bookedon,gender,age,source,destination,fare,seats) VALUES(:pname, :ref, :phone,:travelon, :bookedon, :gender,:age,:source,:destination,:fare,:seat)",
                                        {
                                            'pname': cname.get(),
                                            'ref': reference,
                                            'phone': mno.get(),
                                            'travelon': jdate.get(),
                                            'bookedon': date.today(),
                                            'gender': gender.get(),
                                            'age' : cage.get(),
                                            'source': fname,
                                            'destination': tsname,
                                            'fare': (int(cseat.get())*bus_info[0][3]),
                                            'seat': cseat.get()
                                        }
                                        )

                        new=run_info[check-1][2]-int(cseat.get())
                    
                        cur.execute("UPDATE running set available_seats=:seat where busid=:busid and date=:jdate",
                                {
                                    'seat': new,
                                    'busid': bus_info[0][0],
                                    'jdate': jdate.get()
                                }
                                )
                        
                        if(choice==1):
                            showinfo('Success','Seat booked!')
                            cname.delete(0,END)
                            cage.delete(0,END)
                            cseat.delete(0,END)
                            mno.delete(0,END)
                            gender.set("Select")
                            Frame3.grid_forget()
                            Frame2.grid_forget()
                            to.delete(0,END)
                            frm.delete(0,END)
                            jdate.delete(0,END)
                            con.commit()
                            root.destroy()
                            self.ticket()
                            

                    except:
                        showerror('Invalid Entry','Booking already exist or you may have entered wrong values\nPlease enter valid values...')
                        cname.delete(0,END)
                        cage.delete(0,END)
                        cseat.delete(0,END)
                        mno.delete(0,END)
                        gender.set("Select")
                        
                    
                con.close()

            def mlimit(value):
                entry=mno.get()
                if(len(entry)>9):
                    mno.delete(9,END)
            def alimit(value):
                entry=cage.get()
                if(len(entry)>2):
                    cage.delete(2,END)
                
            Label(Frame3,text='Fill Passenger Details',fg='Red',bg='LightBlue1',font="Arial 21 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
            Frame3.grid(row=7,column=0,columnspan=10)
            Label(Frame3,text="Name",font='Arial 11 bold').grid(row=1,column=0)
            cname=Entry(Frame3)
            cname.grid(row=1,column=1)

            Label(Frame3,text="Gender",font='Arial 11 bold').grid(row=1,column=2)
            gender=StringVar()
            gender.set("Select")
            option=["Male","Female","Other"]
            menu=OptionMenu(Frame3,gender,*option)
            menu.grid(row=1,column=3)

            Label(Frame3,text="Mobile No",font='Arial 11 bold').grid(row=1,column=4)
            mno=Entry(Frame3)
            mno.grid(row=1,column=5)
            mno.bind('<KeyPress>',mlimit)

            Label(Frame3,text="Age",font='Arial 11 bold').grid(row=1,column=6)
            cage=Entry(Frame3,width=10)
            cage.grid(row=1,column=7)
            cage.bind('<KeyPress>',alimit)
            
            Label(Frame3,text="No Of Seats",font='Arial 11 bold').grid(row=1,column=8)
            cseat=Entry(Frame3,width=10)
            cseat.grid(row=1,column=9)

            Button(Frame3,text='Book Seat',fg="black",bg='white',font='Arial 15',command=confirm).grid(row=1,column=10,padx=10)

            
                    

                    

        Frame1=Frame(root)
        Frame1.grid(row=5,column=0,columnspan=10)
        Label(Frame1,text="To",font='Times_New_Roman 14 bold').grid(row=5,column=1,sticky=E)
        to=Entry(Frame1)
        to.grid(row=5,column=2,sticky=W)


        Label(Frame1,text="From",font='Times_New_Roman 14 bold').grid(row=5,column=3,sticky=E)
        frm=Entry(Frame1)
        frm.grid(row=5,column=4,sticky=W)


        Label(Frame1,text="Journey Date",font='Times_New_Roman 14 bold').grid(row=5,column=5,sticky=E)
        jdate=Entry(Frame1)
        Label(Frame1,text='Format : (DD/MM/YYYY)',font='Helvetica 12 italic bold').grid(row=6,column=6)
        jdate.grid(row=5,column=6,sticky=W)

        def home():
            root.destroy()
            self.menu()
        Button(Frame1,text="Show Bus",bg="SpringGreen3",font="Arial 14 bold",command=show).grid(row=5,column=7)
        image=PhotoImage(file="home.png")
        Button(Frame1,image=image,command=home).grid(row=5,column=8,columnspan=3)
        root.mainloop()

    def ticket(self):

        root=Tk()

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()

        root.geometry('%dx%d+0+0'%(w,h))

        img=PhotoImage(file='Bus.png')

        Frame1=Frame(root)

        Frame1.grid(row=0,column=0,columnspan=10,padx=w/2.5)

        Label(Frame1,image=img).pack()

        Label(Frame1,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold").pack()

        con = sqlite3.connect('mydatabase.db')
            
        cur = con.cursor()
            
        Label(Frame1,text='Bus Ticket',fg='black',font="Arial 15 bold",pady=5).pack()

        Frame2=Frame(root,relief='groove',bd=5)

        Frame2.grid(row=1,column=0,columnspan=10,padx=w/2.5,pady=10)

        con.commit()

        cur.execute("SELECT count(*) FROM bookinghistory")

        lastid = cur.fetchall()
        print(lastid)

        cur.execute("SELECT * FROM bookinghistory where bookingid=:lastid",
                        {
                            'lastid': lastid[0][0]
                        }
                        )
        info = cur.fetchall()
        print(info)
        for widget in Frame2.winfo_children():
            widget.destroy()
        Label(Frame2,text='Passenger Name : '+info[0][1],font='Arial 13 bold').grid(row=0,column=0,sticky='w')

        Label(Frame2,text='Age : '+str(info[0][7]),font='Arial 13 bold').grid(row=1,column=0,sticky='w')

        Label(Frame2,text='Gender : '+info[0][6],font='Arial 13 bold').grid(row=2,column=0,sticky='w')

        Label(Frame2,text='Travel Date : '+info[0][4],font='Arial 13 bold').grid(row=0,column=2,sticky='w')

        Label(Frame2,text='Boarding Point : '+info[0][8],font='Arial 13 bold').grid(row=1,column=2,sticky='w')

        Label(Frame2,text='Booked On : '+info[0][5],font='Arial 13 bold').grid(row=2,column=2,sticky='w')

        Label(Frame2,text='Seats Booked : '+str(info[0][11]),font='Arial 13 bold').grid(row=3,column=2,sticky='w')

        Label(Frame2,text='Booking Ref : '+str(info[0][2]),font='Arial 13 bold').grid(row=3,column=0,sticky='w')

        Label(Frame2,text='Fare : '+str(info[0][10]),font='Arial 13 bold').grid(row=4,column=2,sticky='w')

        Label(Frame2,text='Destination : '+info[0][9],font='Arial 13 bold').grid(row=5,column=0,sticky='w')

        Label(Frame2,text='Phone : '+str(info[0][3]),font='Arial 13 bold').grid(row=4,column=0,sticky='w')

        Label(Frame2,text='* Total fare of '+str(info[0][10])+' /- to be paid at the time of boarding the bus',font='Arial 12 italic').grid(row=6,column=0,columnspan=10)
        def exitt():
            a=showinfo('Message','Thank you for using our platform!')
            root.destroy()
        def home():
            root.destroy()
            self.menu()
        Button(root,text='Exit',font='Times_new_roman 10',command=exitt).grid(row=7,column=1,columnspan=10)
        photu=PhotoImage(file="home.png")
        Button(root,image=photu,font='Times_new_roman 10',command=home).grid(row=7,column=0,columnspan=10)
        root.mainloop()

        def checking(self):
    
            root=Tk()

            w,h=root.winfo_screenwidth(),root.winfo_screenheight()

            root.geometry('%dx%d+0+0'%(w,h))

            img=PhotoImage(file='Bus.png')

            Frame1=Frame(root)

            Frame1.grid(row=0,column=0,columnspan=10,padx=w/2.6)

            Label(Frame1,image=img).grid(row=0,column=0,columnspan=7)

            Label(Frame1,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font="Arial 24 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,columnspan=7,pady=10)

            Label(Frame1,text="Check Your Booking",bg="light green",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=2,column=0,columnspan=7,pady=5)

            Frame3=Frame(root,relief='groove',bd=5)


            def display_ticket_frame():
                con = sqlite3.connect('mydatabase.db')
                
                cur = con.cursor()
                
                int(mobile.get())
                
                Frame3.grid(row=3,column=0,columnspan=10)
                            
                cur.execute("SELECT * FROM bookinghistory where phone=:phone", {'phone': mobile.get()} )
                
                info = cur.fetchall()
                
                for widget in Frame3.winfo_children():
                    widget.destroy()
                Label(Frame3,text='Passenger Name : '+info[0][1],font='Arial 13 bold').grid(row=0,column=0,sticky='w')

                Label(Frame3,text='Age : '+str(info[0][7]),font='Arial 13 bold').grid(row=1,column=0,sticky='w')

                Label(Frame3,text='Gender : '+info[0][6],font='Arial 13 bold').grid(row=2,column=0,sticky='w')

                Label(Frame3,text='Travel Date : '+info[0][4],font='Arial 13 bold').grid(row=0,column=2,sticky='w')

                Label(Frame3,text='Boarding Point : '+info[0][8],font='Arial 13 bold').grid(row=1,column=2,sticky='w')

                Label(Frame3,text='Booked On : '+info[0][5],font='Arial 13 bold').grid(row=2,column=2,sticky='w')

                Label(Frame3,text='Seats Booked : '+str(info[0][11]),font='Arial 13 bold').grid(row=3,column=2,sticky='w')

                Label(Frame3,text='Booking Ref : '+str(info[0][2]),font='Arial 13 bold').grid(row=3,column=0,sticky='w')

                Label(Frame3,text='Fare : '+str(info[0][10]),font='Arial 13 bold').grid(row=4,column=2,sticky='w')

                Label(Frame3,text='Destination : '+info[0][9],font='Arial 13 bold').grid(row=5,column=0,sticky='w')

                Label(Frame3,text='Phone : '+str(info[0][3]),font='Arial 13 bold').grid(row=4,column=0,sticky='w')

                Label(Frame3,text='* Total fare of '+str(info[0][10])+' /- to be paid at the time of boarding the bus',font='Arial 12 italic').grid(row=6,column=0,columnspan=10)

            def destroy_ticket_frame():
                Frame3.grid_forget()
                
            def ticket():

                con = sqlite3.connect('mydatabase.db')
                
                cur = con.cursor()
                response=0
                if(mobile.get()==""):
                    showerror('Field Missing','Please enter your mobile number')
                    destroy_ticket_frame()
                else:
                    try:
                        display_ticket_frame()
                        mobile.delete(0,END)
                    except:
                        try:
                            int(mobile.get())
                            if(len(mobile.get())==10):
                               response = askyesno('No Booking Found','Would you like to book a bus?')
                               #if(response == 1):
                                   #go to booking page
                               
                            else:
                                showerror('Bad Request','Enter a 10 digit valid number\n Please try again...')
                            destroy_ticket_frame()
                            mobile.delete(0,END)
                        except:
                            showerror('Bad Request','Input must be a number\n Please try again...')
                            destroy_ticket_frame()
                            mobile.delete(0,END)
                    con.close()
                    if(response==1):
                        root.destroy()
                        self.booking()
                            
            Frame2=Frame(root)
            Frame2.grid(row=1,column=0,columnspan=10)
            Label(Frame2,text="Enter Your Mobile No:").grid(row=1,column=0,sticky=W,padx=10,pady=20)
            def limit(value):
                entry=mobile.get()
                if(len(entry)>9):
                    mobile.delete(9,END)
            mobile=Entry(Frame2)
            mobile.grid(row=1,column=1,sticky=E,pady=20)
            mobile.bind('<KeyPress>',limit)
            Button(Frame2,text="Check Booking",font='helvetica 12',command=ticket).grid(row=1,column=2,padx=10,pady=20)

            def home():
                root.destroy()
                self.menu()
            photu=PhotoImage(file="home.png")
            Button(Frame2,image=photu,command=home).grid(row=1,column=3,columnspan=10,pady=10)
            root.mainloop()

    def loginn(self):
        root=Tk()

        w,h=root.winfo_screenwidth(),root.winfo_screenheight()

        root.geometry('%dx%d+0+0'%(w,h))

        #img=PhotoImage(file='Bus.png')

        Frame1=Frame(root)

        Frame1.grid(row=0,column=0,columnspan=10,padx=w/2.45)

        #Label(Frame1,image=img).grid(row=0,column=0,columnspan=7)

        Label(Frame1,text='ADMIN LOGIN',fg='Red',bg='LightBlue1',font="Arial 24 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,columnspan=10,pady=10)

        Frame2=Frame(root)
        Frame2.grid(row=1,column=0,columnspan=10)

        Label(Frame2,text="Enter your Credentials",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=10)

        Label(Frame2,text="Username",font='helvetica 11').grid(row=1,column=0)

        Label(Frame2,text="(case sensitive)",font='helvetica 9 italic').grid(row=1,column=2)

        user=Entry(Frame2)

        user.grid(row=1,column=1)

        Label(Frame2,text="Password",font='helvetica 11').grid(row=2,column=0)

        password=Entry(Frame2,show = '*')

        password.grid(row=2,column=1)

        def login():
            userw='sb'
            passw='343'
            error=0
            try:
                int(user.get())
                showerror('Invalid Username','Username cannot be only numbers')
                user.delete(0,END)
                return
            except:
                error=0
            if(user.get()==""):
                showerror('Invalid Action','Username Cannot be empty')
                return
            if(password.get()==""):
                showerror('Invalid Action','Please enter Password')
                return
            else:
                if(user.get()==userw):
                    if(password.get()==passw):
                        root.destroy()
                        self.update()
                    else:
                        showerror('Invalid Credentials','Password incorrect\nPlease try again')
                        return
                else:
                    showerror('Invalid Credentials','Username incorrect\nPlease try again')
                    return
        def home():
            root.destroy()
            self.menu()
        pic=PhotoImage(file="home.png")
        Button(Frame2,image=pic,command=home).grid(row=4,column=1,pady=30)
                   
        Button(Frame2,text='Login',font='helvetica 13 italic',command=login).grid(row=3,column=1)

        root.mainloop()

    def update(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file="Bus.png")
        Frame1=Frame(root)
        Frame1.grid(row=0,column=0,columnspan=10)
        Label(Frame1,image=img).grid(row=0,column=0,padx=w/2.45,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame2=Frame(root)
        Frame2.grid(row=3,column=0,columnspan=10)
        Label(Frame2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame_3=Frame(root)
        Frame_3.grid(row=5,column=0,columnspan=10)
        Label(Frame_3,text="Add New Details to DataBase ",fg="green4",bg='light green',font="Arial 12 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)
        Label(root,text="").grid(row=6,column=0)

        def newop():
            root.destroy()
            self.operator()
        def newbus():
            root.destroy()
            self.bus()
        def newroute():
            root.destroy()
            self.route()
        def newrun():
            root.destroy()
            self.run()
        Button(root,text="New Operator",bg="pale green",command=newop).grid(row=7,column=0,columnspan=7)

        Button(root,text="New Bus",bg="salmon",command=newbus).grid(row=7,column=1,columnspan=7)

        Button(root,text="New Route",bg="SteelBlue3",command=newroute).grid(row=7,column=2,columnspan=7)

        Button(root,text="New Run",bg="MistyRose3",command=newrun).grid(row=7,column=3,columnspan=7)
        
        root.mainloop()

    def operator(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))
        img=PhotoImage(file="Bus.png")
        Frame1=Frame(root)
        Frame1.grid(row=0,column=0,columnspan=10)
        Label(Frame1,image=img).grid(row=0,column=0,padx=w/2.45,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame2=Frame(root)
        Frame2.grid(row=3,column=0,columnspan=10)
        Label(Frame2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=w/2.45,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame3=Frame(root)
        Frame3.grid(row=5,column=0,columnspan=10)
        Label(Frame3,text="Add Bus Operator Details ",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=2.45,columnspan=7)
        Label(root,text="").grid(row=6,column=0)
        Label(root,text="").grid(row=7,column=0)

        
        def add():
            
            con=sqlite3.connect('mydatabase.db')
            Frame6.grid_forget()
            cur=con.cursor()
            
            if(oid.get()==""):
                showerror('Feild Missing','Please enter OperatorID')
            elif(name.get()==""):
                showerror('Feild Missing','Please enter name')
            elif(address.get()==""):
                showerror('Feild Missing','Please enter address')
            elif(phone.get()==""):
                showerror('Feild Missing','Please enter phone')
            elif(email.get()==""):
                showerror('Feild Missing','Please enter email')
            else:
                def check(mail):
                    like = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

                    if(re.fullmatch(like, mail)):
                        return True

                    else:
                        return False
                try:
                    int(oid.get())
                    if(int(oid.get())<200 or int(oid.get())>299):
                        showerror('Invalid OID','Operator ID out of range\nPlease enter a valid ID')
                        oid.delete(0,END)
                        return
                except:
                    showerror('Invalid OID','Operator ID must be a number')
                    oid.delete(0,END)
                    return
                try:
                    int(phone.get())
                    if(len(phone.get())!=10):
                        showerror('Invalid Phone','Phone must be a 10 digit number\nPlease try again')
                        phone.delete(0,END)
                        return
                except:
                    showerror('Invalid Phone','Phone must be a number')
                    phone.delete(0,END)
                    return
                try:
                    int(name.get())
                    showerror('Invalid Name','Name cannot be numbers only\nPlease try again')
                    name.delete(0,END)
                    return
                except:
                    m=0
                try:
                    int(address.get())
                    showerror('Invalid Address','Address cannot be numbers only\Please try again')
                    address.delete(0,END)
                    return
                except:
                    m=0

                verify = bool(check(email.get()))
                if(verify==False):
                    showerror('Invalid Email','Please enter a valid email')
                    email.delete(0,END)
                    return

                cur.execute("SELECT oid FROM operator")

                ids=cur.fetchall()
                print(ids)
                idslist=[]
                i=0
                for l in ids:
                    idslist.append(ids[i][0])
                    i=i+1
                print(idslist)
                if(int(oid.get()) in idslist):
                    showinfo('Record Already exist','Record for this Operator ID already exist')
                    return
                    
                cur.execute("INSERT INTO operator VALUES(:oid, :name, :address, :phone, :email)",
                        {
                            'oid': oid.get(),
                            'name': name.get(),
                            'address': address.get(),
                            'phone': phone.get(),
                            'email': email.get()
                            
                        }
                        )
                showinfo('Success','Record added successfully...')

                Frame6.grid(row=10,column=0,columnspan=10)
                for widget in Frame6.winfo_children():
                    widget.destroy()
                Label(Frame6,text='Record Added',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
                
                Label(Frame6,text='Operator ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=20)
                
                Label(Frame6,text='Name',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=20)
                
                Label(Frame6,text='Address',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=20)
                
                Label(Frame6,text='Phone',fg='green3',font='Helvetica 14 bold').grid(row=1,column=6,padx=20)
                
                Label(Frame6,text='Email',fg='green3',font='Helvetica 14 bold').grid(row=1,column=8,padx=20)
                
                Label(Frame6,text= oid.get()).grid(row=2,column=0,padx=20,pady=5)

                Label(Frame6,text= name.get()).grid(row=2,column=2,padx=20,pady=5)

                Label(Frame6,text= address.get()).grid(row=2,column=4,padx=20,pady=5)

                Label(Frame6,text= phone.get()).grid(row=2,column=6,padx=20,pady=5)

                Label(Frame6,text= email.get()).grid(row=2,column=8,padx=20,pady=5)
                
                con.commit()
                con.close()
                oid.delete(0,END)
                name.delete(0,END)
                address.delete(0,END)
                phone.delete(0,END)
                email.delete(0,END)
        def edit():
            

            con=sqlite3.connect('mydatabase.db')

            cur=con.cursor()
            
            Frame6.grid_forget()
            
            
            
            if(oid.get()==""):
                showerror('Feild Missing','Please enter OperatorID')
            elif(name.get()==""):
                showerror('Feild Missing','Please enter name')
            elif(address.get()==""):
                showerror('Feild Missing','Please enter address')
            elif(phone.get()==""):
                showerror('Feild Missing','Please enter phone')
            elif(email.get()==""):
                showerror('Feild Missing','Please enter email')
            else:
                def check(mail):
                    like = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

                    if(re.fullmatch(like, mail)):
                        return True

                    else:
                        return False
                try:
                    int(oid.get())
                    if(int(oid.get())>199 and int(oid.get())<300):
                        m=0
                    else:
                        showerror('Invalid OID','Operator ID out of range\nPlease enter a valid ID')
                        oid.delete(0,END)
                        return
                except:
                    showerror('Invalid OID','Operator ID must be a number')
                    oid.delete(0,END)
                    return
                try:
                    int(phone.get())
                    if(len(phone.get())==10):
                        m=0
                    else:
                        showerror('Invalid Phone','Phone must be a 10 digit number\nPlease try again')
                        phone.delete(0,END)
                        return
                except:
                    showerror('Invalid Phone','Phone must be a number')
                    phone.delete(0,END)
                    return
                try:
                    int(name.get())
                    showerror('Invalid Name','Name cannot be numbers only\nPlease try again')
                    name.delete(0,END)
                    return
                except:
                    m=0
                try:
                    int(address.get())
                    showerror('Invalid Address','Address cannot be numbers only\Please try again')
                    address.delete(0,END)
                    return
                except:
                    m=0

                verify = bool(check(email.get()))
                if(verify==False):
                    showerror('Invalid Email','Please enter a valid email')
                    email.delete(0,END)
                    return
                cur.execute("SELECT oid from operator where oid = :oid",
                                {
                                    'oid': oid.get()
                                }
                                )
                p = cur.fetchall()
                if(p==[]):
                    showinfo('No record found','The record you want to edit does not exist\nTry again')
                    return
                
                cur.execute("UPDATE operator set name=:name,address=:address,phone=:phone,email=:email where oid=:oid",
                                    {
                                        'oid': oid.get(),
                                        'name': name.get(),
                                        'address': address.get(),
                                        'phone': phone.get(),
                                        'email': email.get()
                                        
                                    }
                                    )
                showinfo('Success','Record edited successfully...')

                Frame6.grid(row=10,column=0,columnspan=10)
                for widget in Frame6.winfo_children():
                    widget.destroy()
                Label(Frame6,text='Record Edited',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
                
                Label(Frame6,text='Operator ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=20)
                
                Label(Frame6,text='Name',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=20)
                
                Label(Frame6,text='Address',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=20)
                
                Label(Frame6,text='Phone',fg='green3',font='Helvetica 14 bold').grid(row=1,column=6,padx=20)
                
                Label(Frame6,text='Email',fg='green3',font='Helvetica 14 bold').grid(row=1,column=8,padx=20)
                
                Label(Frame6,text= oid.get()).grid(row=2,column=0,padx=20,pady=5)

                Label(Frame6,text= name.get()).grid(row=2,column=2,padx=20,pady=5)

                Label(Frame6,text= address.get()).grid(row=2,column=4,padx=20,pady=5)

                Label(Frame6,text= phone.get()).grid(row=2,column=6,padx=20,pady=5)

                Label(Frame6,text= email.get()).grid(row=2,column=8,padx=20,pady=5)
                
                
                con.commit()
                con.close()
                oid.delete(0,END)
                name.delete(0,END)
                address.delete(0,END)
                phone.delete(0,END)
                email.delete(0,END)
                
        def show():
            con=sqlite3.connect('mydatabase.db')
            cur=con.cursor()
            Frame6.grid_forget()
            if(oid.get()==""):
                showerror('Feild Missing','Please enter OperatorID')
                return
            try:
                int(oid.get())
                if(int(oid.get())>199 and int(oid.get())<300):
                    m=0
                else:
                    showerror('Invalid OID','Operator ID out of range\nPlease enter a valid ID')
                    oid.delete(0,END)
                    return
            except:
                showerror('Invalid OID','Operator ID must be a number')
                oid.delete(0,END)
                return

            
            cur.execute("SELECT * from operator where oid = :oid",
                                {
                                    'oid': oid.get()
                                }
                                )
            p = cur.fetchall()
            if(p==[]):
                showinfo('No record found','The record you want to see does not exist\nTry again')
                
                return
            else:
                Frame6.grid(row=10,column=0,columnspan=10)

                for widget in Frame6.winfo_children():
                    widget.destroy()
                    
                Label(Frame6,text='Requested Record',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
                
                Label(Frame6,text='Operator ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=20)
                
                Label(Frame6,text='Name',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=20)
                
                Label(Frame6,text='Address',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=20)
                
                Label(Frame6,text='Phone',fg='green3',font='Helvetica 14 bold').grid(row=1,column=6,padx=20)
                
                Label(Frame6,text='Email',fg='green3',font='Helvetica 14 bold').grid(row=1,column=8,padx=20)
                
                Label(Frame6,text= str(p[0][0])).grid(row=2,column=0,padx=20,pady=5)

                Label(Frame6,text= p[0][1]).grid(row=2,column=2,padx=20,pady=5)

                Label(Frame6,text= p[0][2]).grid(row=2,column=4,padx=20,pady=5)

                Label(Frame6,text= str(p[0][3])).grid(row=2,column=6,padx=20,pady=5)

                Label(Frame6,text= p[0][4]).grid(row=2,column=8,padx=20,pady=5)

        def olimit(value):
            entry=oid.get()
            if(len(entry)>2):
                oid.delete(2,END)
        def plimit(value):
            entry=phone.get()
            if(len(entry)>9):
                phone.delete(9,END)
        Frame4=Frame(root)
        Frame4.grid(row=8,column=0,columnspan=10)

        Frame5=Frame(root)
        Frame5.grid(row=9,column=0,columnspan=10)

        Frame6=Frame(root)
        Frame6.grid(row=10,column=0,columnspan=10)
                    
        Label(Frame4,text="Operator ID").grid(row=8,column=0,sticky=E)

        Label(Frame4,text="Range : (200 - 299)",font='helvetica 11 bold italic').grid(row=9,column=1)

        oid=Entry(Frame4,width=15)

        oid.grid(row=8,column=1,sticky=W)

        oid.bind('<KeyPress>',olimit)
        Label(Frame4,text="Name").grid(row=8,column=2,sticky=E)

        name=Entry(Frame4)
        name.grid(row=8,column=3,sticky=W)

        Label(Frame4,text="Address").grid(row=8,column=4,sticky=E)

        address=Entry(Frame4)
        address.grid(row=8,column=5,sticky=E)

        Label(Frame4,text="Phone").grid(row=8,column=6,sticky=E)

        phone=Entry(Frame4)

        phone.grid(row=8,column=7,sticky=W)

        phone.bind('<KeyPress>',plimit)

        Label(Frame4,text="Email").grid(row=8,column=8,sticky=W)

        email=Entry(Frame4)
        email.grid(row=8,column=8,padx=40)

        Button(Frame5,text="Add",font="Helvetica 13",bg="light green",command=add).grid(row=0,column=1)

        Button(Frame5,text="Edit",bg="light green",font="Helvetica 13",command=edit).grid(row=0,column=2,padx=20)

        Button(Frame5,text="Show",font="Helvetica 13",bg="light green",command=show).grid(row=0,column=3)

        Label(Frame4,text="").grid(row=10,column=0)

        Label(Frame4,text="").grid(row=11,column=0)
        def home():
            root.destroy()
            self.menu()
        photu=PhotoImage(file="home.png")
        Button(Frame5,image=photu,command=home).grid(row=0,column=4,columnspan=7,padx=10)
        root.mainloop()

    def bus(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        img=PhotoImage(file="Bus.png")
        Frame1=Frame(root)
        Frame1.grid(row=0,column=0,columnspan=10)
        Label(Frame1,image=img).grid(row=0,column=0,padx=w/2.45,columnspan=7)
        Label(root,text="").grid(row=1,column=0)

        Frame2=Frame(root)
        Frame2.grid(row=2,column=0,columnspan=10)
        Label(Frame2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=w/2.45,pady=10,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame3=Frame(root)
        Frame3.grid(row=3,column=0,columnspan=10)
        Label(Frame3,text="Add Bus Details ",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=w/2.45,pady=10,columnspan=7)
        Label(root,text="").grid(row=6,column=0)
        Label(root,text="").grid(row=7,column=0)

        
        def add():
            
            con=sqlite3.connect('mydatabase.db')
            Frame5.grid_forget()
            cur=con.cursor()
            
            if(busid.get()==""):
                showerror('Feild Missing','Please enter BusID')
            elif(bus=="Select"):
                showerror('Feild Missing','Please seslect bus type')
            elif(capacity.get()==""):
                showerror('Feild Missing','Please enter capacity')
            elif(fare.get()==""):
                showerror('Feild Missing','Please enter fare')
            elif(rid.get()==""):
                showerror('Feild Missing','Please enter RouteID')
            elif(opid.get()==""):
                showerror('Feild Missing','Please enter OperatorID')
            else:
                try:
                    int(busid.get())
                    if(int(busid.get())>399 or int(busid.get())<300):
                        showerror('Invalid BUS ID','Bus ID out of range\nTry again')
                        busid.delete(0,END)
                        return
                except:
                    showerror('Invalid Bus ID','Bus ID must be a number')
                    busid.delete(0,END)
                    return
                try:
                    int(capacity.get())
                    if(int(capacity.get())<1):
                        showerror('Invalid capacity','Please enter a valid capacity')
                        capacity.delete(0,END)
                        return
                except:
                    showerror('Invalid Capacity','Capacity must be a number')
                    capacity.delete(0,END)
                    return
                try:
                    int(fare.get())
                    if(int(fare.get())<1):
                        showerror('Invalid fare','Please enter a valid fare')
                        fare.delete(0,END)
                        return
                except:
                    showerror('Invalid Fare','Fare must be a number')
                    fare.delete(0,END)
                    return
                try:
                    int(opid.get())
                    if(int(opid.get())>299 or int(opid.get())<200):
                        showerror('Invalid Operator ID','Operator ID out of range\nTry again')
                        opid.delete(0,END)
                        return
                except:
                    showerror('Invalid Operator ID','Operator ID must be a number')
                    opid.delete(0,END)
                    return

                try:
                    int(rid.get())
                    if(int(rid.get())<0 or int(rid.get())>100):
                        showerror('Invalid Route ID','Route ID out of range\nTry again')
                        rid.delete(0,END)
                        return
                except:
                    showerror('Invalid Route ID',' Route ID must be a number')
                    rid.delete(0,END)
                    return

                cur.execute("SELECT oid FROM operator")

                ids=cur.fetchall()
                print(ids)
                idslist=[]
                i=0
                for l in ids:
                    idslist.append(ids[i][0])
                    i=i+1
                print(idslist)
                if(int(opid.get()) not in idslist):
                    showinfo('Invalid Operator','No such operator exist')
                    opid.delete(0,END)
                    return

                cur.execute("SELECT rid from route")

                rd=cur.fetchall()
                print(rd)
                rdlist=[]
                i=0
                for l in rd:
                    rdlist.append(rd[i][0])
                    i=i+1
                print(rdlist)
                if(int(rid.get()) not in rdlist):
                    showinfo('Invalid Route','No such Route exist')
                    rid.delete(0,END)
                    return

                cur.execute("Select busid,rid from bus")

                exist = cur.fetchall()
                print(exist)
                i=0
                for l in exist:
                    if(int(busid.get())==exist[i][0]):
                        if(int(rid.get())==exist[i][1]):
                            showerror('Record Exist','Record already exist')
                            return
                    i=i+1
                    
                cur.execute("INSERT INTO Bus VALUES(:busid, :bustype, :capacity,:fare, :rid, :opid)",
                                {
                                    'busid': busid.get(),
                                    'capacity': capacity.get(),
                                    'fare': fare.get(),
                                    'rid': rid.get(),
                                    'opid': opid.get(),
                                    'bustype' : bus.get()
                                }
                                )
                showinfo('Success','Record added successfully...')

                Frame5.grid(row=10,column=0,columnspan=10)
                for widget in Frame5.winfo_children():
                    widget.destroy()

                Label(Frame5,text='Record Added',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
                
                Label(Frame5,text='Bus ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=15)
                
                Label(Frame5,text='Bus Type',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=15)
                
                Label(Frame5,text='Capacity',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=15)
                
                Label(Frame5,text='Fare',fg='green3',font='Helvetica 14 bold').grid(row=1,column=6,padx=15)
                
                Label(Frame5,text='Operator ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=8,padx=15)

                Label(Frame5,text='Route ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=10,padx=15)
                
                Label(Frame5,text= busid.get()).grid(row=2,column=0,padx=15,pady=5)

                Label(Frame5,text= bus.get()).grid(row=2,column=2,padx=15,pady=5)

                Label(Frame5,text= capacity.get()).grid(row=2,column=4,padx=15,pady=5)

                Label(Frame5,text= fare.get()).grid(row=2,column=6,padx=15,pady=5)

                Label(Frame5,text= opid.get()).grid(row=2,column=8,padx=15,pady=5)

                Label(Frame5,text= rid.get()).grid(row=2,column=10,padx=15,pady=5)
                
                con.commit()
                con.close()
                opid.delete(0,END)
                busid.delete(0,END)
                capacity.delete(0,END)
                fare.delete(0,END)
                rid.delete(0,END)
                bus.set("Select")

        def edit():
            

            con=sqlite3.connect('mydatabase.db')

            cur=con.cursor()

            Frame5.grid_forget()
            
            if(busid.get()==""):
                showerror('Feild Missing','Please enter BusID')
            elif(bus=="Select"):
                showerror('Feild Missing','Please select bus type')
            elif(capacity.get()==""):
                showerror('Feild Missing','Please enter capacity')
            elif(fare.get()==""):
                showerror('Feild Missing','Please enter fare')
            elif(rid.get()==""):
                showerror('Feild Missing','Please enter RouteID')
            elif(opid.get()==""):
                showerror('Feild Missing','Please enter OperatorID')
            else:
                try:
                    int(busid.get())
                    if(int(busid.get())>399 or int(busid.get())<300):
                        showerror('Invalid BUS ID','Bus ID out of range\nTry again')
                        busid.delete(0,END)
                        return
                except:
                    showerror('Invalid Bus ID','Bus ID must be a number')
                    busid.delete(0,END)
                    return
                try:
                    int(capacity.get())
                    if(int(capacity.get())<1):
                        showerror('Invalid capacity','Please enter a valid capacity')
                        capacity.delete(0,END)
                        return
                except:
                    showerror('Invalid Capacity','Capacity must be a number')
                    capacity.delete(0,END)
                    return
                try:
                    int(fare.get())
                    if(int(fare.get())<1):
                        showerror('Invalid fare','Please enter a valid fare')
                        fare.delete(0,END)
                        return
                except:
                    showerror('Invalid Fare','Fare must be a number')
                    fare.delete(0,END)
                    return
                try:
                    int(opid.get())
                    if(int(opid.get())>299 or int(opid.get())<200):
                        showerror('Invalid Operator ID','Operator ID out of range\nTry again')
                        opid.delete(0,END)
                        return
                except:
                    showerror('Invalid Operator ID','Operator ID must be a number')
                    opid.delete(0,END)
                    return

                try:
                    int(rid.get())
                    if(int(rid.get())<0 or int(rid.get())>100):
                        showerror('Invalid Route ID','Route ID out of range\nTry again')
                        rid.delete(0,END)
                        return
                except:
                    showerror('Invalid Route ID',' Route ID must be a number')
                    rid.delete(0,END)
                    return

                cur.execute("SELECT oid FROM operator")

                ids=cur.fetchall()
                print(ids)
                idslist=[]
                i=0
                for l in ids:
                    idslist.append(ids[i][0])
                    i=i+1
                print(idslist)
                if(int(opid.get()) not in idslist):
                    showinfo('Invalid Operator','No such operator exist')
                    opid.delete(0,END)
                    return

                cur.execute("SELECT rid from route")

                rd=cur.fetchall()
                print(rd)
                rdlist=[]
                i=0
                for l in rd:
                    rdlist.append(rd[i][0])
                    i=i+1
                print(rdlist)
                if(int(rid.get()) not in rdlist):
                    showinfo('Invalid Route','No such Route exist')
                    rid.delete(0,END)
                    return

                cur.execute("SELECT BusID from Bus where busid = :busid",
                                    {
                                        'busid': busid.get()
                                    }
                                    )
                p = cur.fetchall()
                print(p)
                if(p==[]):
                    showerror('Invalid Bus ID','No Record for this Bus ID exist')
                    return

                try:
                    cur.execute("UPDATE Bus set bustype=:bustype,capacity=:capacity,fare=:fare,rid=:rid,oid=:opid where BusID=:busid and rid=:rid",
                                        {
                                            'busid': busid.get(),
                                            'capacity': capacity.get(),
                                            'fare': fare.get(),
                                            'rid': rid.get(),
                                            'opid': opid.get(),
                                            'bustype': bus.get()
                                        }
                                        )
                except:
                    showerror('Invalid Update','Bad request\nCannot edit data')
                    return
                    
                showinfo('Success','Record edited successfully...')

                Frame5.grid(row=10,column=0,columnspan=10)
                for widget in Frame5.winfo_children():
                    widget.destroy()

                Label(Frame5,text='Record Added',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
                
                Label(Frame5,text='Bus ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=15)
                
                Label(Frame5,text='Bus Type',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=15)
                
                Label(Frame5,text='Capacity',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=15)
                
                Label(Frame5,text='Fare',fg='green3',font='Helvetica 14 bold').grid(row=1,column=6,padx=15)
                
                Label(Frame5,text='Operator ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=8,padx=15)

                Label(Frame5,text='Route ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=10,padx=15)
                
                Label(Frame5,text= busid.get()).grid(row=2,column=0,padx=15,pady=5)

                Label(Frame5,text= bus.get()).grid(row=2,column=2,padx=15,pady=5)

                Label(Frame5,text= capacity.get()).grid(row=2,column=4,padx=15,pady=5)

                Label(Frame5,text= fare.get()).grid(row=2,column=6,padx=15,pady=5)

                Label(Frame5,text= opid.get()).grid(row=2,column=8,padx=15,pady=5)

                Label(Frame5,text= rid.get()).grid(row=2,column=10,padx=15,pady=5)
                    
                con.commit()
                con.close()
                opid.delete(0,END)
                busid.delete(0,END)
                capacity.delete(0,END)
                fare.delete(0,END)
                rid.delete(0,END)
                bus.set("Select")
        def show():

            con=sqlite3.connect('mydatabase.db')

            cur=con.cursor()
            
            Frame5.grid_forget()
            if(busid.get()==""):
                showerror('Feild Missing','Please enter BusID')
                return
            else:
                try:
                    int(busid.get())
                    if(int(busid.get())>399 or int(busid.get())<300):
                        showerror('Invalid BUS ID','Bus ID out of range\nTry again')
                        busid.delete(0,END)
                        return
                except:
                    showerror('Invalid Bus ID','Bus ID must be a number')
                    busid.delete(0,END)
                    return

            
            cur.execute("SELECT busid from Bus where busid = :bus",
                                    {
                                        'bus': busid.get()
                                    }
                                    )
            p = cur.fetchall()
            print(p)
            if(p==[]):
                showerror('Invalid Bus ID','No Record for this Bus ID exist')
                return

            Frame5.grid(row=10,column=0,columnspan=10)
            for widget in Frame5.winfo_children():
                    widget.destroy()

            Label(Frame5,text='Bus Info',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
            
            Label(Frame5,text='Bus ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=15)
            
            Label(Frame5,text='Bus Type',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=15)
            
            Label(Frame5,text='Capacity',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=15)
            
            Label(Frame5,text='Fare',fg='green3',font='Helvetica 14 bold').grid(row=1,column=6,padx=15)
            
            Label(Frame5,text='Operator ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=8,padx=15)

            Label(Frame5,text='Route ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=10,padx=15)

            cur.execute("Select * from bus where busid=:bus",
                        {
                            'bus': busid.get()
                        })

            businfo = cur.fetchall()
            
            cur.execute("SELECT count(*) from bus where busid=:busid",
                        {
                            'busid': busid.get()
                        }
                        )
            labels = cur.fetchall()

            enteries = labels[0][0]
            print(labels)
            counter=2
            t=0
            while(enteries!=0):

                Label(Frame5,text= businfo[t][0]).grid(row=counter,column=0,padx=15,pady=5)

                Label(Frame5,text= businfo[t][1]).grid(row=counter,column=2,padx=15,pady=5)

                Label(Frame5,text= businfo[t][2]).grid(row=counter,column=4,padx=15,pady=5)

                Label(Frame5,text= businfo[t][3]).grid(row=counter,column=6,padx=15,pady=5)

                Label(Frame5,text= businfo[t][4]).grid(row=counter,column=8,padx=15,pady=5)

                Label(Frame5,text= businfo[t][5]).grid(row=counter,column=10,padx=15,pady=5)

                counter=counter+1

                enteries=enteries-1

                t=t+1

                
        def blimit(value):
            entry=busid.get()
            if(len(entry)>2):
                busid.delete(2,END)
        def olimit(value):
            entry=opid.get()
            if(len(entry)>2):
                opid.delete(2,END)
        def rlimit(value):
            entry=rid.get()
            if(len(entry)>2):
                rid.delete(2,END)
            
        Frame4=Frame(root)
        Frame4.grid(row=5,column=0,columnspan=10)
        Label(Frame4,text="Bus ID").grid(row=5,column=0,sticky=E)
        busid=Entry(Frame4,width=15)

        Frame5=Frame(root)
        Frame5.grid(row=6,column=0,columnspan=10)
        Label(Frame4,text="Range : (300 - 399)",font='helvetica 11 bold italic').grid(row=6,column=1)
        busid.grid(row=5,column=1,sticky=W)

        busid.bind('<KeyPress>',blimit)

        Label(Frame4,text="Bus Type").grid(row=5,column=2,sticky=E)
        bus=StringVar()
        bus.set("Select")
        option=["AC 2x2","AC 3x2","Non AC 2x2","Non AC 3x2","AC Sleeper 2x1","Non AC Sleeper 2x1"]
        menu=OptionMenu(Frame4,bus,*option)
        menu.grid(row=5,column=3,sticky=E)

        Label(Frame4,text="Capacity").grid(row=5,column=4,sticky=E)
        capacity=Entry(Frame4,width=15)
        capacity.grid(row=5,column=5,sticky=W)


        Label(Frame4,text="Fare Rs").grid(row=5,column=6,sticky=E)
        fare=Entry(Frame4,width=10)
        fare.grid(row=5,column=7,sticky=W)

        Label(Frame4,text="Operator ID").grid(row=5,column=8,sticky=E)
        opid=Entry(Frame4,width=10)
        Label(Frame4,text="Range : (200 - 299)",font='helvetica 11 bold italic').grid(row=6,column=7)
        opid.grid(row=5,column=9,sticky=W)
        opid.bind('<KeyPress>',olimit)
        Label(Frame4,text="Route ID").grid(row=5,column=10,sticky=E)
        rid=Entry(Frame4,width=10)
        rid.grid(row=5,column=11,sticky=W)
        Label(Frame4,text="Range : (1 - 100)",font='helvetica 11 bold italic').grid(row=6,column=11)
        rid.bind('<KeyPress>',rlimit)
        Label(Frame4,text="").grid(row=9,column=0)
        Label(Frame4,text="").grid(row=10,column=0)

        Button(Frame4,text="Add Bus",bg="light green",command=add).grid(row=11,column=4)

        Button(Frame4,text="Edit Bus",bg="light green",command=edit).grid(row=11,column=5)

        Button(Frame4,text="Show Bus",bg="light green",command=show).grid(row=11,column=6)
        def home():
            root.destroy()
            self.menu()
        photu=PhotoImage(file="home.png")
        Button(Frame4,image=photu,command=home).grid(row=11,column=7,padx=10)

        root.mainloop()

    def route(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        img=PhotoImage(file="Bus.png")
        Frame1=Frame(root)
        Frame1.grid(row=0,column=0,columnspan=10)
        Label(Frame1,image=img).grid(row=0,column=0,padx=w/2.45,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame2=Frame(root)
        Frame2.grid(row=3,column=0,columnspan=10)
        Label(Frame2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame3=Frame(root)
        Frame3.grid(row=5,column=0,columnspan=10)
        Label(Frame3,text="Add Bus Route Details ",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)
        Label(root,text="").grid(row=6,column=0)
        Label(root,text="").grid(row=7,column=0)

        
        def add():
            
            con=sqlite3.connect('mydatabase.db')
            
            Frame6.grid_forget()
            
            cur=con.cursor()
            
            if(routeid.get()==""):
                showerror('Feild Missing','Please enter RouteID')
            elif(sid.get()==""):
                showerror('Feild Missing','Please enter StationID')
            elif(station.get()==""):
                showerror('Feild Missing','Please enter Station Name')
            else:
                try:
                    int(routeid.get())
                    if(int(routeid.get())<0 or int(routeid.get())>100):
                        showerror('Range Error','Route ID out of range\nEnter route ID in given range')
                        return
                except:
                    showerror('Invalid Input','Route ID must be a number')
                    routeid.delete(0,END)
                    return
                try:
                    int(sid.get())
                    if(int(sid.get())<0 or int(sid.get())>10):
                        showerror('Range Error','Station ID out of range\nEnter Station ID in given range')
                        return
                except:
                    showerror('Invalid Input','Station ID must be a number')
                    sid.delete(0,END)
                    return
                try:
                    int(station.get())
                    showerror('Invalid Station','Station Name cannot be numbers only')
                    station.delete(0,END)
                    return
                except:
                    m=0
                sname = station.get().lower()
                
                cur.execute("Select rid,sid from route")

                rinfo = cur.fetchall()
                
                i=0
                for l in rinfo:
                    if(int(routeid.get())==rinfo[i][0]):
                        if(int(sid.get())==rinfo[i][1]):
                            showerror('Record Exist','Record already exist for given Route and Station ID')
                            return
                    i=i+1
                
                cur.execute("INSERT INTO route VALUES(:rid, :sid, :sname)",
                            {
                                'rid': routeid.get(),
                                'sid': sid.get(),
                                'sname': sname
                            }
                            )
                showinfo('Success','Record added successfully...')

                Frame6.grid(row=10,column=0,columnspan=10)
                for widget in Frame6.winfo_children():
                    widget.destroy()

                Label(Frame6,text='Route Info',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
                
                Label(Frame6,text='Route ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=15)
                
                Label(Frame6,text='Station ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=15)
                
                Label(Frame6,text='Station Name',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=15)
                
                Label(Frame6,text= routeid.get()).grid(row=2,column=0,padx=20,pady=5)

                Label(Frame6,text= sid.get()).grid(row=2,column=2,padx=20,pady=5)

                Label(Frame6,text= station.get()).grid(row=2,column=4,padx=20,pady=5)
                    
                
                con.commit()
                con.close()
                routeid.delete(0,END)
                sid.delete(0,END)
                station.delete(0,END)

        def delete():
            
            con=sqlite3.connect('mydatabase.db')
            Frame6.grid_forget()
            cur=con.cursor()
            
            if(routeid.get()==""):
                showerror('Feild Missing','Please enter RouteID')
            elif(sid.get()==""):
                showerror('Feild Missing','Please enter StationID')
            else:

                try:
                    int(routeid.get())
                    if(int(routeid.get())<0 or int(routeid.get())>100):
                        showerror('Range Error','Route ID out of range\nEnter route ID in given range')
                        return
                except:
                    showerror('Invalid Input','Route ID must be a number')
                    routeid.delete(0,END)
                    return
                try:
                    int(sid.get())
                    if(int(sid.get())<0 or int(sid.get())>10):
                        showerror('Range Error','Station ID out of range\nEnter Station ID in given range')
                        return
                except:
                    showerror('Invalid Input','Station ID must be a number')
                    sid.delete(0,END)
                    return
                
                cur.execute("Select rid,sid,sname from route")

                rinfo = cur.fetchall()
                flag=0
                sname='t'
                i=0
                for l in rinfo:
                    if(int(routeid.get())==rinfo[i][0]):
                        if(int(sid.get())==rinfo[i][1]):
                            flag=1
                            sname=rinfo[i][2]
                    i=i+1
                if(flag==0):
                    showerror('Invalid Route','No Route exist for given Route and Staion ID')
                    return
                
                cur.execute("DELETE FROM route WHERE rid=:rid and sid=:sid",
                                {
                                    'rid': routeid.get(),
                                    'sid': sid.get()
                                }
                                )
                showinfo('Success','Record Deleted successfully...')

                Frame6.grid(row=10,column=0,columnspan=10)
                for widget in Frame6.winfo_children():
                    widget.destroy()

                Label(Frame6,text='Route Info',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
                
                Label(Frame6,text='Route ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=15)
                
                Label(Frame6,text='Station ID',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=15)
                
                Label(Frame6,text='Station Name',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=15)
                
                Label(Frame6,text= routeid.get()).grid(row=2,column=0,padx=20,pady=5)

                Label(Frame6,text= sid.get()).grid(row=2,column=2,padx=20,pady=5)

                Label(Frame6,text= sname).grid(row=2,column=4,padx=20,pady=5)
                
                con.commit()
                con.close()
                routeid.delete(0,END)
                sid.delete(0,END)
                station.delete(0,END)

        def rlimit(value):
            entry=len(routeid.get())
            if(entry>2):
                routeid.delete(2,END)

        def slimit(value):
            entry=len(sid.get())
            if(entry>1):
                sid.delete(1,END)
              
        Frame4=Frame(root)
        Frame4.grid(row=7,column=0,columnspan=10)
        Label(Frame4,text="Route ID").grid(row=8,column=0,sticky=E)
        routeid=Entry(Frame4)
        routeid.grid(row=8,column=1,sticky=W)
        routeid.bind('<KeyPress>',rlimit)
        Frame5=Frame(root)

        Frame5.grid(row=8,column=0,columnspan=10,pady=30)

        Frame6=Frame(root)

        Frame6.grid(row=9,column=0,columnspan=10)



        Label(Frame4,text="Station ID").grid(row=8,column=2,sticky=E)
        sid=Entry(Frame4)
        sid.grid(row=8,column=3,sticky=W)
        sid.bind('<KeyPress>',slimit)
        Label(Frame4,text="Station Name").grid(row=8,column=4,sticky=E)
        station=Entry(Frame4)
        station.grid(row=8,column=5,sticky=W)

        Label(Frame4,text="Range : (1 - 100)",font='helvetica 11 bold italic').grid(row=9,column=1)
        Label(Frame4,text="Range : (1 - 10)",font='helvetica 11 bold italic').grid(row=9,column=3)


        Button(Frame5,text="Add Route",bg="light green",command=add).grid(row=0,column=1,padx=10)
        Button(Frame5,text="Delete Route",bg="light green",fg="red",command=delete).grid(row=0,column=2,padx=10)
        def home():
            root.destroy()
            self.menu()
        pic=PhotoImage(file="home.png")
        Button(Frame5,image=pic,command=home).grid(row=0,column=3,padx=10)
        root.mainloop()

    def run(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(w,h))

        img=PhotoImage(file="Bus.png")
        Frame1=Frame(root)
        Frame1.grid(row=0,column=0,columnspan=10)
        Label(Frame1,image=img).grid(row=0,column=0,padx=w/2.45,columnspan=7)
        Label(root,text="").grid(row=2,column=0)

        Frame2=Frame(root)
        Frame2.grid(row=3,column=0,columnspan=10)
        Label(Frame2,text="Online Bus Booking System ",fg="red",bg="light blue",font="Arial 16 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)
        Label(root,text="").grid(row=4,column=0)

        Frame3=Frame(root)
        Frame3.grid(row=5,column=0,columnspan=10)
        Label(Frame3,text="Add Bus Running Details ",fg="green",font="Arial 13 bold",borderwidth=1,relief="ridge").grid(row=1,column=0,padx=400,columnspan=7)
        Label(root,text="").grid(row=6,column=0)
        Label(root,text="").grid(row=7,column=0)

        def datecheck(test):
            format = "%d/%m/%Y"
            res = True
            try:
                    res = bool(datetime.strptime(test, format))
            except ValueError:
                    res = False
            return res

        def add():
            
            con=sqlite3.connect('mydatabase.db')
            Frame6.grid_forget()
            cur=con.cursor()
            if(busids.get()==""):
                showerror('Feild Missing','Please enter Bus ID')
            elif(rundate.get()==""):
                showerror('Feild Missing','Please enter running date')
            elif(seats.get()==""):
                showerror('Feild Missing','Please enter Station Name')
            else:
                
                try:
                    int(busids.get())
                    if(int(busids.get())<300 or int(busids.get())>399):
                        showerror('Range Error','Please enter Bus ID in valid range')
                        return
                except:
                    showerror('Invalid Input','Bus ID must be number only')
                    return

                res=datecheck(rundate.get())
                if(res==True):
                    datelist=rundate.get().split("/")
                    d = str(date.today())
                    dlist=d.split("-")
                    print(datelist)
                    print(dlist)
                    if(len(datelist[0])==2):
                        if(len(datelist[1])==2):
                            m=0
                        else:
                            showerror('Invalid month Format','Please enter month in correct format')
                            Frame2.grid_forget()
                            return
                    else:
                        showerror('Invalid date Format','Please enter date in correct format')
                        Frame2.grid_forget()
                        return
                            
                    if(int(datelist[2])>int(dlist[0])):
                        m=0
                    elif(int(datelist[2])==int(dlist[0])):
                        if(int(datelist[1])>int(dlist[1])):
                            m=0
                        elif(int(datelist[1])==int(dlist[1])):
                            if(int(datelist[0])<int(dlist[2])):
                                showerror('Invalid Date','Please enter a valid date')
                                Frame2.grid_forget()
                                return
                        else:
                            showerror('Invalid month','Please enter a valid month')
                            Frame2.grid_forget()
                            return
                    else:
                        showerror('Invalid Year','Please enter a valid Year')
                        Frame2.grid_forget()
                        return
                else:
                    showerror('Wrong Date','Date or Date format incorrect\nTry again')
                    Frame2.grid_forget()
                    return

                cur.execute("Select capacity from bus where busid=:this",
                        {
                            'this': busids.get()
                        }
                        )
                capa = cur.fetchall()
                print('capacity' + str(capa[0][0]))
                capci = capa[0][0]
                          
                try:
                    int(seats.get())
                    if(int(seats.get())>capci):
                        showerror('ValueError','Available seats cannot exceed capacity')
                        return
                except:
                    showerror('Invalid Input','Seats must be number only')
                    return

                try:
                    cur.execute("INSERT INTO running VALUES(:busids, :rundate, :seats)",
                            {
                                'busids': busids.get(),
                                'rundate': rundate.get(),
                                'seats': seats.get()
                            }
                            )

                except:
                    showinfo('Record Found','Bus is already running on this date')
                    return
                
                showinfo('Success','Record added successfully...')

                Frame6.grid(row=10,column=0,columnspan=10)

                for widget in Frame6.winfo_children():
                    widget.destroy()
                    
                Label(Frame6,text='Added Record',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
                
                Label(Frame6,text='Bus ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=20)
                
                Label(Frame6,text='Running Date',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=20)
                
                Label(Frame6,text='Available seats',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=20)
                
                
                Label(Frame6,text= busids.get()).grid(row=2,column=0,padx=20,pady=5)

                Label(Frame6,text= rundate.get()).grid(row=2,column=2,padx=20,pady=5)

                Label(Frame6,text= seats.get()).grid(row=2,column=4,padx=20,pady=5)


                con.commit()
                con.close()
                busids.delete(0,END)
                rundate.delete(0,END)
                seats.delete(0,END)

        def delete():
            

            con=sqlite3.connect('mydatabase.db')

            cur=con.cursor()
            
            Frame6.grid_forget()
            
            if(busids.get()==""):
                showerror('Feild Missing','Please enter BusID')
            elif(rundate.get()==""):
                showerror('Feild Missing','Please enter Running Date')
            else:
                try:
                    int(busids.get())
                    if(int(busids.get())<300 or int(busids.get())>399):
                        showerror('Range Error','Please enter Bus ID in valid range')
                        return
                except:
                    showerror('Invalid Input','Bus ID must be number only')
                    return


                res=datecheck(rundate.get())

                if(res==True):
                    datelist=rundate.get().split("/")
                    d = str(date.today())
                    dlist=d.split("-")
                    print(datelist)
                    print(dlist)
                    if(len(datelist[0])==2):
                        if(len(datelist[1])==2):
                            m=0
                        else:
                            showerror('Invalid month Format','Please enter month in correct format')
                            Frame2.grid_forget()
                            return
                    else:
                        showerror('Invalid date Format','Please enter date in correct format')
                        Frame2.grid_forget()
                        return
                            
                    if(int(datelist[2])>int(dlist[0])):
                        m=0
                    elif(int(datelist[2])==int(dlist[0])):
                        if(int(datelist[1])>int(dlist[1])):
                            m=0
                        elif(int(datelist[1])==int(dlist[1])):
                            if(int(datelist[0])<int(dlist[2])):
                                showerror('Invalid Date','Please enter a valid date')
                                Frame2.grid_forget()
                                return
                        else:
                            showerror('Invalid month','Please enter a valid month')
                            Frame2.grid_forget()
                            return
                    else:
                        showerror('Invalid Year','Please enter a valid Year')
                        Frame2.grid_forget()
                        return
                else:
                    showerror('Wrong Date','Date or Date format incorrect\nTry again')
                    Frame2.grid_forget()
                    return

                cur.execute("SELECT * from running WHERE BusID=:busids and Date=:run",
                                    {
                                        'busids': busids.get(),
                                        'run': rundate.get()
                                    })
                
                s = cur.fetchall()
                print(s)
                sea = s[0][2]
                try:
                    cur.execute("DELETE FROM running WHERE BusID=:busids and Date=:rundate",
                                    {
                                        'busids': busids.get(),
                                        'rundate': rundate.get()
                                    })
                except:
                    showerror('Record Not Found','No record exist for given data')
                    return
                
                showinfo('Success','Record Deleted successfully...')

                
                
                
                
                Frame6.grid(row=10,column=0,columnspan=10)

                for widget in Frame6.winfo_children():
                    widget.destroy()
                    
                Label(Frame6,text='Added Record',fg='Red',bg='LightBlue1',font="Arial 18 bold",borderwidth=1,relief="ridge").grid(row=0,column=0,columnspan=10,pady=15)
                
                Label(Frame6,text='Bus ID',fg='green3',font='Arial 14 bold').grid(row=1,column=0,padx=20)
                
                Label(Frame6,text='Running Date',fg='green3',font='Helvetica 14 bold').grid(row=1,column=2,padx=20)
                
                Label(Frame6,text='Available seats',fg='green3',font='Helvetica 14 bold').grid(row=1,column=4,padx=20)
                
                
                Label(Frame6,text= busids.get()).grid(row=2,column=0,padx=20,pady=5)

                Label(Frame6,text= rundate.get()).grid(row=2,column=2,padx=20,pady=5)

                Label(Frame6,text= sea).grid(row=2,column=4,padx=20,pady=5)

                con.commit()
                con.close()
                busids.delete(0,END)
                rundate.delete(0,END)
                busids.delete(0,END)
        def blimit(value):
            entry=len(busids.get())
            if(entry>2):
                busids.delete(2,END)
        Frame4=Frame(root)
        Frame4.grid(row=7,column=0,columnspan=10)
        Label(Frame4,text="Bus ID").grid(row=8,column=2,sticky=E)
        busids=Entry(Frame4)
        busids.grid(row=8,column=3,sticky=W)
        busids.bind('<KeyPress>',blimit)
        Frame5=Frame(root)
        Frame5.grid(row=8,column=0,columnspan=10,pady=30)

        Frame6=Frame(root)
        Frame6.grid(row=9,column=0,columnspan=10)


        Label(Frame4,text="Range : (300 - 399)",font='helvetica 11 bold italic').grid(row=9,column=3)
        Label(Frame4,text="Running Date").grid(row=8,column=4,sticky=E)
        rundate=Entry(Frame4)
        rundate.grid(row=8,column=5,sticky=W)
        Label(Frame4,text='Format : (DD/MM/YYYY)',font='Helvetica 12 italic bold').grid(row=9,column=5)
        Label(Frame4,text="Seat Available").grid(row=8,column=6,sticky=E)
        seats=Entry(Frame4)
        seats.grid(row=8,column=7,sticky=W)

        Button(Frame5,text="Add Route",bg="light green",command=add).grid(row=0,column=1,padx=10)
        Button(Frame5,text="Delete Route",bg="light green",fg="red",command=delete).grid(row=0,column=2,padx=10)
        def home():
            root.destroy()
            self.menu()
        pic=PhotoImage(file="home.png")
        Button(Frame5,image=pic,command=home).grid(row=0,column=3,padx=10)

        root.mainloop()



p=main_fn()
p.front()


