import os
import time

def sair():
    a = "."
    b = "."
    for i in range(5):
        os.system('cls')
        print('Encerrando' + a)
        time.sleep(1)
        a = b + a 
        if len(a) == 4:
            a = '.'
    os.system('cls')    
    print('O sistema foi fechado com sucesso 🖐')
    exit()

def preencher_dicionario(dic: dict):
    chave1 = input('Digite a primeira chave: ').strip().title()
    chave2 = input('Digite a segunda chave: ').strip().title()
    dicionario[chave1] = chave2
    

def exibir_dicionario(dic: dict):
    if not dic: 
        print('\nA lista está vazia')
        return
    
    print(f'{"Chave1":<15} Chave2')
    print('-' * 25)
    for chave1, chave2 in dic.items():
        print(f'{chave1:<15} {chave2:<15}')

def editar_dicionario(dic: dict):
    chave = input("Digite a chave que deseja editar: ").strip().title()
    if chave in dicionario:
        novo_valor = input(f"Digite o novo valor para '{chave}': ").strip().title()
        dicionario[chave] = novo_valor
    else:
        print("Chave não encontrada.")

def criar_nova_key(dic: dict):
    nova_key = input('criar nova key: ').strip().title()
    nova_valor = input('criar um novo valor: ').strip().title()
    dicionario[nova_key] = nova_valor

def excluir_key(dic: dict):
    key = input('Excluir uma unica chave: ').strip().title()
    if key in dicionario:
        del dicionario[key]
        print(f'Key{key} foi excluida com exito!')

def excluir_todas_keys(dic: dict):
    if not dic:  
        print('\nA lista está vazia')
        return

    dic.clear()
    print('\nTodos os alunos foram removidos. ✔')


# ------------------------------------------------------------------------------#
#                                      Menu                                     #

dicionario = {}

while True:
    os.system('cls')

    opcao = input(
        '''
        0 - Sair
        1 - Preencher Dicionário 
        2 - Exibir dicionário | Dado a dado
        3 - Editar dicionário | Exibir o estado anterior
        4 - Criar Nova key
        5 - Excluir key
        6 - Excluir todas as keys

        
    Escolha: ''')

    match opcao:
        case '0':
            sair()
        case '1':
            preencher_dicionario(dicionario)
        case '2':
            exibir_dicionario(dicionario)
        case '3':
            editar_dicionario(dicionario)
        case '4':
            criar_nova_key(dicionario)
        case '5':
            excluir_key(dicionario)
        case '6':
            excluir_todas_keys(dicionario)
        case _:
            print('\nSelecione uma das opções acima.')

    input('\nAperte ENTER para continuar ')