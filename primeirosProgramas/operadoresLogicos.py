saldo = 1000
saque = 200
limite = 100

#   and -> Operador "e" V e V = True | F e V = False
print(saldo >= saque and saque <= limite)

#   ou  -> Operador "ou" V ou V = True | F ou V = True | F ou F = False
print(saldo >= saque or saque <= limite)

#   not -> operador de negação
print(not saldo<limite)
