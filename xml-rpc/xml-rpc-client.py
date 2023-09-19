import xmlrpc.client

# Conectar ao servidor RPC
with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    
    # 1. Calcular o IMC
    weight = 70  # peso em kg
    height = 1.75  # altura em metros
    imc_result = proxy.calculate_imc(weight, height)
    print(f"Resultado do IMC: {imc_result}")
    
    # 2. Resolver uma equação do segundo grau
    a = 1
    b = -3
    c = 2
    quadratic_result = proxy.solve_quadratic(a, b, c)
    print(f"Resultado da equação do segundo grau: {quadratic_result}")
    
    # 3. Verificar se uma palavra é um palíndromo
    word = input("Digite a palavra: ")
    palindrome_result = proxy.is_palindrome(word)
    print(f"Resultado do teste de palíndromo: {palindrome_result}")

