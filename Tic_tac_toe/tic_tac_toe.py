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
  victoria()

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

#Funcion para alternar Jugadas
def siguientejugada():
  global contador
  if contador % 2 == 0:
    jugadaO()
    contador = contador + 1
  else:
    jugadaX()
    contador = contador + 1



def jugadaO():
  marca = input('Jugador O escribe el numero doned quieres marcar:')
  gato[marca] = 'O'
  borrarPantalla()
  imprimirjuego()

def jugadaX():
  marca = input('Jugador X escribe el numero doned quieres marcar:')
  gato[marca] = 'X'
  borrarPantalla()
  imprimirjuego()

#Funcion que comprueba si hay ganador
def victoria():
  while ganador == False:
    siguientejugada()


#time.sleep(5)

borrarPantalla()


app()
