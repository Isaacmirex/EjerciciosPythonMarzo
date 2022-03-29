a=int(input("ingrese el numero 1"))
b=int(input("ingrese el numero 2"))
c=int(input("ingrese el numero 3"))
if a==b==c:
    print("Los tres numeros son iguales")
elif a==b or b==c or a==c: 
    print ("Dos numeros iguales")
else:
    print("Todos los numeros son iguales")