import os
import time

gato = {
  "1" : "-", "2" : "-", "3" : "-", 
  "4" : "-", "5" : "-", "6" : "-", 
  "7" : "-", "8" : "-", "9" : "-", 
}


def app():
  imprimirjuego()
  jugadaO()

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

def jugadaO():
  marca = input('Jugador O escribe el numero doned quieres marcar:')
  gato[marca] = 'O'
  borrarPantalla()
  imprimirjuego()


#time.sleep(5)



app()
