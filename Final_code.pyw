from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector 
import time
from datetime import datetime as dt


#MYSQL TK PYTHON CODE

# welcomepage geometry
root = Tk()
root.geometry('800x500')
root.title("Welcome Page")

label_1 = Label(root, text="Your Name",width=20,font=("bold", 10))
label_1.place(x=50,y=130)
entry_1= Entry()
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email ",width=20,font=("bold", 10))
label_2.place(x=50,y=180)
entry_2 = Entry()
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Password",width=20,font=("bold", 10))
label_3.place(x=50,y=230)
entry_3 = Entry()
entry_3.place(x=240,y=230)

label_4 = Label(root, text="Confirm Password",width=20,font=("bold", 10))
label_4.place(x=50,y=280)
entry_4 = Entry()
entry_4.place(x=240,y=280)

label_5 = Label(root, text="Email",width=20,font=("bold", 10))
label_5.place(x=400,y=130)
Username = Entry()
Username.place(x=600,y=130)

label_6 = Label(root, text="Password",width=20,font=("bold", 10))
label_6.place(x=400,y=180)
Password = Entry()
Password.place(x=600,y=180)

def clear():
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    entry_3.delete(0,END)
    entry_4.delete(0,END)

def aftersubmit():
    global n
    global e
    global p
    global cp
    
    n=entry_1.get()
    e=entry_2.get()
    p=entry_3.get()
    cp=entry_4.get()
    
    #Validations
    if(n=="" or e=="" or p=="" or cp==""):
        MessageBox.showinfo("Warning", "All fields are required")

    if not (n==""):
        lst=n.split()
        for i in lst:
            if (i.isalpha()==True):
                print("ok")
                #continue
            else:
                MessageBox.showinfo("Warning", "Enter a valid name")
                
    if (e.isalnum=="True"):
        MessageBox.showinfo("Warning", "Enter a valid email-id")
        
    else:
        x,y=e.split("@")
        print(x,y)
        if (x.isalnum()==True) or x in {"_",".","-"} :
            print("ok")
        else:
            MessageBox.showinfo("Warning", "Enter a valid email-id")
        a,b=y.split(".")
        if (a.isalpha()==True) and (b.isalpha()==True):
            print("ok")
        else:
            MessageBox.showinfo("Warning", "Enter a valid email-id")
    
            
    if not(p==cp):
        MessageBox.showinfo("Warning", "Passwords do not match")
    
        
    else:
        
        # connecting to mysql database   
        con = mysql.connector.connect(host="localhost", user="root", password="Rolis@619", database="register")
        mycur = con.cursor()        
        # inserting into database
        try:
            sql="insert into signup VALUES(%s, %s, %s, %s)"
            val=(n,e,p,cp)
            print(val)
            mycur.execute(sql,val)
            con.commit()
            clear()
            
            mycur.execute("select* from signup")     
            # Printing the result of the query
            MessageBox.showinfo("showinfo","Registered Successfully!")
            # tkinter prompt
            
        except:
            con.rollback()
            print("Error occured")
            
        con.close()
        root.destroy()    
        blockercode()
        
        
# signupbutton
signup= Button(root, text='Sign Up',width=20,bg='brown',fg='white',command=aftersubmit).place(x=150,y=400)


def logintodb(user, passw):
    db = mysql.connector.connect(host ="localhost",user="root", password="Rolis@619", database="register")
    cursor = db.cursor()
    
    # A Table in the database
    savequery = "select * from signup"
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
        # Printing the result of the query
        for x in myresult:
            print(x)
            if x[1]==user:
                if x[2]==passw:
                    # tkinter prompt
                    MessageBox.showinfo("showinfo","Logged In")               
                    break
        else:
            # tkinter prompt
            MessageBox.showinfo("Warning","Incorrect password or email")                
    except:
        db.rollback()
        print("Error occured")

    db.close()
    root.destroy()
    blockercode()

def logintact():     
    user = Username.get()
    passw = Password.get()
    clear2()
    print(f"The name entered by you is {user} {passw}")
    logintodb(user, passw)

def clear2():
    Username.delete(0,END)
    Password.delete(0,END)
    
#loginbutton
login= Button(root, text='Log In',width=20,bg='black',fg='white',command=logintact).place(x=550,y=250)



#BLOCKER CODE

#hosts path according to windows OS
hosts_path = "C:\Windows\System32\drivers\etc"
# localhost's IP
redirect = "127.0.0.1"

website_list=[]
def createweblst(webentry):
    x="www."+webentry+".com"
    y=webentry+".com"
    website_list.append(x)
    website_list.append(y)
    print(website_list)

def clear3():
    website_entry.delete(0,END)

def blockercode():
    global webentry, website_entry
    
    root = Tk()
    root.geometry('500x300')
    root.title("Website Blocker")

    website_entry= Entry()
    website_entry.place(x= 220,y = 80)
    
    label_1=Label(root, text ='Enter website name',width=20, font =("bold",10)).place(x=50 ,y=80)
    
    blockbutton = Button(root, text = 'Block',font = ('bold',10),command = Blocker ,width =10, bg = 'brown', fg="white").place(x = 200, y = 200)

def Blocker():
    # websites That you want to block
    webentry=website_entry.get()
    createweblst(webentry)    
    clear3()
    
    while True:
        # time of your work
        if dt(dt.now().year, dt.now().month, dt.now().day,9)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,17):
            print("Working hours...")
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in website_list:
                    if website in content:
                        MessageBox.showinfo("Already Blocked")
                        pass
                    else:
                        # mapping hostnames to your localhost IP address
                        file.write(redirect + " " + website + "\n")
                        MessageBox.showinfo("Just Blocked")
                        
        #outside work time
        else:
            with open(hosts_path, 'r+') as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
      
                # removing hostnmes from host file
                file.truncate()
      
            print("Fun hours...")
        time.sleep(5)

        
# it is use for display the registration form on the window
root.mainloop()

print("****")
