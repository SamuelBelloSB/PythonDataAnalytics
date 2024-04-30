nome = "Samuel"
idade = 26
profissao = "Programador"
linguagem = "python"

#   opção 1
dados = {"nome": "Samuel",
         "idade": 26,
         "profissao": "Programador",
         "linguagem": "python"}

print("Olá meu é {nome} e eu tenho {idade}. Sou {profissao} de {linguagem}".format(**dados))

#   opção 2 - recomendado.
print(f"Olá meu é {nome} e eu tenho {idade}. Sou {profissao} de {linguagem}")
