# Constantes
PAISES = ('Argentina', 'Bolivia', 'Brasil', 'Chile', 'Paraguay', 'Uruguay', 'Otro')
REGIONES_BRASIL = ('0-1-2-3', '4-5-6-7', '8-9')
IDENITFICADOR_PROVINCIA_ARG = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                                'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 
                                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

PRECIOS = (1100, 1800, 2450, 8300, 10900, 14300, 17900)

# Variables finales
destino = ''
inicial = 0
final = 0

# Variables temporales
region_brasil = ''
esMontevideo = False

def validar_pais_destino(codigo_postal):
    if len(codigo_postal) == 8 and codigo_postal[0].isalpha() and codigo_postal[1:5].isnumeric() and codigo_postal[5:9].isalpha():
        destino = PAISES[0]

    ## Bolivia
    if len(codigo_postal) == 4 and codigo_postal[0:].isnumeric():
        destino = PAISES[1]

    ## Brasil
    if len(codigo_postal) == 9 and codigo_postal[0:5].isnumeric() and codigo_postal[6:9].isnumeric():
        if codigo_postal[5] == '-':
            destino = PAISES[2]
            if codigo_postal[0] == '0' or codigo_postal[0] == '1' or codigo_postal[0] == '2' or codigo_postal[0] == '3':
                region_brasil = REGIONES_BRASIL[0]
            if codigo_postal[0] == '4' or codigo_postal[0] == '5' or codigo_postal[0] == '6' or codigo_postal[0] == '7':
                region_brasil = REGIONES_BRASIL[1]
            if codigo_postal[0] == '8' or codigo_postal[0] == '9':
                region_brasil = REGIONES_BRASIL[2]

    ## Chile
    if len(codigo_postal) == 7 and codigo_postal[0:].isnumeric():
        destino = PAISES[3]

    ## Paraguay
    if len(codigo_postal) == 6 and codigo_postal[0:].isnumeric():
        destino = PAISES[4]

    ## Uruguay
    if len(codigo_postal) == 5 and codigo_postal[0:].isnumeric():
        destino = PAISES[5]
        if codigo_postal[0:2] == '11':
            esMontevideo = True

    ## Otro
    if destino == '':
        destino = PAISES[6]


def asignar_precio_tipo(tipo):
    if tipo == 0:
        inicial = PRECIOS[0]
    if tipo == 1:
        inicial = PRECIOS[1]
    if tipo == 2:
        inicial = PRECIOS[2]
    if tipo == 3:
        inicial = PRECIOS[3]
    if tipo == 4:
        inicial = PRECIOS[4]
    if tipo == 5:
        inicial = PRECIOS[5]
    if tipo == 6:
        inicial = PRECIOS[6]


def validar_envio_internacional():
    if (destino == PAISES[1] 
        or destino == PAISES[4] 
        or esMontevideo
        or region_brasil == REGIONES_BRASIL[2]):
        inicial *= 1.20
    
    if (destino == PAISES[3]
        or (destino == PAISES[5] and not esMontevideo)
        or region_brasil == REGIONES_BRASIL[0]):
        inicial *= 1.25
    
    if region_brasil == REGIONES_BRASIL[1]:
        inicial *= 1.30
    
    if destino == PAISES[6]:
        inicial *= 1.50
    
    
inicial = int(inicial)


## APLICAR PRECIO FINAL
final = inicial

# Aplicar 10% de descuento
if pago == 1:
    final = inicial * 0.90

final = int(final)

# script principal
destino = validar_pais_destino()