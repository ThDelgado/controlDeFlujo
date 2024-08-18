# creando lista de 10 numeros

mylist = [1,2,3,4,5,6,7,8,9,10]

# recorriendo la lista con la sentencia for

for numero in mylist:
    if numero % 2 == 0:
        print(f"el numero" ,{numero},"es par")
    else:
        print(f"el numero" , {numero},"es impar")
        