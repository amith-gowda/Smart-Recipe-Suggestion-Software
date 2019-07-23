#GUI for cocinero
import tkinter
window=tkinter.Tk()

Label(window, text='Enter number of ingredients').grid(row=0) 
Label(window, text='Enter ingredients').grid(row=1) 
e1 = Entry(window) 
e2 = Entry(window) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 

window.mainloop()