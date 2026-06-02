import random

def ler_telemetria():
    """
    Simula a leitura de sensores do satélite AgroSat.
    Retorna um dicionário com os dados simulados.
    """
    # NDVI (Índice de Vegetação) varia de 0.0 a 1.0. Valores baixos indicam seca/anomalia.
    # Vamos simular uma oscilação ao redor de um valor que pode ficar crítico.
    ndvi = round(random.uniform(0.3, 0.85), 2)
    
    # Temperatura do sensor óptico em graus Celsius (Normal: 15°C a 45°C)
    temperatura_sensor = round(random.uniform(18.0, 55.0), 1)
    
    # Nível da bateria do satélite em porcentagem (0% a 100%)
    bateria = round(random.uniform(12.0, 98.0), 1)
    
    return {
        "ndvi_medio": ndvi,
        "temperatura_sensor_optico": temperatura_sensor,
        "bateria_satelite": bateria
    }