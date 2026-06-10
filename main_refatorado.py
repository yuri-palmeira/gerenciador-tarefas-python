import json


def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
        
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    

def salvar_tarefas():
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("\n=== TAREFAS ===")

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice}. {tarefa}")


def adicionar_tarefa():
    nova_tarefa = input("Digite a nova tarefa: ")

    tarefas.append(nova_tarefa)

    salvar_tarefas()

    print("Tarefa adicionada com sucesso!")


def remover_tarefa():
    if not tarefas:
        print("Nenhuma tarefa para remover.")
        return
    
    listar_tarefas()

    try:
        indice_remover = int(
            input("Digite o número da tarefa a remover: ")
            ) - 1

        if 0 <= indice_remover < len(tarefas):
            tarefa_removida = tarefas.pop(indice_remover)

            salvar_tarefas()

            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Número inválido.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")


def exibir_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("4 - Sair")

tarefas = carregar_tarefas()


nome = input("Olá, qual é o seu nome? ")


print(f"Bem-vindo {nome}, à sua lista de tarefas!")


while True:

    exibir_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_tarefas()
    elif opcao == "2":
        adicionar_tarefa()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        print("Saindo do gerenciador de tarefas...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
