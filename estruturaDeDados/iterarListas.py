carros = ["gol", "celta", "palio", "ferrari"]

""" for carro in carros:
    print(carro) """
    
#   Função enumerate
for indice, item in enumerate(carros):
    print(f"{indice}: {item}")
    
#   Compreensão de listas
numeros = [1, 30, 21, 2, 9, 65, 34, 71, 50]
""" pares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
"""
pares = [i for i in numeros if i % 2 == 0]
print(pares) 