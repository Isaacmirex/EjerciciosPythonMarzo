from tokenize import Double


saldo=0
op=0
while(op!=3): 
    op=int(input("Ingrese opcion: \n1.-Deposito\n2.-Retiro\n3.-Salir\nIngrese opcion "))
    if op<0 or op>3: 
        print("Opcion no valida")
        continue
    if op==1: 
        deposito=float(input("Ingrese valor a depositar: "))
        saldo+=deposito
    elif op==2: 
        retiro=float(input("Ingrese valor a Retirat: "))
        if retiro>saldo:
            print("No puede retirar el saldo")
        else:
            saldo-=retiro
    elif op==3:
        print("Saliendin...")
print("Su saldo es: ",saldo)
