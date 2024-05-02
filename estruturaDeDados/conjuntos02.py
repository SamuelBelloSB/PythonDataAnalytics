#   Métodos conjunto
conjunto_a = {1,2,3,4}
conjunto_b = {2,4,5,6}
conjunto_c = {1,2,3,4,5,6,7,8,9}
conjunto_d = {10,11,12,15}
print(f"Conjuntos\nConjunto a: {conjunto_a}\nConjunto b: {conjunto_b}\nConjunto c: {conjunto_c}\nConjunto d: {conjunto_d}")

#   União
print(f"\nUnião: {conjunto_a.union(conjunto_b)}")

#   Intersecção
print(f"\nIntersecção: {conjunto_a.intersection(conjunto_b)}")

#   Diferença
print(f"\nDiferença conjunto_a - conjunto_b: {conjunto_a.difference(conjunto_b)}")
print(f"Diferença conjunto_b - conjunto_a: {conjunto_b.difference(conjunto_a)}")

#   Diferença simétrica
print(f"\nDiferença simétrica: {conjunto_a.symmetric_difference(conjunto_b)}")

#  É disjunto
print(f"\nSer disjunto\nConjunto d é disjunto do Conjunto c? {conjunto_d.isdisjoint(conjunto_c)}")

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


#   .clear limpa o conjunto 
print(f"Conjunto d: {conjunto_d.clear()} | todos objetos foram removidos")

#   .add pra adicionar elemento ao conjunto | só adiciona um elemento por vez
print(f"Antes de .add: Conjunto d -> {conjunto_d}")
conjunto_d.add(13)
conjunto_d.add(14)
print(f"Depois de .add(13,14): Conjunto d -> {conjunto_d}")
      
#   len retorna o tamanho do conjunto
print(f"O conjunto c tem {len(conjunto_c)} objetos.")

#   in verifca se um objeto esta dentro do conjunto

print(f"O objeto 15 está dentro do Conjunto c? {15 in conjunto_c}")

#   .discard exclui o objeto informado do conjunto
conjunto_d.discard(15)
print(f"Conjunto d .discard(15): {conjunto_d}")
print(conjunto_d)
print(conjunto_d.pop())

#   .remove exclui o objeto informado do conjunto, porém retorna um erro caso o elemento não exista
conjunto_d.remove(15)
print(f"Conjunto d .discard(15): {conjunto_d} | 15 foi removido")
conjunto_d.remove(14)
print(f"Conjunto d .discard(14): {conjunto_d} | 14 foi removido")

