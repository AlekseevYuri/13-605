import tkinter
import time
import pack1
from pack1 import simpletest as st
elochka = "        W        "
def click():
    global elochka
    elochka+="\n       WWW       \n    WWWWWWW    \nWWWWWWWWWWWWW"
    a = int(q.get())
    ind.configure(background = 'grey')
    if a == 1:
        answer.configure(text="Обратимый элемент кольца")
        ind.configure(background = 'yellow')
        ind.configure(text = "!!!")
        return
    answer.configure(text="loading...")
    frame.update()
    result = st.test(a)
    score.configure(text = elochka)
    
    if result:
        answer.configure(text="Да")
        ind.configure(text = "=)")
        ind.configure(background = 'green')
    else:
        answer.configure(text="Нет")
        ind.configure(text = "=(")
        ind.configure(background = 'red')
    
    
    frame.update()


frame = tkinter.Tk()
frame.geometry('170x4000')
frame.title("Проверить на простоту")
frame

question = tkinter.Label(frame, text="Число простое?")  
question.grid(column=0, row=0)

answer = tkinter.Label(frame, text="") 
answer.grid(column=0, row=2)

ind = tkinter.Label(frame, text="???")  
ind.grid(column=0, row=5)#бессмысленное окно
ind.configure(background = 'grey') 

q = tkinter.Entry(frame)
q.focus()
q.grid(column=0, row=1,)

score = tkinter.Label(frame,text = "")
score.grid(column = 0, row = 6)



enter = tkinter.Button(frame, text="Enter", command=click)
enter.grid(column=0, row=3) 

#frame.mainloop()

