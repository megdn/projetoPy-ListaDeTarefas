def mostrar_menu():
    print("\n====== LISTA DE TAREFAS ======")
    print("1. Adicionar Nova Tarefa")
    print("2. Ver Lista")
    print("3. Excluir Tarefa")
    print("4. Recuperar Tarefa")
    print("5. Sair")

def adicionar_tarefa(tarefas):
    tarefa = input("\nDigite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def ver_tarefas(tarefas):
    if not tarefas:
        print("\nLista de tarefas vazia.")
        print("Para visualizar sua lista, você deve adicionar ao menos uma tarefa à sua lista.")
    else:
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def excluir_tarefa(tarefas, tarefas_excluidas):
    if not tarefas:
        print("\nLista de tarefas vazia. Não há tarefas para excluir.")
    else:
        print("\nTarefas disponíveis para exclusão:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

        try:
            indice = int(input("Digite o número da tarefa que deseja excluir: "))
            if indice < 1 or indice > len(tarefas):
                print("Número de tarefa inválido.")
            else:
                tarefa_removida = tarefas.pop(indice - 1)
                tarefas_excluidas.append(tarefa_removida)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        except ValueError:
            print("Entrada inválida. Digite um número correspondente à tarefa que deseja excluir.")


def recuperar_tarefa(tarefas, tarefas_excluidas):
    if not tarefas_excluidas:
        print("\nVocê ainda não teve nenhuma tarefa excluída.")
    else:
        print("\nTarefas excluídas:")
        for i, tarefa in enumerate(tarefas_excluidas, 1):
            print(f"{i}. {tarefa}")

        try:
            indice = int(input("\nDigite o número da tarefa que deseja recuperar: "))
            if indice < 1 or indice > len(tarefas_excluidas):
                print("Número de tarefa inválido.")
            else:
                tarefa_recuperada = tarefas_excluidas.pop(indice - 1)
                tarefas.append(tarefa_recuperada)
                print(f"Tarefa '{tarefa_recuperada}' recuperada com sucesso!")
        except ValueError:
            print("\nEntrada inválida. Digite um número correspondente à tarefa que deseja recuperar.")

def salvar_tarefas(tarefas, tarefa_salvas):
    with open(tarefa_salvas, "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(tarefa + "\n")

def carregar_tarefas(tarefa_salvas):
    tarefas = []
    try:
        with open(tarefa_salvas, "r") as arquivo:
            for linha in arquivo:
                tarefas.append(linha.strip())
    except FileNotFoundError:
        pass  # Se o arquivo não existir, retornar uma lista vazia de tarefas
    return tarefas

def main():
    tarefa_salvas_tarefas = "tarefas.txt"
    tarefa_salvas_tarefas_excluidas = "tarefas_excluidas.txt"
    tarefas = carregar_tarefas(tarefa_salvas_tarefas)
    tarefas_excluidas = carregar_tarefas(tarefa_salvas_tarefas_excluidas)
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_tarefa(tarefas)
        elif escolha == '2':
            ver_tarefas(tarefas)
        elif escolha == '3':
            excluir_tarefa(tarefas, tarefas_excluidas)
        elif escolha == '4':
            recuperar_tarefa(tarefas, tarefas_excluidas)
        elif escolha == '5':
            print("Saindo...")
            salvar_tarefas(tarefas, tarefa_salvas_tarefas)
            salvar_tarefas(tarefas_excluidas, tarefa_salvas_tarefas_excluidas)
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções indicadas.")

if __name__== "__main__":
    main()
