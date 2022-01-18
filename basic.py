print("Cuenta regresiva")

def cuentaRegresiva(num=0):
    numeros = []
    for i in range(num,-1,-1):
        numeros.append(i)
    return numeros

print(cuentaRegresiva(5))

print("Imprimir y devolver")

def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]

valor = imprimir_y_devolver([1,2])
print(valor)

print("Primero más longitud")

def primero_mas_longitud(lista):
    return lista[0] + len(lista)

valor2 = primero_mas_longitud([1,2,3,4,5])
print(valor2)

print("Valores mayores que el segundo")

def valores_mayores_que_el_segundo(lista):
    devolver = []
    if(len(lista) < 2):
        return False
    else:
        for i in range(len(lista)):
            if (lista[i] > lista[1]):
                devolver.append(lista[i])
        return devolver

valor3 =  valores_mayores_que_el_segundo([5,2,3,2,1,4])
print(valor3)
valor4 = valores_mayores_que_el_segundo([3])
print(valor4)

print("Esta longitud, ese valor")

def length_and_value(tamanio, valor):
    resultado = []
    for i in range (tamanio):
        resultado.append(valor)
    return resultado

valor5 = length_and_value(4,7)
print(valor5)
valor6 = length_and_value(6,2)
print(valor6)