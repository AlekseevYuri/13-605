import tkinter

def vvod(x):
    
    def click():

        try:
            a = int(q.get())
        except:
            a = 1

        frame.destroy()
        
        x(a)#Делает функцию х от вводимого с клавиатуры числа. Больше ничего не делает.
        
        vvod(x)



    frame = tkinter.Tk()
    frame.geometry('300x200')
    frame.title("Введите число")
    frame

    q = tkinter.Entry(frame)
    q.focus()
    q.grid(column=0, row=0,)
    q.place(x=80,y=40)

    enter = tkinter.Button(frame, text="Enter", command=click)
    enter.grid(column=1, row=0) 
    enter.place(x=120,y=80)

    leave = tkinter.Button(frame, text="Quit", command=quit)
    leave.grid(column=1, row=0) 
    leave.place(x=120,y=160)




