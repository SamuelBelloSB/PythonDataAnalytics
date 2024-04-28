# For
texto = input()
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end=" ")
else: 
    print()

#   While
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando")
        break
    elif opcao == 2:
        print("Exibindo extrato...")
        break
else:
    print("Saindo...")

#   Range
for numero in range(0,100, 3):
    if numero % 2 == 0:
        print(numero, end=" ")