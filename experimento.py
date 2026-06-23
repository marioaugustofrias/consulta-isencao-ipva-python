from datetime import datetime

while True:
    print('\033[;31;40m-=-\033[m' * 19)
    print('\033[7;31;40mConsulta de IPVA - Verifique se seu carro ainda paga IPVA\033[m')
    print('\033[;31;40m-=-\033[m' * 19)

    try:
        ano = int(input('+ Qual o ano do seu carro? '))

        ano_atual = datetime.now().year
        idade_carro = ano_atual - ano
        anos_restantes = 20 - idade_carro

        if idade_carro < 0:
            print("🚨 Ano inválido! Digite um ano menor ou igual ao ano atual.")

        elif idade_carro < 20:
            print(
                f'Seu carro tem {idade_carro} anos. '
                f'Ainda faltam {anos_restantes} anos para possível isenção de IPVA.'
            )

        else:
            print(
                f'Seu carro tem {idade_carro} anos. '
                f'Ele já pode estar isento de IPVA (verifique as regras do seu estado).'
            )

    except ValueError:
        print("🚨 Digite apenas números.")

    novac = input('\nGostaria de fazer uma nova consulta? (s/n): ').strip().lower()

    if novac not in ['s', 'sim']:
        print("\nObrigado por usar o sistema! 🚗💨")
        break
