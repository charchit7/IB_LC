import tkinter as tk
import time
import winsound

def increase_time():
    counter = 10
    for i in range(1,counter):
        show_timer_label['text'] = str(i)
        time.sleep(1)
        window.update()
        if i==5:
            tk.messagebox.showinfo("Time Up")

window =  tk.Tk()
window
window.rowconfigure(0, minsize=200, weight=1)
window.columnconfigure(1, minsize=400, weight=1)


btn_starttimer = tk.Button(master=window,text='START',command=increase_time)
btn_starttimer.grid(row=0, column=0, sticky="nsew")

show_timer_label = tk.Label(master=window,text='0',bg='black',fg='red',width=10,height=10)
show_timer_label.grid(row=0,column=1)




window.mainloop()
