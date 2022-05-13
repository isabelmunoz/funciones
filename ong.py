def factorial(numero):
    total = 1
    for secuencial in range(1, numero + 1):
        total *= secuencial
    return total

def productoria(lista_numeros = []):
    total = 1
    for numero in lista_numeros:
        total *= numero
    return total


def calcular(**kwargs):
    for key, value in kwargs.items():
        if 'fact' in key:
            print(f'El factorial de {value} es {factorial(value)}')
        elif 'prod' in key:
            print(f'La productoria de {value} es {productoria(value)}')

calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)