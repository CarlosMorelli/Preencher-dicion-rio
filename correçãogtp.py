import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def sair():
    a = "."
    for i in range(5):
        limpar_tela()
        print(f'Encerrando{a}')
        time.sleep(1)
        a += "."
        if len(a) > 3:
            a = "."
    limpar_tela()
    print('O sistema foi fechado com sucesso 🖐')
    exit()


def preencher_dicionario(dic: dict):
    chave1 = input('Digite a primeira chave: ').strip().title()
    valor = input('Digite o valor para a chave: ').strip().title()
    dic[chave1] = valor
    print(f"Chave '{chave1}' adicionada com sucesso.")


def exibir_dicionario(dic: dict):
    if not dic: 
        print('\nA lista está vazia.')
        return
    print(f'{"Chave":<15} Valor')
    print('-' * 30)
    for chave, valor in dic.items():
        print(f'{chave:<15} {valor:<15}')
    print('-' * 30)


def editar_dicionario(dic: dict):
    chave = input("Digite a chave que deseja editar: ").strip().title()
    if chave in dic:
        novo_valor = input(f"Digite o novo valor para '{chave}': ").strip().title()
        dic[chave] = novo_valor
        print(f"Chave '{chave}' foi atualizada com sucesso.")
    else:
        print("Chave não encontrada.")


def criar_nova_key(dic: dict):
    chave = input('Digite o nome da nova chave: ').strip().title()
    valor = input('Digite o valor para a nova chave: ').strip().title()
    dic[chave] = valor
    print(f"Chave '{chave}' criada com sucesso.")


def excluir_key(dic: dict):
    chave = input('Digite a chave que deseja excluir: ').strip().title()
    if chave in dic:
        del dic[chave]
        print(f"Chave '{chave}' foi excluída com sucesso.")
    else:
        print("Chave não encontrada.")


def excluir_todas_keys(dic: dict):
    if not dic:
        print('\nA lista já está vazia.')
        return
    dic.clear()
    print('Todas as chaves foram removidas com sucesso.')

#------------------------------------------------------------------------------#
def menu():
    dicionario = {}
    while True:
        limpar_tela()
        opcao = input(
            '''
          0 - Sair
          1 - Preencher Dicionário 
          2 - Exibir dicionário
          3 - Editar uma chave
          4 - Criar nova chave
          5 - Excluir uma chave
          6 - Excluir todas as chaves

        Escolha: ''')

        if opcao == '0':
            sair()
        elif opcao == '1':
            preencher_dicionario(dicionario)
        elif opcao == '2':
            exibir_dicionario(dicionario)
        elif opcao == '3':
            editar_dicionario(dicionario)
        elif opcao == '4':
            criar_nova_key(dicionario)
        elif opcao == '5':
            excluir_key(dicionario)
        elif opcao == '6':
            excluir_todas_keys(dicionario)
        else:
            print('Opção inválida, tente novamente.')

        input('\nAperte ENTER para continuar ')

if __name__ == "__main__":
    menu()
