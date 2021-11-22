import tkinter as tk
import turtle as t
root = tk.Tk()
w = tk.Canvas(root,bg = 'green',width=500,height=500)
image = tk.PhotoImage(file='nedladdning.png')
w.create_image(200,200,image=image)
w.pack()
line = w.create_line(166,0,166,500)
line = w.create_line(332,0,332,500)
line = w.create_line(0,166,500,166)
line = w.create_line(0,332,500,332)
root.mainloop()