import mysql.connector
import tkinter as tk
from tkinter import ttk
import random as r
import socket as so
import _thread as th
from tkcalendar import Calendar

root = tk.Tk()
root.geometry('1536x864')
Canvas = tk.Canvas(root,bg = 'white', height = 2000, width = 3000,bd = 0)
Canvas.pack()
ProfilePic = tk.PhotoImage(file = 'proff.png')
ProfilePic = ProfilePic.subsample(5,5)
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'Databas'
)
mycursor = mydb.cursor()
print('Uppkopplad till databasen')
AdminPrivledges = 0

class Booking():
    def __init__(self, time, date, fromcity, tocity, klass, price):
        self.time = time
        self.date = date
        self.fromcity = fromcity
        self.tocity = tocity
        self.klass = klass
        self.price = price
    def __repr__(self):
        #return '({} {} {} {} {} {})'. format('Time ->',self.time,'Date ->', self.date, 'From City ->', self.fromcity, 'To City ->', self.tocity,'Klass ->', self.klass,'Price ->', self.price)
        return '({} {} {} {} {} {})'. format(self.time, self.date, self.fromcity,  self.tocity, self.klass, self.price)

def RandomizeTrainScheduleTime():
    global HourTime, intHourTime
    HourTime = r.randint(0,23)
    intHourTime = HourTime
    MinuteTime = r.randint(0,59)
    if HourTime < 10:
        HourTime = '0' + str(HourTime)
    if MinuteTime < 10:
        MinuteTime = '0' + str(MinuteTime)
    Time = str(HourTime) + '-'+ str(MinuteTime)
    return Time

def RandomizeTrainScheduleDate():
    Month = r.randint(1,12)
    Day = r.randint(1,28)
    Year = r.randint(2022,2023)
    if Month < 10:
        Month = '0' + str(Month)
    if Day < 10:
        Day = '0' + str(Day)
    Date = str(Year) + '-' + str(Month) + '-' + str(Day)
   
    return Date

def TravelFromCity():
    global FromCity
    TravelCityList = ['Stockholm','Göteborg','Linköping','Malmö','Uppsala','Örebro','Helsingborg','Jönköping','Norrköping','Lund','Umeå','Gävle','Södertälje','Karlstad','Östersund','Mora','Bordlänge','Solna','Halmstad','Nybro','Bålsta','Västerås']
    FromCity = r.choice(TravelCityList)
    return FromCity

def TravelToCity():
    TravelCityList = ['Stockholm','Göteborg','Linköping','Malmö','Uppsala','Örebro','Helsingborg','Jönköping','Norrköping','Lund','Umeå','Gävle','Södertälje','Karlstad','Östersund','Mora','Bordlänge','Solna','Halmstad','Nybro','Bålsta','Västerås']
    ToCity = r.choice(TravelCityList)
    while FromCity == ToCity:
        ToCity = r.choice(TravelCityList)
    return ToCity

def TravelKlass():
    global Klass
    KlassList = ['Economy','Bussiness','First-Class']
    Klass = r.choice(KlassList)
    return Klass

def TravelPrice():
    Price = 0
    if Klass == 'Economy':
        Price += 300
    elif Klass == 'Bussiness':
        Price += 800
    elif Klass == 'First-Class':
        Price += 2000
    if intHourTime > 18 and intHourTime <= 23 or intHourTime < 6 and intHourTime >= 0:
        Price -= 150
        if Klass == 'Bussiness' or Klass == 'First-Class':
            Price -= 150
            if Klass == 'First-Class':
                Price -= 300
    return Price
    
AllBookingsList = []
for i in range(500): #Sätt till 500000 innan testning!
    Timee = RandomizeTrainScheduleTime()
    Datee = RandomizeTrainScheduleDate()
    FromCityy = TravelFromCity()
    ToCityy = TravelToCity()
    Klasss = TravelKlass()
    Pricee = TravelPrice()
    booking = Booking(Timee,Datee,FromCityy,ToCityy,Klasss,Pricee)
    AllBookingsList.append(booking)



'''
for i in AllBookingsList:
    if i.fromcity == 'Stockholm' and i.tocity == 'Gävle' and i.klass == 'First-Class':
        print(i)
'''

def BookTravel():
    BookingBtn.place_forget()
    SupportedLocationsText = tk.Label(root, text = 'These cities have available stations \n Stockholm, Göteborg, Linköping, Malmö, Uppsala, Örebro, Helsingborg, Jönköping, Norrköping, Lund, Umeå, Gävle, Södertälje, Karlstad, Östersund, Mora, Bordlänge, Solna, Halmstad, Nybro, Bålsta, Västerås')
    SupportedLocationsText.place(anchor = tk.CENTER, x = 775, y = 20)
    cal = Calendar(root, selectmode = 'day',year = 2022, month = 6, day = 31)
    cal.place(anchor = tk.CENTER, x = 175, y = 400)
    DepartureDateText = tk.Label(root, text = 'Choose Date Of Departure')
    DepartureDateText.place(anchor = tk.CENTER, x = 175, y = 270)
    '''
    def GetCalanderDate():
        global DateSetted
        
        print(DateSetted)
        for i in AllBookingsList:
            if i.date == DateSetted:
                print(i)
    SetDate = tk.Button(root, text = "Set Date", command = GetCalanderDate)
    SetDate.place(anchor = tk.CENTER, x = 150, y = 300)
    '''
    CurrentLocation = tk.Entry(root)
    CurrentLocation.place(anchor = tk.CENTER,x = 100, y = 200)
    CurrentLocationText = tk.Label(root, text = 'From')
    CurrentLocationText.place(anchor = tk.CENTER,x = 100, y = 150)
    TravelLocation = tk.Entry(root)
    TravelLocation.place(anchor = tk.CENTER,x = 250, y = 200)
    TravelLocationText = tk.Label(root, text = 'To')
    TravelLocationText.place(anchor = tk.CENTER,x = 250, y = 150)

    '''
    def GetCurrentLocation():
        GetCurrentLocation = CurrentLocation.get()
    def GetTravelLocation():
        GetTravelLocation = TravelLocation.get()
    '''
    def BookTravel():
        global DesiredTravel
        selected = AvailableBookings.focus()
        DesiredTravel = AvailableBookings.item(selected,'values')

    def BookClicker(e):
        BookTravel()

    def ActuallyBook():
        query = ("SELECT id FROM signininfo WHERE Username = %s and Password = %s")
        mycursor.execute(query,(SignInUserName, SignInPassWord,))
        info = mycursor.fetchone()
        idresult = info[0]
        TravelInfo = ("INSERT INTO travel (id, Time, Date, FromCity, ToCity, Klass, Price) VALUES (%s,%s,%s,%s,%s,%s,%s)")
        mycursor.execute(TravelInfo,(idresult,DesiredTravel[0],DesiredTravel[1],DesiredTravel[2],DesiredTravel[3],DesiredTravel[4],DesiredTravel[5],))
        mydb.commit()
        YouBookedText = tk.Label(root, text = 'You Booked '+str(DesiredTravel[2]) + '->'+str(DesiredTravel[3]) + ' At '+str(DesiredTravel[0])+ ' ' +str(DesiredTravel[1])+ ' In Class ' +str(DesiredTravel[4])+ ' Which Costs '+str(DesiredTravel[5]))
        YouBookedText.place(anchor = tk.CENTER, x = 775, y = 100)
        root.after(2000,MainCanvas)

        
    def GetCurrentLocationAndTravelLocationAndTimeAndDate():
        global AvailableBookings
        GetCurrentLocation = CurrentLocation.get()
        GetTravelLocation = TravelLocation.get()
        DateSetted = cal.get_date() 
        AvailableBookings = ttk.Treeview(root, column = ('c1','c2','c3','c4','c5','c6'), show = 'headings', height = 27)
        AvailableBookings.column('#1',anchor = tk.CENTER, width = 110)
        AvailableBookings.heading('#1',text = 'Time(h-min)')
        AvailableBookings.column('#2',anchor = tk.CENTER, width = 120)
        AvailableBookings.heading('#2',text = 'Date(YYYY-MM-DD)')
        AvailableBookings.column('#3',anchor = tk.CENTER, width = 120)
        AvailableBookings.heading('#3',text = 'From')
        AvailableBookings.column('#4',anchor = tk.CENTER, width = 120)
        AvailableBookings.heading('#4',text = 'Destination')
        AvailableBookings.column('#5',anchor = tk.CENTER, width = 70)
        AvailableBookings.heading('#5',text = 'Class')
        AvailableBookings.column('#6',anchor = tk.CENTER, width = 65)
        AvailableBookings.heading('#6',text = 'Price(kr)')
        vrtcscrll = ttk.Scrollbar(root,orient = 'vertical',command = AvailableBookings.yview)
        AvailableBookings.config(xscrollcommand=vrtcscrll.set)
        AvailableBookings.place(anchor = tk.CENTER, x = 750 , y = 400)
        AvailableBookings.bind("<ButtonRelease-1>",BookClicker)

        if GetCurrentLocation == '':
            for i in AllBookingsList:
                if i.tocity == GetTravelLocation:
                    AvailableBookings.insert('', tk.END, values = i)
        elif GetTravelLocation == '':
            for i in AllBookingsList:
                if i.fromcity == GetCurrentLocation:
                    AvailableBookings.insert('', tk.END, values = i)
        elif DateSetted == '':
            for i in AllBookingsList:
                if i.tocity == GetTravelLocation and i.fromcity == GetCurrentLocation:
                    AvailableBookings.insert('', tk.END, values = i)
        else:
            for i in AllBookingsList:
                if i.fromcity == GetCurrentLocation and i.tocity == GetTravelLocation and i.date == DateSetted:
                    AvailableBookings.insert('', tk.END, values = i)
                           


    SetCurrentLocationAndTravelLocationBtn = tk.Button(root, text = 'Search Trips', command = GetCurrentLocationAndTravelLocationAndTimeAndDate)
    SetCurrentLocationAndTravelLocationBtn.place(anchor = tk.CENTER, x = 175, y = 600)
    BookTripBtn = tk.Button(root, text = 'Book Selected Trip',command = ActuallyBook)
    BookTripBtn.place(anchor = tk.CENTER, x = 775, y = 700)
    Cancelbtn = tk.Button(root,text = 'Cancel', command = MainCanvas)
    Cancelbtn.place(anchor = tk.CENTER, x = 775, y = 750)

def Reader():
    global tree, tree2, UserNameChanger, PassWordChanger
    mycursor.execute('SELECT * FROM Info')
    myresult = mycursor.fetchall()
    mycursor.execute("SELECT Username, Password FROM signininfo")
    myotherresult = mycursor.fetchall()
    try:
        myotherresult.pop(0)
    except:
        pass
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
    tree.place(anchor = tk.CENTER, x = 600 , y = 120)
    for i in myresult:
        tree.insert('', tk.END, values = i)

    tree2 = ttk.Treeview(root, column = ('c1','c2'), show = 'headings')
    tree2.column('#1',anchor = tk.CENTER)
    tree2.heading('#1',text = 'Username')
    tree2.column('#2',anchor = tk.CENTER)
    tree2.heading('#2',text = 'Password')
    vrtcscrll = ttk.Scrollbar(root,orient = 'vertical',command = tree2.yview)
    tree2.config(xscrollcommand=vrtcscrll.set)
    tree2.place(anchor = tk.CENTER, x = 1200 , y = 120)
    for i in myotherresult:
        tree2.insert('', tk.END, values = i)
    finished = tk.Button(root,text = 'Go Back',command = AdminPage)
    finished.place(anchor = tk.CENTER, x = 775, y = 700)
    RemoveSelecter = tk.Button(root, text = 'Delete Selected',command = GetRev)
    RemoveSelecter.place(anchor = tk.CENTER, x = 775, y = 500)

    UserNameChanger = tk.Entry(root)
    UserNameChanger.place(anchor = tk.CENTER, x = 700, y = 400)
    UserNameChangerText = tk.Label(root, text = 'Change Username')
    UserNameChangerText.place(anchor = tk.CENTER, x = 700, y = 350)
    PassWordChanger = tk.Entry(root)
    PassWordChanger.place(anchor = tk.CENTER, x = 850, y = 400)
    PassWordChangerText = tk.Label(root, text = 'Change Username')
    PassWordChangerText.place(anchor = tk.CENTER, x = 850, y = 350)
    UpdateSignInInfobtn = tk.Button(root, text = 'Update Info', command = AdminChangerGet)
    UpdateSignInInfobtn.place(anchor = tk.CENTER, x = 775, y = 450)
    tree2.bind("<ButtonRelease-1>",clicker)
    return

def AdminChangerGet():
    query = ("UPDATE signininfo SET Username = %s, Password = %s WHERE Username = %s")
    mycursor.execute(query,(UserNameChanger.get(),PassWordChanger.get(),value[0],))
    mydb.commit()

def AdminChanger():
    global value
    try:
        UserNameChanger.delete(0,tk.END)
        PassWordChanger.delete(0,tk.END)
        selected = tree2.focus()
        value = tree2.item(selected,'values')
        UserNameChanger.insert(0,value[0])
        PassWordChanger.insert(0,value[1])
    except:
        pass

def clicker(e):
    AdminChanger()

def GetRev():

    try:
        selected = tree.focus()
        values = tree.item(selected,'values')
        RemoveGet = int(values[0])
    except:
        pass
    try:
        sql = "DELETE FROM Info WHERE id = %s"
        mycursor.execute(sql,(RemoveGet,))
        sql = "DELETE FROM signininfo WHERE id = %s"
        mycursor.execute(sql,(RemoveGet,))
        mydb.commit()
        AdminPage()
    except:
        pass
'''
def Deleter():
    global RemoveInput,RemoveInputGet
    RemoveInput = tk.Entry(root)
    RemoveInput.place(anchor = tk.CENTER,x=775,y=100)
    RemoveText = tk.Label(root, text = 'Enter Id of Person To Be Removed')
    RemoveText.place(anchor = tk.CENTER, x = 600, y = 100)
    RemoveInputGet = tk.Button(root,text='Delete Person?',command = GetRev)
    RemoveInputGet.place(anchor = tk.CENTER,x=900,y=100)
    Adder.place_forget()
    Read.place_forget()
    Remover.place_forget()
    finished = tk.Button(root,text = 'Go Back',command = AdminPage)
    finished.place(anchor = tk.CENTER, x = 775, y = 700)
'''
def Profile():
    Canvas.delete('all')
    ProfileFrame = tk.Frame(root, bg = 'gray', bd = 0, width = 2000, height = 2000)
    ProfileFrame.place(x = 0, y = 0)
    YourProfile = tk.Label(root, text = 'Your profile \n Here you can change your personal information')
    YourProfile.place(anchor = tk.CENTER, x = 775, y = 50)
    GoBackBtn = tk.Button(root, text = 'Go back', command = MainCanvas)
    GoBackBtn.place(anchor = tk.CENTER, x = 775, y = 700)
    query = ("SELECT id FROM signininfo WHERE Username = %s and Password = %s")
    mycursor.execute(query,(SignInUserName, SignInPassWord,))
    info = mycursor.fetchone()
    idresult = info[0]
    query1 = ("SELECT * FROM info WHERE id = %s")
    query2 = ("SELECT * FROM signininfo WHERE id = %s")
    mycursor.execute(query1,(idresult,))
    myresult1 = mycursor.fetchone()
    mycursor.execute(query2,(idresult,))
    myresult2 = mycursor.fetchone()

    namebox = tk.Entry(root)
    namebox.insert(0,myresult1[1])
    namebox.place(anchor = tk.CENTER, x = 775, y = 150)
    nameboxtext = tk.Label(root, text = 'Your Name')
    nameboxtext.place(anchor = tk.CENTER, x = 650, y = 150)
    othernamebox = tk.Entry(root)
    othernamebox.insert(0,myresult1[2])
    othernamebox.place(anchor = tk.CENTER, x = 775, y = 200)
    othernameboxtext = tk.Label(root, text = 'Your Surename')
    othernameboxtext.place(anchor = tk.CENTER, x = 650, y = 200)
    agebox = tk.Entry(root)
    agebox.insert(0,myresult1[3])
    agebox.place(anchor = tk.CENTER, x = 775, y = 250)
    ageboxtext = tk.Label(root, text = 'Your Age')
    ageboxtext.place(anchor = tk.CENTER, x = 650, y = 250)
    usernamebox = tk.Entry(root)
    usernamebox.insert(0,myresult2[1])
    usernamebox.place(anchor = tk.CENTER, x = 775, y = 300)
    usernameboxtext = tk.Label(root, text = 'Your username')
    usernameboxtext.place(anchor = tk.CENTER, x = 650, y = 300)
    passwordbox = tk.Entry(root)
    passwordbox.insert(0,myresult2[2])
    passwordbox.place(anchor = tk.CENTER, x = 775, y = 350)
    passwordboxtext = tk.Label(root, text = 'Your Password')
    passwordboxtext.place(anchor = tk.CENTER, x = 650, y = 350)

    def ChooseToDeleteBooking():
        global TripToBeRemoved
        selected = YourBookings.focus()
        TripToBeRemoved = YourBookings.item(selected,'values')

    def RemoveBookingClicker(e):
        ChooseToDeleteBooking()

    def DeleteBooking():
        query = ("DELETE FROM travel WHERE id = %s AND Time = %s AND Date = %s AND FromCity = %s AND ToCity = %s")
        mycursor.execute(query,(idresult,TripToBeRemoved[0],TripToBeRemoved[1],TripToBeRemoved[2],TripToBeRemoved[3],))
        mydb.commit()
        Profile()


    YourBookingsText = tk.Label(root, text = 'Your Bookings')
    YourBookingsText.place(anchor = tk.CENTER, x = 1200, y = 50)
    query = "SELECT Time,Date,FromCity,ToCity,Klass,Price FROM travel WHERE id = %s"
    mycursor.execute(query,(idresult,))
    MyBookings = mycursor.fetchall()
    YourBookings = ttk.Treeview(root, column = ('c1','c2','c3','c4','c5','c6'), show = 'headings')
    YourBookings.column('#1',anchor = tk.CENTER, width = 110)
    YourBookings.heading('#1',text = 'Time(h-min)')
    YourBookings.column('#2',anchor = tk.CENTER, width = 120)
    YourBookings.heading('#2',text = 'Date(YYYY-MM-DD)')
    YourBookings.column('#3',anchor = tk.CENTER, width = 120)
    YourBookings.heading('#3',text = 'From')
    YourBookings.column('#4',anchor = tk.CENTER, width = 120)
    YourBookings.heading('#4',text = 'Destination')
    YourBookings.column('#5',anchor = tk.CENTER, width = 70)
    YourBookings.heading('#5',text = 'Class')
    YourBookings.column('#6',anchor = tk.CENTER, width = 65)
    YourBookings.heading('#6',text = 'Price(kr)')
    vrtcscrll = ttk.Scrollbar(root,orient = 'vertical',command = YourBookings.yview)
    YourBookings.config(xscrollcommand=vrtcscrll.set)
    YourBookings.place(anchor = tk.CENTER, x = 1200 , y = 200)
    for i in MyBookings:
        YourBookings.insert('', tk.END, values = i)
    YourBookings.bind("<ButtonRelease-1>",RemoveBookingClicker)

    def GetNewChanges():
        name = namebox.get()
        othername = othernamebox.get()
        age = agebox.get()
        username = usernamebox.get()
        password = passwordbox.get()
        query = ("UPDATE info SET FirstName = %s, SureName = %s, Age = %s WHERE id = %s")
        mycursor.execute(query,(name,othername,age,idresult,))
        query = ("UPDATE signininfo SET Username = %s, Password = %s WHERE id = %s")
        mycursor.execute(query,(username,password,idresult,))
        mydb.commit()


    ChangePersonalInfoBtn = tk.Button(root, text = 'Save new changes', command = GetNewChanges )
    ChangePersonalInfoBtn.place(anchor = tk.CENTER, x = 775, y = 600)
    DeleteBookingbtn = tk.Button(root, text = 'Remove Selected Booking', command = DeleteBooking)
    DeleteBookingbtn.place(anchor = tk.CENTER, x = 1200, y = 700)    
    

def LoginFrame():
    SuccessfulLoginFrame = tk.Frame(root, bg = 'blue', bd = 0, width = 2000, height = 2000)
    SuccessfulLoginFrame.place(x = 0, y = 0)

def logout():
    global AdminPrivledges
    logoutFrame = tk.Frame(root,bg = 'green', bd = 0, width = 2000, height = 2000)
    logoutFrame.place(x = 0, y = 0)
    LogoutText = tk.Label(root, text = 'Logout successful!')
    LogoutText.place(anchor = tk.CENTER, x = 775, y = 100)
    AdminPrivledges = 0
    root.after(2000, LoginScreen)

def GetSignInInfo():
    global SignInUserName, SignInPassWord, AdminPrivledges
    AdminPrivledges = 0
    SignInUserName = UserNameIn.get()
    SignInPassWord = PassWordIn.get()
    UserNameIn.delete(0,'end')
    PassWordIn.delete(0,'end')
    query = ("SELECT * FROM signininfo WHERE Username = %s AND Password = %s")
    mycursor.execute(query,(SignInUserName,SignInPassWord))
    rows = mycursor.fetchone()
    try:
        if SignInUserName == 'Admin' and SignInPassWord == 'Admin':
            AdminPage()
            AdminPrivledges += 1
        elif rows[1] == SignInUserName and rows[2] == SignInPassWord:
            Canvas.delete('all')
            LoginFrame()
            success = tk.Label(root,text='Sign in successful!', bg = 'green')
            success.place(anchor = tk.CENTER, x = 775, y = 50)
    
        
            root.after(2000, MainCanvas)
    except:
        WrongSignInData = tk.Label(root, text = 'Incorrect Username or Password')
        WrongSignInData.place(anchor = tk.CENTER, x = 775, y = 200)
        root.after(1500,LoginScreen)
    
def GetSignUpInfo():
    global FirstNameSet, SureNameSet, AgeSet, UserNameSet, PassWordSet, id
    FirstNameSet = FirstNameRegister.get()
    SureNameSet = SureNameRegister.get()
    AgeSet = int(AgeRegister.get())
    UserNameSet = SetUserName.get()
    PassWordSet = SetPassWord.get()
    sql = 'INSERT INTO info (FirstName,SureName, Age) VALUES (%s,%s,%s)'
    InfoInserter = (FirstNameSet,SureNameSet,AgeSet)
    mycursor.execute(sql,InfoInserter)
    sql = 'INSERT INTO signininfo (id,Username,Password) VALUES (%s,%s,%s)'
    query = ("SELECT id FROM info WHERE FirstName = %s AND SureName = %s")
    mycursor.execute(query,(FirstNameSet,SureNameSet,))
    rows = mycursor.fetchone()
    id = int(rows[0])
    SignInInfo = (id,UserNameSet,PassWordSet)
    mycursor.execute(sql,SignInInfo)
    mydb.commit()
    if AdminPrivledges >= 1:
        AdminPage()
    else:
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
    SetPassWord = tk.Entry(root,show = '*')
    SetPassWord.place(anchor = tk.CENTER, x = 775, y = 350)
    PassWordText = tk.Label(root, text = 'Input Your Desired Password')
    PassWordText.place(anchor = tk.CENTER, x = 630, y = 350)
    SetSignInInfo = tk.Button(root,text = 'Create User',command = GetSignUpInfo)
    SetSignInInfo.place(anchor = tk.CENTER, x = 775, y = 400)

    if AdminPrivledges >= 1:
        GoBackBtn = tk.Button(root, text = 'Go back', command = AdminPage)
        GoBackBtn.place(anchor = tk.CENTER, x = 775, y = 500)
    else:
        GoBackBtn = tk.Button(root, text = 'Go back', command = LoginScreen)
        GoBackBtn.place(anchor = tk.CENTER, x = 775, y = 500)

def LoginScreen():
    global UserNameIn, PassWordIn
    ScreenFrame = tk.Frame(root, bg = 'blue', bd = 0, width = 2000, height = 2000)
    ScreenFrame.place(x=0, y=0)
    SignInSign = tk.Label(root, text = 'Already a member, why not sign in and book some cool stuff?', bg = 'blue')
    SignInSign.place(anchor = tk.CENTER, x = 775, y = 100)
    UserNameIn = tk.Entry(root, bg = 'blue')
    UserNameIn.place(anchor = tk.CENTER, x = 775, y = 250)
    UserNameText = tk.Label(root, text = 'Input Your Username', bg = 'blue')
    UserNameText.place(anchor = tk.CENTER, x = 650, y= 250)
    PassWordIn = tk.Entry(root, bg = 'blue',show = '*')
    PassWordIn.place(anchor = tk.CENTER, x = 775, y = 300,)
    PassWordText = tk.Label(root, text = 'Input Your Password', bg = 'blue')
    PassWordText.place(anchor = tk.CENTER, x = 650, y = 300)
    SignIn = tk.Button(root, text = 'Sign in', command = GetSignInInfo, bg = 'blue', activebackground = 'blue' ,bd = 0)
    SignIn.place(anchor = tk.CENTER, x = 775, y = 350)
    SignUpBtn = tk.Button(root, text = 'Sign Up??',command = SignUp, bg = 'blue', activebackground = 'blue', bd = 0, )
    SignUpBtn.place(anchor = tk.CENTER, x = 775, y = 500)
    Killer = tk.Button(root, text = 'Quit?', command = root.destroy, bg = 'blue', bd = 0, fg = 'red', activebackground = 'red')
    Killer.place(anchor = tk.CENTER, x = 775, y = 700)

def AdminPage():
    global Adder, Read

    def ChooseToDeleteBooking():
        global TripToBeRemoved
        try:
            selected = AllBookingstree.focus()
            TripToBeRemoved = AllBookingstree.item(selected,'values')
            print(TripToBeRemoved)
        except:
            pass

    def RemoveBookingClicker(e):
        ChooseToDeleteBooking()

    def DeleteBooking():
        try:
            query = ("DELETE FROM travel WHERE id = %s AND Time = %s AND Date = %s AND FromCity = %s AND ToCity = %s")
            mycursor.execute(query,(TripToBeRemoved[0],TripToBeRemoved[1],TripToBeRemoved[2],TripToBeRemoved[3],TripToBeRemoved[4],))
            mydb.commit()
            AllBookingsViewer()
        except:
            pass

    def AllBookingsViewer():
        global AllBookingstree
        Adder.place_forget()
        Read.place_forget()
        ViewAllBookings.place_forget()
        AllBookingsText = tk.Label(root, text = 'All Current Bookings')
        AllBookingsText.place(anchor = tk.CENTER, x = 775, y = 50)
        query = "SELECT * FROM travel"
        mycursor.execute(query)
        AllBookings = mycursor.fetchall()
        AllBookingstree = ttk.Treeview(root, column = ('c1','c2','c3','c4','c5','c6','c7'), show = 'headings')
        AllBookingstree.column('#1',anchor = tk.CENTER, width = 30)
        AllBookingstree.heading('#1',text = 'id')
        AllBookingstree.column('#2',anchor = tk.CENTER, width = 110)
        AllBookingstree.heading('#2',text = 'Time(h-min)')
        AllBookingstree.column('#3',anchor = tk.CENTER, width = 120)
        AllBookingstree.heading('#3',text = 'Date(YYYY-MM-DD)')
        AllBookingstree.column('#4',anchor = tk.CENTER, width = 120)
        AllBookingstree.heading('#4',text = 'From')
        AllBookingstree.column('#5',anchor = tk.CENTER, width = 120)
        AllBookingstree.heading('#5',text = 'Destination')
        AllBookingstree.column('#6',anchor = tk.CENTER, width = 70)
        AllBookingstree.heading('#6',text = 'Class')
        AllBookingstree.column('#7',anchor = tk.CENTER, width = 65)
        AllBookingstree.heading('#7',text = 'Price(kr)')
        vrtcscrll = ttk.Scrollbar(root,orient = 'vertical',command = AllBookingstree.yview)
        AllBookingstree.config(xscrollcommand=vrtcscrll.set)
        AllBookingstree.place(anchor = tk.CENTER, x = 775 , y = 200)
        for i in AllBookings:
            AllBookingstree.insert('', tk.END, values = i)
        AllBookingstree.bind("<ButtonRelease-1>",RemoveBookingClicker)

        DeleteChosenBooking = tk.Button(root, text = 'Delete Chosen Booking', command = DeleteBooking)
        DeleteChosenBooking.place(anchor = tk.CENTER, x = 775, y = 400)
        GoBackbtn = tk.Button(root, text = 'Return', command = AdminPage)
        GoBackbtn.place(anchor = tk.CENTER, x = 775, y = 750)
        
    AdminFrame = tk.Frame(root,bg = 'purple', bd = 0,width = 2000, height = 2000)
    AdminFrame.place(x = 0, y = 0)
    Adder = tk.Button(root,text = 'Add Person?',command = SignUp)
    Adder.place(anchor = tk.CENTER, x= 775,y=50)
    Read = tk.Button(root,text = 'Print all in database?',command = Reader)
    Read.place(anchor = tk.CENTER, x= 775,y=100)
    LogOutBtn = tk.Button(root, text = 'Logout?', command = logout)
    LogOutBtn.place(anchor = tk.CENTER, x = 775, y = 800)
    Killer = tk.Button(root,text = 'Quit?', command = root.destroy)
    Killer.place(anchor = tk.CENTER,x=775,y=850)
    ViewAllBookings = tk.Button(root, text = 'View All Current Bookings', command = AllBookingsViewer)
    ViewAllBookings.place(anchor = tk.CENTER, x = 775, y = 300)
    ViewChat = tk.Button(root, text = 'Open Chat', command = ChattingFrame)
    ViewChat.place(anchor = tk.CENTER, x = 1500, y = 800)
    

def connect_to_server():
    s = so.socket()
    host = 'localhost'
    port = 12345
    s.connect((host, port))
    return s
    
def click_handler():
    msg = MessageEntry.get()
    b = msg
    c = SignInUserName + '->' + b
    d = c.encode("utf-16") 
    s.send(d)
    MessageEntry.delete(0,1000)

def ChattingFrame():
    global MessageEntry, s, tree
    Canvas.delete('all')
    s = connect_to_server()
    ChatFrame = tk.Frame(root, bg = 'gray', bd = 0, width = 2000, height = 2000)
    ChatFrame.place(x = 0, y = 0)
    MessageEntry = tk.Entry(root)
    MessageEntry.place(anchor = tk.CENTER, x = 775, y = 100)
    MessageSender = tk.Button(root, text ="Skicka", command = click_handler)
    MessageSender.place(anchor = tk.CENTER, x = 775, y = 150)
    finished = tk.Button(root,text = 'Go Back',command = quitchat)
    finished.place(anchor = tk.CENTER, x = 775, y = 700)
    tree = ttk.Treeview(root, column = ('c1'), show = 'headings', height = 20)
    tree.column('#1',anchor = tk.CENTER, width = 800)
    tree.heading('#1',text = 'message')
    vrtcscrll = ttk.Scrollbar(root,orient = 'vertical',command = tree.yview)
    tree.config(xscrollcommand=vrtcscrll.set)
    tree.place(anchor = tk.CENTER, x = 775 , y = 400)
    th.start_new_thread(receiver_thread, ())
    
def quitchat():
    c = 'xqzwy'
    d = c.encode("utf-16") 
    s.send(d)
    if AdminPrivledges >= 1:
        AdminPage()
    else:
        MainCanvas()


def receiver_thread():
    while True:
        try:
            b = s.recv(1024)
            msg = b.decode("utf-16")
        except:
            continue
        if msg == '':
            pass
        else:
            msglist = []
            msglist.append(msg)
            for i in msglist:
                tree.insert('',tk.END, values = msglist,)

def chat():
    global s
    s = connect_to_server()
    th.start_new_thread(receiver_thread, ())

def MainCanvas():
    global BookingBtn
    Canvas.delete('all')
    AdFrame = tk.Frame(root, bg = 'blue', bd = 0, width = 2000, height = 70)
    AdFrame.place(x = 0, y = 0)
    LocationFrame = tk.Frame(root,bg = 'cyan', bd = 0, width = 400, height = 2000)
    LocationFrame.place(x = 0, y = 70)
    CompanyFrame = tk.Frame(root, bg = 'yellow', bd = 0, width = 700, height = 2000)
    CompanyFrame.place(x = 400, y = 70)
    DateFrame = tk.Frame(root, bg = 'purple', bd = 0, width = 1000, height = 2000)
    DateFrame.place(x = 1100 , y = 70)

    BookingBtn = tk.Button(root, text = 'Book Train', command = BookTravel)
    BookingBtn.place(anchor = tk.CENTER, x = 75, y = 150)
    Killer = tk.Button(root,text = 'Quit?', command = root.destroy)
    Killer.place(anchor = tk.CENTER,x=775,y=850)
    LogOutBtn = tk.Button(root, text = 'Logout?', command = logout)
    LogOutBtn.place(anchor = tk.CENTER, x = 775, y = 800)
    ProfileBtn = tk.Button(root, image = ProfilePic, command = Profile)
    ProfileBtn.place(anchor = tk.CENTER, x = 1500, y = 33)
    ChatBtn = tk.Button(root, text = 'Open Chat', command = ChattingFrame)
    ChatBtn.place(anchor = tk.CENTER, x = 1500, y = 800)


LoginScreen()
root.mainloop()