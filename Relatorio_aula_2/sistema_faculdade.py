alunos = []
contador_matriculas = {}

def gerar_matricula(curso: str) -> str:
    if curso not in contador_matriculas:
        contador_matriculas[curso] = 1
    else:
        contador_matriculas[curso] += 1
    return f"{curso}{contador_matriculas[curso]}"

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    curso = input("Digite o curso (GES, GEC, GEA, etc.): ").upper()

    matricula = gerar_matricula(curso)

    alunos.append({
        "nome": nome,
        "email": email,
        "curso": curso,
        "matricula": matricula
    })

    print(f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\nLista de Alunos:")
        for aluno in alunos:
            print(f"- Nome: {aluno['nome']}, E-mail: {aluno['email']}, "
                  f"Curso: {aluno['curso']}, Matrícula: {aluno['matricula']}")

def atualizar_aluno():
    matricula = input("Digite a matrícula do aluno a ser atualizado: ")
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print(f"\nAtualizando aluno {aluno['nome']} ({aluno['matricula']})")
            novo_nome = input("Novo nome (pressione Enter para manter o atual): ")
            novo_email = input("Novo e-mail (pressione Enter para manter o atual): ")
            novo_curso = input("Novo curso (GES, GEC, GEA, etc.) ou Enter para manter: ").upper()

            if novo_nome:
                aluno["nome"] = novo_nome
            if novo_email:
                aluno["email"] = novo_email

            if novo_curso and aluno["curso"] != novo_curso:
                aluno["curso"] = novo_curso
                aluno["matricula"] = gerar_matricula(novo_curso)
                print(f"Curso alterado! Nova matrícula: {aluno['matricula']}")
            else:
                print("Dados atualizados com sucesso!")
            return
    print("Aluno não encontrado.")

def remover_aluno():
    matricula = input("Digite a matrícula do aluno a ser removido: ")
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            print(f"Aluno {aluno['nome']} removido com sucesso!")
            return
    print("Aluno não encontrado.")

def main():
    while True:
        print("\n=== Menu de Opções ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Remover Aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
