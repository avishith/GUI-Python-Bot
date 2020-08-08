from tkinter import *
root=Tk()
#root.geometry('2000x800')
ABC=Frame(root,bg='#010101',bd=20,relief=RIDGE)
ABC.grid()

ABC1=Frame(root,bd=20,)
ABC1.grid()


def bot_reply(msg):
    txt =Text(ABC,height=2,width=40,padx=10,pady=10)
    txt.tag_config("right", justify="right")
    txt.pack()
    a=msg+" <== Bot"
    txt.insert(END,"\n"+a,"right")
    txt.config(state=DISABLED)
    e['text']=''

def sent():

  txt =Text(ABC,height=2,width=40,padx=10,pady=10)

  txt.tag_config("right", justify="right")
  txt.pack()
  v=e.get()
  sent="You => " + v
  txt.insert(END,"\n"+sent)

  if v=='hai':
     root.after(2000, bot_reply, 'hello')
  if v=='hello':
  	root.after(2000, bot_reply, 'hai')
  if v=='how are you':
  	root.after(2000, bot_reply, 'fine..')
  if v=='name':
  	root.after(2000, bot_reply, 'PyBot..')


#txt.tag_configure("green", foreground="green")

#txt.grid(column=0,row=0)

e=Entry(ABC1,width=30,bd=2,insertwidth=5,font=("aril",7))
e.grid(row=1,column=0)
b=Button(ABC1,text='sent',command=sent)
b.grid(row=1,column=1)
root.mainloop()