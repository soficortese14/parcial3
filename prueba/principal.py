import os
import funciones as fn
lista_jugadores=[]
lista_imprimir=['Principiante','Avanzado','Experto']
try:
    while True:
        print('***bienvenido la empresa eSports “eShirlitos” ***')
        print('''
        1.- Registrar puntajes torneo
        2.- Listar los todos puntajes
        3.- Imprimir por Tipo
        4.- Salir del programa''')
        opc=int(input('seleccione opcion: '))
        if opc>0 and opc<5:
            print('accediendo correctamente')
        else:
            print('numero invalido, intente ota vez')
            if opc==1:
                print('='*50)
                print('elegiste: Registrar puntajes torneo ')
                id_jugador=input('ingrese su ID: ')
                nombre=input('ingrese su nombre y apellido: ')
                valorant=int(input('Ingrese puntaje obtenido  valorant: '))
                fornite= int(input('Ingrese puntaje obtenido  fornite: '))
                fifa=int(input('Ingrese puntaje obtenido  fifa: '))
                tipo=input('ingrese su tipo (Principiante-Avanzado - Experto): ')
                print('se ha guardado correctamente')
                fn.registrar_puntaje()
            elif opc==2:
                print('='*50)
                print('elegiste: Listar los todos puntajes')
                fn.listar_puntajes(lista_jugadores)
            elif opc==3:
                print('='*50)
                print('elegiste: Imprimir por Tipo')
                fn.imprimir_tipo()
            elif opc==4:
                print('='*50)
                print('Saliendo del programa,adios')
                break
            else:
                print('='*50)
                print('invalido, intente otra vez')
except Exception as e:
    print('error: ',e)