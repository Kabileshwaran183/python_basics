from tkinter import *

window = Tk()
window.title("My First Program")
window.minsize(500,600)

My_label = Label(text="something",font=("Arial",20,"bold"))
My_label.pack()
print(type(My_label))
My_label["text"] = "hii.."
My_label.config(text="hii...")

def button_click():
    print('button got clicked')
    new_text = input.get()
    My_label.config(text=new_text)

button = Button(text="click",command=button_click)
button.pack()

input=Entry()
input.pack()






window.mainloop()