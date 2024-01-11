#CLASSES

class Aluno:
    def __init__(self):
        self.nome = input("Insira o nome do aluno: ")
        self.status = ["Aprovado", "Em recuperação", "Reprovado"]
        self.nota_1 = float(input("Insira a nota da prova 1: "))
        self.nota_2 = float(input("Insira a nota da prova 2: "))

    #def __str__(self):
        #return f"Aluno: {self.nome}" // PESQUISAR DEPOIS

#FUNÇÕES

def exibir_menu_geral():
    print("""
Bem vindo ao sistema de notas da universidade!
Selecione uma das opções abaixo para prosseguir:\n
1 - Inserir um usuário no sistema.
2 - Alterar dados de um usuário no sistema.
3 - Excluir um usuário do sistema.
4 - Sair
""")

def exibir_menu_opcao2():
    print("""
Informe o dado que deseja atualizar: 
1 - Nome
2 - Nota da prova 1 
3 - Nota da prova 2 
4 - Voltar ao menu inicial 
""")

def encontrar_aluno(alunos, aluno_procurado):
    for chave, valor in alunos.items():
        if valor.nome == aluno_procurado:
            print(f"O aluno: {valor.nome} é associado ao ID: {chave}")
            return chave

    print("\nO aluno não consta no banco de dados. \n")
    return None



