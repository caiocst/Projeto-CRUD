import sys
import classes_funcoes as cf

alunos = {}

def main():
    while True:
        cf.exibir_menu_geral()
        opcao_geral = input("Informe a sua opção: ")

        if opcao_geral in ["1", "2", "3", "4"]:
            if opcao_geral  == "1":
                aluno = cf.Aluno()
                alunos[f"{len(alunos) +1 }"] = aluno #CRIANDO CHAVE ID : aluno  ##### OPÇÃO OK


            elif opcao_geral == "2":
                nome_att = input("Informe o nome do aluno que terá os dados atualizados: ")
                att = cf.encontrar_aluno(alunos,nome_att)

                if att != None:
                    while True:
                        cf.exibir_menu_opcao2()
                        opcao_2 = input("Informe a opção desejada: ")

                        if opcao_2 in ["1", "2", "3", "4"]:
                            if opcao_2 == "1":
                                alunos[att].nome = input("Insira o novo nome: ")
                                print("Nome atualizado.")

                            elif opcao_2 == "2":
                                alunos[att].nota_1 = float(input("Insira a nota atualizada da prova 1: "))   
                                print("Nota da prova 1 atualizada.")

                            elif opcao_2 == "3":
                                alunos[att].nota_2 = float(input("Insira a nota atualizada da prova 2: "))
                                print("Nota da prova 2 atualizada.")
                            
                            elif opcao_2 == "4":
                                break
                        
                        else:
                            print("Opção inválida. Tente novamente!")

            elif opcao_geral == "3":
                    nome_att = input("Informe o nome do aluno que terá os dados excluídos do sistema: ")
                    att = cf.encontrar_aluno(alunos,nome_att)
                    alunos.pop(att)
                    print(f"O cadastro do aluno {nome_att} foi exclúido do sistema.")
            
            elif opcao_geral == "4":
                print("Você encerrou o sistema!")
                sys.exit()
        
        else:
            print("Opção inválida. Tente novamente!")

            
            
main()