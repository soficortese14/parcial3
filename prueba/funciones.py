def registrar_puntaje(lista_jugadores,id_jugador,nombre,valorant,fifa,tipo,ingresado):
    if ingresado==True:
        diccionario={
                'ID jugador': id_jugador,
                'Nombre' : nombre,
                'Valorant': valorant,
                'Fifa' : fifa,
                'Tipo' : tipo,
            }
        diccionario.append(lista_jugadores)
        return lista_jugadores
    elif ingresado is not True:
        print('no hay datos ingresados')
   
def listar_puntajes(lista_jugadoes):
   return(lista_jugadoes)

def imprimir_tipo(tipo,lista_imprimir,tipo_imprimir,tipo_seleccionado_imprimir):
    tipo=input('ingrese su tipo (Principiante-Avanzado - Experto): ')
    if tipo_imprimir=="":
         nombre_archivo='imprimir_tipo.txt'
    elif tipo in lista_imprimir:
        tipo_seleccionado_imprimir=[]
        for tipo in tipo_seleccionado_imprimir:
            if tipo ['Lista_impimir']==tipo_imprimir:
                tipo_imprimir.append(tipo)
        nombre_archivo=(f'archivo{tipo_seleccionado_imprimir}.txt')
    else:
        print('no valido')
        return

with open ('nombre_archivo', 'r') as archivo:
        archivos= archivo.read()
        print(archivos)

