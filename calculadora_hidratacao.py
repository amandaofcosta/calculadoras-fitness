def calcular_agua_diaria(peso, idade, atividade_fisica, clima):

    # Definindo a quantidade base de água por kg:
    if idade <= 17:
        agua_por_kg = 40  # ml por kg
    elif idade <= 55:
        agua_por_kg = 35  # ml por kg
    else:
        agua_por_kg = 25  # ml por kg

    # Calculando a ingestão base:
    ingestao_base = peso * agua_por_kg  # em ml

    # Ajuste por nível de atividade física:
    if atividade_fisica == 1:
        ingestao_base += 500  # ml
    elif atividade_fisica == 2:
        ingestao_base += 750  # ml
    elif atividade_fisica == 3:
        ingestao_base += 1000  # ml

    # Ajuste por clima:
    if clima == 2:
        ingestao_base += 500  # ml

    # Convertendo para litros:
    ingestao_base_litros = ingestao_base / 1000  # em litros

    return round(ingestao_base_litros, 2)

peso = float(input("Digite seu peso em kg: "))
idade = int(input("Digite sua idade em anos: "))
atividade_fisica = int(input("Nível de atividade física (0 - Sedentário, 1 - Leve, 2 - Moderado, 3 - Intenso): "))
clima = int(input("Clima (0 - Frio, 1 - Ameno, 2 - Quente): "))

agua_recomendada = calcular_agua_diaria(peso, idade, atividade_fisica, clima)
print(f"Ingestão diária recomendada de água: {agua_recomendada} litros.")
