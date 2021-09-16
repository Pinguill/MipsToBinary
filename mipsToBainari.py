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
def main():
    matrix = []
    opcion = 0
    clear()
    print("Bienvenido al conversor de mips a binario\n")
    while(opcion != 2 and opcion != 1):
        opcion = int(input("por favor ingrese la opcion que desea realizar:\n1. Convertir codigo mips a codigo binario\n2. Cerrar\n:"))
        clear()
        if(opcion==1):
            lectura(matrix)
            opcion = 0
    clear()
main()