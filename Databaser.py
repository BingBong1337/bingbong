import mysql.connector
import tkinter as tk
root = tk.Tk()
root.geometry('1920x1080')
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'Databas'
)
mycursor = mydb.cursor()
print('Uppkopplad till databasen')

def Inserter():
    global NameInput,AgeInput,sql,NameGet
    sql = 'INSERT INTO Info (Name, Age) VALUES (%s,%s)'
    NameInput = tk.Entry(root)
    NameInput.place(anchor = tk.CENTER, x=775,y=100)
    AgeInput = tk.Spinbox(root,from_=0, to = 99,wrap =True)
    AgeInput.place(anchor = tk.CENTER, x=775,y=150)
    NameGet = tk.Button(root,command = GetI)
    NameGet.place(anchor = tk.CENTER,x=850,y=100)
    return

def GetI():
    global Name,Age
    Name = NameInput.get()
    Age = int(AgeInput.get())
    val = (Name,Age)
    mycursor.execute(sql,val)
    mydb.commit()
    print(val, 'inserted')
    NameInput.place_forget()
    AgeInput.place_forget()
    NameGet.place_forget()

'''
def IdReciever():
    mycursor.execute("SELECT Id FROM Info")
    Ids = mycursor.fetchall()
    print(Ids)
    Ids = int(Ids)
    Id = 1
    while Id == Ids:
        Id = Id+1
        print(Id)
    return
'''

def Reader():
    mycursor.execute('SELECT * FROM Info') #Ändra '*' till namnet på kollumn som vill readas
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
    return

def Deleter():
    ItemDeleter = input('Vad vill du ta bort?')
    sql = "DELETE FROM Info WHERE Name = %s"
    mycursor.execute(sql,(ItemDeleter,))
    mydb.commit()
    return

'''
val = ''
while val != 'q':
    val = input('Vad är ditt val?-->')
    if val == 'I':
        Inserter()
    elif val == 'D':
        Deleter()
    elif val == 'R':
        Reader()
'''        


b1 = tk.Button(root,text = 'Add person?',command = Inserter)
b1.pack()

root.mainloop()