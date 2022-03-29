from random import randint
from traceback import print_tb
from unittest import result 
v = True
acietos=0
while v and acietos!=10: 
    op = randint(1,2)
    n1=randint(1,10)
    n2=randint(1,10)
    if op==1: 
        res = n1*n2
        print(n1,"*",n2,"=")
        resUsuario= int(input("Ingrese su respuesta: "))
        if  resUsuario==res: 
            print("Correcto")
            acietos+=1
        else:
            print("Incorrecto")
            v=False
    elif op==2:
        res=n1//n2
        print(n1,"/",n2,"=")
        resUsuario= int(input("Ingrese su respuesta: "))
        if  resUsuario==res: 
            print("Correcto")
            acietos+=1
        else:
            print("Incorrecto")
            v=False
print("Sus aciertos son:",acietos)
