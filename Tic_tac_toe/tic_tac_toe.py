import os
import time
 #Funcion que detecta el sistema operativo y borra la consola
def borrarPantalla():
  if os.name == "posix":
    os.system ("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system ("cls")

gato = {
  "1" : "-", "2" : "-", "3" : "-", 
  "4" : "-", "5" : "-", "6" : "-", 
  "7" : "-", "8" : "-", "9" : "-", 
}

print('Titc-Tac-Toe (Gato)')
print(' Juego   Posiciones')
print('════════════════════')
print(' '+ gato["1"] + '│'+ gato["2"] + '│' + gato["3"]+ "   1│2│3")
print(' ─┼─┼─   ─┼─┼─')
print(' '+ gato["4"] + '│'+ gato["5"] + '│' + gato["6"]+ "   4│5│6")
print(' ─┼─┼─   ─┼─┼─')
print(' '+ gato["7"] + '│'+ gato["8"] + '│' + gato["9"]+ "   7│8│9")

#time.sleep(5)

#borrarPantalla()
