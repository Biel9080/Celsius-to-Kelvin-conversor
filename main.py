# --- CONVERSOR DE TEMPERATURA PARA O PEDRO ---

# Criamos a variável para controlar o ciclo do programa
# Começamos com "s" para ele iniciar a primeira vez
continuar = "s"

# O 'while' faz o programa repetir enquanto a resposta for "s"
while continuar.lower() == "s":
    
    # --- Passo 1: Entrada de Dados ---
    # O 'float' garante que o Python aceite números (inteiros ou com ponto)
    # O 'input' faz a pergunta inicial que você pediu
    celsius_pedro = float(input("\nQual a temperatura de Pedro em Celsius? "))

    # --- Passo 2: O Cálculo Científico ---
    # Na física, para chegar em Kelvin, somamos o zero absoluto (273.15)
    kelvin_pedro = celsius_pedro + 273.15

    # --- Passo 3: Exibição do Resultado ---
    # O 'print' mostra o valor calculado com carinho na tela
    print("---------------------------------------------")
    print("A temperatura de Pedro em Kelvin é:", kelvin_pedro, "K")
    print("---------------------------------------------")

    # --- Passo 4: Pergunta de Continuidade ---
    # Aqui o programa espera você digitar 's' para repetir ou 'n' para parar
    continuar = input("Deseja continuar? (s/n): ")

# --- Passo 5: Finalização ---
# Quando você digita 'n', o programa sai do 'while' e lê esta última linha
print("\nTenha uma boa saúde Pedro, meu bem.")
