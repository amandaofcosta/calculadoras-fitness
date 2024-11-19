def calcular_tmb(sexo, peso, altura, idade):
    
    if sexo.lower() == 'masculino':
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
    elif sexo.lower() == 'feminino':
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
    else:
        return "Sexo inválido. Use 'masculino' ou 'feminino'."

    return tmb

sexo = input("Digite seu sexo (masculino ou feminino): ").strip().lower()
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em cm: "))
idade = int(input("Digite sua idade em anos: "))

tmb = calcular_tmb(sexo, peso, altura, idade)

if isinstance(tmb, (int, float)):
    print(f"Sua Taxa de Metabolismo Basal (TMB) é: {tmb:.2f} calorias por dia")
else:
    print(tmb)
