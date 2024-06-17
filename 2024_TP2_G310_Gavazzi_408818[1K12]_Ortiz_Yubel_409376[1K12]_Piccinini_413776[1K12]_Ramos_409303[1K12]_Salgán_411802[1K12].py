# Constantes
PAISES = ('Argentina', 'Bolivia', 'Brasil', 'Chile', 'Paraguay', 'Uruguay', 'Otro')
REGIONES_BRASIL = ('0-1-2-3', '4-5-6-7', '8-9')
IMPORTES = (1100, 1800, 2450, 8300, 10900, 14300, 17900)

# Recorre y analiza el código postal y retorna el país destino. Si el país destino es Brasil, 
# retorna como segundo valor una cadena que contiene la región. Si el país destino es Uruguay y la ciudad 
# es Montevideo, retorna como tercer valor un True.
def obtener_pais_destino(codigo_postal):
    # ... inicializar variables ...
    destino = ''
    region_brasil = None
    es_montevideo = None

    # ... validar si el país destino es Argentina ...
    if (len(codigo_postal) == 8 
    and codigo_postal[0].isalpha() 
    and codigo_postal[1:5].isnumeric() 
    and codigo_postal[5:9].isalpha()
    and not codigo_postal[0] in 'IO'):
        destino = PAISES[0]

    # ... validar si el país destino es Bolivia ...
    elif len(codigo_postal) == 4 and codigo_postal[0:].isnumeric():
        destino = PAISES[1]

    # ... validar si el país destino es Brasil ...
    elif len(codigo_postal) == 9 and codigo_postal[0:5].isnumeric() and codigo_postal[6:9].isnumeric():
        if codigo_postal[5] == '-':
            destino = PAISES[2]
            if codigo_postal[0] in '0123':
                region_brasil = REGIONES_BRASIL[0]
            if codigo_postal[0] in '4567':
                region_brasil = REGIONES_BRASIL[1]
            if codigo_postal[0] in '89':
                region_brasil = REGIONES_BRASIL[2]

    # ... validar si el país destino es Chile ...
    elif len(codigo_postal) == 7 and codigo_postal[0:].isnumeric():
        destino = PAISES[3]

    # ... validar si el país destino es Paraguay ...
    elif len(codigo_postal) == 6 and codigo_postal[0:].isnumeric():
        destino = PAISES[4]

    # ... validar si el país destino es Uruguay ...
    elif len(codigo_postal) == 5 and codigo_postal[0:].isnumeric():
        destino = PAISES[5]
        if codigo_postal[0] == '1':
            es_montevideo = True

    # ... validar si el país destino es Otro ...
    else:
        destino = PAISES[6]

    # ... retornar variables asignadas y procesadas ...
    return destino, region_brasil, es_montevideo

# Analiza el tipo de envio y asigna el importe inicial.
def asignar_importe_inicial(tipo):
    # ... validar tipo de envío y retornar su importe ... 
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
    # ... validar impuestos 20% ...
    if (destino == PAISES[1] 
        or destino == PAISES[4] 
        or es_montevideo
        or region_brasil == REGIONES_BRASIL[2]):
        # ... retornar importe con impuesto 20% aplicado ...
        return importe_envio * 1.20
    
    # ... validar impuestos 25% ...
    elif (destino == PAISES[3]
        or (destino == PAISES[5] and not es_montevideo)
        or region_brasil == REGIONES_BRASIL[0]):
        # ... retornar importe con impuesto 25% aplicado ...
        return importe_envio * 1.25
    
    # ... validar impuestos 30% ...
    elif region_brasil == REGIONES_BRASIL[1]:
        # ... retornar importe con impuesto 30% aplicado ...
        return importe_envio * 1.30
    
    # ... validar impuestos 50% ...
    else:
        # ... retornar importe con impuesto 50% aplicado ...
        return importe_envio * 1.50
    
# Aplica descuento final por pago en efectivo.
def aplicar_descuento_efectivo(importe_envio):
    # ... aplicar 10% de descuento al importe del envío y retornar importe ...
    return importe_envio * 0.90

# Obtiene el importe final de un envío tomando los datos del mismo.
def obtener_importe_envio(codigo_postal, tipo, forma_pago):
    # ... obtener país desitino, región de Brasil y validación de Montevideo ...
    destino, region_brasil, es_montevideo = obtener_pais_destino(codigo_postal)

    # ... asignar importe inicial al envío de acuerdo su tipo ...
    importe_envio = asignar_importe_inicial(tipo)

    # ... validar si el país destino del envío no es Argentina ... 
    if destino != PAISES[0]:
        # ... aplicar impuesto internacional al envío ...
        importe_envio = aplicar_impuesto_internacional(importe_envio, destino, region_brasil, es_montevideo)

    # ... validar forma de pago del envío ...
    if forma_pago == '1':
        # ... aplicar descuento por pago en efectivo ...
        importe_envio = aplicar_descuento_efectivo(int(importe_envio))
        
    # ... retornar importe del envío ...
    return int(importe_envio)

# Lee una archivo y retorna sus líneas como una lista de cadenas.
def leer_archivo(archivo):
    # ... inicializar variables ...
    lineas = ()

    # ... inicializar variables auxiliares ...
    indice_car = 0
    saltos_linea = 0
    saltos_indice = ()

    # ... abrir archivo ...
    archivo_abierto = open(archivo, 'rt')

    # ... leer archvo ...
    archivo_leido = archivo_abierto.read()
    
    # ... iterar caracteres del archivo leído ...
    for caracter in archivo_leido:
        # ... validar si el caracter es un salto de línea ...
        if caracter == '\n':
            # ... acumular cantidad de veces que se repite el salto de línea y agregar el índice del mismo a una tupla ...
            saltos_linea += 1
            saltos_indice += indice_car,
        
        # ... acumular índice del caracter ...
        indice_car += 1

    # ... iterar índices de todos los saltos de línea ...
    for i in range(saltos_linea):
        # ... validar si es la primer iteración ...
        if i == 0:
            # ... inicializar variable que contendrá el índice del caracter inicial de cada línea nueva ...
            inicio_linea = 0

            # ... agregar línea nueva a la tupla que contendrá todas las líneas del archivo mediante un slice
            # que toma como índice inicial al índice del caracter inicial de cada línea nueva, y toma como índice final
            # al índice del salto de línea final de cada línea ...
            lineas += archivo_leido[inicio_linea:saltos_indice[i]],
        
        else:
            # ... inicializar variable que contendrá el índice del caracter inicial de cada línea nueva ...
            inicio_linea = saltos_indice[i-1] 

            # ... validar si existe algún caracter en la nueva línea ...
            if archivo_leido[inicio_linea + 1:saltos_indice[i]] != '':
                # ... agregar línea nueva a la tupla que contendrá todas las líneas del archivo mediante un slice
                # que toma como índice inicial al índice del caracter inicial de cada línea nueva, y toma como índice final
                # al índice del salto de línea final de cada línea ...
                lineas += archivo_leido[inicio_linea + 1:saltos_indice[i]],
    
    # ... validar si existe algún caracter en la última línea ...
    if archivo_leido[saltos_indice[-1] + 1:len(archivo_leido)] != '':
        # ... agregar la última línea a la tupla que contendrá todas las líneas del archivo mediante un slice
        # que toma como índice inicial al índice del salto de línea final, y toma como índice final
        # al índice del último elemento de la última línea ...
        lineas += archivo_leido[saltos_indice[-1] + 1:len(archivo_leido)],

    # ... retornar líneas del archivo ...
    return lineas

# Valida y retorna el tipo de control de un envío.
def obtener_tipo_control(envio):
    # ... validar tipo de control del envío ...
    if 'HC' in envio:
        # ... retornar tipo de control ...
        return 'Hard Control'
    else:
        # ... retornar tipo de control ...
        return 'Soft Control'

# Elimina espacios en blanco y retorna el código postal de un envío.
def obtener_codigo_postal(envio):
    # ... inicializar índice de caracter ...
    indice_car = 0

    # ... iterar caracteres del envío ...
    for caracter in envio:

        # ... validar si el caracter es un espacio en blanco ...
        if caracter != ' ':
            # ... retornar código postal ...
            return envio[indice_car:9]
        # ... sumar 1 al índice del caracter ...
        indice_car += 1

# Retorna la dirección de un envío.
def obtener_direccion(envio):
    # ... retornar dirección ...
    return envio[9:29]

# Retorna el tipo de envío.
def obtener_tipo_envio(envio):
    # ... retornar tipo de envío ...
    return envio[29]

# Retorna la forma de pago de un envío.
def obtener_forma_pago(envio):
    # ... retornar forma de pago del envío ...
    return envio[30]

# Valida la direccion de un envío. Si la dirección es válida retorna True.
# Si la dirección no es válida retorna False.
def validar_direccion(direccion):
    # ... inicialiar variables auxiliares ...
    car_temp = None
    indice_car = 0

    # ... inicializar variables de condición en caso de cumplimiento ...
    palabra_alphanum = True
    dos_mayus_seg = False
    palabra_num = True
    
    # ... iterar caracteres de la dirección ...
    for caracter in direccion:

        # ... validar primer condición de la dirección ...
        if caracter != ' ' and caracter != '.' and not caracter.isalpha() and not caracter.isnumeric():
            # ... negar primer condición en caso de no cumplirse ...
            palabra_alphanum = False
        
        # ... validar segunda condición de la dirección ...
        # ... validar si es primer caracter ...
        if car_temp == None:
            # ... asginar primer caracter ...
            car_temp = caracter
        else:
            # ... validar si dos letras seguidas son mayúsculas ...
            if caracter.isupper() and car_temp.isupper():
                # ... negar segunda condicion en caso de no cumplirse ...
                dos_mayus_seg = True
        
        # ... validar tercer condición de la dirección ...
        if caracter == '.':
            # ... inicializar índice decremental ...
            indice_decremento = -1

            # ... iterar en reversa los caracteres de la dirección ...
            while direccion[indice_car + indice_decremento] != ' ':
                # ... validar si una palabra está compuesta sólo por dígitos ...
                if not direccion[indice_car + indice_decremento].isnumeric():
                    # ... negar tercer condición en caso de no cumplirse ...
                    palabra_num = False
                
                # ... decrementar índice ...
                indice_decremento -= 1
        
        # ... asignar caracter temporal ...
        car_temp = caracter

        # ... incrementar índice del caracter ...
        indice_car += 1
            
    # ... validar si las tres condiciones de la dirección se cumplen ...
    if palabra_alphanum and not dos_mayus_seg and palabra_num:
        # ... retornar True en caso de cumplimiento ...
        return True
    else:
        # ... retornar False en caso de incumplimiento ...
        return False
          
# Valida y acumula el tipo de carta de un envio.
def acumular_tipo_carta(tipo, ccs, ccc, cce):
    # ... validar tipo de carta del envío ...
    if tipo in '012':
        # ... acumular cantidad de cartas simples ...        
        ccs += 1
    elif tipo in '34':
        # ... acumular cantidad de cartas certificadas ...
        ccc += 1
    else:
        # ... acumular cantidad de cartas expresas ...        
        cce += 1
    
    # ... retornar cantidad de tipo de cartas acumuladas ...
    return ccs, ccc, cce

# Compara y obtiene el tipo de carta con mayor cantidad de envios.
def carta_mayor_enviada(ccs, ccc, cce):
    # ... validar tipo de carta con mayor cantidad de envíos ...
    if (ccs > ccc and ccs > cce) or (ccs > cce and ccs == ccc) or (ccs > ccc and ccs == cce):
        # ... retornar tipo de carta simple ...
        return 'Carta Simple'   
    elif (ccc > cce) or (ccc > ccs and ccc == cce):
        # ... retornar tipo de carta certificada ...
        return 'Carta Certificada'
    else:
        # ... retornar tipo de carta expresa ...        
        return 'Carta Expresa'

# Asigna el código postal del primer envío y lo acumula por primera vez.
def asignar_primer_cp(primer_cp, cant_primer_cp, codigo_postal):
    # ... asignar código postal del primer envío ...
    primer_cp = codigo_postal

    # ... acumular código postal del primer envío ...
    cant_primer_cp += 1

    # ... retornar código postal y cantidad del código postal del primer envío ...
    return primer_cp, cant_primer_cp

# Acumula la cantidad de veces que se repite el código postal del primer envío.
def acumular_primer_cp(cant_primer_cp):
    # ... acumular y retornar código postal del primer envío ...
    return cant_primer_cp + 1

# Valida el menor importe por un envío a Brasil.
def es_men_imp(codigo_postal, destino, importe_envio, menimp, mencp):
    # ... validar si ya existe menor importe y código postal del envío con menor importe y si el país destino es Brasil ...
    if (menimp != None and mencp != None) and destino == PAISES[2]:
        # ... validar si el código postal del envío con menor importe es igual al código postal y si el importe
        # del envío es menor al menor importe guardado ...
        if (mencp != codigo_postal) and importe_envio < menimp:
            # ... retornar True en caso de cumplimiento ...
            return True
    
    # ... validar si no existe menor importe y código postal del envío con menor importe y si el país destino es Brasil ...
    if (menimp == None and mencp == None) and destino == PAISES[2]:
        # ... retornar True en caso de cumplimiento ...
        return True
    
    # ... retornar False en caso de incumplimiento ...
    return False
            
# Asigna el menor importe por un envío a Brasil.
def asignar_men_impo(codigo_postal, importe_envio, menimp, mencp):
    # ... asignar menor importe por un envío a Brasil ...
    menimp = importe_envio

    # ... asignar código postal del envío con menor importe por un envío a Brasil ...
    mencp = codigo_postal

    # ... retornar valores ...
    return menimp, mencp

# Valida la provincia destino de un envío dentro de Argentina. Si la provincia es Pcia. de Buenos Aires
# retorna True. Si es otra pcia. retorna False.
def es_pcia_bsas(codigo_postal):
    # ... validar si el primer caracter del código postal de un envío es la letra B mayúscula ...
    if codigo_postal[0] == 'B':
        # ... retornar True en caso de cumplimiento ...
        return True
    else:
        # ... retornar False en caso de incumplimiento ...
        return False

# Aplica control rígido a todos los envíos y retorna todas las salidas procesadas.
def aplicar_hard_control(envios):
    # ... inicializar varbiales ...
    cedvalid = 0
    cedinvalid = 0
    imp_acu_total = 0
    ccs = 0
    ccc = 0
    cce = 0
    cant_primer_cp = 0
    porc = 0
    prom = 0
    imp_acu_pcia_bsas = 0
    primer_cp = None
    menimp = None
    mencp = None

    # ... iterar envíos de las líneas del archivo ...
    for envio in envios:
        # ... validar si no es la primer línea del archivo ...
        if envio != envios[0]:

            # ... obtener datos del envío ...
            codigo_postal = obtener_codigo_postal(envio)
            destino, _, _ = obtener_pais_destino(codigo_postal)
            direccion = obtener_direccion(envio)
            tipo = obtener_tipo_envio(envio)
            forma_pago = obtener_forma_pago(envio)
            importe_envio = obtener_importe_envio(codigo_postal, tipo, forma_pago)

            # ... validar dirección del envío ...
            direccion_valida = validar_direccion(direccion)
            if direccion_valida:

                # ... acumular cantidad de envíos ...
                cedvalid += 1

                # ... acumular importe del envío válido ...
                imp_acu_total += importe_envio

                # ... acumular cantidad por tipo de carta del envío válido ... 
                ccs, ccc, cce = acumular_tipo_carta(tipo, ccs, ccc, cce)
                
                # ... validar si el país destino del envío no es Argentina ...
                if destino != PAISES[0]:
                    # ... acumular cantidad de envíos válidos fuera de Argentina ...
                    porc += 1

                # ... validar si el país y provincia destino del envío son Argentina y  Pcia. de BsAs. ...
                if destino == PAISES[0] and es_pcia_bsas(codigo_postal):
                    # ... acumular cantidad e importe de envíos a la Pcia. de BsAs. ...
                    prom += 1
                    imp_acu_pcia_bsas += importe_envio

            else:
                # ... acumular cantidad de envíos inválidos ...
                cedinvalid += 1
                
            # ... validar si el código postal del envío actual es igual al código postal del primer envío ...
            if primer_cp != None and codigo_postal == primer_cp:
                # ... acumular cantidad de veces que se repite el primer código postal ...
                cant_primer_cp = acumular_primer_cp(cant_primer_cp)

            # ...validar si existe el código postal del primer envío ...
            if envio == envios[1] and primer_cp == None:
                # ... asignar código postal del primer envío ...
                primer_cp, cant_primer_cp = asignar_primer_cp(primer_cp, cant_primer_cp, codigo_postal)

            # ... validar si el importe del envío actual es menor que el menor importe guardado ...
            if es_men_imp(codigo_postal, destino, importe_envio, menimp, mencp):
                # ... acumular cantidad e importe de envíos a la Pcia. de BsAs. ...
                menimp, mencp = asignar_men_impo(codigo_postal, importe_envio, menimp, mencp)

    # ... retornar variables asignadas y procesadas ...
    return (cedvalid, cedinvalid, imp_acu_total, 
            ccs, ccc, cce, primer_cp, cant_primer_cp, 
            menimp, mencp, porc, prom, imp_acu_pcia_bsas) 

# Aplica control ligero a todos los envíos y retorna todas las salidas procesadas. 
def aplicar_soft_control(envios):
    # ... inicializar varbiales ...
    cedvalid = 0
    cedinvalid = 0
    imp_acu_total = 0
    ccs = 0
    ccc = 0
    cce = 0
    cant_primer_cp = 0
    porc = 0
    prom = 0
    imp_acu_pcia_bsas = 0
    primer_cp = None
    menimp = None
    mencp = None

    # ... iterar envíos de las líneas del archivo ...
    for envio in envios:
        if envio != envios[0]:

            # ... obtener datos del envío ...
            codigo_postal = obtener_codigo_postal(envio)
            destino, _, _ = obtener_pais_destino(codigo_postal)
            tipo = obtener_tipo_envio(envio)
            forma_pago = obtener_forma_pago(envio)
            importe_envio = obtener_importe_envio(codigo_postal, tipo, forma_pago)

            # ... acumular cantidad de envíos
            cedvalid += 1

            # ... acumular importe de envíos
            imp_acu_total += importe_envio

            # ... acumular cantidad por tipo de carta del envío ...
            ccs, ccc, cce = acumular_tipo_carta(tipo, ccs, ccc, cce)

            # ... validar si el código postal del envío actual es igual al código postal del primer envío ...
            if primer_cp != None and codigo_postal == primer_cp:
                # ... acumular cantidad de veces que se repite el primer código postal ...
                cant_primer_cp = acumular_primer_cp(cant_primer_cp)

            # ...validar si existe el código postal del primer envío ...
            if envio == envios[1] and primer_cp == None:
                # ... asignar código postal del primer envío ...
                primer_cp, cant_primer_cp = asignar_primer_cp(primer_cp, cant_primer_cp, codigo_postal)

            # ... validar si el importe del envío actual es menor que el menor importe guardado ...
            if es_men_imp(codigo_postal, destino, importe_envio, menimp, mencp):
                # ... asignar el importe del envío actual como menor importe y asignar su código postal ...
                menimp, mencp = asignar_men_impo(codigo_postal, importe_envio, menimp, mencp)

            # ... validar si el país destino del envío no es Argentina ...
            if destino != PAISES[0]:
                # ... acumular cantidad de envíos válidos fuera de Argentina ...
                porc += 1

            # ... validar si el país y provincia destino del envío son Argentina y  Pcia. de BsAs. ...
            if destino == PAISES[0] and es_pcia_bsas(codigo_postal):
                # ... acumular cantidad e importe de envíos a la Pcia. de BsAs. ...
                prom += 1
                imp_acu_pcia_bsas += importe_envio

    # ... retornar variables asignadas y procesadas ...
    return (cedvalid, cedinvalid, imp_acu_total, 
            ccs, ccc, cce, primer_cp, cant_primer_cp, 
            menimp, mencp, porc, prom, imp_acu_pcia_bsas) 

def principal():
    # ... leer y obtener envíos del archivo que los contiene ...
    envios = leer_archivo('envios.txt')
    # ... obtener el tipo de control de los envíos ...
    control = obtener_tipo_control(envios[0])

    # ... validar el tipo de control ...
    if control == 'Hard Control':
        # ... aplicar tipo de control y obtener variables procesadas ...
        (cedvalid, cedinvalid, imp_acu_total,
         ccs, ccc, cce, primer_cp, cant_primer_cp,
         menimp, mencp, porc, prom, imp_acu_pcia_bsas) = aplicar_hard_control(envios)
    else:
        (cedvalid, cedinvalid, imp_acu_total,
         ccs, ccc, cce, primer_cp, cant_primer_cp,
         menimp, mencp, porc, prom, imp_acu_pcia_bsas) = aplicar_soft_control(envios)

    # ... obtener tipo de carta con mayor cantidad de envíos ...
    tipo_mayor = carta_mayor_enviada(ccs, ccc, cce)

    # ... calcular el porcentaje que representa la cantidad total de envíos al exterior sobre la cantidad total de envíos ...
    porc = int(porc * 100 / (len(envios) - 1))

    # ... validar si existe algún envío a la Pcia. de BsAs.
    if prom != 0:
        # ... calcular el importe final promedio de los envíos a la Pcia. de BsAs.
        prom = int(imp_acu_pcia_bsas / prom)

    # Salidas
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

# Script principal
principal()