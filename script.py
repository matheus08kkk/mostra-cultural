
def calcular():
    print("===== CALCULADORA EM PYTHON =====")

    numero1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    numero2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = numero1 + numero2

    elif operacao == "-":
        resultado = numero1 - numero2

    elif operacao == "*":
        resultado = numero1 * numero2

    elif operacao == "/":
        if numero2 == 0:
            print("Erro: divisão por zero não é permitida.")
            return
        resultado = numero1 / numero2

    else:
        print("Operação inválida!")
        return

    print("Resultado:", resultado)


calcular()

