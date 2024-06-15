# Constantes
PAISES = ('Argentina', 'Bolivia', 'Brasil', 'Chile', 'Paraguay', 'Uruguay', 'Otro')
REGIONES_BRASIL = ('0-1-2-3', '4-5-6-7', '8-9')
IDENITFICADOR_PROVINCIA_ARG = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                                'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 
                                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

PRECIOS = (1100, 1800, 2450, 8300, 10900, 14300, 17900)

# validar pais destino
def asignar_pais_destino(codigo_postal):
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
        if codigo_postal[0] == '1':
            es_montevideo = True

    ## Otro
    if destino == '':
        destino = PAISES[6]

    return destino, region_brasil, es_montevideo

# asignar precio por tipo de envio
def asignar_precio_inicial(tipo):
    if tipo == 0:
        importe_envio = PRECIOS[0]
    if tipo == 1:
        importe_envio = PRECIOS[1]
    if tipo == 2:
        importe_envio = PRECIOS[2]
    if tipo == 3:
        importe_envio = PRECIOS[3]
    if tipo == 4:
        importe_envio = PRECIOS[4]
    if tipo == 5:
        importe_envio = PRECIOS[5]
    if tipo == 6:
        importe_envio = PRECIOS[6]
    return importe_envio

# asignar precio por envio internacional
def asignar_precio_internacional(importe_envio, destino, region_brasil, es_montevideo):
    if (destino == PAISES[1] 
        or destino == PAISES[4] 
        or es_montevideo
        or region_brasil == REGIONES_BRASIL[2]):
        importe_envio *= 1.20
    
    elif (destino == PAISES[3]
        or (destino == PAISES[5] and not es_montevideo)
        or region_brasil == REGIONES_BRASIL[0]):
        importe_envio *= 1.25
    
    elif region_brasil == REGIONES_BRASIL[1]:
        importe_envio *= 1.30
    
    elif destino == PAISES[6]:
        importe_envio *= 1.50

    return importe_envio
    
# Aplicar 10% de descuento
def aplicar_descuento_efectivo(importe_envio):
    return importe_envio * 0.90

def obtener_importe_envio(codigo_postal, tipo, forma_pago):
    destino, region_brasil, es_montevideo = asignar_pais_destino(codigo_postal)
    importe_envio = asignar_precio_inicial(tipo)
    if destino != 'Argentina':
        importe_envio = asignar_precio_internacional(importe_envio, destino, region_brasil, es_montevideo)
    if forma_pago == '1':
        importe_envio = aplicar_descuento_efectivo(importe_envio)
        
    return int(importe_envio)

cedvalid = None
cedinvalid = None
imp_acu_total = None
ccs = None
ccc = None
cce = None
mayor = None
tipo_mayor = None
primer_cp = None
cant_primer_cp = None
menimp = None
mencp = None
porc = None
prom = None

def leer_archivo(nombre_archivo = 'envios25.txt'):
    """Procesa un archivo y devuelve una sucesion de cadena de caracteres correspondientes a cada linea del archivo.

    Args:
        nombre_archivo (string): ruta del archivo

    Returns:
        string: Sucesion de cadena de caracteres del archivo.
    """
    archivo = open(nombre_archivo)
    lineas = archivo.readlines()       
    archivo.close()
    return lineas

def obtener_tipo_control(envio):
    """Procesa una cadena de caracteres y devuelve el tipo de control.

    Args:
        linea (string): Cadena de caracteres a procesar.

    Returns:
        string: Cadena literal que indica el tipo de control.
    """

    if 'HC' in envio:
        control = 'Hard Control'
    else:
        control = 'Soft Control'
    return control

def obtener_codigo_postal(envio):
    return envio[0:8]

def obtener_direccion(envio):
    return envio[9:29]

def obtener_tipo_envio(envio):
    return envio[29]

def obtener_forma_pago(envio):
    return envio[30]

def validar_direccion(direccion):
    car_temp = None
    nueva_palabra = None
    palabra_alphanum = True
    dos_mayus_seg = False
    palabra_num = True
    
    for caracter in direccion:
        if not caracter.isalpha() and not caracter.isnumeric():
            palabra_alphanum = False
        
        if car_temp == None:
            car_temp = caracter
        else:
            if caracter.isupper() and car_temp.isupper():
                dos_mayus_seg = True
        
        if nueva_palabra and not caracter.isnumeric():
            palabra_num = False
        if caracter == ' ' and nueva_palabra:
            nueva_palabra = False
        if caracter == ' ' and nueva_palabra == None:
            nueva_palabra = True
        
        car_temp = caracter
            
    if palabra_alphanum and not dos_mayus_seg and palabra_num:
        return True
    else:
        return False
          
def acumular_tipo_carta(tipo, ccs, ccc, cce):
    if tipo in '012':
        ccs += 1
    if tipo in '34':
        ccc += 1
    if tipo in '56':
        cce += 1
    return 

def carta_mayor_enviada():
    if (ccs > ccc and ccs > cce) or (ccs > cce and ccs == ccc) or (ccs > ccc and ccs == cce):
        return 'Carta Simple'
    if (ccc > cce) or (ccc > ccs and ccc == cce):
        return 'Carta Certificada'
    else:
        return 'Carta Expresa'

def acumular_primer_cp(cant_primer_cp):
    cant_primer_cp += 1

def validar_menor_importe(importe_envio):

# script principal
envios = leer_archivo()
control = obtener_tipo_control(envios[0])

if control == 'Hard Control':
    for envio in envios:
        if envio != envio[0]:
            direccion = obtener_direccion(envio)
            direccion_valida = validar_direccion(direccion)
            if direccion_valida:
                codigo_postal = obtener_codigo_postal(envio)
                tipo = obtener_tipo_envio(envio)
                forma_pago = obtener_forma_pago(envio)
                importe_envio = obtener_importe_envio(codigo_postal, tipo, forma_pago)

                cedvalid += 1
                imp_acu_total += importe_envio
                acumular_tipo_carta(tipo, ccs, ccc, cce)
            else:
                cedinvalid += 1
        
else:
    cedinvalid = 0
    importe_temp = None
    for envio in envios:
        if envio != envios[0]:
            codigo_postal = obtener_codigo_postal(envio)
            tipo = obtener_tipo_envio(envio)
            forma_pago = obtener_forma_pago(envio)
            destino, _ ,_ = asignar_pais_destino(codigo_postal)
            importe_envio = obtener_importe_envio(codigo_postal, tipo, forma_pago)

            cedvalid =+ 1
            imp_acu_total += importe_envio
            acumular_tipo_carta(tipo, ccs, ccc, cce)

            if primer_cp != None and primer_cp == codigo_postal:
                acumular_primer_cp(cant_primer_cp)
            if envio == envio[1]:
                primer_cp = codigo_postal
                acumular_primer_cp(cant_primer_cp)

            if importe_temp != None and destino == 'Brasil':
                if validar_menor_importe(importe_envio, importe_temp):
                    menimp = importe_envio
            if importe_temp == None:
                importe_temp = importe_envio

            importe_temp = importe_envio

tipo_mayor = carta_mayor_enviada(ccs, ccc, cce)

print(' (r1) - Tipo de control de direcciones:', control)
print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
print(' (r5) - Cantidad de cartas simples:', ccs)
print(' (r6) - Cantidad de cartas certificadas:', ccc)
print(' (r7) - Cantidad de cartas expresas:', cce)
print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
# print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
# print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
# print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
# print('(r14) - Importe final promedio de los envios a Buenos Aires:', prom)