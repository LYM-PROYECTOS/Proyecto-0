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
    Reservadas = Procesamiento["RES"]
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
                        print("Entra", pos, Programa[pos])
                        Procesamiento=Verify_Block(Procesamiento)
                        pos+=1
                        print("Entra", pos, Programa[pos])
                        Programa = Procesamiento["PROG"]
                        pos= Procesamiento["i"]
<<<<<<< HEAD
                        
=======
>>>>>>> 354194e9dcec64e279994455229c80a9dd892e87
                    else:
                        Procesamiento["Funciona"]= False
                else:
                    Procesamiento["Funciona"]=False
            else:
                Procesamiento["Funciona"]=False
        else:
            Procesamiento["Funciona"]=False
    elif Programa[pos]=="REPEAT":
        pos += 1
        print("vamos bien ------")
        if (Programa[pos].isalnum() or Programa[pos].isdigit())and Programa[pos] not in Reservadas:
            print("vamos bien22222222---")
            pos +=1
            if Programa[pos]=="TIMES":
                print("vamos bien33333333333---")
                pos +=1
                if Programa[pos] =="{":
                    pos +=1
                    Procesamiento["i"] =pos
                    Procesamiento = Verify_Block(Procesamiento)
                    print(Procesamiento["Funciona"], Procesamiento["i"])
                else:
                    Procesamiento["Funciona"] =False
            else:
               Procesamiento["Funciona"] =False 
        else:
            Procesamiento["Funciona"] =False
    return Procesamiento

def Verifycondicion(Procesamiento):
    Programa = Procesamiento["PROG"]
    pos=Procesamiento["i"]
    if Programa[pos] in Condition:
        pos += 1
        if Programa[pos]=="(":
            pos = pos+1
            Procesamiento["i"]=pos
            Procesamiento=Verify_Command(Procesamiento) 
            pos=Procesamiento["i"]  
            if Programa[pos]==")":
                pos = pos +1
                if Programa[pos]=="{":
                    pos = pos+1
                    Procesamiento["i"]=pos
                    Procesamiento=Verify_Block(Procesamiento) 
                    pos=Procesamiento["i"] 
                    if Programa[pos]=="ELSE":
                        pos = pos +1
                        if Programa[pos]=="{":
                            pos = pos +1
                            Procesamiento["i"]=pos
                            Procesamiento=Verify_Block(Procesamiento) 
                            pos=Procesamiento["i"] 
                            
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

def Verify_Block(Procesamiento):
    Programa = Procesamiento["PROG"]
    pos=Procesamiento["i"]
    ejecuta = True
    coma=False
    while ejecuta:
        if Programa[pos] in Procesamiento["Command"] or  Programa[pos] in Procesamiento["PROC"] :
            Procesamiento["i"]=pos
            print(Programa[pos], "entro a comando por bloque")
            Procesamiento=Verify_Command(Procesamiento) 
            pos=Procesamiento["i"]  
            print(pos,  "validando bloque", "aqiuiiii")
            coma=False    
            print(Programa[pos],"ayuda socorro jesus")    
        elif Programa[pos]==";" :
            pos=pos+1
            print(Programa[pos],"aaaaaaaaaaaaa")
            coma = True
            if Programa[pos] == "{":
                pos += 1
                Procesamiento["i"]=pos
                Procesamiento = Verify_Block(Procesamiento)
                pos=Procesamiento["i"]
                coma=False
            if Programa[pos] in Procesamiento["Command"] or  Programa[pos] in Procesamiento["PROC"] :
                Procesamiento["i"]=pos
                print(Programa[pos], "entro a comando por bloque")
                Procesamiento=Verify_Command(Procesamiento) 
                pos=Procesamiento["i"]  
        elif Programa[pos] == "}":
            ejecuta = False
            pos +=1
            Procesamiento["i"]=pos
            print("funciona al salir good", ejecuta, Programa[pos])
            
        elif Programa[pos] == "{":
            pos += 1
            Procesamiento["i"]=pos
            Procesamiento = Verify_Block(Procesamiento)
            pos=Procesamiento["i"]
            coma=False
        elif Programa[pos]=="WHILE" or Programa[pos]=="REPEAT" :
            Procesamiento["i"]=pos
            Procesamiento = verifycycle(Procesamiento)
            pos=Procesamiento["i"]
            coma=False
        elif Programa[pos]=="IF":
            pos =pos+1
            Procesamiento["i"]=pos
            Procesamiento = Verifycondicion(Procesamiento)
            pos=Procesamiento["i"]
            coma=False
        else:
            Procesamiento["Funciona"]=False
            Procesamiento["i"]=pos
            ejecuta = False 

# volver a meter lo de while y lo de condiciones
    
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
    elif Programa[pos] in Procesamiento["PROC"].keys():
        print(Programa[pos],"comando en procesos")
        Parametros = Procesamiento["PROC"][Programa[pos]]
        pos += 1
        if Programa[pos]== "(":
            pos +=1
            verify= True
            coma = False
            conteo =0
            while verify:
                if Programa[pos].isalnum() and Programa[pos] not in Reservadas and not Programa[pos] in Procesamiento["PROC"].keys():
                    conteo += 1
                    coma = False
                elif Programa[pos] =="," and not coma:
                    coma = True
                elif Programa[pos] =="," and coma:
                    Procesamiento["Funciona"] =False
                    verify= False
                elif Programa[pos] ==")" and coma:
                    Procesamiento["Funciona"] =False
                    verify = False
                elif Programa[pos] ==")" and not coma:
                    verify = False
                else:
                    Procesamiento["Funciona"] =False
                    verify = False
                pos +=1
            Procesamiento["i"]=pos
            print(Parametros, conteo)
            if Parametros != conteo:
                Procesamiento["Funciona"] =False
                print(Parametros, conteo, "error numero")
        else:
            Procesamiento["Funciona"] =False 
            print(Procesamiento["PROC"].keys(), "llllll")
            print(Programa[pos], "andreaaa")
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
            print("retorno", Programa[pos])

        else: 
            Procesamiento["Funciona"]=False
    if Procesamiento["Funciona"]:
        print("El programa es CORRECTO")
    else:
        print("El programa es ERRONEO")
        Programa=Procesamiento["PROG"]
        pos =Procesamiento["i"]
        print(Programa[pos-2],Programa[pos-1],Programa[pos],Programa[pos+1],Programa[pos+2], Programa[pos+3])
        print(pos)
        
Inicio(Procesamiento)