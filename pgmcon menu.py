# import only system from os 
from os import system, name
  
# import sleep to show output for some time period 
from time import sleep 


def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')
        

####################################################################################################
# Menú Principal
import os
def menu() :
   # os.system('cls') cuando la pongo intenta crear una nueva ventana y se cierra manteniendo la original
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print ("             Areas de poliedros - Area Lateral - Area de la Base - Area total")
    print  ("    ")
    print ("        Seleccione el cuerpo a calcular")
    print  ("    ")
    print  ("    ")
    print  ("          1 - Cubo")
    print  ("          2 - Prisma rectangular    ")
    print  ("          3 - Pirámide rectangular    ")
    print  ("         99 - Ley de Euler para calculo de (V)ertices, (A)ristas, (C)aras    ")
    print  ("    ")
    print  ("          0 - Salir    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")
    print  ("    ")    
#Fin Menú principal
##################################################################################################


while True:
# Mostramos el menu
    menu()
    
    seleccion = int(input())
#
#   Cubo
#
    if seleccion == 1 :
            x = int(input("Ingresa el lado del cubo en cm: "))
            pb = x * 4
            y = x ** 2 *2
            z = x * 4 * x
            print (" El perimetro de la base es de :" , pb , "cm")
            print (" El área de la base es :" , y , "cm2")
            print (" El área lateral es :", z , "cm2")
            print (" El área total es ", y + z, "cm2")
            print  ("    ")
            print  ("    ")
            sleep(5)  #Espera n segundos y continua
            clear()   #limpia la pantalla
            lineabca = ' \n \n \n \n \n \n \n \n '  #Repito lineas en blanco
            input ("Presione Enter para volver al menú principal")
            print (1 * lineabca)
#
#  Fin Cubo
#
#
#  Prisma Rectangular
#
    elif seleccion == 2 :
        a = int(input("Ingresa la medida de un lado de base del prima en cm: "))
        b = int(input("Ingresa la medida del segundo lado de base del prima en cm: "))
        c = int(input("Ingresa la medida de la altura del prisma en cm: "))
        pb = 2 * a + 2 *b
        print (" El perimetro de la base es de :" , pb , "cm")
        ab = a *b * 2
        print (" El area de la base es de :" , ab , "cm2")
        al = pb * c
        print (" El area lateral es de :" , al , "cm2")
        print (" El área total es ", ab + al, "cm2")
        print  ("    ")
        print  ("    ")
        sleep(5)  #Espera n segundos y continua
        clear()   #limpia la pantalla
        lineabca = ' \n \n \n \n \n \n \n \n '  #Repito lineas en blanco
        input ("Presione Enter para volver al menú principal")
        print (1 * lineabca)
#
#  Fin Prisma Rectangular
#
#
#  Pirámide rectangular
#
    elif seleccion == 3 :
        a = int(input("Ingresa la medida de la arista de la base en cm: "))
        b = int(input("Ingresa la medida de la altura /(h) de la pirámide en cm: "))
        c = int(input("Ingresa la medida de la apotema de la pirámide en cm: "))
        pb = 4 * a 
        print (" El perimetro de la base es de :" , pb , "cm")
        ab = a **2 
        print (" El area de la base es de :" , ab , "cm2")
        al = pb * c / 2
        print (" El area lateral es de :" , al , "cm2")
        print (" El área total es ", ab + al, "cm2")
        print  ("    ")
        print  ("    ")
        sleep(5)  #Espera n segundos y continua
        clear()   #limpia la pantalla
        lineabca = ' \n \n \n \n \n \n \n \n '  #Repito lineas en blanco
        input ("Presione Enter para volver al menú principal")
        print (1 * lineabca)
#
#  Fin Pirámide rectangular
#
#
#  Ley de Euler
#

    elif seleccion == 99 :
        a = int(input("Ingresa la cantidad de Caras o -1 si no la sabe "))
        b = int(input("Ingresa la cantidad de Vertices o -1 si no la sabe "))
        c = int(input("Ingresa la cantidad de Aristas o -1 si no la sabe "))
        conmenosuno = 0
        if a == -1 :
            conmenosuno = conmenosuno + 1
        if b == -1 :
            conmenosuno = conmenosuno + 1    
        if c == -1 :
            conmenosuno = conmenosuno + 1    
        if a == -1 and conmenosuno < 2 :
            a= c + 2 - b
            print (" La cantidad de caras es de :" , a )
        if b == -1 and conmenosuno < 2 :
                b = c + 2 - a
                print (" La cantidad de vertices es de :" , b )
        if c == -1 and conmenosuno < 2 :
                c = a + b - 2
                print (" La cantidad de aristas es de :" , c )
        if conmenosuno > 1 :
           print ("Error: Introdujo mas de una incógnita")
    
        print (" Recuerde que la formula de Euler dice C + V = A + 2")
        print  ("    ")
        print  ("    ")
        sleep(5)  #Espera n segundos y continua
        clear()   #limpia la pantalla
        lineabca = ' \n \n \n \n \n \n \n \n '  #Repito lineas en blanco
        input ("Presione Enter para volver al menú principal")
        print (1 * lineabca)
#
#  Fin Ley de Euler
#




    else :
        if seleccion == 0 :
            break
        else :
            print ("Opción inválida")
    
        
