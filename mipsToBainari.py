from sys import stdin
import os

def clear():
    os.system('cls')
def lectura(matrix):
    mips_binario = 'mips/mipsToBinary.txt'
    with open(mips_binario) as f_obj:
        for line in f_obj:
            particiones = line.split(" ")
            matrix.append(particiones)
    print(matrix)
    
def verificar(matrix):
    diccionario1 = {"add":1,"addu":2,"addi":3,"addiu":4,"and":5,"andi":6,"div":7,"divu":8,"mult":9,"multu":10,
    "nor":11,"or":12,"ori":13,"sll":14,"beq":15,"j":16,"jal":16,"jr":18,"lbu":19,"lhu":20,"ll":21,"lui":22,"lw":23,
    "slt":24,"slti":25,"sltiu":26,"sltu":27,"srl":28,"sb":29,"sc":30,"sh":31,"sw":32,"sub":33,"subu":34,"mfhi":35,"mflo":36}
    for line in len(matrix):
        if(diccionario1[matrix[line]] == 1):
            if(len(matrix[line])!=4):
                print("Su codigo presenta un eror en la linea " ,line+1 ,"\n")
                return False
            else:
                for i in range(1,len(matrix[line])):
                    if(((matrix[line][i][0] == "$" and matrix[line][i][1] == "a" and matrix[line][i][2] == "t") or 
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="v" and (matrix[line][i][2] == "1" or matrix[line][i][2] == "0")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="a" and (matrix[line][i][2] == "0" or matrix[line][i][2] == "1" or matrix[line][i][2] == "2" or matrix[line][i][2] == "3")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="t" and (matrix[line][i][2] == "0" or matrix[line][i][2] == "1" or matrix[line][i][2] == "2" or matrix[line][i][2] == "3" or matrix[line][i][2] == "4" or matrix[line][i][2] == "5" or matrix[line][i][2] == "6" or matrix[line][i][2] == "7")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="s" and (matrix[line][i][2] == "0" or matrix[line][i][2] == "1" or matrix[line][i][2] == "2" or matrix[line][i][2] == "3" or matrix[line][i][2] == "4" or matrix[line][i][2] == "5" or matrix[line][i][2] == "6" or matrix[line][i][2] == "7" or matrix[line][i][2] == "8" or matrix[line][i][2] == "9")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="k" and (matrix[line][i][2] == "1" or matrix[line][i][2] == "0")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] == "s" and matrix[line][i][2] == "p") or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] == "f" and matrix[line][i][2] == "p") or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] == "r" and matrix[line][i][2] == "a")) == False):
                        print("Su codigo presenta un eror en la linea " ,line+1 ,"\n")
                        return False
        elif(diccionario1[matrix[line]] == 2):
            if(len(matrix[line])!=4):
                print("Su codigo presenta un eror en la linea " ,line+1 ,"\n")
                return False
            else:
                for i in range(1,len(matrix[line])):
                    if(((matrix[line][i][0] == "$" and matrix[line][i][1] == "a" and matrix[line][i][2] == "t") or 
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="v" and (matrix[line][i][2] == "1" or matrix[line][i][2] == "0")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="a" and (matrix[line][i][2] == "0" or matrix[line][i][2] == "1" or matrix[line][i][2] == "2" or matrix[line][i][2] == "3")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="t" and (matrix[line][i][2] == "0" or matrix[line][i][2] == "1" or matrix[line][i][2] == "2" or matrix[line][i][2] == "3" or matrix[line][i][2] == "4" or matrix[line][i][2] == "5" or matrix[line][i][2] == "6" or matrix[line][i][2] == "7")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="s" and (matrix[line][i][2] == "0" or matrix[line][i][2] == "1" or matrix[line][i][2] == "2" or matrix[line][i][2] == "3" or matrix[line][i][2] == "4" or matrix[line][i][2] == "5" or matrix[line][i][2] == "6" or matrix[line][i][2] == "7" or matrix[line][i][2] == "8" or matrix[line][i][2] == "9")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="k" and (matrix[line][i][2] == "1" or matrix[line][i][2] == "0")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] == "s" and matrix[line][i][2] == "p") or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] == "f" and matrix[line][i][2] == "p") or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] == "r" and matrix[line][i][2] == "a")) == False):
                        print("Su codigo presenta un eror en la linea " ,line+1 ,"\n")
                        return False
        elif(diccionario1[matrix[line]] == 3):
            if(len(matrix[line])!=4):
                print("Su codigo presenta un eror en la linea " ,line+1 ,"\n")
                return False
            else:
                for i in range(1,len(matrix[line])-1):
                    if(((matrix[line][i][0] == "$" and matrix[line][i][1] == "a" and matrix[line][i][2] == "t") or 
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="v" and (matrix[line][i][2] == "1" or matrix[line][i][2] == "0")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="a" and (matrix[line][i][2] == "0" or matrix[line][i][2] == "1" or matrix[line][i][2] == "2" or matrix[line][i][2] == "3")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="t" and (matrix[line][i][2] == "0" or matrix[line][i][2] == "1" or matrix[line][i][2] == "2" or matrix[line][i][2] == "3" or matrix[line][i][2] == "4" or matrix[line][i][2] == "5" or matrix[line][i][2] == "6" or matrix[line][i][2] == "7")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="s" and (matrix[line][i][2] == "0" or matrix[line][i][2] == "1" or matrix[line][i][2] == "2" or matrix[line][i][2] == "3" or matrix[line][i][2] == "4" or matrix[line][i][2] == "5" or matrix[line][i][2] == "6" or matrix[line][i][2] == "7" or matrix[line][i][2] == "8" or matrix[line][i][2] == "9")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] =="k" and (matrix[line][i][2] == "1" or matrix[line][i][2] == "0")) or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] == "s" and matrix[line][i][2] == "p") or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] == "f" and matrix[line][i][2] == "p") or
                    (matrix[line][i][0] == "$" and matrix[line][i][1] == "r" and matrix[line][i][2] == "a")) == False):
                        print("Su codigo presenta un eror en la linea " ,line+1 ,"\n")
                        return False
                if((matrix[line][3][0] == "0" and matrix[line][3][1] == "x" ) == False):
                    print("Su codigo presenta un eror en la linea " ,line+1 ,"\n")
                    return False
        elif(diccionario1[matrix[line]] == 4):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 5):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 6):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 7):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 8):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 9):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 10):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 11):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 12):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 13):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 14):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 15):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 16):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 17):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 18):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 19):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 20):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 21):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 22):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 23):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 24):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 25):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 26):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 27):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 28):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 29):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 30):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 31):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 32):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 33):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 34):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 35):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
        elif(diccionario1[matrix[line]] == 36):
            if(len(matrix[line])==1):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
def main():
    opcion = 0
    clear()
    print("Bienvenido al conversor de mips a binario\n")
    while(opcion != 2 and opcion != 1):
        opcion = int(input("por favor ingrese la opcion que desea realizar:\n1. Convertir codigo mips a codigo binario\n2. Cerrar\n:"))
        clear()
        if(opcion==1):
            matrix = []
            lectura(matrix)
            opcion = 0
    clear()
main()