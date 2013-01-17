#Agenda Segundo periodo
def agenda():
    print "*******************************************"
    print "*                 Agenda                  *"
    print "*******************************************"
    print "* 1. Anadir Contacto                      *"
    print "* 2. Modificar Contacto                   *"
    print "* 3. Eliminar Contacto                    *"
    print "* 4. Buscar Contacto                      *"
    print "*******************************************"
    print "* 5. Salir                                *"
    print "*******************************************"
    m=input("Digite opcion: ")
    if m==1:
        agregar()
        agenda()
    elif m==2:
        l1=raw_input("Digite apellido en mayusculas del usuario a editar: ")
        editar(l1)
        agenda()
    elif m==3:
        eliminar()
        agenda()
    elif m==4:
        buscar()
        agenda()
    elif m==5:
        print "vuelve pronto"
    else:
        print "Error"
        agenda()
def editar(r):
    print "*******************************************"
    print "*                 Agenda                  *"
    print "*******************************************"
    print "* 1. Nombre del Contacto                  *"
    print "* 2. Apellidos del Contacto                *"
    print "* 3. Telefono del Contacto                *"
    print "* 4. E-mail del Contacto                  *"
    print "* 5. Direccion del Contacto               *"
    print "* 6. Fecha de nacimiento del Contacto     *"
    print "* 7. Hobbie del Contacto                  *"
    print "*******************************************"
    m1=input("digite opcion: ")
    print "RECUERDE QUE TODOS LOS DATOS DEBEN IR EN MAYUSCULA"
    if m1==1:
        m=raw_input("Digite antiguo nombre: ")
        f=raw_input("Digite nuevo nombre: ")
        r="Nombre: "+m
        nr="Nombre: "+f
        editar1(r,nr)
    elif m1==2:
        m=raw_input("Digite antiguo apellido: ")
        f=raw_input("Digite nuevo apellido: ")
        editar1(r,f)
        r="Apellido: "+m
        nr="Apellido: "+f
        editar1(r,nr)
    elif m1==3:
        m=raw_input("Digite antiguo telefono: ")
        f=raw_input("Digite nuevo telefono: ")
        r="Numero de Telefono: "+m
        nr="Numero de Telefono: "+f
        editar1(r,nr)
    elif m1==4:
        m=raw_input("Digite antiguo E-mail (no colocar en mayuscula si no lo es necesario): ")
        f=raw_input("Digite nuevo E-mail (no colocar en mayuscula si no lo es necesario): ")
        r="Email: "+m
        nr="Email: "+f
        editar1(r,nr)
    elif m1==5:
        m=raw_input("Digite antiguo direccion: ")
        f=raw_input("Digite nuevo direccion: ")
        r="Direccion: "+m
        nr="Direccion: "+f
        editar1(r,nr)
    elif m1==6:
        m=raw_input("Digite antigua fecha de nacimiento: ")
        f=raw_input("Digite nuevo fecha de nacimiento: ")
        r="Fecha de nacimiento: "+m
        nr="Fecha de nacimiento: "+f
        editar1(r,nr)
    elif m1==7:
        m=raw_input("Digite antiguo hobbie: ")
        f=raw_input("Digite nuevo hobbie: ")
        r="Hobbie: "+m
        nr="Hobbie: "+f
        editar1(r,nr)
    we=raw_input("Desea editar algun otoro dato? (Y/N) ")
    if we=="Y" or we=="y":
        editar(r)
def agregar():
      print "RECUERDE QUE TODOS LOS DATOS DEBEN IR EN MAYUSCULA"
      gf=open('archivo.txt', 'a')
      d=raw_input("Digite Apellido: ")
      gf.write(d+"\n")
      n=raw_input("Digite Nombre: ")
      n1="Nombre: "+n
      gf.write(n1+"\n")
      d1="Apellido: "+d
      gf.write(d1+"\n")
      f=raw_input("Digite Telefono: ")
      f1="Numero de Telefono: "+f
      gf.write(f1+"\n")
      h=raw_input("Digite Direccion: ")
      h1="Direccion: "+h
      gf.write(h1+"\n")
      g=raw_input("Digite E-mail(no colocar en mayuscula si no lo es necesario): ")
      g1="Email: "+g
      gf.write(g1+"\n")
      j=raw_input("Digite Fecha de nacimiento: ")
      j1="Fecha de nacimiento: "+j
      gf.write(j1+"\n")
      l=raw_input("Digite Hobbie: ")
      l1="Hobbie: "+l
      gf.write(l1+"\n")
      gf.close()
      r=raw_input("Desea agragar otro contacto? (Y/N) ")
      if r=="y" or r=="Y":
          agregar()
def buscar():
    a=open("archivo.txt","r")
    l=[]
    r= raw_input ("Digite el apellido de la persona en mayusculas: ")
    for u in a:
        l.append(u)
    m=0
    h=0
    for i in l:
        if len(r)==len(i)-1:
            for g in range(len(r)):
                if r[g] == i[g]:
                    h+=1
            if h==(len(r)):
                for j in range(m+1,m+8):
                    print l[j]
                break
            elif m==len(l)-1:
                print "No se encuentra"
            else:
                h=0
        elif m==len(l)-1:
            print "No se encuentra"
            h=0
        m+=1
    a.close()
def eliminar():
    a=open("archivo.txt","r")
    l=[]
    r= raw_input ("Digite el apellido de la persona a eliminar en mayusculas: ")
    for u in a:
        l.append(u)
    m=0
    h=0
    for i in l:
        if len(r)==len(i)-1:
            for g in range(len(r)):
                if r[g] == i[g]:
                    h+=1
            if h==(len(r)):
                for i in range(m,m+8):
                    l[i]=""
                print "Ha sido eliminado con exito!"
                break
            elif m==len(l)-1:
                print "No Existe"
            else:
                h=0
        elif m==len(l)-1:
            print "No Existe"
            h=0
        m+=1
    a.close()
    a=open("archivo.txt","w")
    for i in l:
        a.write(i)
    a.close()
def editar1(r,nr):
    a=open("archivo.txt","r")
    l=[]
    for u in a:
        l.append(u)
    m=0
    h=0
    for i in l:
        if len(r)==len(i)-1:
            for g in range(len(r)):
                if r[g] == i[g]:
                    h+=1
            if h==(len(r)):
                l[m]=nr+"\n"
                print "Ha sido reemplazado con exito!"
                break
            elif m==len(l)-1:
                print "No Existe"
            else:
                h=0
        elif m==len(l)-1:
            print "No Existe"
            h=0
        m+=1
    a=open("archivo.txt","w")
    for i in l:
        a.write(i)
    a.close()
agenda()
