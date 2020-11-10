'''
Crear un programa que teng una funcion que reciba una lista de numeros, 
y nos regrese la suma de sus cuadrados
Por ejemplo: [0,1,2]= 0^2 + 1^2 + 2^2 = 5
'''
def square_sum(numbers):
    r=0
    for num in numbers:
        r= r + num**2
    print(r)

square_sum([0,1,2])

square_sum([0,4,5,7])
