import tkinter as tk
root = tk.Tk()
def bbox():
    E = box.get()
    if E == '':
        pass
    else:
        namelist.append(E)
        print(E)
        box.delete(0,1000)

namelist = []
bg = tk.PhotoImage(file = 'nedladdning.png')
label1 = tk.Label(root,image = bg)
label1.place(x=0,y=0)
Label = tk.Label(root, text = 'hejhej')
root.geometry('500x500')
root.title('victor')
Label.grid(row = 0, column = 0)
b1 = tk.Button(root,text='no',command = bbox)
b1.grid(row = 5, column = 0,)
b2 = tk.Button(root,text='quit?',command=quit)
b2.grid(row=20,column=50)
box = tk.Entry(root)
box.grid(row = 5,column=5)
root.mainloop()
