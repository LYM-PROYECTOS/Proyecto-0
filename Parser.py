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
listaog = tokenize_string(ReadFile)
global redflag 
redflag = True 
# Funcion verificacion de variables terminada (verificar si en el 3 parametro se puede tener mas de un digito)
def verifyvar(i:int, lista:list, redflag:bool, comandos:list):
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    if lista[i] == "DEFVAR":
        i =i+1
        if lista[i] not in comandos:
            i=i+1
        if len(lista[i])>1:
            i = 0
            while i != len(lista[i]) and redflag == True:
                if lista[i] in numeros:   
                    i =i+1
                else :
                    redflag = False
        else:
            if lista[i] not in numeros:
                redflag = False 
            else: 
                i= i+1
    else:
        redflag = False
    return(i, redflag)

#print(verifyvar(2, listaog, redflag, comandos))


def verifycycle(i:int, lista:list, redflag:bool, comandos:list):
    pass