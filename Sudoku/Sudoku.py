import random

bloque_01 = {
  'a1' : 0, 'b1' : 0, 'c1' : 0, 'd1' : 0, 'e1' : 0, 'f1' : 0, 'g1' : 1, 'h1' : 2, 'i1' : 3,
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
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
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

#Definiendo el valor de f2
tup_comp = (bloque_01['a2'], bloque_01['b2'],
bloque_01['c2'], bloque_01['d1'], bloque_01['e1'], bloque_01['f1'], bloque_01['d2'], bloque_01['e2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['f2'] = num_rand

#Definiendo el valor de d3
tup_comp = (bloque_01['a3'], bloque_01['b3'],
bloque_01['c3'], bloque_01['d1'], bloque_01['e1'], bloque_01['f1'], bloque_01['d2'], bloque_01['e2'], bloque_01['f2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['d3'] = num_rand

#Definiendo el valor de e3
tup_comp = (bloque_01['a3'], bloque_01['b3'],
bloque_01['c3'], bloque_01['d1'], bloque_01['e1'], bloque_01['f1'], bloque_01['d2'], bloque_01['e2'], bloque_01['f2'], bloque_01['d3'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['e3'] = num_rand

#Definiendo el valor de f3
tup_comp = (bloque_01['a3'], bloque_01['b3'],
bloque_01['c3'], bloque_01['d1'], bloque_01['e1'], bloque_01['f1'], bloque_01['d2'], bloque_01['e2'], bloque_01['f2'], bloque_01['d3'], bloque_01['e3'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
bloque_01['f3'] = num_rand

print('  a b c d e f g h i')
print(' ╔═════╦═════╦═════╗')
print('1║'+str(bloque_01['a1'])+'│'+str(bloque_01['b1'])+'│'+str(bloque_01['c1'])+'║'+str(bloque_01['d1'])+'│'+str(bloque_01['e1'])+'│'+str(bloque_01['f1'])+'║'+str(bloque_01['g1'])+'│'+str(bloque_01['h1'])+'│'+str(bloque_01['i1'])+'║')

print('2║'+str(bloque_01['a2'])+'│'+str(bloque_01['b2'])+'│'+str(bloque_01['c2'])+'║'+str(bloque_01['d2'])+'│'+str(bloque_01['e2'])+'│'+str(bloque_01['f2'])+'║')

print('3║'+str(bloque_01['a3'])+'│'+str(bloque_01['b3'])+'│'+str(bloque_01['c3'])+'║'+str(bloque_01['d3'])+'│'+str(bloque_01['e3'])+'│'+str(bloque_01['f3'])+'║')
print(' ╚═════╬═════╬')
