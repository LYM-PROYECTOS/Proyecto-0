#"D:\OneDrive - Universidad de los andes\U.ANDES\2023-2\LyM\4-PTO\Proyecto-0\Prueba.txt"
#"C:\Users\andre\OneDrive\Desktop\universidad\tercer semestre\LYM\Proyecto-0\Prueba.txt"
#VARIABLES CREADAS
file = open(input("Ingrese ruta de acceso del archivo con el programa (formato .txt): "))
ReadFile = file.read()
Command= ["=","JUMP","WALK","LEAP","TURN","TURNTO","DROP","GET","GRAB","LETGO","NOP"]
Condition = ["FACING", "CAN", "NOT"]
Cycle=["WHILE", "REPEAT"]
RES =["=","JUMP","WALK","LEAP","TURN","TURNTO","DROP","GET","GRAB","LETGO","NOP","WHILE", "REPEAT",
      "FACING", "CAN", "NOT","DEFVAR","DEFPROC","IF"]
#DICCIONARIO PROCESAMIENTO
Procesamiento = {"PROG": ReadFile, "i":0, "Funciona":True, "Command":Command, "Condition":Condition, "Cycle": Cycle,
                 "FD":["LEFT", "RIGHT", "AROUND"], "SD":["NORTH", "SOUTH", "EAST", "WEST"], "VAR":{},
                 "RES":RES,"PROC":{}}
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
    print(Procesamiento["VAR"])
    return Procesamiento
#revisar si puede haber un proceso asi (""""defProc putCB (c)"""") IMPORTANTE por el momento se toma erroneo
def Verify_Proceso(Procesamiento):
    Programa = Procesamiento["PROG"]
    pos=Procesamiento["i"]+1
    contador = 0 
    nombre = ""
    if Programa[pos] not in Command:
        nombre = Programa[pos]
        pos +=1     
        Procesamiento["PROC"][nombre]= contador   
        if Programa[pos]=="(":
            pos += 1            
            if Programa[pos].isalnum():
                pos += 1
                contador = contador+1
                Procesamiento["PROC"][nombre]= contador

                if Programa[pos]==",":
                    pos +=1
                                       
                    if Programa[pos].isalnum():
                        pos += 1
                        contador = contador+1
                        if Programa[pos]==")":
                            pos=pos+1
                            Procesamiento["i"]=pos
                            Procesamiento["PROG"]=Programa
                        else:
                            Procesamiento["Funciona"]= False
                    else:
                        Procesamiento["Funciona"]=False
                elif Programa[pos]==")":
                    pos += 1
                else:
                    Procesamiento["Funciona"]=False
            elif Programa[pos]==")":

                pos=pos+1
                Procesamiento["i"]=pos
    Procesamiento["PROC"][nombre]= contador
    print(Procesamiento["PROC"])
    return Procesamiento

def verifycycle(Procesamiento):
    Programa = Procesamiento["PROG"]
    pos=Procesamiento["i"]
    if Programa[pos]=="WHILE":
        pos += 1
        if Programa[pos] in Condition:
            pos = pos+1
            if Programa[pos] == "(":
                pos =pos+1
                Procesamiento["i"]=pos
                Procesamiento =Verify_Command(Procesamiento)
                Programa = Procesamiento["PROG"]
                pos=Procesamiento["i"]
                if Programa[pos]==")":
                    pos = pos+1
                    if Programa[pos]=="{":
                        pos = pos+1
                        Procesamiento["i"]=pos
                        Procesamiento=Verify_Block(Procesamiento)
                        Programa = Procesamiento["PROG"]
                        pos= Procesamiento["i"]
                        if Programa[pos]=="}":
                           pos+=1
                           Procesamiento["i"]=pos
                           Procesamiento["PROG"]=Programa
                    else:
                        Procesamiento["Funciona"]= False
                else:
                    Procesamiento["Funciona"]=False
            else:
                Procesamiento["Funciona"]=False
        else:
            Procesamiento["Funciona"]=False
    return Procesamiento

def Verifycondicion(Procesamiento):
    Programa = Procesamiento["PROG"]
    pos=Procesamiento["i"]
    pos +=1
    if Programa[pos] in Condition:
        pos = pos+1
        if Programa[pos] == "(":
            pos =pos+1
            Procesamiento["i"]=pos
            Procesamiento =Verify_Command(Procesamiento)
            Programa = Procesamiento["PROG"]
            pos=Procesamiento["i"]
            if Programa[pos]==")":
                pos = pos+1
                if Programa[pos]=="{":
                    pos =pos+1
                    Procesamiento["i"]=pos
                    Procesamiento =Verify_Block(Procesamiento)
                    Programa = Procesamiento["PROG"]
                    pos=Procesamiento["i"]
                    if Programa[pos]=="ELSE":
                        pos = pos+1
                        if Programa[pos]=="{":
                            pos=pos+1
                            Procesamiento["i"]=pos
                            Procesamiento["PROG"]=Programa
                            Procesamiento=Verify_Command(Procesamiento)
                            Programa = Procesamiento["PROG"]
                            pos=Procesamiento["i"]
                            if Programa[pos]=="}":
                                pos = pos +1
                                if Programa[pos]=="}":
                                    pos = pos +1
                                    Procesamiento["i"]=pos
                                    Procesamiento["PROG"]=Programa
                            else:
                                Procesamiento["Funciona"]= False
                        else:
                            Procesamiento["Funciona"]= False
                    else:
                            Procesamiento["Funciona"]= False
                else:
                    Procesamiento["Funciona"]= False
            else:
                Procesamiento["Funciona"]=False
        else:
            Procesamiento["Funciona"]=False
    else:
        Procesamiento["Funciona"]=False
    return Procesamiento

def Verify_Block(Procesamiento):
    Programa = Procesamiento["PROG"]
    pos=Procesamiento["i"]
    
    if Programa[pos]in Procesamiento["Command"]:
        Procesamiento=Verify_Command(Procesamiento)
        Programa=Procesamiento["PROG"]
        pos=Procesamiento["i"]
        
        if  Programa[pos]==";":
            pos=pos+1
            Procesamiento["i"]=pos
            Procesamiento =Verify_Block(Procesamiento)
        elif Programa[pos]=="}":
            pos=pos+1
            Procesamiento["i"]=pos
            
        else:
            Procesamiento["Funciona"]=False
    elif Programa[pos] in Cycle:
        pos = pos+1
        if Programa[pos] in Condition:
            pos = pos+1
            if Programa[pos] == "(":
                pos = pos+1
                Procesamiento =verifycycle(Procesamiento)
                pos = Procesamiento["i"]
                Programa=Procesamiento["PROG"]
            else:
                Procesamiento["Funciona"]=False
        else:
            Procesamiento["Funciona"]=False
    elif Programa[pos] == "IF":
        Procesamiento=Verifycondicion(Procesamiento)
    
    return Procesamiento

def Verify_Command(Procesamiento):
    Programa = Procesamiento["PROG"]
    pos=Procesamiento["i"]
    Reservadas = Procesamiento["RES"]
    FD=Procesamiento["FD"]
    SD=Procesamiento["SD"]
    OC=["DROP","GET","GRAB","LETGO"]
    if Programa[pos] =="WALK" or Programa[pos] =="LEAP":
        pos +=1
        if Programa[pos] =="(":
            pos +=1
            if Programa[pos].isalnum() and Programa[pos] not in Reservadas:
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
            if Programa[pos].isalnum() and Programa[pos] not in Reservadas:
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
            if Programa[pos].isalnum() and Programa[pos] not in Reservadas:
                pos +=1
                if Programa[pos] ==",":
                    pos+=1
                    if Programa[pos].isalnum() and Programa[pos] not in Reservadas:
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
            Procesamiento["i"] +=1
            Procesamiento = Verify_Block(Procesamiento)
        else: 
            Procesamiento["Funciona"]=False
    if Procesamiento["Funciona"]:
        print("El programa es CORRECTO")
    else:
        print("El programa es ERRONEO")
Inicio(Procesamiento)