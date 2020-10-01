from tkinter import *
from tkinter import ttk
import pymysql
class Service:
    def __init__(self,root):
        self.root=root
        self.root.title("Service module")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="Manage Service",bd=10,font="TrebuchetMS 30 bold",bg="gold",fg="white")
        title.pack(side=TOP,fill=X)


        # +++++++++++++++++++Variables setting+++++++++++++++++++++
        self.id_var = StringVar()
        self.name_var=StringVar()
        self.contact_var=StringVar()
        self.machine_var=StringVar()
        self.servicedate_var=StringVar()
        self.service_var=StringVar()

        #++++++++++++++++++++Manage Frame+++++++++++++++++++
        Manage_frame=Frame(self.root,bd=4,relief=RIDGE)
        Manage_frame.place(x=20,y=90,width=400,height=600)

        Manage_frame_name = Frame(self.root, bd=4, relief=RIDGE)
        Manage_frame_name.place(x=20, y=700, width=1000, height=50)

        name_label=Label(Manage_frame_name,text="Project by : Ashutosh S Kumbhar,Sudhansh Jawale,Girish Nalawade,Omkar Patil,Suyash Mate",font="TrebuchetMS 20 bold",bg="gold",fg="black")
        name_label.pack()



        manage_title=Label(Manage_frame,text="Fill Information",bd=10,font="TrebuchetMS 20 bold",bg="gold",fg="black")
        manage_title.grid(row=0,columnspan=2,padx=40,pady=10)

        Service_id=Label(Manage_frame,text="Service ID",bd=10,font="TrebuchetMS 15 bold",bg="gold",fg="white")
        Service_id.grid(row=1,column=0,pady=7,padx=0,sticky="w")

        Service_id_entry=Entry(Manage_frame,textvariable=self.id_var,font="TrebuchetMS 20 bold")
        Service_id_entry.grid(row=1, column=1, pady=7, padx=5)

        Customer_name = Label(Manage_frame, text="Customer Name", bd=10, font="TrebuchetMS 15 bold", bg="gold", fg="white")
        Customer_name.grid(row=2, column=0, pady=7, padx=0, sticky="w")

        Customer_name_entry = Entry(Manage_frame,textvariable=self.name_var, font="TrebuchetMS 20 bold")
        Customer_name_entry.grid(row=2, column=1, pady=7, padx=5)

        Customer_contact = Label(Manage_frame, text="Contact no", bd=10, font="TrebuchetMS 15 bold", bg="gold",fg="white")
        Customer_contact.grid(row=3, column=0, pady=7, padx=0, sticky="w")

        Customer_contact_entry = Entry(Manage_frame,textvariable=self.contact_var, font="TrebuchetMS 20 bold")
        Customer_contact_entry.grid(row=3, column=1, pady=7, padx=5)

        Machine_Name = Label(Manage_frame, text="Machine Name", bd=10, font="TrebuchetMS 15 bold", bg="gold",fg="white")
        Machine_Name.grid(row=4, column=0, pady=7, padx=0, sticky="w")

        Machine_Name_entry = Entry(Manage_frame,textvariable=self.machine_var, font="TrebuchetMS 20 bold")
        Machine_Name_entry.grid(row=4, column=1, pady=7, padx=5)

        Customer_service_date = Label(Manage_frame, text="Last Serviced", bd=10, font="TrebuchetMS 15 bold", bg="gold", fg="white")
        Customer_service_date.grid(row=5, column=0, pady=7, padx=0, sticky="w")

        Customer_service_date_entry = Entry(Manage_frame,textvariable=self.servicedate_var, font="TrebuchetMS 20 bold")
        Customer_service_date_entry.grid(row=5, column=1, pady=7, padx=5)

        Customer_service = Label(Manage_frame, text="What Serviced?", bd=10, font="TrebuchetMS 15 bold", bg="gold",fg="white")
        Customer_service.grid(row=6, column=0, pady=7, padx=0, sticky="w")

        Customer_service_entry= Entry(Manage_frame,textvariable=self.service_var, font="TrebuchetMS 20 bold")
        Customer_service_entry.grid(row=6, column=1, pady=7, padx=5)

        #+++++++++++++++++++++++++++++++++++++button Frame++++++++++++++++
        btn_frame=Frame(Manage_frame)
        btn_frame.place(x=10,y=450,width=350)

        Add_btn=Button(btn_frame,text="Add",font="TrebuchetMS 15 bold",fg="gold",command=self.add_data)
        Add_btn.grid(row=0,column=0,padx=2,ipadx=15,ipady=20)

        update_btn = Button(btn_frame,command=self.update_data, text="Update",font="TrebuchetMS 15 bold",fg="gold")
        update_btn.grid(row=0, column=1, padx=2, ipadx=15, ipady=20)

        delete_btn = Button(btn_frame,command=self.delete_data, text="Delete",font="TrebuchetMS 15 bold",fg="gold")
        delete_btn.grid(row=0, column=2, padx=2, ipadx=15, ipady=20)

        clear_btn = Button(btn_frame,command=self.clear, text="Clear",font="TrebuchetMS 15 bold",fg="gold")
        clear_btn.grid(row=0, column=3, padx=2, ipadx=15, ipady=20)

        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        Detail_frame=Frame(self.root,bd=4,relief=RIDGE)
        Detail_frame.place(x=450,y=90,width=900,height=600)

        search_label = Label(Detail_frame, text="Search By", bd=10, font="TrebuchetMS 15 bold", bg="gold", fg="black")
        search_label.grid(row=0, columnspan=2, padx=40, pady=10)

        combo_search = ttk.Combobox(Detail_frame, font="TrebuchetMS 20 bold", state="readonly", width=10)
        combo_search['values'] = ["Company name", "Machines", "Serviced Date"]
        combo_search.grid(row=0,column=2,pady=10)

        Search_entry = Entry(Detail_frame, font="TrebuchetMS 20 bold")
        Search_entry.grid(row=0, column=3, pady=7, padx=5)

        search_btn = Button(Detail_frame, text="Search", font="TrebuchetMS 15 bold", fg="gold")
        search_btn.grid(row=0, column=4, padx=2, ipadx=10, ipady=10)

        showall_btn = Button(Detail_frame, text="ShowAll", font="TrebuchetMS 15 bold", fg="gold")
        showall_btn.grid(row=0, column=5, padx=2, ipadx=10, ipady=10)

        #++++++++++++++++Table data+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        table_frame = Frame(Detail_frame, bd=4, relief=RIDGE)
        table_frame.place(x=10,y=70,width=800,height=500)

        scroll_bar_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_bar_y = Scrollbar(table_frame, orient=VERTICAL)
        self.data_table = ttk.Treeview(table_frame, columns=("id", "Company_Name", "Contact_no", "Machine_Name", "Last_Serviced", "Service_Done"),xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y)
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)
        scroll_bar_x.config(command=self.data_table.xview)
        scroll_bar_y.config(command=self.data_table.yview)
        self.data_table.heading("id", text="Service id")
        self.data_table.heading("Company_Name", text="Name")
        self.data_table.heading("Contact_no", text="Contact")
        self.data_table.heading("Machine_Name", text="Machine")
        self.data_table.heading("Last_Serviced", text="Service Date")
        self.data_table.heading("Service_Done", text="Serviced")
        self.data_table["show"] = "headings"
        self.data_table.column("id", width=30)
        self.data_table.column("Company_Name",width=100 )
        self.data_table.column("Contact_no", width=100)
        self.data_table.column("Machine_Name", width=100)
        self.data_table.column("Last_Serviced",width=100 )
        self.data_table.column("Service_Done", width=100)
        self.data_table.pack(fill=BOTH,expand=1)
        self.data_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_data(self):
        con=pymysql.connect(host="192.168.64.2",user="root",password="password",database='serv')
        cur=con.cursor()
        cur.execute("insert into customers values(%s,%s,%s,%s,%s,%s)",(self.id_var.get(),
                                                                       self.name_var.get(),
                                                                       self.contact_var.get(),
                                                                       self.machine_var.get(),
                                                                       self.servicedate_var.get(),
                                                                       self.service_var.get()
                                                                       ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def fetch_data(self):
        con=pymysql.connect(host="192.168.64.2",user="root",password="password",database='serv')
        cur = con.cursor()
        cur.execute("select * from customers")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.data_table.delete(*self.data_table.get_children())
            for row in rows:
                self.data_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.id_var.set("")
        self.name_var.set("")
        self.contact_var.set("")
        self.machine_var.set("")
        self.servicedate_var.set("")
        self.service_var.set("")
    def get_cursor(self,ev):
        cursor_row=self.data_table.focus()
        contents=self.data_table.item(cursor_row)
        row=contents['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.contact_var.set(row[2])
        self.machine_var.set(row[3])
        self.servicedate_var.set(row[4])
        self.service_var.set(row[5])
    def update_data(self):
        con = pymysql.connect(host="192.168.64.2", user="root", password="password", database='serv')
        cur = con.cursor()
        cur.execute("update customers set name=%s,contact=%s,machine=%s,date=%s,service=%s where id=%s",(
                                                                        self.name_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.machine_var.get(),
                                                                        self.servicedate_var.get(),
                                                                        self.service_var.get(),
                                                                        self.id_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="192.168.64.2", user="root", password="password", database='serv')
        cur = con.cursor()
        cur.execute("delete * from customers where id=%s",self.id_var.get())
        con.commit()
        con.close()

        nameframe = Frame(self.root)
        nameframe.pack(side=BOTTOM)
        labelnames=Label(nameframe,text="project by :-Ashutosh kumbhar,Sudhansh javale")
        labelnames.pack()





root=Tk()
ob=Service(root)
root.mainloop()