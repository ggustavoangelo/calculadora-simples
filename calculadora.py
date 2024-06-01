def mostrar_opcoes():
    print('Nossas opções são: ')
    print('1 - Soma')
    print('2 - Substração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Potenciação')
    print('6 - Sair')

def obter_opcao():
    while True:
        opcao = int(input('Escolha uma das nossas opções: '))
        if opcao >= 1 and opcao <= 6:
            return opcao
        else:
            print('Digite uma opção válida. ')

def obter_numero():
    while True:
        num1 = float(input('Digite aqui o primeiro número: '))
        num2 = float(input('Digite aqui o segundo número: '))
        return num1, num2


def main():
    while True:
        mostrar_opcoes()
        opcao = obter_opcao()
        if opcao == 6:
            print('Saindo... ')
            break

        num1, num2 = obter_numero()

        if opcao == 1:
            resultado = num1 + num2
            print(f'O resultado da operação é {resultado}')
        elif opcao == 2:
            resultado = num1 - num2
            print(f'O resultado da operação é {resultado}')
        elif opcao == 3:
            resultado = num1 * num2
            print(f'O resultado da operação é {resultado}')
        elif opcao == 4:
            resultado = num1 / num2
            print(f'O resultado da operação é {resultado}')
        elif opcao == 5:
            resultado = num1 ** num2
            print(f'O resultado da operação é: ')

if __name__ == "__main__":
    main()



print('oiiiiiiii')