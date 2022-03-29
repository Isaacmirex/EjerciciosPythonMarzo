htrabajo=int(input("ingreso de horas"))
jornada=48
pagoHora=2
pagoExtra=3.5
pago=0
if  htrabajo<=48 and htrabajo>0:
    pago=htrabajo*pagoHora
else:
    if htrabajo>48: 
        pago=(48*pagoHora)+((htrabajo-48)*pagoExtra)
    else:
        pago=0

print ("El pago es: ",pago)

    