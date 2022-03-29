from random import randint
def llenarSec(n): 
    lista=[]
    for i in range(1,(n+1)): 
        lista+=[i]
    return lista
def llenarAle(n):
    listaA=[]
    num = randint(1,n)
    listaA+=[num] 
    for i in range(n-1): 
        while num in listaA:
             num= randint(1,n)
        listaA+=[num]
    return listaA
listaA=llenarSec(10)
listaB=llenarAle(10)
for i in range (len(listaA)): 
    print("A la persona: ",listaA[i]," Es pareja con ",listaB[i])
print(listaA)
print(listaB)

