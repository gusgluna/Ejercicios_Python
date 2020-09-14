import random

sud = {
  'a1' : 0, 'b1' : 0, 'c1' : 0, 'd1' : 0, 'e1' : 0, 'f1' : 0, 'g1' : 0, 'h1' : 0, 'i1' : 0,
  'a2' : 0, 'b2' : 0, 'c2' : 0, 'd2' : 0, 'e2' : 0, 'f2' : 0, 'g2' : 0, 'h2' : 0, 'i2' : 0,
  'a3' : 0, 'b3' : 0, 'c3' : 0, 'd3' : 0, 'e3' : 0, 'f3' : 0, 'g3' : 0, 'h3' : 0, 'i3' : 0,
}

#Definiendo el valor de a1
num_rand = random.randint(1,9)
sud['a1'] = num_rand

#Definiendo el valor de b1
num_rand = random.randint(1,9)
while num_rand == sud['a1']:
  num_rand = random.randint(1,9)
sud['b1'] = num_rand

#Definiendo el valor de c1
tup_comp = (sud['a1'], sud['b1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['c1'] = num_rand

#Definiendo el valor de a2
tup_comp = (sud['a1'], sud['b1'],
sud['c1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['a2'] = num_rand

#Definiendo el valor de b2
tup_comp = (sud['a1'], sud['b1'],
sud['c1'], sud['a2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['b2'] = num_rand

#Definiendo el valor de c2
tup_comp = (sud['a1'], sud['b1'],
sud['c1'], sud['a2'], sud['b2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['c2'] = num_rand

#Definiendo el valor de a3
tup_comp = (sud['a1'], sud['b1'],
sud['c1'], sud['a2'], sud['b2'],sud['c2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['a3'] = num_rand

#Definiendo el valor de b3
tup_comp = (sud['a1'], sud['b1'],
sud['c1'], sud['a2'], sud['b2'],sud['c2'],sud['a3'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['b3'] = num_rand

#Definiendo el valor de c3
tup_comp = (sud['a1'], sud['b1'],
sud['c1'], sud['a2'], sud['b2'],sud['c2'],sud['a3'],sud['b3'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['c3'] = num_rand

#Definiendo el valor de d1
tup_comp = (sud['a1'], sud['b1'],
sud['c1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['d1'] = num_rand

#Definiendo el valor de e1
tup_comp = (sud['a1'], sud['b1'],
sud['c1'], sud['d1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['e1'] = num_rand

#Definiendo el valor de f1
tup_comp = (sud['a1'], sud['b1'],
sud['c1'], sud['d1'], sud['e1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['f1'] = num_rand

#Definiendo el valor de d2
tup_comp = (sud['a2'], sud['b2'],
sud['c2'], sud['d1'], sud['e1'], sud['f1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['d2'] = num_rand

#Definiendo el valor de e2
tup_comp = (sud['a2'], sud['b2'],
sud['c2'], sud['d1'], sud['e1'], sud['f1'], sud['d2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['e2'] = num_rand

#Definiendo el valor de f2
tup_comp = (sud['a2'], sud['b2'],
sud['c2'], sud['d1'], sud['e1'], sud['f1'], sud['d2'], sud['e2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['f2'] = num_rand

#Definiendo el valor de d3
tup_comp = (sud['a3'], sud['b3'],
sud['c3'], sud['d1'], sud['e1'], sud['f1'], sud['d2'], sud['e2'], sud['f2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['d3'] = num_rand

#Definiendo el valor de e3
tup_comp = (sud['a3'], sud['b3'],
sud['c3'], sud['d1'], sud['e1'], sud['f1'], sud['d2'], sud['e2'], sud['f2'], sud['d3'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['e3'] = num_rand

#Definiendo el valor de f3
tup_comp = (sud['a3'], sud['b3'],
sud['c3'], sud['d1'], sud['e1'], sud['f1'], sud['d2'], sud['e2'], sud['f2'], sud['d3'], sud['e3'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['f3'] = num_rand

#Definiendo el valor de g1
tup_comp = (sud['a1'], sud['b1'],
sud['c1'], sud['d1'], sud['e1'], sud['f1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['g1'] = num_rand

#Definiendo el valor de h1
tup_comp = (sud['a1'], sud['b1'],
sud['c1'], sud['d1'], sud['e1'], sud['f1'], sud['g1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['h1'] = num_rand

#Definiendo el valor de i1
tup_comp = (sud['a1'], sud['b1'],
sud['c1'], sud['d1'], sud['e1'], sud['f1'], sud['g1'], sud['h1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['i1'] = num_rand

#Definiendo el valor de g2
tup_comp = (sud['a2'], sud['b2'],
sud['c2'], sud['d2'], sud['e2'], sud['f2'], sud['g1'], sud['h1'], sud['i1'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['g2'] = num_rand

#Definiendo el valor de h2
tup_comp = (sud['a2'], sud['b2'],
sud['c2'], sud['d2'], sud['e2'], sud['f2'], sud['g1'], sud['h1'], sud['i1'], sud['g2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['h2'] = num_rand

#Definiendo el valor de i2
tup_comp = (sud['a2'], sud['b2'],
sud['c2'], sud['d2'], sud['e2'], sud['f2'], sud['g1'], sud['h1'], sud['i1'], sud['g2'], sud['h2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['i2'] = num_rand

#Definiendo el valor de g3
tup_comp = (sud['a3'], sud['b3'],
sud['c3'], sud['d3'], sud['e3'], sud['f3'], sud['g1'], sud['h1'], sud['i1'], sud['g2'], sud['h2'], sud['i2'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['g3'] = num_rand

#Definiendo el valor de h3
tup_comp = (sud['a3'], sud['b3'],
sud['c3'], sud['d3'], sud['e3'], sud['f3'], sud['g1'], sud['h1'], sud['i1'], sud['g2'], sud['h2'], sud['i2'], sud['g3'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['h3'] = num_rand

#Definiendo el valor de i3
tup_comp = (sud['a3'], sud['b3'],
sud['c3'], sud['d3'], sud['e3'], sud['f3'], sud['g1'], sud['h1'], sud['i1'], sud['g2'], sud['h2'], sud['i2'], sud['g3'], sud['h3'])
num_rand = random.randint(1,9)
while num_rand in tup_comp:
  num_rand = random.randint(1,9)
sud['i3'] = num_rand






print('  a b c d e f g h i')

print(' ╔═════╦═════╦═════╗')
print('1║'+str(sud['a1'])+'│'+str(sud['b1'])+'│'+str(sud['c1'])+'║'+str(sud['d1'])+'│'+str(sud['e1'])+'│'+str(sud['f1'])+'║'+str(sud['g1'])+'│'+str(sud['h1'])+'│'+str(sud['i1'])+'║')

print('2║'+str(sud['a2'])+'│'+str(sud['b2'])+'│'+str(sud['c2'])+'║'+str(sud['d2'])+'│'+str(sud['e2'])+'│'+str(sud['f2'])+'║'+str(sud['g2'])+'│'+str(sud['h2'])+'│'+str(sud['i2'])+'║')

print('3║'+str(sud['a3'])+'│'+str(sud['b3'])+'│'+str(sud['c3'])+'║'+str(sud['d3'])+'│'+str(sud['e3'])+'│'+str(sud['f3'])+'║'+str(sud['g3'])+'│'+str(sud['h3'])+'│'+str(sud['i3'])+'║')

print(' ╠═════╬═════╬═════╣')

print('4║')


