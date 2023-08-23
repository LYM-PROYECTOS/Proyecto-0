#"D:\OneDrive - Universidad de los andes\U.ANDES\2023-2\LyM\4-PTO\Proyecto-0\Prueba.txt"
file = open(input("Ingrese ruta de acceso del archivo con el programa (formato .txt): "))
ReadFile = file.read()
comandos = ["JUMP","WALK","LEAP","TURN","TURNTO","DROP","GET","GRAB","LETGO","NOP", "FACING"]
Procesamiento = (0, True, [],comandos)
#FUNCIONES DE LECTURA ARCHIVO
def tokenize_string(text):
    Pro0=""
    text= text.split("\n")
    for item in text:
        Pro0 += item.upper()
        Pro0+=" "
    

    PROGRAMA1 = []
    palabra = ""
    
    for caracter in Pro0:
        if caracter in "{}(),;=":
            if palabra:
                PROGRAMA1.append(palabra)
                palabra = ""
            PROGRAMA1.append(caracter)
        elif caracter == " ":
            if palabra:
                PROGRAMA1.append(palabra)
                palabra = ""
        else:
            palabra += caracter
    
    if palabra:
        PROGRAMA1.append(palabra)

     
    return PROGRAMA1


print(tokenize_string(ReadFile))

#FUNCIONES DE VERIFICACION