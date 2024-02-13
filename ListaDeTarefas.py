AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

def mostrar_menu():
   print("\n====== LISTA DE TAREFAS ======")
   print("1. Adicionar Nova Tarefa")
   print("2. Ver Lista")
   print("3. Excuir Tarefa")
   print("4. Sair")

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

def excluir_tarefa(tarefas):
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
               print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
       except ValueError:
           print("Entrada inválida. Digite um número correspondente à tarefa que deseja excluir.")

def main():
   tarefas = []
   while True:
       mostrar_menu()
       escolha = input("Escolha uma opção: ")
       if escolha == '1':
           adicionar_tarefa(tarefas)
       elif escolha == '2':
           ver_tarefas(tarefas)
       elif escolha == '3':
           excluir_tarefa(tarefas)
       elif escolha == '4':
           print("Saindo...")
           break
       else:
           print("Opção inválida. Por favor, escolha uma das opções indicadas.")

if __name__ == "__main__":
   main()
