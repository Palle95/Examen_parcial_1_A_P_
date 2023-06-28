#algoritmo para ingresar un numero entero 
num =  int(input("A continuacion ingrese un numero: "))
if num < 0:
    print("El numero ",num, " es negativo")
elif num > 0:
    print("El numero ", num, " es positivo")
elif num == 0:
    print("El numero ingresado es igual a: ",num)
