from sys import stdin
import os

diccionarioRegister = {"$zero":"00000", "$at": "00001", "$v0":"00010", "$v1":"00011", "$a0":"00100", "$a1":"00101", "$a2":"00110", "$a3":"00111", "$t0":"01000", "$t1":"01001", "$t2":"01010", "$t3":"01011", "$t4":"01100", "$t5":"01101", "$t6":"01110", "$t7":"01111", "$s0":"10000", "$s1":"10001", "$s2":"10010", "$s3":"10011", "$s4":"10100", "$s5":"10101", "$s6":"10110", "$s7":"10111", "$t8":"11000", "$t9":"11001", "$k0":"11010", "$k1":"11011", "$gp":"11100", "$sp":"11101", "$fp":"11110", "$ra":"11111"}
functs = {"sll":"000000", "srl":"000010", "sra":"000011", "sllv":"000100", "srlv":"000110", "srav":"000111", "jr":"001000", "jalr":"001001", "movz":"001010", "movn":"001011", "syscall":"001100", "break":"001101", "sync":"001111", "mfhi":"010000", "mthi":"010001", "mflo":"010010", "mtlo":"010011", "mult":"011000", "multu":"011001", "div":"011010", "divu":"011011", "add":"100000", "addu":"100001", "sub":"100010", "subu":"100011", "and":"100100", "or":"100101", "xor":"100110", "nor":"100111", "slt":"101010", "sltu":"101011", "tge":"110000", "tgeu":"110001", "tlt":"110010", "tltu":"110011", "teq":"110100", "tne":"110110"}
opcodes = {"j":"000010", "jal":"000011", "beq":"000100", "bne":"000101", "blez":"000110", "bgtz":"000111", "addi":"001000", "addiu":"001001", "slti":"001010", "sltiu":"001011", "andi":"001100", "ori":"001101", "xori":"001110", "lui":"001111", "lb":"100000", "lh":"100001", "lwl":"100010", "lw":"100011", "lbu":"100100", "lhu":"100101", "lwr":"100110", "sb":"101000", "sh":"101001", "swl":"101010", "sw":"101011", "swr":"101110", "cache":"101111", "ll":"110000", "lwc1":"110001", "lwc2":"110010", "pref":"110011", "ldc1":"110101", "ldc2":"110110", "sc":"111000", "swc1":"111001", "swc2":"111010", "sdc1":"111101", "sdc2":"111110"}
address = []

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
    x = matriz[0].replace(')', ' ')
    x = x.replace('(', ' ')
    x = x.replace(',', ' ')
    x = x.split()
    opcode = opcodes[x[0]]
    if x[0] == "beq" or x[0] == "bne":
        a
    else:
        rt = diccionarioRegister[x[1]]
        rs = diccionarioRegister[x[3]]
        immediate = format(int(x[2], 0), '016b')


def translateJ(matriz):
    opcode = "000000"
    address = "00000000000000000000000000"
    x = matriz[0].replace(',', ' ').split()
    opcode = opcodes[x[0]]



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