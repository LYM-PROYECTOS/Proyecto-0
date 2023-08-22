
file = open(input("Ingrese ruta de acceso del archivo con el programa (formato .txt): "))
ReadFile = file.read()
program = ReadFile.split("\n")
Procesamiento = (0, True, program)

def SaveProgram(Procesamiento):
    Final_Program=[]
    program=Procesamiento[2]
    for i in range(len(program)):
        palabra = program[i]
        if palabra != " ":


    return Procesamiento