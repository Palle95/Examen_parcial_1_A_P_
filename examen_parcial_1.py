#algoritmo para ingresar un numero entero 
print("seleccione que accion desea realizar: 1.determinar si un numero es positivo o negativo \n 2. almacenar numeros para saber el resultado total de la sumatoria de los mismos ")
 
op1 = 1
op2 = 2
op = int(input("ingrese la opcion: "))
if op == 1:

    num =  int(input("A continuacion ingrese un numero: "))

    if num < 0:
        print("El numero ",num, " es negativo")
    elif num > 0:
        print("El numero ", num, " es positivo")
    elif num == 0:
        print("El numero ingresado es igual a: ",num)
elif op == 2:
    print("programa para calcular la sumatoria y el promedio")
    
    
    lista = []
    while True:
        numeros = int(input("a continuacion ingrese numeros: "))
        lista.append(numeros)
        if numeros == 0:
            break
    
print("numeros ingresados: ", lista)

    
