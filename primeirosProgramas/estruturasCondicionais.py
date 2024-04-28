conta_normal = True
conta_universitaria = True

saldo = 2000
saque = 2500
cheque_especial = 600

if conta_normal:
    if saldo >= saque:
        saldo -= saque
        print('Conta normal | Saque realizado com sucesso! Saldo atual:',+saldo)
    elif (saldo+cheque_especial) >= saque:
        saldo +=cheque_especial
        saldo -= saque
        print('Conta normal | Saque realizado com cheque especial! Saldo atual:',+saldo)
    else:
        print('Não foi possível realizar saque, saldo insuficiente!')
elif conta_universitaria:
    if saldo >= saque:
        saldo -= saque
        print('Conta universitária | Saque realizado com sucesso! Saldo atual:',+saldo)
    elif (saldo+cheque_especial) >= saque:
        saldo +=cheque_especial
        saldo -= saque
        print('Conta universitária | Saque realizado com cheque especial! Saldo atual:',+saldo)
else:
    print('Conta invalida')