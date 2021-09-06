def GeraEmail():
    nome = input('Digite seu nome ')
    sobrenome = input('Digite seu sobrenome ')
    RU = input('Informe seu RU')

    email = nome[0] + sobrenome + RU[0] + RU[1] + '@algoritmos.com.br'
    print(f'{nome}, seu email é {email}')


GeraEmail()
