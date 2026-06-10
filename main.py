nome = input("Olá, qual é o seu nome? ")
print(f"Bem-vindo {nome}, à sua lista de tarefas!")
tarefas = []

while True:

    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opção = input("Escolha uma opção: ")

    if opção == "1":

        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for indice, tarefa in enumerate(tarefas):
                print(f"{indice + 1}. {tarefa}")
    
    elif opção == "2":
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opção == "3":
        if not tarefas:
            print("Nenhuma tarefa para remover.")
        else:
            for indice, tarefa in enumerate(tarefas):
                print(f"{indice + 1}. {tarefa}")
            indice_remover = int(input("Digite o número da tarefa a remover: ")) - 1
            if 0 <= indice_remover < len(tarefas):
                tarefas.pop(indice_remover)
                print("Tarefa removida com sucesso!")
            else:
                print("Número inválido.")
    elif opção == "4":
        print("Saindo do gerenciador de tarefas...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
