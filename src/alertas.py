def processar_alertas(telemetria):
    """
    Analisa os dados de telemetria usando regras lógicas em Python
    e gera uma lista de alertas estruturados caso os limites sejam violados.
    """
    alertas_gerados = []
    
    # Regra 1: Validação do NDVI (Seca grave detectada na região monitorada)
    if telemetria["ndvi_medio"] < 0.4:
        alertas_gerados.append({
            "parametro": "NDVI Médio",
            "valor": telemetria["ndvi_medio"],
            "status": "CRÍTICO",
            "mensagem": "Índice de vegetação abaixo do limite operacional. Indício de seca severa ou quebra de safra detectada em solo."
        })
    elif telemetria["ndvi_medio"] < 0.55:
        alertas_gerados.append({
            "parametro": "NDVI Médio",
            "valor": telemetria["ndvi_medio"],
            "status": "ATENÇÃO",
            "mensagem": "Declínio sutil na atividade clorofiliana da região."
        })

    # Regra 2: Superaquecimento do Sensor Óptico de Imagem
    if telemetria["temperatura_sensor_optico"] > 50.0:
        alertas_gerados.append({
            "parametro": "Temperatura do Sensor",
            "valor": f"{telemetria['temperatura_sensor_optico']}°C",
            "status": "CRÍTICO",
            "mensagem": "Sensor óptico superaquecido. Risco de degradação das imagens de satélite fornecidas às cooperativas."
        })
    elif telemetria["temperatura_sensor_optico"] > 42.0:
        alertas_gerados.append({
            "parametro": "Temperatura do Sensor",
            "valor": f"{telemetria['temperatura_sensor_optico']}°C",
            "status": "ATENÇÃO",
            "mensagem": "Temperatura interna operando acima da média ideal."
        })

    # Regra 3: Energia Crítica na Bateria do Satélite
    if telemetria["bateria_satelite"] < 20.0:
        alertas_gerados.append({
            "parametro": "Bateria do Satélite",
            "valor": f"{telemetria['bateria_satelite']}%",
            "status": "CRÍTICO",
            "mensagem": "Energia insuficiente. Sistema de Processamento de Borda do Satélite ativou MODO DE ECONOMIA automatizado."
        })

    return alertas_gerados