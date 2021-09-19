from sys import stdin
import os

diccionarioRegister = {"$zero":"00000", "$at": "00001", "$v0":"00010", "$v1":"00011", "$a0":"00100", "$a1":"00101", "$a2":"00110", "$a3":"00111", "$t0":"01000", "$t1":"01001", "$t2":"01010", "$t3":"01011", "$t4":"01100", "$t5":"01101", "$t6":"01110", "$t7":"01111", "$s0":"10000", "$s1":"10001", "$s2":"10010", "$s3":"10011", "$s4":"10100", "$s5":"10101", "$s6":"10110", "$s7":"10111", "$t8":"11000", "$t9":"11001", "$k0":"11010", "$k1":"11011", "$gp":"11100", "$sp":"11101", "$fp":"11110", "$ra":"11111"}
functs = {"sll":"000000", "srl":"000010", "sra":"000011", "sllv":"000100", "srlv":"000110", "srav":"000111", "jr":"001000", "jalr":"001001", "movz":"001010", "movn":"001011", "syscall":"001100", "break":"001101", "sync":"001111", "mfhi":"010000", "mthi":"010001", "mflo":"010010", "mtlo":"010011", "mult":"011000", "multu":"011001", "div":"011010", "divu":"011011", "add":"100000", "addu":"100001", "sub":"100010", "subu":"100011", "and":"100100", "or":"100101", "xor":"100110", "nor":"100111", "slt":"101010", "sltu":"101011", "tge":"110000", "tgeu":"110001", "tlt":"110010", "tltu":"110011", "teq":"110100", "tne":"110110"}

traduccion = []

def translateR(matriz): #Se tiene que pasar la matrix en la posicion en la que se va a traducir
    opcode = "000000"
    rd = "00000"
    rs = "00000"
    rt = "00000"
    shamt = "00000"
    funct = "000000"
    x = matriz[0].replace(',', ' ').split()
    if x[0] == "slr" or x[0] == "sll":
        rd = diccionarioRegister[x[1]]
        rt = diccionarioRegister[x[2]]
        shamt = format(int(x[3]), '05b')
        if x[0] == "slr":
            funct = functs["slr"]
        elif x[0] == "sll":
            funct = functs["sll"]
    else:
        rd = diccionarioRegister[x[1]]
        rs = diccionarioRegister[x[2]]
        rd = diccionarioRegister[x[3]]
        funct = functs[x[0]]

def translateI(matriz):
    opcode = "000000"
    rs = "00000"
    rt = "00000"
    immediate = "0000000000000000"
    x = matriz[0].replace(',', ' ').split()

def translateJ(matriz):
    opcode = "000000"
    address = "00000000000000000000000000"


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
    diccionario1 = {"add":1,"addu":1,"addi":2,"addiu":2,"and":1,"andi":2,"div":3,"divu":3,"mult":3,"multu":3,
    "nor":1,"or":1,"ori":2,"sll":2,"beq":4,"j":5,"jal":5,"jr":6,"lbu":7,"lhu":7,"ll":7,"lui":7,"lw":7,
    "slt":1,"slti":2,"sltiu":2,"sltu":1 ,"srl":2,"sll":2,"sb":7,"sc":7,"sh":7,"sw":7,"sub":1,"subu":1,"mfhi":6,"mflo":6}
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
        elif(diccionario1[matrix[line]] == 3):
            if(len(matrix[line])!=3):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
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
        elif(diccionario1[matrix[line]] == 4):
            if(len(matrix[line])!=4):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
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
                existe = False
                for i in range(len(matrix)):
                    if(len(matrix[i]) == 1 ):
                        matrix[i][0].replace(":","")
                        if(matrix[line][3] == matrix[i][0]):
                            existe = True
                if(existe==False):
                    print("Su codigo presenta un eror en la linea " ,line+1 ,"\n")
                    return False
        elif(diccionario1[matrix[line]] == 5):
            if(len(matrix[line])!=2):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
                return False
            else:
                existe = False
                for i in range(len(matrix)):
                    if(len(matrix[i]) == 1 ):
                        matrix[i][0].replace(":","")
                        if(matrix[line][1] == matrix[i][0]):
                            existe = True
                if(existe==False):
                    print("Su codigo presenta un eror en la linea " ,line+1 ,"\n")
                    return False
        elif(diccionario1[matrix[line]] == 6):
            if(len(matrix[line])!=2):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
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
        elif(diccionario1[matrix[line]] == 7):
            if(len(matrix[line])!=3):
                print("Su codigo presenta un eror en la linea " ,line ,"\n")
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