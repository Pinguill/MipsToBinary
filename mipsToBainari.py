from sys import stdin
import os

diccionarioRegister = {"$zero":"00000", "$at": "00001", "$v0":"00010", "$v1":"00011", "$a0":"00100", "$a1":"00101", "$a2":"00110", "$a3":"00111", "$t0":"01000", "$t1":"01001", "$t2":"01010", "$t3":"01011", "$t4":"01100", "$t5":"01101", "$t6":"01110", "$t7":"01111", "$s0":"10000", "$s1":"10001", "$s2":"10010", "$s3":"10011", "$s4":"10100", "$s5":"10101", "$s6":"10110", "$s7":"10111", "$t8":"11000", "$t9":"11001", "$k0":"11010", "$k1":"11011", "$gp":"11100", "$sp":"11101", "$fp":"11110", "$ra":"11111"}
functs = {"sll":"000000", "srl":"000010", "sra":"000011", "sllv":"000100", "srlv":"000110", "srav":"000111", "jr":"001000", "jalr":"001001", "movz":"001010", "movn":"001011", "syscall":"001100", "break":"001101", "sync":"001111", "mfhi":"010000", "mthi":"010001", "mflo":"010010", "mtlo":"010011", "mult":"011000", "multu":"011001", "div":"011010", "divu":"011011", "add":"100000", "addu":"100001", "sub":"100010", "subu":"100011", "and":"100100", "or":"100101", "xor":"100110", "nor":"100111", "slt":"101010", "sltu":"101011", "tge":"110000", "tgeu":"110001", "tlt":"110010", "tltu":"110011", "teq":"110100", "tne":"110110"}
opcodes = {"beq":"000100", "bne":"000101", "blez":"000110", "bgtz":"000111", "addi":"001000", "addiu":"001001", "slti":"001010", "sltiu":"001011", "andi":"001100", "ori":"001101", "xori":"001110", "lui":"001111", "lb":"100000", "lh":"100001", "lwl":"100010", "lw":"100011", "lbu":"100100", "lhu":"100101", "lwr":"100110", "sb":"101000", "sh":"101001", "swl":"101010", "sw":"101011", "swr":"101110", "cache":"101111", "ll":"110000", "lwc1":"110001", "lwc2":"110010", "pref":"110011", "ldc1":"110101", "ldc2":"110110", "sc":"111000", "swc1":"111001", "swc2":"111010", "sdc1":"111101", "sdc2":"111110"}
opcodesJ = {"j":"000010", "jal":"000011"}
address = []
traduccion = []
ciclos = 0
ciclos2 = 0

def contadorDeCiclos(matriz):
    global ciclos, ciclos2
    flag = False
    for i in range(len(matriz)):
        if matriz[i][0] == "lb" or matriz[i][0] == "lbu" or matriz[i][0] == "lh" or matriz[i][0] == "lhu" or matriz[i][0] == "lw" :
            ciclos += 5
        elif matriz[i][0] == "beq" or matriz[i][0] == "bne":
            ciclos += 3
            for j in range(i, len(matriz)):
                if(flag == False):
                    ciclos2 += 3
                    print(matriz[j][0])
                    if matriz[j][0] == "lb" or matriz[j][0] == "lbu" or matriz[j][0] == "lh" or matriz[j][0] == "lhu" or matriz[j][0] == "lw" :
                        ciclos2 += 5
                        i += 1
                        if matriz[j + 1][0] == "j" or "jal":
                            ciclos2 += 3
                            flag = True
                            i += 1
                    elif matriz[j][0] in functs:
                        ciclos2 += 4
                        i += 1
                        if matriz[j + 1][0] == "j" or "jal":
                            ciclos2 += 3
                            flag = True
                            i += 1
                    elif matriz[j][0] in  opcodes:
                        ciclos2 += 4
                        i +=1
                        if matriz[j + 1][0] == "j" or "jal":
                            ciclos2 += 3
                            flag = True
                            i += 1
        elif matriz[i][0] in functs:
            ciclos += 4
        elif matriz[i][0] in opcodes:
            ciclos += 4



def translateR(matriz , i): #Se tiene que pasar la matrix en la posicion en la que se va a traducir
    opcode = "000000"
    rd = "00000"
    rs = "00000"
    rt = "00000"
    shamt = "00000"
    funct = "000000"
    if matriz[i][0] == "slr" or matriz[i][0] == "sll":
        rd = diccionarioRegister[matriz[i][1]]
        rt = diccionarioRegister[matriz[i][2]]
        shamt = format(int(matriz[i][3]), '05b')
        if matriz[i][0] == "slr":
            funct = functs["slr"]
        elif matriz[i][0] == "sll":
            funct = functs["sll"]
    else:
        if matriz[i][0] == "jr":
            rs = diccionarioRegister[matriz[i][1]]
            funct = functs[matriz[i][0]]
        else:
            rd = diccionarioRegister[matriz[i][1]]
            rs = diccionarioRegister[matriz[i][2]]
            rt = diccionarioRegister[matriz[i][3]]
            funct = functs[matriz[i][0]]
    traduccion.append(opcode + rs + rt + rd + shamt + funct)

def translateI(matriz, i, address):
    opcode = "000000"
    rs = "00000"
    rt = "00000"
    immediate = "0000000000000000"
    opcode = opcodes[matriz[i][0]]
    actual = address[i]
    if matriz[i][0] == "beq" or matriz[i][0] == "bne":
        for j in range(len(matriz)): #   (label - (actual + 4))/4
            if matriz[i][3] == matriz[j][0]:
                label = address[j]
        rs = diccionarioRegister[matriz[i][1]]
        rt = diccionarioRegister[matriz[i][2]]
        immediate = format(int((int(label, 0) - (int(actual, 0) + 4))/4), '016b' )
    else:
        if matriz[i][0] == "lui":
            rt = diccionarioRegister[matriz[i][1]]
            immediate = format(int(matriz[i][2], 0), '016b')
        else:
            if matriz[i][0] == "lw" or matriz[i][0] == "lhu" or matriz[i][0] == "lh" or matriz[i][0] == "lbu" or matriz[i][0] == "lb" or matriz[i][0] == "sw" or matriz[i][0] == "sh" or matriz[i][0] == "sb" or matriz[i][0] == "sc":
                rt = diccionarioRegister[matriz[i][1]]
                rs = diccionarioRegister[matriz[i][3]]
                immediate = format(int(matriz[i][2], 0), '016b')
            else:
                print(matriz[i])
                rt = diccionarioRegister[matriz[i][1]]
                rs = diccionarioRegister[matriz[i][2]]
                immediate = format(int(matriz[i][3], 0), '016b')
    traduccion.append(opcode + rs + rt + immediate)


def translateJ(matriz, i, address):
    opcode = "000000"
    addressJ = "00000000000000000000000000"
    opcode = opcodesJ[matriz[i][0]]
    for j in range(len(matriz)):
        if matriz[i][1] == matriz[j][0]:
            addressJ = format(int(int(address[j], 0)/4), '026b')
    traduccion.append(opcode + addressJ)


def clear():
    os.system('cls')
def lectura(matrix):
    mips_binario = 'mips/mipsToBinary.txt'
    with open(mips_binario) as f_obj:
        i = 0
        hexa = "0x00400000"
        for line in f_obj:
            particiones = line.replace("\n", '')
            particiones = particiones.replace(',', ' ')
            particiones = particiones.replace('(', ' ')
            particiones = particiones.replace(')', ' ')
            particiones = particiones.replace(':', ' ')
            particiones = particiones.split()
            matrix.append(particiones)
            if ":" in matrix[i][0]:
                address.append(hexa)
            else:
                address.append(hexa)
                hexa = hex(int(hexa, 0) + int("0x4", 0))
            i += 1

    #print(matrix, address)
    
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
    global ciclos, ciclos2
    clear()
    print("Bienvenido al conversor de mips a binario\n")
    while(opcion != 2 and opcion != 1):
        i = 0
        opcion = int(input("por favor ingrese la opcion que desea realizar:\n1. Convertir codigo mips a codigo binario\n2. Cerrar\n:"))
        clear()
        if(opcion==1):
            matrix = []
            lectura(matrix)
            while i != len(matrix):
                if matrix[i][0] in functs:
                    translateR(matrix , i)
                elif matrix[i][0] in opcodes:
                    translateI(matrix, i, address)
                elif matrix[i][0] in opcodesJ:
                    translateJ(matrix, i, address)
                else:
                    print("Error, no se reconocio ninguna instruccion", matrix[i][0])
                i += 1
            contadorDeCiclos(matrix)
            for i in range(len(traduccion)):
                print(traduccion[i])
            print("tcpu =", ciclos, " + ", ciclos2, "n")
            print
            opcion = 0
    clear()
main()