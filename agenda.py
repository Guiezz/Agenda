
def adicionar_contato(agenda,nome, telefone, email):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    agenda.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")
    return

def listar_contatos(agenda):
    print("\nLista de contatos: ")
    for indice, contato in enumerate(agenda, start=1):
        favorito = "✓" if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. [{favorito}] Nome: {nome} - Telefone: {telefone} - Email: {email}")
    return

def editar_contato(agenda, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
        agenda[indice_contato_ajustado] ["nome"] = novo_nome
        agenda[indice_contato_ajustado] ["telefone"] = novo_telefone
        agenda[indice_contato_ajustado] ["email"] = novo_email
        print(f"Contato {indice_contato} atualizado para {novo_nome}!")
    else:
        print("Contato não encontrado!")
    return

def marcar_favorito(agenda, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
        if agenda[indice_contato_ajustado] ["favorito"]:
            agenda[indice_contato_ajustado] ["favorito"] = False
            print(f"Contato {indice_contato} desmarcado como favorito!")
        else:
            agenda[indice_contato_ajustado] ["favorito"] = True
            print(f"Contato {indice_contato} marcado como favorito!")
    else:
        print("Contato não encontrado!")
    return

def listar_favoritos(agenda):
    for indice, contato in enumerate(agenda, start=1):
        if contato["favorito"]:
            favorito = "✓" if contato["favorito"] else " "
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"{indice}. [{favorito}] Nome: {nome} - Telefone: {telefone} - Email: {email}")
    return

def apagar_contato(agenda, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
        del agenda[indice_contato_ajustado]             # Remove a tarefa da lista // Del Remove primeiro valor encontrado 
        print(f"Contato {indice_contato} apagado com sucesso!") 
    else:
        print("Contato não encontrado!")
    return

agenda = []

while True:
    print("\n Menu da Agenda:")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Editar contato")
    print("4 - Marcar/Desmarcar contato como favorito")
    print("5 - Listar contatos favoritos")
    print("6 - Apagar contato")
    print("7 - Sair")

    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha < 1 or escolha > 7:
            raise ValueError
    except ValueError:
        print("Escolha inválida. Por favor, escolha um número de 1 a 7.")

    if escolha == 1:
        nome_contato = input("Digite o nome do contato: ")
        try:
            telefone_contato = int(input("Digite o número do contato: "))     
        except ValueError as e:
            print(f"Número inválido: {e}")
            continue
        email_contato = input("Digite o email do contato: ")
        adicionar_contato(agenda, nome_contato, telefone_contato, email_contato)

    elif escolha == 2:
        listar_contatos(agenda)

    elif escolha == 3:
        listar_contatos(agenda)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome_contato = input("Digite o novo nome do contato: ")
        try:
            novo_telefone_contato = int(input("Digite o novo telefone do contato: "))
        except ValueError as e:
            print(f"Número inválido: {e}")
            continue
        novo_email_contato = input("Digite o novo email do contato: ")
        editar_contato(agenda, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato)
    elif escolha == 4:
        listar_contatos(agenda)
        indice_contato = input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")
        marcar_favorito(agenda, indice_contato)

    elif escolha == 5:
        listar_favoritos(agenda)

    elif escolha == 6:
        listar_contatos(agenda)
        indice_contato = input("Digite o número do contato que deseja apagar: ")
        apagar_contato(agenda, indice_contato)
    elif escolha == 7:
        break