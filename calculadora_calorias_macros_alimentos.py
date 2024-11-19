import mysql.connector

def calcular_macros_alimento(nome_alimento, quantidade_em_gramas):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='NutriTreino'
    )
    
    cursor = conn.cursor()

    cursor.execute('''
    SELECT calorias, proteina, carboidrato, gordura FROM Alimentos WHERE nome = %s
    ''', (nome_alimento,))

    alimento = cursor.fetchone()

    if alimento:
        calorias_100g, proteinas_100g, carboidratos_100g, gorduras_100g = alimento
        
        # Calcular as quantidades para a quantidade fornecida
        calorias_totais = (calorias_100g * quantidade_em_gramas) / 100
        proteinas_totais = (proteinas_100g * quantidade_em_gramas) / 100
        carboidratos_totais = (carboidratos_100g * quantidade_em_gramas) / 100
        gorduras_totais = (gorduras_100g * quantidade_em_gramas) / 100
        
        # Exibir os resultados
        print(f"Para {quantidade_em_gramas}g de {nome_alimento}:")
        print(f"Calorias: {calorias_totais:.2f} kcal")
        print(f"Proteínas: {proteinas_totais:.2f}g")
        print(f"Carboidratos: {carboidratos_totais:.2f}g")
        print(f"Gorduras: {gorduras_totais:.2f}g")
    else:
        print("Alimento não encontrado!")

    conn.close()

nome_alimento = input("Digite o nome do alimento: ")
quantidade_em_gramas = float(input("Digite a quantidade (em gramas): "))

calcular_macros_alimento(nome_alimento, quantidade_em_gramas)
