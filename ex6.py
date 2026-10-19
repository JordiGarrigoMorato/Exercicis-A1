(a) = int (input ("Ingrese un número del 1 al 10 : "))
if (a) < 1 or (a) > 10:
    print ("El número ingresado no está en el rango permitido")
else:
    for i in range (1, 11):
        print (a, "x", i, "=", a * i)
