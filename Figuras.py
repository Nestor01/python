def menu():
    print "*******************************************"
    print "*                 Figuras                 *"
    print "*******************************************"
    print "* 1. Cuadrado Vacio                       *"
    print "* 2. Cuadrado Lleno                       *"
    print "* 3. Triangulo Rectangulo Vacio  1        *"
    print "* 4. Triangulo Rectangulo Lleno  1        *"
    print "* 5. Rombo Vacio                          *"
    print "* 6. Rombo Lleno                          *"
    print "* 7. Reloj Vacio                          *"
    print "* 8. Reloj Lleno                          *"
    print "* 9. Corbata Vacio                        *"
    print "* 10. Corbata Lleno                       *"
    print "* 11. Triangulo Isoceles Vacio            *"
    print "* 12. Triangulo Isoceles Lleno            *"
    print "* 13. Triangulo Rectangulo Vacio 2        *"
    print "* 14. Triangulo Rectangulo Lleno 2        *"
    print "* 15. Triangulo Rectangulo Vacio 3        *"
    print "* 16. Triangulo Rectangulo Lleno 3        *"
    print "* 17. Triangulo Rectangulo Vacio 4        *"
    print "* 18. Triangulo Rectangulo Lleno 4        *"
    print "*******************************************"
    print "* 19. Salir                               *"
    print "*******************************************"
    f=input("Digite opcion (1-19): ")
    if f==1:
        n=input("digite numero: ")
        print "*"*n
        for i in range(n-2):
            print "*"+(" "*(n-2))+"*"
        print "*"*n
        menu()
    elif f==2:
        n=input("digite numero: ")
        for i in range(n):
            print "*"*n
        menu()
    elif f==3:
        n=input("digite numero: ")
        print "*"
        for i in range(n-2):
            print "*"+(" "*(i))+"*"
        print "*"*n
        menu()
    elif f==4:
        n=input("digite numero: ")
        for i in range(n):
            print "*"*i
        menu()
    elif f==5:
        n=input("digite numero: ")
        print " "*n+"*"
        for i in range (1,n):
            print (n-i)*" "+"*"+(2*i-1)*" "+"*"
        for i in range (1,n):
            print (i)*" "+"*"+(2*(n-i)-1)*" "+"*"
        print " "*n+"*"
        menu()
    elif f==6:
        n=input("digite numero: ")
        for i in range (1,n):
            print (n-i)*" "+((i)*"* ")
        for i in range (1,n):
            print (i)*" "+(((n-i))*"* ")
        menu()
    elif f==7:
        n=input("digite numero: ")
        for i in range (n):
            print "*",
        print "*"
        for i in range (1,n):
            print (i)*" "+"*"+(2*(n-i)-1)*" "+"*"
        print " "*n+"*"
        for i in range (1,n):
            print (n-i)*" "+"*"+(2*i-1)*" "+"*"
        for i in range (n):
            print "*",
        print "*"
        menu()
    elif f==8:
        n=input("digite numero: ")
        for i in range (0,n):
            print (i)*" "+((n-i))*"* "
        for i in range (2,n+1):
            print (n-i)*" "+(i)*"* "
        menu()
    elif f==9:
        n=input("digite numero: ")
        print "*"+("  "*(n-2))+"*"
        for i in range (2,n-1):
            print "*"+(i-2)*" "+"*"+(2*(n-i)-1)*" "+"*"+(" "*(i-2))+"*"
        print "*"+" "*(n-2)+"*"+(" "*(n-2))+"*"
        for i in range (2,n-1):
            print "*"+((n-i)-2)*" "+"*"+(2*i-1)*" "+"*"+(" "*((n-i)-2))+"*"
        print "*"+("  "*(n-2))+"*"
        menu()
    elif f==10:
        n=input("digite numero: ")
        for i in range (1,n):
            print (i)*"*"+(2*(n-i)-1)*" "+("*"*i)
        print "*"*n+"*"+("*"*(n-2))
        for i in range (1,n):
            print (n-i)*"*"+(2*i-1)*" "+("*"*(n-i))
        menu()
    elif f==11:
        n=input("digite numero: ")
        print " "*n+"*"
        for i in range (1,n):
            print (n-i)*" "+"*"+(2*i-1)*" "+"*"
        for i in range (n):
            print "*",
        print "*"
        menu()
    elif f==12:
        n=input("digite numero: ")
        for i in range (1,n+1):
            print (n-i)*" "+(i)*"* "
        menu()
    elif f==13:
        n=input("digite numero: ")
        for i in range(n,0,-1):
            print i*"*"
        menu()
    elif f==14:
        n=input("digite numero: ")
        print n*"*"
        for i in range(n-1,1,-1):
            print "*"+(i-2)*" "+"*"
        print "*"
        menu()
    elif f==15:
        n=input("digite numero: ")
        for i in range(1,n):
            print (n-i)*" "+i*"*"
        menu()
    elif f==16:
        n=input("digite numero: ")
        print " "*(n-1)+"*"
        for i in range(2,n):
            print (n-i)*" "+"*"+(i-2)*" "+"*"
        print n*"*"
        menu()
    elif f==17:
        n=input("digite numero: ")
        for i in range(n,0,-1):
            print " "*(n-i)+i*"*"
        menu()
    elif f==18:
        n=input("digite numero: ")
        print n*"*"
        for i in range(n-1,1,-1):
            print " "*(n-i)+"*"+(i-2)*" "+"*"
        print " "*(n-1)+"*"
        menu()
    elif f==19:
        print "vuelve pronto"
    else:
        print "error"
        menu()
menu()
