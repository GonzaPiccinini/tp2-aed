# Constantes
PAISES = ('Argentina', 'Bolivia', 'Brasil', 'Chile', 'Paraguay', 'Uruguay', 'Otro')
REGIONES_BRASIL = ('0-1-2-3', '4-5-6-7', '8-9')
IDENITFICADOR_PROVINCIA_ARG = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                                'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 
                                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
PROVINCIAS_ARG = ('Salta',
                   'Provincia de Buenos Aires',
                   'Ciudad Autónoma de Buenos Aires',
                   'San Luis', 'Entre Ríos', 'La Rioja',
                   'Santiago del Estero',
                   'Chaco', 'San Juan',
                   'Catamarca', 'La Pampa',
                   'Mendoza', 'Misiones', 'Formosa', 'Neuquén',
                   'Río Negro','Santa Fe', 'Tucumán', 'Chubut',
                   'Tierra del Fuego', 'Corrientes', 'Córdoba',
                   'Jujuy', 'Santa Cruz')

PRECIOS = (1100, 1800, 2450, 8300, 10900, 14300, 17900)

# Variables finales
inicial = 0
final = 0

# Variables temporales
if len(cp) == 8 and cp[0].isalpha() and cp[1:5].isnumeric() and cp[5:9].isalpha():
    destino = PAISES[0]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[0]:
        provincia = PROVINCIAS_ARG[0]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[1]:
        provincia = PROVINCIAS_ARG[1]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[2]:
        provincia = PROVINCIAS_ARG[2]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[3]:
        provincia = PROVINCIAS_ARG[3]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[4]:
        provincia = PROVINCIAS_ARG[4]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[5]:
        provincia = PROVINCIAS_ARG[5]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[6]:
        provincia = PROVINCIAS_ARG[6]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[7]:
        provincia = PROVINCIAS_ARG[7]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[8]:
        provincia = PROVINCIAS_ARG[8]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[9]:
        provincia = PROVINCIAS_ARG[9]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[10]:
        provincia = PROVINCIAS_ARG[10]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[11]:
        provincia = PROVINCIAS_ARG[11]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[12]:
        provincia = PROVINCIAS_ARG[12]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[13]:
        provincia = PROVINCIAS_ARG[13]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[14]:
        provincia = PROVINCIAS_ARG[14]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[15]:
        provincia = PROVINCIAS_ARG[15]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[16]:
        provincia = PROVINCIAS_ARG[16]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[17]:
        provincia = PROVINCIAS_ARG[17]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[18]:
        provincia = PROVINCIAS_ARG[18]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[19]:
        provincia = PROVINCIAS_ARG[19]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[20]:
        provincia = PROVINCIAS_ARG[20]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[21]:
        provincia = PROVINCIAS_ARG[21]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[22]:
        provincia = PROVINCIAS_ARG[22]
    if cp[0] == IDENITFICADOR_PROVINCIA_ARG[23]:
        provincia = PROVINCIAS_ARG[23]


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
            if codigo_postal[0] in '0123':
                region_brasil = REGIONES_BRASIL[0]
            if codigo_postal[0] in '4567':
                region_brasil = REGIONES_BRASIL[1]
            if codigo_postal[0] in '89':
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

    return destino, region_brasil, esMontevideo


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
    return inicial


def validar_envio_internacional(inicial, destino, region_brasil, esMontevideo):
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
def aplicar_descuento_efectivo(importe_inicial):
    return importe_inicial * 0.90

final = int(final)
