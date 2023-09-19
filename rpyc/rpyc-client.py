import rpyc

# Conecta ao servidor rodando no localhost na porta 8000
conn = rpyc.connect("localhost", 8000)

# Chama a função calculate_imc
imc_result = conn.root.calculate_imc(70, 1.75)
print(f"Resultado do IMC: {imc_result}")

# Chama a função solve_quadratic
quadratic_result = conn.root.solve_quadratic(1, -3, 2)
print(f"Resultado da equação quadrática: {quadratic_result}")

# Chama a função is_palindrome
palindrome_result = conn.root.is_palindrome("radar")
print(f"Resultado do teste de palíndromo: {palindrome_result}")

# Fecha a conexão
conn.close()
