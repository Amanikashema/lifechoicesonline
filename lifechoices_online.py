# Developed and Designed By Amani Kashema
# Admin Details: Username = lifechoices , Password = @lifechoices1234
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
    root1 = Tk()
    root1.title("Login")
    root1.geometry("300x300")
    root1.configure(bg="brown")

    l1 = Label(root1,text="Username")
    l1.place(x=0,y=0)

    username_entry = Entry(root1)
    username_entry.place(x=100,y=0)

    l3 = Label(root1,text="Password")
    l3.place(x=0,y=50)

    password_student = Entry(root1,show="*")
    password_student.place(x=100,y=50)

    # function to login students who are already registered in the system
    def login():
        try:
            username = username_entry.get()
            password = password_student.get()
            username_entry.delete(0,END)
            password_student.delete(0,END)
            if username == "" or password == "":
                mb.showinfo("Attention","Please Enter Valid Literals In Required Fields")
            sql = "Select * from Users where username = %s and password = %s"
            mycursor.execute(sql,([(username),(password)]))
            results = mycursor.fetchall()
            if results:
                for i in results:
                    # sql command to update login time
                    sql2 = "UPDATE Users SET login_time = CURRENT_TIMESTAMP WHERE username = %s "
                    mycursor.execute(sql2,([(username)]))
                    mydb.commit()
                    mb.showinfo("Login Status","Login Successful Enjoy Your Day")
                    root1.destroy()
                    root3 = Tk()
                    root3.title("Login Status")
                    root3.configure(bg="black")

                    # Function to set the logout time
                    def logout():
                        # sql command to update logout time
                        sql2 = "UPDATE Users SET logout_time = CURRENT_TIMESTAMP WHERE username = %s "
                        mycursor.execute(sql2,([(username)]))
                        mydb.commit()
                        mb.showinfo("Logout Status","Logout Successfully Enjoy your Day")
                        root3.destroy()

                    logout_button = Button(root3,text="Log Out",command=logout)
                    logout_button.pack()
        finally:
            pass

    login_but = Button(root1, text="Login",command=login)
    login_but.place(x=50,y=200)

    # Function to go back
    def back():
        root1.destroy()
        root.mainloop()

    back_but = Button(root1, text="<-Back", command=back)
    back_but.place(x=150,y=200)


# Function to Register new students or People entering the building
def register_new():
    root2 = Tk()
    root2.title("Register")
    root2.geometry("300x300")
    root2.configure(bg="brown")

    # New user information to be captured
    firstname_label = Label(root2,text="First Name")
    firstname_label.place(x=0,y=0)

    first_name_entry = Entry(root2)
    first_name_entry.place(x=100,y=0)

    user_name_label = Label(root2,text="User-Name")
    user_name_label.place(x=0,y=100)

    user_name_entry = Entry(root2)
    user_name_entry.place(x=100,y=100)

    password_label = Label(root2,text="Password")
    password_label.place(x=0,y=200)

    password_entry = Entry(root2,show="*")
    password_entry.place(x=100,y=200)

    # Function to add students or workers into the database
    def register():
        firstname = first_name_entry.get()
        username = user_name_entry.get()
        password = password_entry.get()

        first_name_entry.delete(0,END)
        user_name_entry.delete(0,END)
        password_entry.delete(0,END)

        # statement to catch if user enters nothing in entry box
        if firstname == "" or username == "" or password == "":
            mb.showinfo("Attention","Please Enter Valid Literals In Required Fields")
        else:
            sql = "INSERT INTO Users (full_name,username,password) VALUES(%s,%s,%s)"
            mycursor.execute(sql,([firstname,username,password]))
            mydb.commit()
            mb.showinfo("Registration Status","Successfully Added User")
            root2.destroy()

    register_button1 = Button(root2,text="Apply",command=register)
    register_button1.place(x=50,y=250)

    # Function to go back
    def back():
        root2.destroy()
        root.mainloop()

    back_but = Button(root2, text="<-Back", command=back)
    back_but.place(x=150,y=250)


welcome_label = Label(root,text="Welcome To Lifechoices Online",height=3, width=56)
welcome_label.place(x=0,y=0)

login_button_student = Button(root,text="Sign-in as Student",command=login_student)
login_button_student.place(x=30,y=100)


# Login as an admin
def admin():
    root2 = Tk()
    root2.title("Admin Login")
    root2.geometry("300x300")
    root2.configure(bg="brown")

    l1 = Label(root2,text="Username")
    l1.place(x=0,y=0)

    username_admin = Entry(root2)
    username_admin.place(x=100,y=0)

    l3 = Label(root2,text="Password")
    l3.place(x=0,y=50)

    password_admin = Entry(root2,show="*")
    password_admin.place(x=100,y=50)

    # function to login as admin user
    def login():
        username = username_admin.get()
        password = password_admin.get()

        username_admin.delete(0,END)
        password_admin.delete(0,END)

        # statement to catch if user enters nothing in entry box
        if username == "" or password == "":
            mb.showinfo("Attention","Please Enter Valid Literals In Required Fields")
        else:
            sql = "Select * from Admin where username = %s and password = %s "
            mycursor.execute(sql, ([username,password]))
            results = mycursor.fetchall()

            if results:
                for i in results:
                    mb.showinfo("Login Status","Congratulations You have successfully Login")
                    root2.destroy()
                admin_section = Tk()
                admin_section.title("Administration")
                admin_section.geometry("500x300")
                admin_section.configure(bg="green")

                id_number_label = Label(admin_section,text=" Delete By ID#")
                id_number_label.place(x=0,y=0)

                id_number_entry = Entry(admin_section)
                id_number_entry.place(x=120,y=0)

                # Function to Register new user
                def add_user():
                    register_new()

                add_data_button = Button(admin_section,text="Add Users",command=add_user)
                add_data_button.place(x=350,y=0)

                # Function to delete users from the database
                def delete_user():
                    id_num = id_number_entry.get()

                    if id_num == "":
                        mb.showinfo("Attention","Please Enter Valid Literals In Required Fields")
                    else:
                        # sql code to delete users from database
                        del_sql = "DELETE FROM Users WHERE id = %s"
                        user_id = (int(id_num),)
                        mycursor.execute(del_sql, user_id)
                        mydb.commit()
                        mb.showinfo("Delete Status", "Successfully Deleted User")

                delete_data_button = Button(admin_section,text="Delete Users",command=delete_user)
                delete_data_button.place(x=350,y=50)

                # Function to display logged in and logged out database
                def tmanage():
                    root3 = Tk()
                    root3.title("Time Management")
                    root3.geometry("450x400")
                    root3.configure(bg="brown")

                    def display():
                        sql = "SELECT * from Users"
                        mycursor.execute(sql)
                        results1 = mycursor.fetchall()
                        mydb.commit()

                        for i in results1:
                            text.insert(END, i)

                    text = Listbox(root3,height=10,width=50)
                    text.place(x=10,y=20)

                    display_button = Button(root3,text="Show Database", command=display)
                    display_button.place(x=50,y=250)


                time_management_button = Button(admin_section,text="Time Management", command=tmanage)
                time_management_button.place(x=350,y=100)

                # Function to quit and to go back to the main screen
                def quit():
                    admin_section.destroy()
                    root.mainloop()

                quit_button = Button(admin_section,text="Quit",command=quit)
                quit_button.place(x=350,y=200)

                # function to display results from the database
                def display():
                    sql = "SELECT * from Users"
                    mycursor.execute(sql)
                    results1 = mycursor.fetchall()
                    mydb.commit()

                    for i in results1:
                        text.insert(END, i)

                # text box to display stored results from database
                text = Listbox(admin_section,height=10,width=40)
                text.place(x=10,y=50)

                display_button = Button(admin_section,text="Show Database", command=display)
                display_button.place(x=350,y=150)

            else:
                mb.showinfo("login Status", "Please enter a Valid username or password")

    login_but = Button(root2, text="Login",command=login)
    login_but.place(x=50,y=200)

    # Function to go back
    def back():
        root2.destroy()
        root.mainloop()

    back_but = Button(root2, text="<-Back", command=back)
    back_but.place(x=150,y=200)

# Buttons to login as admin
login_button_admin = Button(root,text="Sign-in as Admin",command=admin)
login_button_admin.place(x=300,y=100)

# Buttons to login as new user
register_button = Button(root,text="Register",command=register_new)
register_button.place(x=200,y=100)


# function to exit code
def close():
    mydb.close()
    root.destroy()

exit_button = Button(root,text="Exit",command=close)
exit_button.place(x=374,y=150)

root.mainloop()
