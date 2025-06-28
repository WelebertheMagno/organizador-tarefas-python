import json
import os

# === Funções para salvar e carregar ===

def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return []

def salvar_tarefas():
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

# === Funções principais do menu ===

def exibir_menu():
    print('\n===== MENU DE TAREFAS =====')
    print('1. Adicionar nova tarefa')
    print('2. Listar todas as tarefas')
    print('3. Marcar tarefa como concluída')
    print('4. Mostrar apenas pendentes')
    print('5. Sair')

def adicionar_tarefa():
    nome = input('Digite o nome da tarefa: ')
    prioridade = input('Digite a prioridade (Alta, Média ou Baixa): ')
    tarefa = {
        'nome': nome.capitalize(),
        'prioridade': prioridade.capitalize(),
        'status': 'Pendente'
    }
    tarefas.append(tarefa)
    salvar_tarefas()
    print('✅ Tarefa adicionada com sucesso!')

def listar_tarefas():
    if not tarefas:
        print('🔔 Nenhuma tarefa cadastrada ainda.')
        return

    print('\n📋 Lista de Tarefas:')
    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1}. {tarefa['nome']} | Prioridade: {tarefa['prioridade']} | Status: {tarefa['status']}")

def marcar_como_concluida():
    if not tarefas:
        print('🔔 Nenhuma tarefa cadastrada ainda.')
        return

    print('\n📌 Tarefas Pendentes:')
    for i, tarefa in enumerate(tarefas):
        if tarefa['status'] == 'Pendente':
            print(f'{i + 1}. {tarefa["nome"]} | Prioridade: {tarefa["prioridade"]}')

    try:
        escolha = int(input('Digite o número da tarefa que deseja marcar como concluída: '))
        if 1 <= escolha <= len(tarefas):
            if tarefas[escolha - 1]['status'] == 'Pendente':
                tarefas[escolha - 1]['status'] = 'Concluída'
                salvar_tarefas()
                print('✅ Tarefa marcada como concluída!')
            else:
                print('⚠️ Esta tarefa já está concluída.')
        else:
            print('❌ Número inválido.')
    except ValueError:
        print('⚠️ Digite um número válido.')

def mostrar_pendentes():
    pendentes = [t for t in tarefas if t['status'] == 'Pendente']

    if not pendentes:
        print('✅ Nenhuma tarefa pendente!')
        return

    print('\n🕒 Tarefas Pendentes:')
    for i, tarefa in enumerate(pendentes):
        print(f"{i + 1}. {tarefa['nome']} | Prioridade: {tarefa['prioridade']}")

# === Início do programa ===

tarefas = carregar_tarefas()

while True:
    exibir_menu()
    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        adicionar_tarefa()
    elif escolha == '2':
        listar_tarefas()
    elif escolha == '3':
        marcar_como_concluida()
    elif escolha == '4':
        mostrar_pendentes()
    elif escolha == '5':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Tente novamente.')
