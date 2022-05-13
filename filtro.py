import sys

precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtro_mayores_que(umbral):
    productos_mayores_que = {}
    for key, value in precios.items():
        if value > umbral:
            productos_mayores_que[key] = value
    return productos_mayores_que


def filtro_mayores_menores(umbral, direccion):
    productos_cumplen = {}
    if direccion =='mayor':
       productos_cumplen = filtro_mayores_que(umbral)
    else:
        for key, value in precios.items():
            if value < umbral:
                productos_cumplen[key] = value
    return productos_cumplen


def validar_entrada(cadena):
    estado = True
    if cadena != 'menor' and cadena !='mayor':
        estado = False
    return estado

def filtrado(largo):
    if largo == 3:
        umbral = int(sys.argv[1])
        direccion = sys.argv[2]
        if validar_entrada(direccion):
            lista = list(filtro_mayores_menores(umbral, direccion).keys())
            print(f'Los productos {direccion}es al umbral son {", ".join(lista)}')
        else:
            print('Lo sentimos, no es una operación válida')
    elif largo == 2:
        umbral = int(sys.argv[1])
        print(f'Los productos mayores al umbral son: {", ".join(list(filtro_mayores_que(umbral).keys()))}')

filtrado(len(sys.argv))