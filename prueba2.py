n=int(input("Ingrese el numero maximo: "))
for i in range (1,(n+1)): 
    if i%3==0 and i%5!=0: 
        print(str(i)+" Fizz")
    else: 
        if i%5==0 and i%3!=0: 
            print(str(i)+" Buzz")
        else: 
            if i%3==0 and i%5==0: 
                print(str(i)+" FizzBuzz")

