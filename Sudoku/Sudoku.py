import random

bloque_01 = {
  'a1' : 0, 'b1' : 0, 'c1' : 0, 'd1' : 0, 'e1' : 0, 'f1' : 0,
  'a2' : 0, 'b2' : 0, 'c2' : 0, 'd2' : 0, 'e2' : 0, 'f2' : 0,
  'a3' : 0, 'b3' : 0, 'c3' : 0, 'd3' : 0, 'e3' : 0, 'f3' : 0,
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

#Definiendo el valor de c2
tup_comp = (bloque_01['a1'], bloque_01['b1'],
bloque_01['c1'], bloque_01['a2'], bloque_01['b2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['c2'] = num_rand

#Definiendo el valor de a3
tup_comp = (bloque_01['a1'], bloque_01['b1'],
bloque_01['c1'], bloque_01['a2'], bloque_01['b2'],bloque_01['c2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['a3'] = num_rand

#Definiendo el valor de b3
tup_comp = (bloque_01['a1'], bloque_01['b1'],
bloque_01['c1'], bloque_01['a2'], bloque_01['b2'],bloque_01['c2'],bloque_01['a3'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['b3'] = num_rand

#Definiendo el valor de c3
tup_comp = (bloque_01['a1'], bloque_01['b1'],
bloque_01['c1'], bloque_01['a2'], bloque_01['b2'],bloque_01['c2'],bloque_01['a3'],bloque_01['b3'])
num_rand = 1
while num_rand in tup_comp:
  num_rand = num_rand + 1
bloque_01['c3'] = num_rand

#Definiendo el valor de d1
tup_comp = (bloque_01['a1'], bloque_01['b1'],
bloque_01['c1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['d1'] = num_rand

#Definiendo el valor de e1
tup_comp = (bloque_01['a1'], bloque_01['b1'],
bloque_01['c1'], bloque_01['d1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['e1'] = num_rand

#Definiendo el valor de f1
tup_comp = (bloque_01['a1'], bloque_01['b1'],
bloque_01['c1'], bloque_01['d1'], bloque_01['e1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['f1'] = num_rand

#Definiendo el valor de d2
tup_comp = (bloque_01['a2'], bloque_01['b2'],
bloque_01['c2'], bloque_01['d1'], bloque_01['e1'], bloque_01['f1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['d2'] = num_rand

#Definiendo el valor de e2
tup_comp = (bloque_01['a2'], bloque_01['b2'],
bloque_01['c2'], bloque_01['d1'], bloque_01['e1'], bloque_01['f1'], bloque_01['d2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['e2'] = num_rand


print('╔═════╦═════╦')
print('║'+str(bloque_01['a1'])+'│'+str(bloque_01['b1'])+'│'+str(bloque_01['c1'])+'║'+str(bloque_01['d1'])+'│'+str(bloque_01['e1'])+'│'+str(bloque_01['f1'])+'║')

print('║'+str(bloque_01['a2'])+'│'+str(bloque_01['b2'])+'│'+str(bloque_01['c2'])+'║'+str(bloque_01['d2'])+'│'+str(bloque_01['e2'])+'│'+str(bloque_01['f2'])+'║')

print('║'+str(bloque_01['a3'])+'│'+str(bloque_01['b3'])+'│'+str(bloque_01['c3'])+'║'+str(bloque_01['d3'])+'│'+str(bloque_01['e3'])+'│'+str(bloque_01['f3'])+'║')
print('╚═════╬═════╬')
