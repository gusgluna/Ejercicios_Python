'''
Dado un conjunto de números, devuelve el inverso aditivo de cada uno. 
Cada positivo se vuelve negativo y los negativos se vuelven positivos.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []

'''

def invert(lst):
    n = 0
    ilst=[]
    for i in lst:
        ilst.append(lst[n]*-1)
        n += 1
    print(ilst)

invert([-12,4,-3,-5])