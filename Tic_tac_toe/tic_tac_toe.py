import os
import time
import random


contador = random.randint(1,2)

gato = {
  "1" : "-", "2" : "-", "3" : "-", 
  "4" : "-", "5" : "-", "6" : "-", 
  "7" : "-", "8" : "-", "9" : "-", 
}

ganador = False #Variable que comprueba si hay un ganador




def app():
  imprimirjuego()
  siguientejugada()

#Funcion que detecta el sistema operativo y borra la consola
def borrarPantalla():
  if os.name == "posix":
    os.system ("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system ("cls")

def imprimirjuego():
  print('Titc-Tac-Toe (Gato)')
  print(' Juego   Posiciones')
  print('════════════════════')
  print(' '+ gato["1"] + '│'+ gato["2"] + '│' + gato["3"]+ "   1│2│3")
  print(' ─┼─┼─   ─┼─┼─')
  print(' '+ gato["4"] + '│'+ gato["5"] + '│' + gato["6"]+ "   4│5│6")
  print(' ─┼─┼─   ─┼─┼─')
  print(' '+ gato["7"] + '│'+ gato["8"] + '│' + gato["9"]+ "   7│8│9")
  print(ganador)

#Funcion para alternar Jugadas
def siguientejugada():
  global contador
  while ganador == False:
    if contador % 2 == 0:
      jugadaO()
      ganador_1()
      contador = contador + 1
    else:
      jugadaX()
      ganador_1()
      contador = contador + 1



def jugadaO():
  marca = input('Jugador O escribe el numero donde quieres marcar:')
  gato[marca] = 'O'
  ganador_1()
  borrarPantalla()
  imprimirjuego()

def jugadaX():
  marca = input('Jugador X escribe el numero donde quieres marcar:')
  if gato[marca] == '-':
    gato[marca] = 'X'
    ganador_1()
    borrarPantalla()
    imprimirjuego()
  else:
    print('Selecciona una casilla vacia');
    time.sleep(1)
    borrarPantalla()
    imprimirjuego()
    jugadaX()



#Funcion que detecta quien gano
def ganador_1():
  global ganador
  if gato["1"] == "X" and gato["2"] == "X" and gato["3"] == "X":
    ganador = True
    


#time.sleep(5)

borrarPantalla()


app()
