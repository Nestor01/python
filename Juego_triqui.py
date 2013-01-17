from Tkinter import *
from string import capwords
import anydbm
import tkMessageBox
root=Tk(className="Triqui")
jugador2= StringVar()
jugador1= StringVar()
def jugar():
    root.destroy()
    juego=Tk(className="Triqui")
    def jugada():
        if m[0][0]==m[0][1] and m[0][1]==m[0][2] and m[0][0]!=2:
            return m[0][0]
        if m[1][0]==m[1][1] and m[1][1]==m[1][2] and m[1][0]!=2:
            return m[1][1]
        if m[2][0]==m[2][1] and m[2][1]==m[2][2] and m[2][0]!=2:
            return m[2][2]
        if m[0][0]==m[1][1] and m[1][1]==m[2][2] and m[0][0]!=2:
            return m[0][0]
        if m[0][0]==m[1][0] and m[1][0]==m[2][0] and m[0][0]!=2:
            return m[0][0]
        if m[0][1]==m[1][1] and m[1][1]==m[2][1] and m[0][1]!=2:
            return m[1][1]
        if m[0][2]==m[1][2] and m[1][2]==m[2][2] and m[0][2]!=2:
            return m[2][2]
        if m[0][2]==m[1][1] and m[1][1]==m[2][0] and m[0][2]!=2:
            return m[2][0]
        else:
            return 2
    m=[[2,2,2],[2,2,2],[2,2,2]]
    n=0
    gana=2
    
    fg= StringVar()
    g=Entry(juego,bd=1,textvariable=fg,width=3)
    g.grid(row=1,column=1)  
    
    fg1= StringVar()
    g=Entry(juego,bd=1,textvariable=fg1,width=3)
    g.grid(row=1,column=2)
    
    fg2= StringVar()
    g=Entry(juego,bd=1,textvariable=fg2,width=3)
    g.grid(row=1,column=3)
    
    fg3= StringVar()
    g=Entry(juego,bd=1,textvariable=fg3,width=3)
    g.grid(row=2,column=1)
    
    fg4= StringVar()
    g=Entry(juego,bd=1,textvariable=fg4,width=3)
    g.grid(row=2,column=2)
    
    fg5= StringVar()
    g=Entry(juego,bd=1,textvariable=fg5,width=3)
    g.grid(row=2,column=3)
    
    fg6= StringVar()
    g=Entry(juego,bd=1,textvariable=fg6,width=3)
    g.grid(row=3,column=1)
    
    fg7= StringVar()
    g=Entry(juego,bd=1,textvariable=fg7,width=3)
    g.grid(row=3,column=2)
    
    fg8= StringVar()
    g=Entry(juego,bd=1,textvariable=fg8,width=3)
    g.grid(row=3,column=3)

    m12= Label( juego, text="Jugador 1: "+capwords(jugador1.get())+" 0 \n Jugador 2: "+capwords(jugador2.get())+" 1" )
    m12.grid(row=1,rowspan=4,column=4)
    
    def menu(n):
        if fg.get()=='1' or fg.get()=='0':
            m[0][0]=fg.get()
        if fg1.get()=='1' or fg1.get()=='0':
            m[0][1]=fg1.get()
        if fg2.get()=='1' or fg2.get()=='0':
            m[0][2]=fg2.get()
        if fg3.get()=='1' or fg3.get()=='0':
            m[1][0]=fg3.get()
        if fg4.get()=='1' or fg4.get()=='0':
            m[1][1]=fg4.get()
        if fg5.get()=='1' or fg5.get()=='0':
            m[1][2]=fg5.get()
        if fg6.get()=='1' or fg6.get()=='0':
            m[2][0]=fg6.get()
        if fg7.get()=='1' or fg7.get()=='0':
            m[2][1]=fg7.get()
        if fg8.get()=='1' or fg8.get()=='0':
            m[2][2]=fg8.get()
        gana=jugada()
        if gana=='0':
            tkMessageBox.showinfo("Felicitaciones!", "Ha Ganado el Jugador "+capwords(jugador1.get()))
        elif gana=='1':
            tkMessageBox.showinfo("Felicitaciones!", "Ha Ganado el Jugador "+capwords(jugador2.get()))
        else:
            f=0
            for i in m:
                if i==2:
                    f+=1
            if f==0:
                tkMessageBox.showinfo("Empate", "Jugada Terminada")
            #menu(f,n)
    def menu1():
        menu(n)
    Jugar = Button(juego, text="Jugada!", width=9, command=menu1)
    Jugar.grid(row=4,columnspan=4)
    menubar = Menu(juego)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Salir", command=juego.destroy)
    menubar.add_cascade(label="Archivo", menu=filemenu)
    juego.config(menu=menubar)
    
    juego.mainloop()
def nuevojuego():
    m=Label(root,text="Digite Su Nombre: ")
    m.grid(row=1,column=1,sticky='W')
    g=Entry(root,bd=1,textvariable=jugador1)
    g.grid(row=1,column=2)
    
    m=Label(root,text="Digite Su Nombre: ")
    m.grid(row=2,column=1,sticky='W')
    g=Entry(root,bd=1,textvariable=jugador2)
    g.grid(row=2,column=2)
    
    Jugar = Button(root, text="Jugar", width=20, command=jugar)
    Jugar.grid(row=3,column=2)
    
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Nuevo Juego", command=nuevojuego)
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=root.destroy)
    menubar.add_cascade(label="Archivo", menu=filemenu)
    root.config(menu=menubar)
    
    root.mainloop()
nuevojuego()
