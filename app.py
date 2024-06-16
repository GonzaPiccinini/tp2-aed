# Constantes
PAISES = ('Argentina', 'Bolivia', 'Brasil', 'Chile', 'Paraguay', 'Uruguay', 'Otro')
REGIONES_BRASIL = ('0-1-2-3', '4-5-6-7', '8-9')
IMPORTES = (1100, 1800, 2450, 8300, 10900, 14300, 17900)

# Recorre y analiza el codigo postal y retorna el pais destino. Si el pais destino es Brasil, 
# retorna como segundo valor una cadena que contiene la region. Si el pais destino es Uruguay y la ciudad 
# es Montevideo, retorna como tercer valor un True.
def obtener_pais_destino(codigo_postal):
    destino = ''
    region_brasil = None
    es_montevideo = None

    # Argentina
    if len(codigo_postal) == 8 and codigo_postal[0].isalpha() and codigo_postal[1:5].isnumeric() and codigo_postal[5:9].isalpha():
        destino = PAISES[0]

    # Bolivia
    elif len(codigo_postal) == 4 and codigo_postal[0:].isnumeric():
        destino = PAISES[1]

    # Brasil
    elif len(codigo_postal) == 9 and codigo_postal[0:5].isnumeric() and codigo_postal[6:9].isnumeric():
        if codigo_postal[5] == '-':
            destino = PAISES[2]
            if codigo_postal[0] in '0123':
                region_brasil = REGIONES_BRASIL[0]
            if codigo_postal[0] in '4567':
                region_brasil = REGIONES_BRASIL[1]
            if codigo_postal[0] in '89':
                region_brasil = REGIONES_BRASIL[2]

    # Chile
    elif len(codigo_postal) == 7 and codigo_postal[0:].isnumeric():
        destino = PAISES[3]

    # Paraguay
    elif len(codigo_postal) == 6 and codigo_postal[0:].isnumeric():
        destino = PAISES[4]

    # Uruguay
    elif len(codigo_postal) == 5 and codigo_postal[0:].isnumeric():
        destino = PAISES[5]
        if codigo_postal[0] == '1':
            es_montevideo = True

    # Otro
    else:
        destino = PAISES[6]

    return destino, region_brasil, es_montevideo

# Analiza el tipo de envio y asigna el importe inicial.
def asignar_importe_inicial(tipo):
    if tipo == '0':
        return IMPORTES[0]
    elif tipo == '1':
        return IMPORTES[1]
    elif tipo == '2':
        return IMPORTES[2]
    elif tipo == '3':
        return IMPORTES[3]
    elif tipo == '4':
        return IMPORTES[4]
    elif tipo == '5':
        return IMPORTES[5]
    else:
        return IMPORTES[6]

# Aplica un impuesto al importe inicial para los envios internacionales.
def aplicar_impuesto_internacional(importe_envio, destino, region_brasil, es_montevideo):
    if (destino == PAISES[1] 
        or destino == PAISES[4] 
        or es_montevideo
        or region_brasil == REGIONES_BRASIL[2]):
        return importe_envio * 1.20
    
    elif (destino == PAISES[3]
        or (destino == PAISES[5] and not es_montevideo)
        or region_brasil == REGIONES_BRASIL[0]):
        return importe_envio * 1.25
    
    elif region_brasil == REGIONES_BRASIL[1]:
        return importe_envio * 1.30
    
    else:
        return importe_envio * 1.50
    
# Aplica descuento final por pago en efectivo.
def aplicar_descuento_efectivo(importe_envio):
    return importe_envio * 0.90

# Obtiene el importe final de un envio tomando los datos del mismo.
def obtener_importe_envio(codigo_postal, tipo, forma_pago):
    destino, region_brasil, es_montevideo = obtener_pais_destino(codigo_postal)
    importe_envio = asignar_importe_inicial(tipo)
    if destino != PAISES[0]:
        importe_envio = aplicar_impuesto_internacional(importe_envio, destino, region_brasil, es_montevideo)
    if forma_pago == '1':
        importe_envio = aplicar_descuento_efectivo(int(importe_envio))
        
    return int(importe_envio)

cedvalid = 0
cedinvalid = 0
imp_acu_total = 0
ccs = 0
ccc = 0
cce = 0
tipo_mayor = ''
primer_cp = None
cant_primer_cp = 0
menimp = None
mencp = None
porc = 0
prom = 0

# Lee una archivo y retorna sus lineas como una lista de cadenas.
def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, 'rt')
    lineas = archivo.readlines()       
    archivo.close()
    return lineas

# Valida y retorna el tipo de control de un envio.
def obtener_tipo_control(envio):
    if 'HC' in envio:
        control = 'Hard Control'
    else:
        control = 'Soft Control'
    return control

# Elimina espacios en blanco y retorna el codigo postal de un envio.
def obtener_codigo_postal(envio):
    indice_car = 0
    for caracter in envio:
        if caracter != ' ':
            return envio[indice_car:9]
        indice_car += 1

# Retorna la direccion de un envio.
def obtener_direccion(envio):
    return envio[9:29]

# Retorna el tipo de envio.
def obtener_tipo_envio(envio):
    return envio[29]

# Retorna la forma de pago de un envio.
def obtener_forma_pago(envio):
    return envio[30]

# Valida la direccion de un envio. Si la direccion es valida retorna True.
# Si la direccion no es valida retorna False.
def validar_direccion(direccion):
    car_temp = None
    indice_car = 0
    palabra_alphanum = True
    dos_mayus_seg = False
    palabra_num = True
    
    for caracter in direccion:
        if caracter != ' ' and caracter != '.' and not caracter.isalpha() and not caracter.isnumeric():
            palabra_alphanum = False
        
        if car_temp == None:
            car_temp = caracter
        else:
            if caracter.isupper() and car_temp.isupper():
                dos_mayus_seg = True
        
        if caracter == '.':
            indice_decremento = -1
            while direccion[indice_car + indice_decremento] != ' ':
                if not direccion[indice_car + indice_decremento].isnumeric():
                    palabra_num = False
                indice_decremento -= 1
        
        car_temp = caracter
        indice_car += 1
            
    if palabra_alphanum and not dos_mayus_seg and palabra_num:
        return True
    else:
        return False
          
# Valida y acumula el tipo de carta de un envio.
def acumular_tipo_carta(tipo, ccs, ccc, cce):
    if tipo in '012':
        ccs += 1
    elif tipo in '34':
        ccc += 1
    else:
        cce += 1
    return ccs, ccc, cce

# Compara y obtiene el tipo de carta con mayor cantidad de envios.
def carta_mayor_enviada():
    if (ccs > ccc and ccs > cce) or (ccs > cce and ccs == ccc) or (ccs > ccc and ccs == cce):
        return 'Carta Simple'
    if (ccc > cce) or (ccc > ccs and ccc == cce):
        return 'Carta Certificada'
    else:
        return 'Carta Expresa'

# Valida la provincia destino de un envio dentro de Argentina. Si la provincia es Pcia. de Buenos Aires
# retorna True. Si es otra pcia. retorna False.
def es_pcia_bsas(codigo_postal):
    if codigo_postal[0] == 'B':
        return True
    else:
        return False

# Script principal
envios = leer_archivo('envios25.txt')
control = obtener_tipo_control(envios[0])
imp_acu_pcia_bsas = 0

if control == 'Hard Control':
    for envio in envios:
        if envio != envios[0]:

            codigo_postal = obtener_codigo_postal(envio)
            destino, _, _ = obtener_pais_destino(codigo_postal)
            direccion = obtener_direccion(envio)
            tipo = obtener_tipo_envio(envio)
            forma_pago = obtener_forma_pago(envio)
            importe_envio = obtener_importe_envio(codigo_postal, tipo, forma_pago)

            direccion_valida = validar_direccion(direccion)
            if direccion_valida:

                cedvalid += 1
                imp_acu_total += importe_envio
                ccs, ccc, cce = acumular_tipo_carta(tipo, ccs, ccc, cce)
                
                if destino != PAISES[0]:
                    porc += 1

                if destino == PAISES[0] and es_pcia_bsas(codigo_postal):
                    prom += 1
                    imp_acu_pcia_bsas += importe_envio

            else:
                cedinvalid += 1
            if primer_cp != None and codigo_postal == primer_cp:
                cant_primer_cp += 1
            if envio == envios[1] and primer_cp == None:
                primer_cp = codigo_postal
                cant_primer_cp += 1

            if (menimp != None and mencp != None) and destino == PAISES[2]:
                if (mencp != codigo_postal) and importe_envio < menimp:
                    menimp = importe_envio
                    mencp = codigo_postal
            if (menimp == None and mencp == None) and destino == PAISES[2]:
                menimp = importe_envio
                mencp = codigo_postal

else:
    cedinvalid = 0

    for envio in envios:
        if envio != envios[0]:

            codigo_postal = obtener_codigo_postal(envio)
            destino, _, _ = obtener_pais_destino(codigo_postal)
            tipo = obtener_tipo_envio(envio)
            forma_pago = obtener_forma_pago(envio)
            importe_envio = obtener_importe_envio(codigo_postal, tipo, forma_pago)

            cedvalid += 1
            imp_acu_total += importe_envio
            ccs, ccc, cce = acumular_tipo_carta(tipo, ccs, ccc, cce)

            if primer_cp != None and codigo_postal == primer_cp:
                cant_primer_cp += 1
            if envio == envios[1] and primer_cp == None:
                primer_cp = codigo_postal
                cant_primer_cp += 1

            if (menimp != None and mencp != None) and destino == PAISES[2]:
                if (mencp != codigo_postal) and importe_envio < menimp:
                    menimp = importe_envio
                    mencp = codigo_postal
            if (menimp == None and mencp == None) and destino == PAISES[2]:
                menimp = importe_envio
                mencp = codigo_postal

            if destino != PAISES[0]:
                porc += 1

            if destino == PAISES[0] and es_pcia_bsas(codigo_postal):
                prom += 1
                imp_acu_pcia_bsas += importe_envio

tipo_mayor = carta_mayor_enviada()

if cedvalid != 0:
    porc = int(porc * 100 / cedvalid)

if prom != 0:
    prom = int(imp_acu_pcia_bsas / prom)

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
print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
print('(r14) - Importe final promedio de los envios a Buenos Aires:', prom)