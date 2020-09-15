import os
import time
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
  if os.name == "posix":
    os.system ("clear")
  elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system ("cls")

print('Juego Titc-Tac-Toe (Gato)')

print(' x│o│o')
print(' ─┼─┼─')
print(' x│o│o')
print(' ─┼─┼─')
print(' x│o│o')

time.sleep(1)

borrarPantalla()
