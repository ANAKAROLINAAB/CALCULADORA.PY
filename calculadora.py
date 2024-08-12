# Função para somar dois números
def somar(x, y):
    return x + y

# Função para subtrair dois números
def subtrair(x, y):
    return x - y

# Função para multiplicar dois números
def multiplicar(x, y):
    return x * y

# Função para dividir dois números
def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    return x / y

# Função principal da calculadora
def calculadora():
    print("Selecione a operação desejada:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    
    operacao = input("Digite o número da operação (1/2/3/4): ")

    if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida")
        return

    try:
 
