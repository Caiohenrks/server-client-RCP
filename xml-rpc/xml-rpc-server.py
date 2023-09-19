from xmlrpc.server import SimpleXMLRPCServer
import math

# Função para calcular o IMC e fornecer a classificação
def calculate_imc(weight, height):
    imc = weight / (height ** 2)
    classification = "Desconhecido"
    
    if imc < 18.5:
        classification = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        classification = "Peso normal"
    elif 25 <= imc < 29.9:
        classification = "Sobrepeso"
    elif 30 <= imc < 34.9:
        classification = "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        classification = "Obesidade grau 2"
    elif imc >= 40:
        classification = "Obesidade grau 3"
        
    return f"IMC: {imc:.2f}, Classificação: {classification}"

# Função para resolver uma equação do segundo grau
def solve_quadratic(a, b, c):
    if a == 0:
        return "O coeficiente 'a' não pode ser zero em uma equação do segundo grau."
    
    delta = b ** 2 - 4 * a * c
    
    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0:
        x = -b / (2 * a)
        return f"A equação possui uma raiz real: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"A equação possui duas raízes reais: x1 = {x1}, x2 = {x2}"

# Função para verificar se uma palavra é um palíndromo
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    reversed_word = word[::-1]
    
    if word == reversed_word:
        return f"A palavra '{word}' é um palíndromo."
    else:
        return f"A palavra '{word}' não é um palíndromo."

# Configuração do servidor
server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor RPC rodando em http://localhost:8000/")

# Registrar as funções
server.register_function(calculate_imc, "calculate_imc")
server.register_function(solve_quadratic, "solve_quadratic")
server.register_function(is_palindrome, "is_palindrome")

# Rodar o servidor
server.serve_forever()
