import mysql.connector

def conectar_db():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='NutriTreino'
    )
    return conn

def calcular_gasto_energetico(met, peso, duracao):
    gasto = met * peso * duracao
    return round(gasto, 2)


def obter_mets_atividade(nome_atividade):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT mets FROM Exercicios WHERE nome = %s
    ''', (nome_atividade,))

    resultado = cursor.fetchone()  # Retorna o MET da atividade
    conn.close()

    if resultado:
        return resultado[0]  # Retorna o valor de MET
    else:
        print(f"Atividade {nome_atividade} não encontrada.")
        return None


def main():
    peso = float(input("Digite seu peso em kg: "))
    duracao = float(input("Digite a duração da atividade em horas: "))

    atividades = [
        "Alongamento_leve",
        "Aeróbico_degrau_com_degrau_de_6_a_8_polegadas",
        "Aeróbico_degrau_com_degrau_de_10_a_12_polegadas",
        "Discoteca_folclórica_praça_dança_em_linha_dança_irlandesa_polca_contra_e_dança_country",
        "Dança_Anishinaabe_Jingle_ou_outra_dança_tradicional_indígena_americana",
        "Esfregar",
        "Várias_tarefas_domésticas_ao_mesmo_tempo_esforço_leve",
        "Várias_tarefas_domésticas_ao_mesmo_tempo_esforço_moderado",
        "Várias_tarefas_domésticas_ao_mesmo_tempo_esforço_vigoroso",
        "Limpar",
        "Animais_de_abate",
        "Alimentação_de_animais",
        "Regar_plantas",
        "Construindo_uma_fogueira_dentro",
        "Carregando_crianças_pequenas",
        "Cuidados_com_idosos_adultos_com_deficiência_apenas_períodos_ativos",
        "Reclinável_com_bebê",
        "Sentado_brincando_com_animais_leve_apenas_períodos_ativos",
        "Em_pé_brincando_com_animais_leve_apenas_períodos_ativos",
        "Caminhar/correr_brincar_com_animais_luz_apenas_períodos_ativos",
        "Caminhar/correr_brincar_com_animais_moderado_apenas_períodos_ativos",
        "Caminhar/correr_brincar_com_animais_vigoroso_apenas_períodos_ativos",
        "Cão_em_pé_–_tomar_banho",
        "Pintura",
        "Deitado_estranhamente_sem_fazer_nada_deitado_na_cama_acordado_ouvindo_música_(sem_falar_ou_ler)",
        "Sentado_em_silêncio_sentado_fumando_ouvindo_música_(sem_falar_ou_ler)_assistir_a_um_filme_em_um_cinema",
        "Cortar_grama_cortador_de_grama",
        "Gramado_de_ajuntamento",
        "Colher_frutas_de_árvores_colher_frutas/legumes_esforço_moderado",
        "Em_pé_–_diversos",
        "Sentado_-_artes_e_ofícios_esforço_leve",
        "Sentado_-_artes_e_ofícios_esforço_moderado",
        "Em_pé_-_artes_e_ofícios_esforço_leve",
        "Em_pé_-_artes_e_ofícios_esforço_moderado",
        "De_pé_-_artes_e_ofícios_esforço_vigoroso",
        "Atividades_de_retiro/reunião_familiar_envolvendo_sentar_relaxar_conversar_comer",
        "Passeios_/_viagens_/_férias_envolvendo_caminhadas_e_passeios",
        "Acampar_envolvendo_ficar_em_pé_caminhar_sentar_esforço_leve_a_moderado",
        "Sentado_em_um_evento_esportivo_espectador",
        "Padaria_esforço_leve",
        "Custódia_polimento_do_chão_com_um_amortecedor_elétrico",
        "Custódia_limpeza_de_pia_e_vaso_sanitário_esforço_leve",
        "Custódia_poeira_esforço_leve",
        "Custódia_piso_de_arena_de_penas_esforço_moderado",
        "Custódia_limpeza_geral_esforço_moderado",
        "Custódia_limpeza_esforço_moderado",
        "Custódia_tirar_o_lixo_esforço_moderado",
        "Custódia_aspiração_esforço_leve",
        "Custódia_aspiração_esforço_moderado",
        "Agricultura_perseguição_de_gado_ou_outro_gado_a_cavalo_esforço_moderado",
        "Agricultura_perseguição_de_gado_ou_outro_gado_condução_esforço_leve",
        "Agricultura_cuidar_de_animais_(tosa_escovação_tosquia_de_ovelhas_assistência_no_parto_cuidados_médicos_marcação)",
        "Mergulho_livre_ou_mergulho_autônomo",
        "Levantar_itens_continuamente_10–20_libras_com_caminhada_ou_descanso_limitado",
        "Alfaiataria_tecelagem",
        "Caminhando_juntando_coisas_no_trabalho_pronto_para_sair",
        "Andando_empurrando_uma_cadeira_de_rodas",
        "Correr_em_um_mini-trampolim",
        "Tomar_medicação_sentado_ou_em_pé",
        "Penteado",
        "Ter_cabelo_ou_unhas_feitas_por_outra_pessoa_sentar",
        "Golfe_caminhar_e_carregar_tacos",
        "Tacos_de_golfe_caminhada_e_puxar",
        "Patins_(patinação_em_linha)",
        "Tênis_jogo_de_duplas",
        "Voleibol_jogo_competitivo_em_um_ginásio",
        "Atletismo_(arremesso_disco_lançamento_de_martelo)",
        "Atletismo_(salto_em_altura_salto_em_distância_salto_triplo_dardo_salto_com_vara)_",
        "Atletismo_(corrida_com_obstáculos_barreiras)",
        "Andar_de_carro_ou_caminhão",
        "Andar_de_ônibus",
        "Carregar/descarregar_um_carro",
        "Observação_de_aves",
        "Empurrar_uma_cadeira_de_rodas_ambiente_não_ocupacional",
        "Caminhando_menos_de_2_0_mph_terreno_plano_passeando_muito_lento",
        "Caminhada_2_0_mph_nível_ritmo_lento_superfície_firme",
        "Andar_de_casa_para_carro_ou_ônibus_de_carro_ou_ônibus_para_ir_a_lugares_de_carro_ou_ônibus_de_e_para_o_local_de_trabalho",
        "Caminhar_até_a_casa_do_vizinho_ou_da_família_por_motivos_sociais",
        "Passeando_com_o_cachorro",
        "Caminhando_5.0_mph",
        "Caminhando_de_e_para_um_banheiro_externo",
        "Canoagem_colheita_de_arroz_selvagem_derrubando_arroz_dos_talos",
        "Hidroginástica_calistenia_aquática",
        "Corrida_aquatica"
        ]

    print("\nAtividades disponíveis:")
    for i, atividade in enumerate(atividades, 1):
        print(f"{i}. {atividade}")

    opcao = int(input("\nEscolha o número da atividade: "))
    atividade_escolhida = atividades[opcao - 1]
 
    met_atividade = obter_mets_atividade(atividade_escolhida)

    if met_atividade:
        gasto = calcular_gasto_energetico(met_atividade, peso, duracao)
        print(f"\nGasto energético para {atividade_escolhida} de {duracao} horas: {gasto} kcal")

if __name__ == "__main__":
    main()

