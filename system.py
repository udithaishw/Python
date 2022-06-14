from tkinter import*
from tkinter import messagebox,ttk
import pymysql
import time

class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Emplyer Payrol Management Sytem | Developed By Uditha Ishara ")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Employer Payrol Management System",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.root,text="All Emplyees",command=self.employee_frame,font=("times new roman",13),bg="Gray",fg="White").place(x=1100,y=11,height=30,width=120)
       
        #========================frame1======================
        #=======================Veriables====================
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_dob=StringVar()
        self.var_name=StringVar()
        self.var_doj=StringVar()
        self.var_age=StringVar()
        self.var_experience=StringVar()
        self.var_gender=StringVar()
        self.var_proof=StringVar()  ###Adhaar Card
        self.var_email=StringVar()   
        self.var_contact=StringVar()
        self.var_hired=StringVar()
        self.var_status=StringVar()
        
        
        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=750,height=620)
        title2=Label(Frame1,text="Employer Details",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_code=Label(Frame1,text="Employer code",font=("times new roman",20),bg="white",fg="black",).place(x=10,y=70)
        self.txt_code=Entry(Frame1,font=("times new roman",15),textvariable=self.var_emp_code,bg="lightyellow",fg="black",)
        self.txt_code.place(x=200,y=74,width=200)
        btn_search=Button(Frame1,text="Search",command=self.search,font=("times new roman",20),bg="gray",fg="black",).place(x=440,y=72,height=30)
 

        #======Row1=====
        lbl_designation=Label(Frame1,text="Designation",font=("times new roman",20),bg="white",fg="black",).place(x=10,y=120)
        txt_designation=Entry(Frame1,font=("times new roman",15),textvariable=self.var_designation,bg="lightyellow",fg="black",).place(x=170,y=125,width=200)
        lbl_dob=Label(Frame1,text="D.O.B",font=("times new roman",20),bg="white",fg="black",).place(x=390,y=120)
        txt_dob=Entry(Frame1,font=("times new roman",15),textvariable=self.var_dob,bg="lightyellow",fg="black",).place(x=520,y=125)

        #======Row2=======
        lbl_name=Label(Frame1,text="Name",font=("times new roman",20),bg="white",fg="black",).place(x=10,y=170)
        txt_name=Entry(Frame1,font=("times new roman",15),textvariable=self.var_name,bg="lightyellow",fg="black",).place(x=170,y=175,width=200)
        lbl_doj=Label(Frame1,text="D.O.J",font=("times new roman",20),bg="white",fg="black",).place(x=390,y=170)
        txt_doj=Entry(Frame1,font=("times new roman",15),textvariable=self.var_doj,bg="lightyellow",fg="black",).place(x=520,y=175)

        #======Row3========
        lbl_age=Label(Frame1,text="Age",font=("times new roman",20),bg="white",fg="black",).place(x=10,y=220)
        txt_age=Entry(Frame1,font=("times new roman",15),textvariable=self.var_age,bg="lightyellow",fg="black",).place(x=170,y=225,width=200)
        lbl_experience=Label(Frame1,text="Experience",font=("times new roman",19),bg="white",fg="black",).place(x=390,y=220)
        txt_experience=Entry(Frame1,font=("times new roman",15),textvariable=self.var_experience,bg="lightyellow",fg="black",).place(x=520,y=225)
       
        #======Row4========
        lbl_gender=Label(Frame1,text="Gender",font=("times new roman",20),bg="white",fg="black",).place(x=10,y=270)
        txt_gender=Entry(Frame1,font=("times new roman",15),textvariable=self.var_gender,bg="lightyellow",fg="black",).place(x=170,y=275,width=200)
        lbl_proof=Label(Frame1,text="Proof ID",font=("times new roman",20),bg="white",fg="black",).place(x=390,y=270)
        txt_proof=Entry(Frame1,font=("times new roman",15),textvariable=self.var_proof,bg="lightyellow",fg="black",).place(x=520,y=275)
              
        #======Row5=========
        lbl_email=Label(Frame1,text="Email",font=("times new roman",20),bg="white",fg="black",).place(x=10,y=320)
        txt_email=Entry(Frame1,font=("times new roman",15),textvariable=self.var_email,bg="lightyellow",fg="black",).place(x=170,y=325,width=200)
        lbl_contact=Label(Frame1,text="Contact",font=("times new roman",20),bg="white",fg="black",).place(x=390,y=320)
        txt_contact=Entry(Frame1,font=("times new roman",15),textvariable=self.var_contact,bg="lightyellow",fg="black",).place(x=520,y=325)

        #======Row6=========
        lbl_hired=Label(Frame1,text="Hired Location",font=("times new roman",17),bg="white",fg="black",).place(x=10,y=372)
        txt_hired=Entry(Frame1,font=("times new roman",15),textvariable=self.var_hired,bg="lightyellow",fg="black",).place(x=170,y=375,width=200)
        lbl_status=Label(Frame1,text="Status",font=("times new roman",20),bg="white",fg="black",).place(x=390,y=370)
        txt_status=Entry(Frame1,font=("times new roman",15,),textvariable=self.var_status,bg="lightyellow",fg="black",).place(x=520,y=375)
        
        #======Row7=========
        lbl_address=Label(Frame1,text="Address",font=("times new roman",17),bg="white",fg="black",).place(x=10,y=422)
        self.txt_address=Text(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",)
        self.txt_address.place(x=170,y=425,width=550,height=150)
  



        #=========================frame2======================
        #========================Veriables====================
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_days=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_salary=StringVar()
        self.var_netsalary=StringVar()
        self.var_allowance=StringVar()
        self.var_ot=StringVar() 


        Frame2 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame2.place(x=770, y=70, width=580, height=300)

        title3=Label(Frame2,text="Employer Salary Details",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_month=Label(Frame2,text="Month",font=("times new roman",18),bg="white",fg="black",).place(x=10,y=60)
        txt_month=Entry(Frame2,font=("times new roman",15),textvariable=self.var_month,bg="lightyellow",fg="black",).place(x=90,y=62,width=100)
       
        lbl_year=Label(Frame2,text="Year",font=("times new roman",18),bg="white",fg="black",).place(x=210,y=60)
        txt_year=Entry(Frame2,font=("times new roman",15),textvariable=self.var_year,bg="lightyellow",fg="black",).place(x=270,y=62,width=100)
       
        lbl_salary=Label(Frame2,text="Salary",font=("times new roman",18),bg="white",fg="black",).place(x=380,y=60)
        txt_salary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_salary,bg="lightyellow",fg="black",).place(x=455,y=62,width=100)
       

        #======Row1===============
        lbl_days=Label(Frame2,text="Total Days",font=("times new roman",15),bg="white",fg="black",).place(x=10,y=120)
        txt_days=Entry(Frame2,font=("times new roman",15),textvariable=self.var_days,bg="lightyellow",fg="black",).place(x=170,y=125,width=100)
        lbl_adsent=Label(Frame2,text="Absents",font=("times new roman",15),bg="white",fg="black",).place(x=300,y=120)
        txt_absent=Entry(Frame2,font=("times new roman",15),textvariable=self.var_absent,bg="lightyellow",fg="black",).place(x=400,y=125,width=120)

        #======Row2===============
        lbl_medical=Label(Frame2,text="Medical",font=("times new roman",15),bg="white",fg="black",).place(x=10,y=150)
        txt_medical=Entry(Frame2,font=("times new roman",15),textvariable=self.var_medical,bg="lightyellow",fg="black",).place(x=170,y=155,width=100)
        lbl_pf=Label(Frame2,text="PF",font=("times new roman",15),bg="white",fg="black",).place(x=300,y=150)
        txt_pf=Entry(Frame2,font=("times new roman",15),textvariable=self.var_pf,bg="lightyellow",fg="black",).place(x=400,y=155,width=120)

        #======Row3===============
        lbl_convence=Label(Frame2,text="Convence",font=("times new roman",15,),bg="white",fg="black",).place(x=10,y=180)
        txt_convence=Entry(Frame2,font=("times new roman",15),textvariable=self.var_convence,bg="lightyellow",fg="black",).place(x=170,y=185,width=100)
        lbl_ot=Label(Frame2,text="OT",font=("times new roman",15),bg="white",fg="black",).place(x=300,y=180)
        txt_ot=Entry(Frame2,font=("times new roman",15),textvariable=self.var_ot,bg="lightyellow",fg="black",).place(x=400,y=185,width=120)

        #======Row4================

        lbl_allownce=Label(Frame2,text="Allowance",font=("times new roman",15),bg="white",fg="black",).place(x=10,y=210)
        txt_allownce=Entry(Frame2,font=("times new roman",15),textvariable=self.var_allowance,bg="lightyellow",fg="black",).place(x=170,y=215,width=100)
        lbl_netsalary=Label(Frame2,text="Net Salary",font=("times new roman",15),bg="white",fg="black",).place(x=300,y=210)
        txt_netsalary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_netsalary,bg="lightgray",fg="black",).place(x=400,y=215,width=120)

        btn_calcuate=Button(Frame2,text="Calcuate",command=self.calculate,font=("times new roman",15),bg="Orange",fg="black",).place(x=10,y=260,height=25,width=90)

        self.btn_update=Button(Frame2,text="Update",state=DISABLED,command=self.update,font=("times new roman",15),bg="lightblue",fg="black",)
        self.btn_update.place(x=120,y=260,height=25,width=90)

        self.btn_save=Button(Frame2,text="Save",command=self.add,font=("times new roman",15),bg="Green",fg="white",)
        self.btn_save.place(x=230,y=260,height=25,width=90)

        btn_clear=Button(Frame2,text="Clear",command=self.clear,font=("times new roman",15),bg="gray",fg="black",).place(x=450,y=260,height=25,width=90)

        self.btn_delete=Button(Frame2,text="Delete",state=DISABLED,command=self.delete,font=("times new roman",15),bg="red",fg="white",)
        self.btn_delete.place(x=340,y=260,height=25,width=90)
        
       
 



        #========================frame3=========================
        Frame3 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame3.place(x=770, y=380, width=580, height=310)
    

        #================Calcaulator Frame===================
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
            print(num)
        
        
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''

        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''

    
        Cal_Frame=Frame(Frame3,bg="white",bd="2",relief=RIDGE)
        Cal_Frame.place(x=2,y=2,width=245,height=300)

        txt_Result=Entry(Cal_Frame,bg='lightyellow',textvariable=self.var_txt,font=("times new roman",20,"bold"),justify=RIGHT).place(x=0,y=0,relwidth=1,height=50)
        

        #=======================row1
        btn_7=Button(Cal_Frame,text="7",command=lambda:btn_click(7),font=("times new roman",15)).place(x=0,y=52,w=60,h=60)
        btn_8=Button(Cal_Frame,text="8",command=lambda:btn_click(8),font=("times new roman",15,)).place(x=61,y=52,w=60,h=60)
        btn_9=Button(Cal_Frame,text="9",command=lambda:btn_click(9),font=("times new roman",15)).place(x=122,y=52,w=60,h=60)
        btn_div=Button(Cal_Frame,text="/",command=lambda:btn_click('/'),font=("times new roman",15)).place(x=183,y=52,w=60,h=60)

        #=======================row2
        btn_4=Button(Cal_Frame,text="4",command=lambda:btn_click(4),font=("times new roman",15)).place(x=0,y=112,w=60,h=60)
        btn_5=Button(Cal_Frame,text="5",command=lambda:btn_click(5),font=("times new roman",15)).place(x=61,y=112,w=60,h=60)
        btn_6=Button(Cal_Frame,text="6",command=lambda:btn_click(6),font=("times new roman",15)).place(x=122,y=112,w=60,h=60)
        btn_mul=Button(Cal_Frame,text="*",command=lambda:btn_click('*'),font=("times new roman",15)).place(x=183,y=112,w=60,h=60)

        #=======================row3
        btn_1=Button(Cal_Frame,text="1",command=lambda:btn_click(1),font=("times new roman",15)).place(x=0,y=172,w=60,h=60)
        btn_2=Button(Cal_Frame,text="2",command=lambda:btn_click(2),font=("times new roman",15)).place(x=61,y=172,w=60,h=60)
        btn_3=Button(Cal_Frame,text="3",command=lambda:btn_click(3),font=("times new roman",15)).place(x=122,y=172,w=60,h=60)
        btn_min=Button(Cal_Frame,text="-",command=lambda:btn_click('-'),font=("times new roman",15)).place(x=183,y=172,w=60,h=60)
    
        #=======================row3
        btn_0=Button(Cal_Frame,text="0",command=lambda:btn_click(0),font=("times new roman",15)).place(x=0,y=233,w=60,h=60)
        btn_dot=Button(Cal_Frame,text="C",command=clear_cal,font=("times new roman",15)).place(x=61,y=233,w=60,h=60)
        btn_sum=Button(Cal_Frame,text="+",command=lambda:btn_click('+'),font=("times new roman",15)).place(x=122,y=233,w=60,h=60)
        btn_equal=Button(Cal_Frame,text="=",command=result,font=("times new roman",15)).place(x=183,y=233,w=60,h=60)
    
        #================SALLARY Frame====================
        sal_frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_frame.place(x=251,y=2,width=320,height=300)
        title_sal=Label(sal_frame,text="Pay Slip",font=("times new roman",18),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)


        sal_frame2=Frame(sal_frame,bg="white",bd=2,relief=RIDGE)
        sal_frame2.place(x=0,y=30,relwidth=1,height=230)

        self.sample=f'''\tJayanthaa Electricals\n\t       Pannipitiya\n\t         Kottawa
________________________________

Emplyee ID\t\t:  
Salary of\t\t:  Mon-YYYY
Generated on\t\t:  DD-MM-YYYY
________________________________

Total Worked Days\t\t: DD
Total Present\t\t : DD
Total Absent\t\t : DD
Convence\t\t : Rs.-------
Medical\t\t : Rs.-------
Pf\t\t : Rs.-------
Gross Payment\t\t : Rs.------------
Net Sallary\t\t : Rs.--------------
_______________________________

This is Computer generated slip,
not required any Signature.'''

        scroll_y=Scrollbar(sal_frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_recipt=Text(sal_frame2,font=("time new roman",13
        ),bg='lightyellow',yscrollcommand=scroll_y.set)

        self.txt_salary_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)
        self.txt_salary_recipt.insert(END,self.sample)

        
        btn_print=Button(sal_frame,text="Print",font=("times new roman",15),bg="Lightblue",fg="black",).place(x=180,y=263,height=30,width=120)

        self.check_connection()
     
        #============All Function Started=====================================================================
    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)

        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')             
        self.var_hired.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_experience.set('')
        self.var_proof.set('')
        self.var_contact.set('')
        self.var_status.set('')
        self.txt_address.delete('1.0',END)   

        self.var_month.set('')
        self.var_year.set('')
        self.var_salary.set('')
        self.var_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_allowance.set('')
        self.var_ot.set('')
        self.var_netsalary.set('')
        self.txt_salary_recipt.delete('1.0',END)
        self.txt_salary_recipt.insert(END,self.sample)
  
    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror('Error',"Emplyee ID must be required")
        else:

            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where emp_code=%s",(self.var_emp_code.get()))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID, Please try with another employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:                    
                        cur.execute("delete from emp_salary where emp_code=%s",(self.var_emp_code.get()))
                        con.commit()
                        con.close()  
                        messagebox.showinfo("Delete","Employee Record Deleted Successfuly",parent=self.root)             
                        self.clear()
            except Exception as ex:
                    messagebox.showerror("Error",f'Error due to: {str(ex)}')
                    

    def search(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary where emp_code=%s",(self.var_emp_code.get()))
            row=cur.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid Employee ID, Please try with another employee ID",parent=self.root)
            else:
                print(row)
                self.var_emp_code.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])             
                self.var_hired.set(row[6])
                self.var_doj.set(row[7])
                self.var_dob.set(row[8])
                self.var_experience.set(row[9])
                self.var_proof.set(row[10])
                self.var_contact.set(row[11])
                self.var_status.set(row[12])
                self.txt_address.delete('1.0',END) 
                self.txt_address.insert(END,row[13])      
                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_salary.set(row[16])
                self.var_days.set(row[17])
                self.var_absent.set(row[18])
                self.var_medical.set(row[19])
                self.var_pf.set(row[20])
                self.var_convence.set(row[21])
                self.var_allowance.set(row[22])
                self.var_ot.set(row[23])
                self.var_netsalary.set(row[24])

                file_=open('Pay_Slips/'+str(row[25]),'r')
                self.txt_salary_recipt.delete('1.0',END)
                for i in file_:
                    self.txt_salary_recipt.insert(END,i)
                file_.close()
                self.btn_save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_code.config(state='readonly')




                        

        except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
            

    def update(self):
        if self.var_emp_code.get()=='' or self.var_netsalary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee details are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where emp_code=%s",(self.var_emp_code.get()))
                row=cur.fetchone() 
                if row==None:
                    messagebox.showerror("Error","This Emplyee ID is Invalid,try again with Valid ID",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hired`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`salary`=%s,`days`=%s,`absent`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`allowance`=%s,`ot`=%s,`net_salary`=%s,`pay_slip`=%s WHERE `emp_code`=%s",
                    (                   
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),             
                        self.var_hired.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof.get(),
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0',END),         
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_allowance.get(),
                        self.var_ot.get(),
                        self.var_netsalary.get(),
                        self.var_emp_code.get()+".txt",
                        self.var_emp_code.get()

                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('Pay_Slips/'+str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.txt_salary_recipt.get('1.0',END))
                    file_.close
                    messagebox.showinfo("Success","Record Updated Successfully")


            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')



    def add(self):
        if self.var_emp_code.get()=='' or self.var_netsalary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee details are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where emp_code=%s",(self.var_emp_code.get()))
                row=cur.fetchone() 
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","This Emplyee ID has alreday available in our database,try again with another ID",parent=self.root)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_emp_code.get(),
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),             
                        self.var_hired.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof.get(),
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0',END),         
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_days.get(),
                        self.var_absent.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_allowance.get(),
                        self.var_ot.get(),
                        self.var_netsalary.get(),
                        self.var_emp_code.get()+".txt"

                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('Pay_Slips/'+str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.txt_salary_recipt.get('1.0',END))
                    file_.close
                    messagebox.showinfo("Success","Record Added Successfully")


            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
            

    def calculate(self):
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_days.get()==''or self.var_convence.get()=='' or self.var_salary.get()=='' :
            messagebox.showerror("Error","All Fileds as are required")
        else:
            # self.var_net_salary.set("RESULT")
            # 35000/31==1752
            # 31-10=21*1752
            per_day=int(self.var_salary.get())/int(self.var_days.get())
            work_day=int(self.var_days.get())-int(self.var_absent.get())
            sal_=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convence.get())+int(self.var_allowance.get())
            net_sal=sal_-deduct+addition
            self.var_netsalary.set(str(round(net_sal,2)))

            #===================Update Slip========================
            new_sample=f'''\tJayanthaa Electricals\n\t       Pannipitiya\n\t         Kottawa
_______________________________

Emplyee ID\t\t:  {self.var_emp_code.get()}
Salary of\t\t:  {self.var_month.get()}-{self.var_year.get()}
Generated on\t\t:  {str(time.strftime("%d-%m-%Y"))}
________________________________

Total Worked Days\t\t: {self.var_days.get()}
Total Present\t\t : {str(int(self.var_days.get())-int(self.var_absent.get()))}
Total Absent\t\t : {self.var_absent.get()}
Convence\t\t : Rs.{self.var_convence.get()}
Medical\t\t : Rs.{self.var_medical.get()}
Pf\t\t : Rs.{self.var_pf.get()}
Gross Payment\t\t : Rs.{self.var_salary.get()}
Net Sallary\t\t : Rs.{self.var_netsalary.get()}
_______________________________

This is Computer generated slip,
not required any Signature
'''
            self.txt_salary_recipt.delete('1.0',END)
            self.txt_salary_recipt.insert(END,new_sample)

    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            print(rows)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')
    
    def employee_frame(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Emplyer Payrol Management Sytem | Developed By Uditha Ishara ")
        self.root2.geometry("1000x500+120+100")
        self.root2.config(bg="white")
        title=Label(self.root2,text="All Emplyees",font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor="w",padx=10).pack(side=TOP,fill=X)
        self.root2.focus_force()

        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=RIGHT,fill=X)

        self.employee_tree=ttk.Treeview(self.root2,columns=('emp_code', 'designation', 'name', 'age', 'gender', 'email', 'hired', 'doj', 'dob', 'experience', 'proof', 'contact', 'status', 'address', 'month', 'year', 'salary', 'days', 'absent', 'medical', 'pf', 'convence', 'allowance', 'ot', 'net_salary', 'pay_slip'))
        self.employee_tree.heading('emp_code',text='Employee Num')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('hired',text='Hired Location')
        self.employee_tree.heading('doj',text='DOJ')
        self.employee_tree.heading('dob',text='DOB')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('proof',text='Proof ID')
        self.employee_tree.heading('contact',text='Contact')
        self.employee_tree.heading('satus',text='Status')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('salary',text='Basic Sallary')
        self.employee_tree.heading('days',text='Total Days')
        self.employee_tree.heading('absent',text='Absent Days')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='PF')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('allowance',text='Allowance')
        self.employee_tree.heading('ot',text='OT')
        self.employee_tree.heading('net_salary',text='Net Sallary')
        self.employee_tree.heading('pay_slip',text='Pay Slip')
        self.employee_tree['show']='headings'

        self.employee_tree.column('emp_code',width=100)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hired',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof',width=200)
        self.employee_tree.column('contact',width=500)
        self.employee_tree.column('satus',width=100)
        self.employee_tree.column('address',width=200)
        self.employee_tree.column('month',width=200)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('salary',width=100)
        self.employee_tree.column('days',width=100)
        self.employee_tree.column('absent',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=500)
        self.employee_tree.column('allowance',width=500)
        self.employee_tree.column('ot',width=500)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('pay_slip',width=100)
        self.employee_tree.pack(fill=BOTH,expand=1)


        
        self.root2.mainloop()

       






root=Tk()
object=EmployeeSystem(root)
root.mainloop()



