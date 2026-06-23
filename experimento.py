while True:
    print('\033[;31;40m-=-\033[m' * 19)
    print('\033[7;31;40mConsulta de IPVA - erifique se seu carro ainda paga IPVA\033[m')
    print('\033[;31;40m-=-\033[m' * 19)

    ano = int(input('+Qual o ano do seu carro? '))
    carro = 2025 - ano
    anoc = 20 - carro

    if carro < 0:
        print("🚨 Ano inválido! Digite um ano menor ou igual a 2025.")
    elif carro <= 20:
        print(f'Seu carro tem {carro} anos. Ainda faltam {anoc} anos para que ele fique isento de IPVA.')
    else:
        print(f'Seu carro tem {carro} anos. Ele já não paga mais IPVA, apenas o licenciamento!')

    # Pergunta se quer repetir
    novac = input('\nGostaria de fazer uma nova consulta? (s/n): ').strip().lower()
    if novac not in ['s', 'sim']:
        print("\nObrigado por usar o sistema! 🚗💨")
    break
