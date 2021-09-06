def RetornaConceito(nota):
    conceito  = ''
    if nota >= 0 and nota <= 2.9:
        conceito = 'E'
    elif nota >= 3 and nota <= 4.9:
        conceito = 'D'
    elif nota >= 5 and nota <= 6.9:
        conceito = 'C'
    elif nota >= 7 and nota <= 8.9:
        conceito = 'B'
    elif nota >= 9 and nota <= 10:
        conceito = 'A'

    return conceito


def ReceberDados():
    insere_dados = True

    while insere_dados:
        nota_errada = True
        inserir_dados = input('Inserir dados? 0 - Sim / 1 - Não ')
        if inserir_dados == '0':
            nome = input('Digite seu nome ')
            while nota_errada:
                nota = int(input('Digite sua nota final '))
                if nota >= 0 and nota <= 10:
                    break
                else:
                    nota = int(input('Nota deve estar entre 0 e 10, pressione qualquer tecla para digitar novamente'))
                    nota_errada = True
            conceito = RetornaConceito(nota)
            print('O aluno(a) ', nome, ' tirou a nota ', nota, ' e se enquadra no conceito', conceito)
        else:
            print('Encerrando')
            break


ReceberDados()