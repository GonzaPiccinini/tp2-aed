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
    """Procesa un archivo y devuelve el mismo pero como sucesion de caracteres

    Args:
        nombre_archivo (string): ruta del archivo

    Returns:
        string: Sucesion de cadena de caracteres del archivo.
    """
    archivo = open(nombre_archivo)
    lineas = archivo.readlines()       
    archivo.close()
    return lineas

def tipo_de_control(envio = None):
    """Procesa una cadena de caracteres y devuelve el tipo de control

    Args:
        linea (string): Cadena de caracteres a procesar

    Returns:
        string: Cadena literal que indica el tipo de control
    """
    if envio == None:
        return 
    if 'HC' in envio:
        control = 'Hard Control'
    else:
        control = 'Soft Control'
    return control

def obtener_cp(envio):
    return envio[0:8]

def obtener_direccion(envio):
    return envio[9:29]

def obtener_tipo_envio(envio):
    return envio[29]

def obtener_forma_pago(envio):
    return envio[30]

def validar_direccion(envio):
    car_temp = None
    nueva_palabra = None
    palabra_alphanum = True
    dos_mayus_seg = False
    palabra_num = True
    
    direccion = obtener_direccion(envio)
    
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
          




                    
    
                        
            

       

# r5 r6 r7
def cantidad_cartas_sc(ccs, ccc, cce):
    if control == 'Soft Control':
        if linea[-2] == (0,1,2):
            ccs += 1
        elif linea[-2] == (3,4):
            ccc += 1
        elif linea[-2] == (5,6):
            cce += 1

def cantidad_cartas_hc(ccs, ccc, cce):
    ccs += 1
    ccc += 1
    cce += 1

# r8
def carta_mayor_enviada():
    if ccs > ccc and ccs > cce:
        mayor = ccs
    if ccc > ccs and ccc > cce:
        mayor = ccc
    if cce > ccs and cce > ccc:
        mayor = cce
    return mayor

# r9


# script principal
envios = leer_archivo()
control = tipo_de_control(envios[0])

if control == 'Hard Control':
    for envio in envios:
        if envio != envios[0]:
            es_valida = validar_direccion(envio)
            if es_valida:
                cedvalid += 1
            else:
                cedinvalid += 1
        
else:
    cedinvalid = 0
    for envio in envios:
        if envio != envios[0]:
            cedvalid =+ 1

        
        
        

mayor = carta_mayor_enviada(ccs, ccc, cce)
cantidad_cartas_sc(ccs, ccc, cce)
tipo_mayor = mayor

print(' (r1) - Tipo de control de direcciones:', control)
print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
# print(' (r4) - Total acumulado de importes finales:', imp_acu_total
print(' (r5) - Cantidad de cartas simples:', ccs)
print(' (r6) - Cantidad de cartas certificadas:', ccc)
print(' (r7) - Cantidad de cartas expresas:', cce)
print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
# print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
# print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
# print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
# print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
# print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
# print('(r14) - Importe final promedio de los envios a Buenos Aires:', prom)