from os import supports_bytes_environ


dias= int(input("Ingrese los dias"))
años= dias//365
meses= (dias%365) //30
semanas= (dias-(años*365+meses*30))//7
dias2 =  dias-(años*365+meses*30+semanas*7)
print ("Los dias son: ",str(dias),"las semans son:",str(semanas)," Los años son:",str(años),"Los dias son: ",dias2)