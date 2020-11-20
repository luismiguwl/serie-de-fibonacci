def calcular_fibonacci(numero_inserido):
    numero_anterior = 0
    numero_posterior = 1
    resultado_da_soma = 0

    print(numero_anterior, end = " ")
    print(numero_posterior, end = " ")

    while (True):
        resultado_da_soma = numero_anterior + numero_posterior
        numero_anterior = numero_posterior
        numero_posterior = resultado_da_soma

        print(resultado_da_soma, end = ' ')

        if (resultado_da_soma == numero_inserido):
            return True

        if (resultado_da_soma > numero_inserido):
            return False

def solicitar_numero():
    print('Informe um número inteiro: ', end = '')
    return int(input())

def main():
    # Usabilidade
    while (True):
        numero_inserido = solicitar_numero()        

        pertence_serie_fibonacci = calcular_fibonacci(numero_inserido)

        print('\n')

        if (pertence_serie_fibonacci):
            print(numero_inserido, 'pertence à Série de Fibonacci')
        else:
            print(numero_inserido, 'não pertence à Série de Fibonacci')

        print('\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*\n')

    
main()
calcular_fibonacci()