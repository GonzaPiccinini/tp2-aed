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

def obtener_direccion(envio):
    return envio[9:29]

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
    
envios = leer_archivo('envios100HC.txt')

direcciones_validas = 0
for envio in envios:
    if envio != envios[0]:
        direccion = obtener_direccion(envio)
        valida = validar_direccion(direccion)
        if valida:
            direcciones_validas += 1
print(direcciones_validas)