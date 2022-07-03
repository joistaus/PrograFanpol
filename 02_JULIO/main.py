
def obtener_mes(fecha):
    MESES = [
        'Enero', 
        'Febrero',
        'Marzo', 
        'Abril', 
        'Mayo',
        'Junio',
        'Julio',
        'Agosto',
        'Septiembre', 
        'Octubre',
        'Noviembre',
        'Diciembre'
    ]
    mes = int(fecha.split('-')[-1]) 
    return MESES[mes-1]


def indice_valor_maximo(lista):
    maximo = lista[0]
    idx_maximo = 0

    for i in range(len(lista)):
        elemento = lista[i]
        if elemento > maximo:
            maximo = elemento
            idx_maximo = i
    
    return idx_maximo



info_obras = [
    "Kokoro:09-07:50",
    "Mambo:16-07:60",
    "El casting:07-08:70",
    "Fiesta:15-08:50",
    "La leyenda:04-09:45",
    "Corazon:11-09:60",
    "Camino secreto:09-10:50"
]


meses = [
    'Julio',
    'Agosto',
    'Septiembre',
    'Octubre',
    'Noviembre',
    'Diciembre'
]

entradas_por_mes = [0] * len(meses)

for info in info_obras:
    obra, fecha, entradas_vendidas = info.split(':')
    entradas_vendidas = int(entradas_vendidas)
    mes_obra = obtener_mes(fecha)
    
    idx = meses.index(mes_obra)
    entradas_por_mes[idx] += entradas_vendidas


print('Número de entradas compradas en cada mes:')
for i in range(len(meses)):
    mes = meses[i]
    ventas = entradas_por_mes[i]
    print(mes, ':', ventas)



idx_valor_maximo = indice_valor_maximo(entradas_por_mes)
entradas_max = entradas_por_mes[idx_valor_maximo]
mes_max = meses[idx_valor_maximo]

print('El mes con mayor cantidad de entradas (', entradas_max, ') es', mes_max)