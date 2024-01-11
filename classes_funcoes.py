#CLASSES

class Aluno:
    def __init__(self,nome,nota_1,nota_2):
        self.nome = nome
        self.status = ["Aprovado", "Em recuperação", "Reprovado"]
        self.nota_1 = nota_1
        self.nota_2 = nota_2


    def calcular_media(self):
        return ((self.nota_1 + self.nota_2) / 2)
    
    def definir_status(self,media):
        if media >= 5:
            self.status = self.status[0]
        
        else:
            self.status = self.status[1]

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



