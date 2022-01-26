from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import sqlite3

con = sqlite3.connect('patient_record.db')
c=con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS patient_database
         (PID INT      NOT NULL,
         PNAME           TEXT    NOT NULL,
         PNO            INT     NOT NULL,
         FILENAME        CHAR(50),
         PADDRESS         CHAR(50),
         PCOMPLAINTS      CHAR(200),
         CHIKITSA         CHAR(150));''')
con.commit()

def insert():
    pid = pId_entry.get()
    pname=pName_entry.get()
    pno=pNo_entry.get()
    filename=fName_entry.get()
    address=add_entry.get()
    complaint=complaints_entry.get()
    chik=chikitsa_entry.get()
    if (pname=="" or pno=="" or filename=="" or address=="" or complaint=="" or chik==""):
        messagebox.showinfo("Status","All Fields are required..!")
    else:
        c.execute("INSERT INTO patient_database VALUES (?,?,?,?,?,?,?)",(pid,pname,pno,filename,address,complaint,chik))
        con.commit()
        pId_entry.delete(0,'end')
        pName_entry.delete(0, 'end')
        pNo_entry.delete(0, 'end')
        fName_entry.delete(0, 'end')
        add_entry.delete(0, 'end')
        complaints_entry.delete(0,'end')
        chikitsa_entry.delete(0,'end')
        messagebox.showinfo("status","Patient Record is Saved..")

def update():
    pid = pId_entry.get()
    pname = pName_entry.get()
    pno = pNo_entry.get()
    filename = fName_entry.get()
    address = add_entry.get()
    complaint = complaints_entry.get()
    chik = chikitsa_entry.get()
    if (pid == "" or pname == "" or pno == "" or filename == "" or address == "" or complaint == "" or chik==""):
        messagebox.showinfo("Status", "All Fields are required..!")
    else:
        c.execute("UPDATE patient_database SET PNAME=?,PNO=?,FILENAME=?,PADDRESS=?,PCOMPLAINTS=?,CHIKITSA=? WHERE PID=?",(pname,pno,filename,address,complaint,chik,pid))
        con.commit()
        pId_entry.delete(0, 'end')
        pName_entry.delete(0, 'end')
        pNo_entry.delete(0, 'end')
        fName_entry.delete(0, 'end')
        add_entry.delete(0, 'end')
        complaints_entry.delete(0, 'end')
        chikitsa_entry.delete(0, 'end')
        messagebox.showinfo("status", "Patient Record is Updated..")

def delete():
    pid = pId_entry.get()
    if (pid==""):
        messagebox.showinfo("Status","Please Enter the Patient ID")
    else:
        c.execute("DELETE FROM patient_database WHERE PID=?",(pid))
        con.commit()
        pId_entry.delete(0, 'end')
        pName_entry.delete(0, 'end')
        pNo_entry.delete(0, 'end')
        fName_entry.delete(0, 'end')
        add_entry.delete(0, 'end')
        complaints_entry.delete(0, 'end')
        chikitsa_entry.delete(0, 'end')
        messagebox.showinfo("status", "Patient Record is Deleted..")

def get():
    pid = pId_entry.get()
    pname = pName_entry.get()
    if (pId_entry.get() == ""):
        messagebox.showinfo("Status", "Please enter patient ID!")
    else:
        c.execute("SELECT * FROM patient_database WHERE PID=?",(pid))
        rows = c.fetchall()
        con.commit()
        for i in rows:
            pName_entry.insert(0,i[1])
            pNo_entry.insert(0,i[2])
            fName_entry.insert(0,i[3])
            add_entry.insert(0,i[4])
            complaints_entry.insert(0,i[5])
            chikitsa_entry.insert(0, i[6])

def clear():
    pId_entry.delete(0, 'end')
    pName_entry.delete(0, 'end')
    pNo_entry.delete(0, 'end')
    fName_entry.delete(0, 'end')
    add_entry.delete(0, 'end')
    complaints_entry.delete(0, 'end')
    chikitsa_entry.delete(0, 'end')

def viewdb():
    c.execute("SELECT * FROM patient_database")
    rows=c.fetchall()
    con.commit()
    for row in rows:
        tv.insert('','end',values=row)
def refresh():
    tv.delete(*tv.get_children())
    c.execute("SELECT * FROM patient_database")
    rows = c.fetchall()
    con.commit()
    for row in rows:
        tv.insert('', 'end', values=row)

root = Tk()
root.title("Patient Record Management system")
root.geometry("1180x660")
root.minsize(340, 240)
#root.iconbitmap('window.ico')

f1 = Frame(root, borderwidth=9, relief=SUNKEN)
f1.pack(side=TOP , fill=X)
l1 = Label(f1, text="Aatnam Panchkarm Chikitsalay ", font="lucida 22 bold")
l1.pack(padx=10, pady=10)

f2 = Frame(root, borderwidth=5 ,  relief=SUNKEN)
f2.pack(anchor=NW,padx=10, pady=10)

f3 = Frame(root, borderwidth=5 , relief=GROOVE)
f3.pack(side=BOTTOM, fill=X)

b6 =Button(root, text="REFRESH", command= refresh, font="lucida 11 bold ")
b6.place(x=800,y=92)
listlabel=Label(root, text="Patients Record:", font="lucida 12 bold")
la=Label(root, text="(please click on REFRESH button after saving record)",font="lucida 9 bold")
listlabel.place(x=430,y=90)
la.place(x=430,y=110)

f6 = Frame(root, borderwidth=5 ,  relief=SUNKEN)
f6.place(x=430,y=130)
tv=ttk.Treeview(f6,columns=(1,2,3,4,5,6,7),show="headings",height=15)
tv.pack()
viewdb()
vscrollbar=ttk.Scrollbar(f6,orient=VERTICAL,command=tv.yview)
vscrollbar.pack(side=RIGHT, fill=Y)
tv.configure(yscroll=vscrollbar.set)
tv.heading(1,text="Patient ID")
tv.heading(2,text="Patient Name")
tv.heading(3,text="Patient NO")
tv.heading(4,text="Patient File No")
tv.heading(5,text="Patient Add")
tv.heading(6,text="Patient complaints")
tv.heading(7,text="Chikitsa")
tv.column(1,width=50, minwidth=60)
tv.column(2,width=100, minwidth=150)
tv.column(3,width=70, minwidth=80)
tv.column(4,width=80, minwidth=90)
tv.column(5,width=150, minwidth=200)
tv.column(6,width=200, minwidth=250)
tv.column(7,width=200, minwidth=250)

hscrollbar=ttk.Scrollbar(f6,orient=HORIZONTAL,command=tv.xview)
tv.configure(xscroll=hscrollbar.set)
hscrollbar.pack(side=BOTTOM,fill=X)

statusvar =StringVar()
statusvar.set("ABOUT US: ********* \n ADDRESS: *************** \n\n © :Rupesh Neve")
sbar=Label(f3, textvariable=statusvar, relief=GROOVE)
sbar.pack(side=BOTTOM, fill=X)

pId=Label(f2, font="lucida 11 bold ",text="Patient Id")
pName=Label(f2,font="lucida 11 bold ", text="Patient Name")
pNo=Label(f2,font="lucida 11 bold ", text="Patient number")
fName=Label(f2,font="lucida 11 bold ", text="File Name")
add=Label(f2,font="lucida 11 bold ", text="Patient Address")
complaints=Label(f2,font="lucida 11 bold ", text="Patient Major Complaints")
chikitsa=Label(f2,font="lucida 11 bold ", text="Chikitsa")
warning=Label(f2, font="lucida 9 bold", text="(Please Enter unique Patient Id for each patient.\n To search patient provide only Patient Id )")


pId.grid(row=0,column=0)
pName.grid(row=1,column=0)
pNo.grid(row=2,column=0)
fName.grid(row=3,column=0)
add.grid(row=4,column=0)
complaints.grid(row=5,column=0)
chikitsa.grid(row=6,column=0)
warning.grid(row=7,column=0)

pId_value=IntVar()
pName_value=StringVar()
pNo_value=StringVar()
fName_value=StringVar()
add_value=StringVar()
complaints_value=StringVar()
chikitsa_value=StringVar()

pId_entry=Entry(f2, textvariable=pId_value)
pName_entry=Entry(f2, textvariable=pName_value)
pNo_entry=Entry(f2, textvariable=pNo_value)
fName_entry=Entry(f2, textvariable=fName_value)
add_entry=Entry(f2, textvariable=add_value)
complaints_entry=Entry(f2, textvariable=complaints_value)
chikitsa_entry = Entry(f2, textvariable=chikitsa_value)

pId_entry.grid(row =0, column =1, pady=3, ipady= 3 , ipadx= 3)
pName_entry.grid(row =1, column =1, pady=3, ipady= 3 , ipadx= 3)
pNo_entry.grid(row = 2, column =1, pady=3, ipady= 3 , ipadx= 3)
fName_entry.grid(row =3 , column =1, pady=3, ipady= 3 , ipadx= 3)
add_entry.grid(row = 4, column =1, pady=3, ipady= 3 , ipadx= 3)
complaints_entry.grid(row =5, column =1 , ipady= 5 , ipadx= 5)
chikitsa_entry.grid(row =6, column =1 , ipady= 5 , ipadx= 5)

b1 =Button(f2, text="SAVE", command= insert, font="lucida 11 bold ")
b2 =Button(f2, text="UPDATE", command= update, font="lucida 11 bold ")
b3 =Button(f2, text="DELETE", command= delete, font="lucida 11 bold ")
b4 =Button(f2, text="SEARCH", command= get, font="lucida 11 bold ")
clr =Button(f2, text="CLEAR", command= clear, font="lucida 11 bold ")



b1.grid(row=8,column=0,padx=(10, 100))
b2.grid(row=9,column=0,padx=(10, 100))
b3.grid(row=10,column=0,padx=(10, 100))
b4.grid(row=11,column=0,padx=(10, 100))
clr.grid(row=12,column=0,padx=(10, 100))

root.mainloop()