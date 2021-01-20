from tkinter import *
import mysql.connector
from tkinter import messagebox as mb

mydb = mysql.connector.connect(user="lifechoices",password="@Lifechoices1234",host="localhost",database="lifechoicesonline")
mycursor = mydb.cursor()


root = Tk()
root.title("Life choices Online")
root.geometry("450x200")
root.configure(bg="brown")


# Login as a student or worker in the system
def login_student():
    root = Tk()
    root.title("Login")
    root.geometry("300x300")
    root.configure(bg="brown")

    l1 = Label(root,text="Username")
    l1.place(x=0,y=0)

    username_entry = Entry(root)
    username_entry.place(x=100,y=0)

    l3 = Label(root,text="Password")
    l3.place(x=0,y=50)

    password_student = Entry(root)
    password_student.place(x=100,y=50)

    # function to login students who are already registered in the system
    def login():
        username = username_entry.get()
        password = password_student.get()

        if username == "" or password == "":
            mb.showinfo("Attention","Please Enter Valid Literals In Required Fields")
        else:
            sql = "Select * from Users where username = %s and password = %s "
            mycursor.execute(sql,([username,password]))
            results = mycursor.fetchall()
            if results:
                for i in results:
                    mb.showinfo("Login Status","Congratulations You have successfully Login")
                    break
            else:
                mb.showinfo("login Status", "Please enter a Valid username or password")
            mydb.close()

    login_but = Button(root, text="Login",command=login)
    login_but.place(x=50,y=200)

    # Function to go back
    def back():
        root.destroy()
        root.mainloop()

    back_but = Button(root, text="<-Back", command=back)
    back_but.place(x=150,y=200)


# Function to Register new students or People entering the building
def register_new():
    root = Tk()
    root.title("Register")
    root.geometry("300x300")
    root.configure(bg="brown")

    # New user information to be captured
    firstname_label = Label(root,text="First Name")
    firstname_label.place(x=0,y=0)

    first_name_entry = Entry(root)
    first_name_entry.place(x=100,y=0)

    second_name_label = Label(root,text="Surname")
    second_name_label.place(x=0,y=50)

    second_name_entry = Entry(root)
    second_name_entry.place(x=100,y=50)

    user_name_label = Label(root,text="User-Name")
    user_name_label.place(x=0,y=100)

    user_name_entry = Entry(root)
    user_name_entry.place(x=100,y=100)

    id_label = Label(root,text="ID number")
    id_label.place(x=0,y=150)

    id_entry = Entry(root)
    id_entry.place(x=100,y=150)

    password_label = Label(root,text="Password")
    password_label.place(x=0,y=200)

    password_entry = Entry(root)
    password_entry.place(x=100,y=200)

    # Function to add students or workers into the database
    def register():
        firstname = first_name_entry.get()
        username = user_name_entry.get()
        password = password_entry.get()

        if firstname == "" or username == "" or password == "":
            mb.showinfo("Attention","Please Enter Valid Literals In Required Fields")
        else:
            sql = "INSERT INTO Users (full_name,username,password) VALUES(%s,%s,%s)"
            mycursor.execute(sql,([firstname,username,password]))
            mydb.commit()
            mb.showinfo("Registration Status","Congratulation You have Registered into the the system")
            mydb.close()

    register_button1 = Button(root,text="Apply",command=register)
    register_button1.place(x=50,y=250)

    # Function to go back
    def back():
        root.destroy()
        root.mainloop()

    back_but = Button(root, text="<-Back", command=back)
    back_but.place(x=150,y=250)


welcome_label = Label(root,text="Welcome To Lifechoices Online",height=3, width=56)
welcome_label.place(x=0,y=0)

login_button_student = Button(root,text="Sign-in as Student",command=login_student)
login_button_student.place(x=30,y=100)


# Login as an admin
def admin():
    root = Tk()
    root.title("Admin Login")
    root.geometry("300x300")
    root.configure(bg="brown")

    l1 = Label(root,text="Username")
    l1.place(x=0,y=0)

    username_admin = Entry(root)
    username_admin.place(x=100,y=0)

    l3 = Label(root,text="Password")
    l3.place(x=0,y=50)

    password_admin = Entry(root)
    password_admin.place(x=100,y=50)

    # function to login as admin user
    def login():
        username = username_admin.get()
        password = password_admin.get()

        if username == "" or password == "":
            mb.showinfo("Attention","Please Enter Valid Literals In Required Fields")
        else:
            sql = "Select * from Admin where username = %s and password = %s "
            mycursor.execute(sql,([username,password]))
            results = mycursor.fetchall()
            if results:
                for i in results:
                    mb.showinfo("Login Status","Congratulations You have successfully Login")
                    root.destroy()
                admin_section = Tk()
                admin_section.title("Administration")
                admin_section.geometry("500x500")
                admin_section.configure(bg="green")

                user_name_label = Label(admin_section,text="User-Name")
                user_name_label.place(x=0,y=0)

                user_name_entry = Entry(admin_section)
                user_name_entry.place(x=100,y=0)

                password_label = Label(admin_section,text="Password")
                password_label.place(x=0,y=50)

                password_entry = Entry(admin_section)
                password_entry.place(x=100,y=50)

                firstname_label = Label(admin_section,text="Full Name")
                firstname_label.place(x=0,y=100)

                first_name_entry = Entry(admin_section)
                first_name_entry.place(x=100,y=100)

                def add_user():
                    register_new()

                add_data_button = Button(admin_section,text="Add Users",command=add_user)
                add_data_button.place(x=350,y=0)

                def delete_user():
                    full_name = first_name_entry.get()
                    username = user_name_entry.get()
                    password = password_entry.get()

                    if full_name == "" or username == "" or password == "":
                        mb.showinfo("Attention","Please Enter Valid Literals In Required Fields")
                    else:
                        sql = "Delete from Users (full_name,username,password) VALUES(%s,%s,%s)"
                        mycursor.execute(sql,(full_name,username,password))
                        mydb.commit()
                        mb.showinfo("Delete","Deleted")
                        mydb.close()


                delete_data_button = Button(admin_section,text="Delete Users",command=delete_user)
                delete_data_button.place(x=350,y=50)

                time_management_button = Button(admin_section,text="Time Management")
                time_management_button.place(x=350,y=100)

                def quit():
                    admin_section.destroy()
                    root.mainloop()

                quit_button = Button(admin_section,text="Quit",command=quit)
                quit_button.place(x=350,y=150)

            else:
                mb.showinfo("login Status", "Please enter a Valid username or password")
            mydb.close()

    login_but = Button(root, text="Login",command=login)
    login_but.place(x=50,y=200)

    # Function to go back
    def back():
        root.destroy()
        root.mainloop()

    back_but = Button(root, text="<-Back", command=back)
    back_but.place(x=150,y=200)


login_button_admin = Button(root,text="Sign-in as Admin",command=admin)
login_button_admin.place(x=300,y=100)

register_button = Button(root,text="Register",command=register_new)
register_button.place(x=200,y=100)


# function to exit code
def close():
    root.destroy()

exit_button = Button(root,text="Exit",command=close)
exit_button.place(x=374,y=150)


root.mainloop()
