def adicionar_contato(contatos, nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)

    print(f"Contato {nome} adicionado com sucesso!")

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "★" if contato["favorito"] else " "
        print(f"{indice}. [{favorito}] {contato["nome"]} - {contato["telefone"]} - {contato["email"]}")

def editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_ajustado = int(indice_contato) - 1
    contatos[indice_ajustado]["nome"] = novo_nome
    contatos[indice_ajustado]["telefone"] = novo_telefone
    contatos[indice_ajustado]["email"] = novo_email
    print("Contato atualizado!")

def favoritar_contato(contatos, indice_contato):
    indice_ajustado = int(indice_contato) - 1
    contatos[indice_ajustado]["favorito"] = True
    print(f"{indice_contato} favoritado com sucesso!")

def deletar_contato(contatos, indice_contato):
    indice_ajustado = int(indice_contato) - 1
    del contatos[indice_ajustado]
    print("Contato deletado!")

contatos = []

while True:
    print("\nGerenciador de Contatos")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Favoritar contato")
    print("5. Deletar contato")
    print("6. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        adicionar_contato(contatos, nome, telefone, email)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha  == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja editar: ")
        novo_nome = input("Digite o novo nome: ")
        novo_telefone = input("Digite o novo telefone:")
        novo_email = input("Digite o novo email: ")
        editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email) 

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número que deseja favoritar: ")
        favoritar_contato(contatos, indice_contato) 

    elif escolha == "5":
        ver_contatos(contatos)
        indice_contato = input("Digite o número que deseja deletar: ")
        deletar_contato(contatos, indice_contato)

    elif escolha == "6":
        break

print("Sistema encerrado. Até logo!")




