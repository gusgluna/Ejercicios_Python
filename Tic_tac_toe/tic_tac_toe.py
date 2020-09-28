import os
import time
import random

contador = random.randint(1,2) #Variable utilizada para alternar las jugadas.
ganador ="ninguno" #Variable que comprueba si hay un ganador
gato = {
  "1" : "-", "2" : "-", "3" : "-", 
  "4" : "-", "5" : "-", "6" : "-", 
  "7" : "-", "8" : "-", "9" : "-", 
}

def app():
  imprimirjuego()
  siguientejugada()

#Funcion que detecta el sistema operativo y borra la consola
def borrarPantalla():
  if os.name == "posix":
    os.system ("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system ("cls")
    
#Funcion que Imprime el juego en la consola
def imprimirjuego():
  print('Titc-Tac-Toe (Gato)')
  print(' Juego  Posiciones')
  print('════════════════════')
  print(' '+ gato["1"] + '│'+ gato["2"] + '│' + gato["3"]+ "   1│2│3")
  print(' ─┼─┼─   ─┼─┼─')
  print(' '+ gato["4"] + '│'+ gato["5"] + '│' + gato["6"]+ "   4│5│6")
  print(' ─┼─┼─   ─┼─┼─')
  print(' '+ gato["7"] + '│'+ gato["8"] + '│' + gato["9"]+ "   7│8│9")
  
#Funcion para alternar Jugadas y detecta cual es el ganador
def siguientejugada():
  global contador
  while ganador == "ninguno":
    if contador % 2 == 0:
      jugadaO()
      contador = contador + 1
    else:
      jugadaX()
      contador = contador + 1
  if ganador == "Gana X":
    print('*** El Ganador es X ***')
  if ganador == "Gana O":
    print('*** El Ganador es O ***')

def jugadaO():
  marca = input('Jugador O escribe el numero donde quieres marcar:')
  valores = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
  if marca in valores:
    if gato[marca] == '-':
      gato[marca] = 'O'
      gana_O()
      borrarPantalla()
      imprimirjuego()
    else:
      print('Selecciona una casilla vacia')
      time.sleep(1)
      borrarPantalla()
      imprimirjuego()
      jugadaO()
  else:
    print("Solo puedes ingresar numeros enteros del 1 al 9")
    time.sleep(1)
    borrarPantalla()
    imprimirjuego()
    jugadaO()

def jugadaX():
  marca = input('Jugador X escribe el numero donde quieres marcar:')
  valores = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
  if marca in valores:
    if gato[marca] == '-':
      gato[marca] = 'X'
      gana_X()
      borrarPantalla()
      imprimirjuego()
    else:
      print('Selecciona una casilla vacia')
      time.sleep(1)
      borrarPantalla()
      imprimirjuego()
      jugadaX()
  else:
    print("Solo puedes ingresar numeros enteros del 1 al 9")
    time.sleep(1)
    borrarPantalla()
    imprimirjuego()
    jugadaX()

#Funcion que detecta quien gano
def gana_X():
  global ganador
  if gato["1"] == "X" and gato["2"] == "X" and gato["3"] == "X":
    ganador = "Gana X"
  if gato["4"] == "X" and gato["5"] == "X" and gato["6"] == "X":
    ganador = "Gana X"
  if gato["7"] == "X" and gato["8"] == "X" and gato["9"] == "X":
    ganador = "Gana X"
  if gato["1"] == "X" and gato["4"] == "X" and gato["7"] == "X":
    ganador = "Gana X"
  if gato["2"] == "X" and gato["5"] == "X" and gato["8"] == "X":
    ganador = "Gana X"
  if gato["3"] == "X" and gato["6"] == "X" and gato["9"] == "X":
    ganador = "Gana X"
  if gato["1"] == "X" and gato["5"] == "X" and gato["9"] == "X":
    ganador = "Gana X"
  if gato["3"] == "X" and gato["5"] == "X" and gato["7"] == "X":
    ganador = "Gana X"

def gana_O():
  global ganador
  if gato["1"] == "O" and gato["2"] == "O" and gato["3"] == "O":
    ganador = "Gana O"
  if gato["4"] == "O" and gato["5"] == "O" and gato["6"] == "O":
    ganador = "Gana O"
  if gato["7"] == "O" and gato["8"] == "O" and gato["9"] == "O":
    ganador = "Gana O"
  if gato["1"] == "O" and gato["4"] == "O" and gato["O"] == "O":
    ganador = "Gana O"
  if gato["2"] == "O" and gato["5"] == "O" and gato["8"] == "O":
    ganador = "Gana O"
  if gato["3"] == "O" and gato["6"] == "O" and gato["9"] == "O":
    ganador = "Gana O"
  if gato["1"] == "O" and gato["5"] == "O" and gato["9"] == "O":
    ganador = "Gana O"
  if gato["3"] == "O" and gato["5"] == "O" and gato["7"] == "O":
    ganador = "Gana O"

borrarPantalla()

app()
