#   Métodos conjunto
conjunto_a = {1,2,3,4}
conjunto_b = {2,4,5,6}
conjunto_c = {1,2,3,4,5,6,7,8,9}
print(f"Conjuntos\nConjunto a: {conjunto_a}\nConjunto b: {conjunto_b}\nConjunto c: {conjunto_c}")

#   União
print(f"\nUnião: {conjunto_a.union(conjunto_b)}")

#   Intersecção
print(f"\nIntersecção: {conjunto_a.intersection(conjunto_b)}")

#   Diferença
print(f"\nDiferença conjunto_a - conjunto_b: {conjunto_a.difference(conjunto_b)}")
print(f"Diferença conjunto_b - conjunto_a: {conjunto_b.difference(conjunto_a)}")

#   Diferença simétrica
print(f"\nDiferença simétrica: {conjunto_a.symmetric_difference(conjunto_b)}")

#   É subconjunto
print(f"\nSer subconjuntos\nConjunto a é subconjunto do Conjunto c? {conjunto_a.issubset(conjunto_c)}")
print(f"Conjunto c é subconjunto do Conjunto a? {conjunto_c.issubset(conjunto_a)}")
print(f"Conjunto b é subconjunto do Conjunto c? {conjunto_b.issubset(conjunto_c)}")
print(f"Conjunto c é subconjunto do Conjunto b? {conjunto_c.issubset(conjunto_b)}")
print(f"Conjunto a e b são subconjunto do Conjunto c? {(conjunto_b and conjunto_a).issubset(conjunto_c)}")
print(f"Conjunto c é subconjunto do Conjunto a e b? {conjunto_c.issubset(conjunto_b and conjunto_a)}")

#   É superconjunto
print(f"\nSer superconjunto\nConjunto a é superconjunto do Conjunto c? {conjunto_a.issuperset(conjunto_c)}")
print(f"Conjunto c é superconjunto do Conjunto a? {conjunto_c.issuperset(conjunto_a)}")
print(f"Conjunto b é superconjunto do Conjunto c? {conjunto_b.issuperset(conjunto_c)}")
print(f"Conjunto c é superconjunto do Conjunto a? {conjunto_c.issuperset(conjunto_a)}")
print(f"Conjunto a e b são superconjunto do Conjunto c? {(conjunto_a and conjunto_b).issuperset(conjunto_c)}")
print(f"Conjunto c é superconjunto do Conjunto a e b? {conjunto_c.issuperset(conjunto_a and conjunto_b)}")

