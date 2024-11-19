def calcular_tmb(sexo, peso, altura, idade):
    
    if sexo.lower() == 'masculino':
        tmb = 66.5 + (13.75 * peso) + (5.003 * altura) - (6.755 * idade)
    elif sexo.lower() == 'feminino':
        tmb = 655.1 + (9.563 * peso) + (1.850 * altura) - (4.676 * idade)
    else:
        return "Sexo inválido. Use 'masculino' ou 'feminino'."
    return tmb

def calcular_gebt(tmb, nivel_atividade):
    
    fatores_atividade = {
        1: 1.2,   # Sedentário
        2: 1.375, # Leve (exercício leve 1-3 dias/semana)
        3: 1.55,  # Moderado (exercício moderado 3-5 dias/semana)
        4: 1.725, # Intenso (exercício intenso 6-7 dias/semana)
        5: 1.9    # Muito intenso (exercício muito intenso ou trabalho físico intenso)
    }
    
    fator_atividade = fatores_atividade.get(nivel_atividade, 1.2)
    gebt = tmb * fator_atividade
    return gebt

def calcular_macros(peso, objetivo, gebt):
    
    # Definindo calorias diárias com base no objetivo
    if objetivo == 1:  # Perda de peso
        calorias_diarias = gebt * 0.8  # 20% de déficit calórico
    elif objetivo == 2:  # Manutenção
        calorias_diarias = gebt
    elif objetivo == 3:  # Ganho de massa
        calorias_diarias = gebt * 1.2  # 20% de superávit calórico
    else:
        print("Objetivo inválido!")
        return None
    
    # Calculando os macronutrientes com base nas calorias diárias
    proteina = peso * 2  # 2g de proteína por kg de peso
    gordura = peso * 1  # 1g de gordura por kg de peso
    calorias_restantes = calorias_diarias - (proteina * 4 + gordura * 9)  # Calorias restantes para carboidratos
    carboidrato = calorias_restantes / 4  # 4 calorias por grama de carboidrato

    return {
        "proteina (g)": round(proteina, 2),
        "carboidrato (g)": round(carboidrato, 2),
        "gordura (g)": round(gordura, 2),
        "calorias diarias": round(calorias_diarias, 2)
    }

sexo = input("Digite seu sexo (masculino ou feminino): ").strip().lower()
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em cm: "))
idade = int(input("Digite sua idade em anos: "))
nivel_atividade = int(input("Digite seu nível de atividade (1 - Sedentário, 2 - Leve, 3 - Moderado, 4 - Intenso, 5 - Muito intenso): "))
objetivo = int(input("Digite seu objetivo (1 - Perda de peso, 2 - Manutenção, 3 - Ganho de massa): "))

# Calcular TMB
tmb = calcular_tmb(sexo, peso, altura, idade)
if isinstance(tmb, str):  # Se houver erro no cálculo da TMB
    print(tmb)
else:
    # Calcular GEBT
    gebt = calcular_gebt(tmb, nivel_atividade)

    # Calcular os macronutrientes
    macros = calcular_macros(peso, objetivo, gebt)
    if macros:
        print(f"Quantidade diária de macronutrientes recomendada:")
        for key, value in macros.items():
            print(f"{key}: {value}")