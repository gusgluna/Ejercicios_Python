import random

bloque01 = {
  'a1' : '', 'b1' : '', 'c1' : '',
  'a2' : '', 'b2' : '', 'c2' : '',
}

for numeros in bloque01.values():
  print(numeros,end="")

rand = random.randint(0,10)
print(rand)
