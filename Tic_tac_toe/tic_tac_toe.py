import os
import time
import random

contador = random.randint(1,2)

gato = {
  "1" : "-", "2" : "-", "3" : "-", 
  "4" : "-", "5" : "-", "6" : "-", 
  "7" : "-", "8" : "-", "9" : "-", 
}

ganador ="ninguno" #Variable que comprueba si hay un ganador




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
  print(' Juego  Posiciones')
  print('════════════════════')
  print(' '+ gato["1"] + '│'+ gato["2"] + '│' + gato["3"]+ "   1│2│3")
  print(' ─┼─┼─   ─┼─┼─')
  print(' '+ gato["4"] + '│'+ gato["5"] + '│' + gato["6"]+ "   4│5│6")
  print(' ─┼─┼─   ─┼─┼─')
  print(' '+ gato["7"] + '│'+ gato["8"] + '│' + gato["9"]+ "   7│8│9")
#  print("ganador: " + ganador)

#Funcion para alternar Jugadas
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
      borrarPantalla()
      imprimirjuego()
    else:
      print('Selecciona una casilla vacia');
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
      print('Selecciona una casilla vacia');
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

    


#time.sleep(5)

borrarPantalla()


app()
