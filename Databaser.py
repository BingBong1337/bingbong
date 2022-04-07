import mysql.connector
import tkinter as tk
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
    SureNameInput = tk.Entry(root)
    SureNameInput.place(anchor = tk.CENTER , x = 775 , y = 150)
    AgeInput = tk.Spinbox(root,from_=0, to = 99,wrap =True)
    AgeInput.place(anchor = tk.CENTER, x = 775, y = 200)
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
    print(val, 'inserted')
    '''
    NameInput.place_forget()
    AgeInput.place_forget()
    NameGet.place_forget()
    '''
    MainCanvas()
    

def Reader():
    mycursor.execute('SELECT * FROM Info') #Ändra '*' till namnet på kollumn som vill readas
    myresult = mycursor.fetchall()
    print('Everyone in database->:')
    for i in myresult:
        print(i)
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
    RemoveInputGet = tk.Button(root,text='Delete Person?',command = GetRev)
    RemoveInputGet.place(anchor = tk.CENTER,x=900,y=100)
    Adder.place_forget()
    Read.place_forget()
    Remover.place_forget()

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


MainCanvas()
root.mainloop()