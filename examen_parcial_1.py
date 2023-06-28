
print("seleccione que accion desea realizar: \n 1. Determinar si un numero es positivo o negativo \n 2. Almacenar numeros para saber el resultado total de la sumatoria de los mismos \n 3. Determinar la suma de los digitos de un numero")
op1 = 1
op2 = 2
op3 = 3
op = int(input("ingrese la opcion: "))
if op == 1:
    print("Programa para determinar si un numero es positivo, negativo o igual a 0")
    num =  int(input("A continuacion ingrese un numero: "))
    if num < 0:
        print("El numero ", num, " es negativo")
    elif num > 0:
        print("El numero ", num, " es positivo")
    elif num == 0:
        print("El numero ingresado es igual a: ",num)

elif op == 2:
    print("Programa para calcular la sumatoria y el promedio de los numeros de una lista.")
    lista = []
    while True:
        numeros = int(input("a continuacion ingrese numeros: "))
        lista.append(numeros)
        if numeros == 0:
            break
    print("numeros ingresados: ", lista) 
    suma = sum(lista)
    print("La sumatoria de los numeros de la lista es: ",suma)
    cantidad = len(lista)
    promedio = suma/cantidad
    print("A continuacion se verá el promedio de los numeros de la lista: ",promedio)
elif op == 3:
    print("Programa para realizar la suma de los digitos de un numero entero")
    ing_num = int(input("ingrese un numero entero con más de un digito "))
    cad_num = str(ing_num)
    suma_digit = 0

    for digitos in cad_num:
        suma_digit += int(digitos)

    print("la suma de los digitos del numero 3",ing_num,"nos da un resultado de: ",suma_digit)
 

    
