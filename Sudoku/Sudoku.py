import random

bloque_01 = {
  'a1' : 0, 'b1' : 0, 'c1' : 0, 
  'a2' : 0, 'b2' : 0, 'c2' : 0,
  'a3' : 0, 'b3' : 0, 'c3' : 0,
}

#Definiendo el valor de a1
num_rand = random.randint(1,9)
bloque_01['a1'] = num_rand

#Definiendo el valor de b1
num_rand = random.randint(1,9)
while num_rand == bloque_01['a1']:
  num_rand = random.randint(1,9)
bloque_01['b1'] = num_rand

#Definiendo el valor de c1
tup_comp = (bloque_01['a1'], bloque_01['b1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['c1'] = num_rand

#Definiendo el valor de a2
tup_comp = (bloque_01['a1'], bloque_01['b1'],
bloque_01['c1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['a2'] = num_rand

#Definiendo el valor de b2
tup_comp = (bloque_01['a1'], bloque_01['b1'],
bloque_01['c1'], bloque_01['a2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['b2'] = num_rand



print('╔═════╦')
print('║'+str(bloque_01['a1'])+'│'+str(bloque_01['b1'])+'│'+str(bloque_01['c1'])+'║')

print('║'+str(bloque_01['a2'])+'│'+str(bloque_01['b2'])+'│'+str(bloque_01['c2'])+'║')

print('║'+str(bloque_01['a3'])+'│'+str(bloque_01['b3'])+'│'+str(bloque_01['c3'])+'║')
print('╚═════╬')
