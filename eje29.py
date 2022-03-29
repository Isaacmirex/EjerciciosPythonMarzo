def imprimir(dic): 
    for indice in dic: 
        print("Producto: ",indice,"Precio: ",dic[indice])
dic={}
dic["pan"]=.12
menu=True 
total=0
while menu: 
    op = int(input("Elija una opcion\n1.-Agregar Producto\n2._Factura\n3.-Salir\n"))
    if op==1:
        indice = input("Ingrese un Producto: ")
        valor = float(input("Ingrese un valor: "))
        dic[indice]=valor
        print(dic)
    elif op==2: 
        factura= True
        while factura: 
            imprimir(dic)
            print("Elija una op\n1.-Agregar a factura\n2.-finalizar")
            opf= int(input("Ingrese opcion "))
            if opf==1:
                indice = input("Ingrese un Producto: ")
                cantidad = int(input("Ingrese un valor: "))
                total+=dic.get(indice)*cantidad
                print("El total es: ",total)
            else: 
                factura=False
                total = 0      
    elif op==3:
        menu = False
    else: 
        print("Ingrese una opcion valida")