import mysql.connector
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry('1920x1080')
Canvas = tk.Canvas(root,bg = 'white', height = 2000, width = 3000,bd = 0)
Canvas.pack()
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'Databas'
)
mycursor = mydb.cursor()
print('Uppkopplad till databasen')

def Inserter():
    global NameInput,AgeInput,sql,NameGet, SureNameInput
    sql = 'INSERT INTO Info (FirstName,SureName, Age) VALUES (%s,%s,%s)'
    NameInput = tk.Entry(root)
    NameInput.place(anchor = tk.CENTER, x = 775, y = 100)
    NameText = tk.Label(root,text = 'First Name')
    NameText.place(anchor = tk.CENTER, x=650, y = 100)
    SureNameInput = tk.Entry(root)
    SureNameInput.place(anchor = tk.CENTER , x = 775 , y = 150)
    SureNameText = tk.Label(root,text = 'Sure Name')
    SureNameText.place(anchor = tk.CENTER, x = 650, y = 150)
    AgeInput = tk.Spinbox(root,from_=0, to = 99,wrap =True)
    AgeInput.place(anchor = tk.CENTER, x = 775, y = 200)
    AgeText = tk.Label(root,text = 'Age')
    AgeText.place(anchor = tk.CENTER, x = 650, y = 200)
    NameGet = tk.Button(root,text = 'Add Person?',command = GetI)
    NameGet.place(anchor = tk.CENTER,x=900,y=100)
    Adder.place_forget()
    Remover.place_forget()
    Read.place_forget()
    return

def GetI():
    global Name,Age
    Name = NameInput.get()
    SureName = SureNameInput.get()
    Age = int(AgeInput.get())
    val = (Name,SureName,Age)
    mycursor.execute(sql,val)
    mydb.commit()
    print(val, 'Entered')
    MainCanvas()
    

def Reader():
    mycursor.execute('SELECT * FROM Info') #Ändra '*' till namnet på kollumn som vill readas
    myresult = mycursor.fetchall()
    tree = ttk.Treeview(root, column = ('c1','c2','c3','c4'), show = 'headings')
    tree.column('#1',anchor = tk.CENTER)
    tree.heading('#1',text = 'id')
    tree.column('#2',anchor = tk.CENTER)
    tree.heading('#2',text = 'FirstName')
    tree.column('#3',anchor = tk.CENTER)
    tree.heading('#3',text = 'SureName')
    tree.column('#4',anchor = tk.CENTER)
    tree.heading('#4',text = 'Age')
    vrtcscrll = ttk.Scrollbar(root,orient = 'vertical',command = tree.yview)
    tree.config(xscrollcommand=vrtcscrll.set)
    tree.place(anchor = tk.CENTER, x = 800 , y = 120)
    for i in myresult:
        print(i)
        tree.insert('',tk.END,values = i)
    finished = tk.Button(root,text = 'Go Back',command = MainCanvas)
    finished.place(anchor = tk.CENTER, x = 775, y = 700)
    return

def GetRev():
    global RemoveGet
    RemoveGet = RemoveInput.get()
    RemoveInput.place_forget()
    RemoveInputGet.place_forget()
    sql = "DELETE FROM Info WHERE FirstName = %s"
    mycursor.execute(sql,(RemoveGet,))
    mydb.commit()
    MainCanvas()

def Deleter():
    global RemoveInput,RemoveInputGet
    RemoveInput = tk.Entry(root)
    RemoveInput.place(anchor = tk.CENTER,x=775,y=100)
    RemoveText = tk.Label(root, text = 'Enter Name To Be Removed')
    RemoveText.place(anchor = tk.CENTER, x = 600, y = 100)
    RemoveInputGet = tk.Button(root,text='Delete Person?',command = GetRev)
    RemoveInputGet.place(anchor = tk.CENTER,x=900,y=100)
    Adder.place_forget()
    Read.place_forget()
    Remover.place_forget()

def GetSignInInfo():
    global SignInUserName, SignInPassWord
    SignInUserName = UserNameIn.get()
    SignInPassWord = PassWordIn.get()

def GetSignUpInfo():
    global FirstNameSet, SureNameSet, AgeSet, UserNameSet, PassWordSet
    FirstNameSet = FirstNameRegister.get()
    SureNameSet = SureNameRegister.get()
    AgeSet = int(AgeRegister.get())
    UserNameSet = SetUserName.get()
    PassWordSet = SetPassWord.get()
    sql = 'INSERT INTO info (FirstName,SureName, Age) VALUES (%s,%s,%s)'
    InfoInserter = (FirstNameSet,SureNameSet,AgeSet)
    mycursor.execute(sql,InfoInserter)
    sql = 'INSTER INTO signininfo (id,Username,Password) VALUES (%s,%s,%s)'
    query = ("SELECT id FROM info WHERE FirstName = %s AND SureName = %s")
    mycursor.execute(query,(FirstNameSet,SureNameSet,))
    #mycursor.execute("SELECT id FROM info WHERE EXISTS(SELECT * FROM info WHERE FirstName = '%s'" % FirstNameSet and "SureName = '%s'" % SureNameSet))
    rows = mycursor.fetchall()
    id = rows
    print(id)
    SignInInfo = (id,UserNameSet,PassWordSet)
    mycursor.execute(sql,SignInInfo)
    mydb.commit()
    LoginScreen()

def SignUp():
    global FirstNameRegister, SureNameRegister, AgeRegister, SetUserName, SetPassWord
    Canvas.delete('all')
    ScreenFrame = tk.Frame(root, bg = 'blue', bd = 0, width = 2000, height = 2000)
    ScreenFrame.place(x=0, y=0)
    SignUpSign = tk.Label(root, text = 'Please input desired Username and Password in the boxes')
    SignUpSign.place(anchor = tk.CENTER, x = 775, y = 100)
    FirstNameRegister = tk.Entry(root)
    FirstNameRegister.place(anchor = tk.CENTER, x = 775, y = 150)
    FirstNameRText = tk.Label(root, text = 'Input Your Firstname')
    FirstNameRText.place(anchor = tk.CENTER, x = 650, y= 150)
    SureNameRegister = tk.Entry(root)
    SureNameRegister.place(anchor = tk.CENTER, x = 775, y = 200) 
    SureNameText = tk.Label(root, text = 'Input Your Surename')
    SureNameText.place(anchor = tk.CENTER, x = 650, y = 200)
    AgeRegister = tk.Spinbox(root,from_=0, to = 99,wrap =True)
    AgeRegister.place(anchor = tk.CENTER, x = 775, y = 250)
    AgeText = tk.Label(root, text = 'Input Your Age')
    AgeText.place(anchor = tk.CENTER, x = 660, y = 250)
    SetUserName = tk.Entry(root)
    SetUserName.place(anchor = tk.CENTER, x = 775, y = 300)
    UserNameText = tk.Label(root, text = 'Input Your Desired Username')
    UserNameText.place(anchor = tk.CENTER, x = 630, y = 300)
    SetPassWord = tk.Entry(root)
    SetPassWord.place(anchor = tk.CENTER, x = 775, y = 350)
    PassWordText = tk.Label(root, text = 'Input Your Desired Password')
    PassWordText.place(anchor = tk.CENTER, x = 630, y = 350)
    SetSignInInfo = tk.Button(root,text = 'Create User',command = GetSignUpInfo)
    SetSignInInfo.place(anchor = tk.CENTER, x = 775, y = 400)
    GoBackBtn = tk.Button(root, text = 'Go back to sign in screen', command = LoginScreen)
    GoBackBtn.place(anchor = tk.CENTER, x = 775, y = 500)

def LoginScreen():
    global UserNameIn, PassWordIn
    ScreenFrame = tk.Frame(root, bg = 'blue', bd = 0, width = 2000, height = 2000)
    ScreenFrame.place(x=0, y=0)
    SignInSign = tk.Label(root, text = 'Already a member, why not sign in and book some cool stuff?')
    SignInSign.place(anchor = tk.CENTER, x = 775, y = 100)
    UserNameIn = tk.Entry(root)
    UserNameIn.place(anchor = tk.CENTER, x = 775, y = 250)
    UserNameText = tk.Label(root, text = 'Input Your Username')
    UserNameText.place(anchor = tk.CENTER, x = 650, y= 250)
    PassWordIn = tk.Entry(root)
    PassWordIn.place(anchor = tk.CENTER, x = 775, y = 300)
    PassWordText = tk.Label(root, text = 'Input Your Password')
    PassWordText.place(anchor = tk.CENTER, x = 650, y = 300)
    SignIn = tk.Button(root, text = 'Sign in', command = GetSignInInfo)
    SignIn.place(anchor = tk.CENTER, x = 775, y = 350)
    SignUpBtn = tk.Button(root, text = 'Sign Up??',command = SignUp)
    SignUpBtn.place(anchor = tk.CENTER, x = 775, y = 500)
    Killer = tk.Button(root, text = 'Quit?', command = root.destroy)
    Killer.place(anchor = tk.CENTER, x = 775, y = 700)

def MainCanvas():
    global Adder, Read, Remover
    Canvas.delete('all')
    AdFrame = tk.Frame(root, bg = 'blue', bd = 0, width = 2000, height = 70)
    AdFrame.place(x = 0, y = 0)
    LocationFrame = tk.Frame(root,bg = 'cyan', bd = 0, width = 400, height = 2000)
    LocationFrame.place(x = 0, y = 70)
    CompanyFrame = tk.Frame(root, bg = 'yellow', bd = 0, width = 700, height = 2000)
    CompanyFrame.place(x = 400, y = 70)
    DateFrame = tk.Frame(root, bg = 'purple', bd = 0, width = 1000, height = 2000)
    DateFrame.place(x = 1100 , y = 70)

    Adder = tk.Button(root,text = 'Add Person?',command = Inserter)
    Adder.place(anchor = tk.CENTER, x= 775,y=50)
    Remover = tk.Button(root,text = 'Remove Person?',command = Deleter)
    Remover.place(anchor = tk.CENTER, x= 775,y=100)
    Read = tk.Button(root,text = 'Print all in database?',command = Reader)
    Read.place(anchor = tk.CENTER, x= 775,y=150)
    Killer = tk.Button(root,text = 'Quit?', command = root.destroy)
    Killer.place(anchor = tk.CENTER,x=775,y=750)

LoginScreen()
#MainCanvas()
root.mainloop()