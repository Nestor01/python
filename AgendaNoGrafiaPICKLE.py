import pickle
from string import capwords
def menu():
    print "****************************************************"
    print "         Base de Datos de la Biblioteca            *"
    print "****************************************************"
    print " 1. Agregar Libro                                  *"
    print " 2. Eliminar Libro                                 *"
    print " 3. Modificar Informacion del Libro                *"
    print " 4. Mostrar todo                                   *"
    print " 5. Buscar Libro                                   *"
    print "****************************************************"
    print " 6. Salir                                          *"
    print "****************************************************"
    a=input("Digite numero de opcion a ejecutar: ")
    if a==1:
        agregar()
    elif a==2:
        eliminar()
    elif a==3:
        modificar()
    elif a==4:
        mostrartodo()
    elif a==5:
        buscar()
    elif a==6:
        print "vuelva pronto"
    else:
        print "Error"
        menu()
def agregar():
    n=capwords(raw_input("Digite Nombre del Libro: "))
    au=capwords(raw_input("Digite Autor del Libro: "))
    e=capwords(raw_input("Digite Editorial del Libro: "))
    w=raw_input("Digite A;o de Publicacion: ")
    r=raw_input("Digite una rese;a del Libro: ")
    p=raw_input("Digite Precio del Libro: ")
    l=capwords(raw_input("Digite Idioma del Libro: "))
    d[str(len(d))]=n+"*"+au+"*"+e+"*"+w+"*"+r+"*"+p+"*"+l
    menu()
def eliminar():
    n=capwords(raw_input('Digite nombre o autor que quiere eliminar: '))
    for i in ag.keys():
        if n in d[i]:
            del(d[i])
    menu()
def modificar():
    f=capwords(raw_input("Digite Nombre o autor: "))
    print "****************************************************"
    print "                  Buscar Libro(s)                  *"
    print "****************************************************"
    print " 1. Modificar Nombre                               *"
    print " 2. Modificar Autor                                *"
    print " 3. Modificar Editorial                            *"
    print " 4. Modificar A;o                                  *"
    print " 5. Modificar Rese:a                               *"
    print " 6. Modificar Precio                               *"
    print " 7. Modificar Idioma                               *"
    print "****************************************************"
    print " 8. Volver                                         *"
    print "****************************************************"
    b=input("Digite numero de opcion a ejecutar: ")
    fg=capwords(raw_input("Digite Dato nuevo: "))
    au=[]
    for i in d.keys():
        if f in d[i]:
            au=d[i].split("*")
            a=i
    if b==1:
        au[0]=fg
        menu()
    elif b==2:
        au[1]=fg
        menu()
    elif b==3:
        au[2]=fg
        menu()
    elif b==4:
        au[3]=fg
        menu()
    elif b==5:
        au[4]=fg
        menu()
    elif b==6:
        au[5]=fg
        menu()
    elif b==7:
        au[6]=fg
        menu()
    elif b==8:
        menu()
    else:
        print "Error"
        modificar()
    d[a]=au[0]+"*"+au[1]+"*"+au[2]+"*"+au[3]+"*"+au[4]+"*"+au[5]+"*"+au[6]
def mostrartodo():
    au=[]
    for i in d.keys():
        print "-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o--o-o-o-o-o-o-o--o"
        au=d[i].split("*")
        for j in au:
            print j
    menu()
def buscar():
    l=capwords(raw_input("Digite Autor: "))
    au=[]
    m=1
    for i in d.keys():
        if l in d[i]:
            au=d[i].split("*")
        else:
            print "No esta registrado"
            m=0
    if m==1:
        for j in au:
            print j
    menu()
try:
    ag=open('datos.pick','r')
    d=pickle.load(f)
    ag.close()
except:
    ag=open('datos.pick','w')
    d={}
    ag.close()

menu()
ag=open('datos.pick','w')
pickle.dump(d,f)
