from tkinter import *
root=Tk()
#root.geometry('2000x800')
ABC=Frame(root,bg='#010101',bd=20,relief=RIDGE)
ABC.grid()

def sent():
#	root=Tk()
	txt=Text(ABC,height=2,width=40,padx=10,pady=10)
	txt.tag_config("right", justify="right")
	txt.pack()
	
	#txt.config(state=NORMAL)
	
	
	v=e.get()
	sent="You => " + v
	txt.insert(END,"\n"+sent)

	
	if v=='hai':
		txt=Text(ABC,height=2,width=40,padx=10,pady=10)
		txt.tag_config("right", justify="right")
		txt.pack()
		a='hello'+" <== Bot "
		txt.insert(END,"\n"+a,"right")
		txt.config(state=DISABLED)
	if v=='Da':
		txt=Text(ABC,height=2,width=40,padx=10,pady=10)
		txt.tag_config("right", justify="right")
		txt.pack()		
		a='Aah da para'+" <== Bot "
		txt.insert(END,"\n"+a,"right")
		txt.config(state=DISABLED)
	if v=='evidey ya':
		txt=Text(ABC,height=2,width=40,padx=10,pady=10)
		txt.tag_config("right", justify="right")
		txt.pack()
		a='evidey oke tanne ind da'
		txt.insert(END,"\n"+a,"right")
		txt.config(state=DISABLED)
	if v=='ninte ammadey peru ntha':
		txt=Text(ABC,height=2,width=40,padx=10,pady=10)
		txt.tag_config("right", justify="right")
		txt.pack()
		a='shaliya'+" <== Bot "
		txt.insert(END,"\n"+a,"right")
		txt.config(state=DISABLED)
	if v=='pinne ntha':
		txt=Text(ABC,height=2,width=40,padx=10,pady=10)
		txt.tag_config("right", justify="right")
		txt.pack()
		a='sugam'+" <== Bot "
		#txt.insert(END,"\n"+a,'right')
		txt.insert(END, "\n"+a, "right")
		txt.config(state=DISABLED)
	e.delete(0,END)
	
	
ABC1=Frame(root,bd=20,)
ABC1.grid()



#txt.tag_configure("green", foreground="green")

#txt.grid(column=0,row=0)

e=Entry(ABC1,width=30,bd=2,insertwidth=5,font=("aril",7))
e.grid(row=1,column=0)
b=Button(ABC1,text='sent',command=sent)
b.grid(row=1,column=1)
root.mainloop()