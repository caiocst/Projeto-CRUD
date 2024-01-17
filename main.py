import sys
import classes_funcoes as cf

storage = cf.Storage()

def main():
    while True:
        cf.exibir_menu_geral()
        opcao_geral = input("Informe a sua opção: ")
      
        if opcao_geral  == "1":
            nome = input("Informe o nome do aluno a ser cadastrado: ")
            nota_1 = None
            while nota_1 == None:
                nota_1 = cf.validar_nota(input("Informe a nota do aluno na prova 1: "))

            nota_2 = None
            while nota_2 == None:
                nota_2 = cf.validar_nota(input("Informe a nota do aluno na prova 2: "))
                
            aluno = cf.Aluno(nome, nota_1, nota_2)
            media = aluno.calcular_media()
            aluno.definir_status(media)
            storage.store(len(storage.data) + 1, aluno)    #CRIANDO CHAVE ID : aluno
            print(f"O aluno {aluno.nome} foi cadastrado para o ID {len(storage.data)}.")
    
            cf.exibir_menu_pos()
            while True:
                opcao_pos = input("Informe a opção escolhida: ")

                if opcao_pos == "1":
                    break
                elif opcao_pos == "2":
                    print("Você encerrou o sistema!")
                    sys.exit()
                else:
                    print("Informe uma opção válida para prosseguir: ")
    
        elif opcao_geral == "2":
            while True:
                cf.exibir_menu_opcao2()
                opcao_att = input("Informe a opção desejada: ")

                if opcao_att == "1":
                    nome_aluno = input("Informe o nome do aluno para saber o ID associado a ele: ")
                    cf.encontrar_aluno(storage,nome_aluno)

                elif opcao_att == "2":
                    while True:
                        try:
                            id_aluno = int(input("Informe o ID do aluno que terá os dados atualizados: "))
                            att = storage.get(id_aluno)
                        except ValueError:
                            print("ID inválido. Insira um número inteiro para o ID.")
                            continue

                        if att == None:
                            break

                        while True:
                            cf.exibir_menu_att()
                            opcao_2 = input("Informe a opção desejada: ")

                            if opcao_2 == "1":
                                att.nome = input("Insira o novo nome: ")
                                print("Nome atualizado.")

                            elif opcao_2 == "2":

                                nota_1 = None
                                while nota_1 == None:
                                    nota_1 = cf.validar_nota(input("Informe a nota do aluno na prova 1: "))
                                    att.nota_1 = nota_1
                                    if nota_1 != None:
                                        print("A nota da prova 1 foi atualizada.")

                            elif opcao_2 == "3":
                                nota_2 = None
                                while nota_2 == None:
                                    nota_2 = cf.validar_nota(input("Informe a nota do aluno na prova 2: "))
                                    att.nota_2 = nota_2
                                    if nota_2 != None:
                                        print("A nota da prova 2 foi atualizada.")

                            elif opcao_2 == "4":
                                break

                            else:
                                print("Opção inválida. Tente novamente!")
                            
                        break       
                   
                elif opcao_att == "3":
                    break

        elif opcao_geral == "3":
            while True:
                try:
                    id_aluno = int(input("Informe o ID do aluno que será excluído do sistema: "))
                except ValueError:
                    print("ID inválido. Insira um número inteiro para o ID.")
                    continue

                storage.remove(id_aluno)
                break
        
        elif opcao_geral == "4":
            nome_aluno = input("Informe o nome do aluno que deseja buscar: ")
            cf.encontrar_aluno(storage,nome_aluno)
  
        elif opcao_geral == "5":
            print("Você encerrou o sistema!")
            sys.exit()

        else:
            print("Opção inválida. Tente novamente!")

            
            
main()