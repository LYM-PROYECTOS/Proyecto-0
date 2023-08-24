#"D:\OneDrive - Universidad de los andes\U.ANDES\2023-2\LyM\4-PTO\Proyecto-0\Prueba.txt"
#VARIABLES CREADAS
file = open(input("Ingrese ruta de acceso del archivo con el programa (formato .txt): "))
ReadFile = file.read()
Command= ["=","JUMP","WALK","LEAP","TURN","TURNTO","DROP","GET","GRAB","LETGO","NOP"]
Condition = ["FACING", "CAN", "NOT"]
Cycle=["WHILE", "REPEAT"]

#DICCIONARIO PROCESAMIENTO
Procesamiento = {"PROG": ReadFile, "i":0, "Funciona":True, "Command":Command, "Condition":Condition, "Cycle": Cycle,
                 "FD":["LEFT", "RIGHT", "AROUND"], "SD":["NORTH", "SOUTH", "EAST", "WEST"], "VAR":{},
                 }
#FUNCIONES DE CONTROL
def Adapt_Program(Procesamiento):
    text= Procesamiento["PROG"]
    dictV={"{":0,"}":0,"(":0, ")":0,";":0, ",":0,"=":0}
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
            dictV[caracter] +=1
            PROGRAMA1.append(caracter)
        elif caracter == " ":
            if palabra:
                PROGRAMA1.append(palabra)
                palabra = ""
        else:
            palabra += caracter
    
    if palabra:
        PROGRAMA1.append(palabra)
    Procesamiento["PROG"]=PROGRAMA1
    if (dictV["{"]!=dictV["}"]) or (dictV["("]!=dictV[")"]):
        
        Procesamiento["Funciona"]= False
    return Procesamiento



#FUNCIONES DE VERIFICACION

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
def Verify_VAR(Procesamiento):
    Programa = Procesamiento["PROG"]
    pos=Procesamiento["i"]
    if Programa[pos].isalnum():
        pos +=1
        if Programa[pos].isdigit():
            Procesamiento["VAR"][Programa[pos-1]]=  Programa[pos]
            pos +=1
            Procesamiento["i"] = pos
        else:
            Procesamiento["Funciona"] =False
    else:
        Procesamiento["Funciona"] =False
    return Procesamiento
def Verify_Proceso(Procesamiento):
    return Procesamiento
def verifycycle(i:int, lista:list, redflag:bool, comandos:list):
    pass
def Verify_Block(Procesamiento):
    Programa = Procesamiento["PROG"]
    return Procesamiento

def Verify_Command(Procesamiento):
    Programa = Procesamiento["PROG"]
    pos=Procesamiento["i"]
    FD=Procesamiento["FD"]
    SD=Procesamiento["SD"]
    OC=["DROP","GET","GRAB","LETGO"]
    if Programa[pos] =="WALK" or Programa[pos] =="LEAP":
        pos +=1
        if Programa[pos] =="(":
            pos +=1
            if Programa[pos].isalnum():
                pos +=1
                if Programa[pos] ==")":
                    pos+=1
                    Procesamiento["i"]=pos
                elif Programa[pos] ==",":
                    pos+=1
                    if Programa[pos] in FD or Programa[pos] in SD :
                        pos +=1
                        if Programa[pos] ==")":
                            pos+=1
                            Procesamiento["i"]=pos
                        else:
                            Procesamiento["Funciona"] =False
                    else:
                        Procesamiento["Funciona"] =False
                else:
                    Procesamiento["Funciona"] =False
            else:
               Procesamiento["Funciona"] =False 
        else:
            Procesamiento["Funciona"] =False
    elif Programa[pos] in OC:
        pos +=1
        if Programa[pos] =="(":
            pos +=1
            if Programa[pos].isalnum():
                pos +=1
                if Programa[pos] ==")":
                    pos+=1
                    Procesamiento["i"]=pos
                else:
                    Procesamiento["Funciona"] =False
            else:
                Procesamiento["Funciona"] =False
        else:
            Procesamiento["Funciona"] =False
    elif Programa[pos] == "TURN":
        pos +=1
        if Programa[pos] =="(":
            pos +=1
            if Programa[pos] in FD:
                pos +=1
                if Programa[pos] ==")":
                    pos+=1
                    Procesamiento["i"]=pos
                else:
                    Procesamiento["Funciona"] =False
            else:
                Procesamiento["Funciona"] =False
        else:
            Procesamiento["Funciona"] =False
    elif Programa[pos] == "TURNTO":
        pos +=1
        if Programa[pos] =="(":
            pos +=1
            if Programa[pos] in SD:
                pos +=1
                if Programa[pos] ==")":
                    pos+=1
                    Procesamiento["i"]=pos
                else:
                    Procesamiento["Funciona"] =False
            else:
                Procesamiento["Funciona"] =False
        else:
            Procesamiento["Funciona"] =False
    elif Programa[pos] == "NOP":
        pos +=1
        if Programa[pos] =="(":
            pos +=1
            if Programa[pos] ==")":
                pos+=1
                Procesamiento["i"]=pos
            else:
                Procesamiento["Funciona"] =False
        else:
            Procesamiento["Funciona"] =False
    elif Programa[pos] == "JUMP":
        pos +=1
        if Programa[pos] =="(":
            pos +=1
            if Programa[pos].isalnum():
                pos +=1
                if Programa[pos] ==",":
                    pos+=1
                    if Programa[pos].isalnum():
                        pos +=1
                        if Programa[pos] ==")":
                            pos+=1
                            Procesamiento["i"]=pos
                        else:
                            Procesamiento["Funciona"] =False
                    else:
                        Procesamiento["Funciona"] =False
                else:
                    Procesamiento["Funciona"] =False
            else:
               Procesamiento["Funciona"] =False 
        else:
               Procesamiento["Funciona"] =False 
    return Procesamiento
##CONTROLADOR 
def Inicio(Procesamiento):
    Procesamiento = Adapt_Program(Procesamiento)
    Programa = Procesamiento["PROG"]
    print(Programa)
    while Procesamiento["Funciona"] and Procesamiento["i"]<len(Programa):
        pos=Procesamiento["i"]
        if Programa[pos] =="DEFPROC":
            Procesamiento = Verify_Proceso(Procesamiento)
        elif Programa[pos] =="DEFVAR":
            Procesamiento["i"] +=1
            Procesamiento = Verify_VAR(Procesamiento)
        elif Programa[pos] =="{":
            Procesamiento = Verify_Block(Procesamiento)
        else: 
            Procesamiento["Funciona"]=False
    if Procesamiento["Funciona"]:
        print("El programa es CORRECTO")
    else:
        print("El programa es ERRONEO")
Inicio(Procesamiento)