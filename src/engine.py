"""Motor de análise da Mission Control AI."""
import os
from ollama import Client
from dotenv import load_dotenv
from pathlib import Path

# Força a leitura do arquivo .env explicitando o caminho atual
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Identificação da trilha
TRILHA = "agrosat"

# Pega o token garantindo que, se não achar, use uma string vazia em vez de None
api_key = os.environ.get('OLLAMA_API_KEY') or ''

# Configuração oficial do cliente Ollama Cloud
client = Client(
    host="https://ollama.com",
    headers={'Authorization': f'Bearer {api_key}'}
)

def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    """Envia prompt ao gpt-oss:120b via Ollama Cloud."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    
    try:
        return client.chat(
            model="gpt-oss:120b", 
            messages=messages,
            options={"num_predict": max_tokens, "temperature": temperature},
            stream=False
        )['message']['content'].strip()
    except Exception as e:
        return f"⚠️ Erro ao consultar IA: {e}"

def load_system_prompt():
    """Lê o system prompt do arquivo prompts/system_prompt.md"""
    path = Path("prompts/system_prompt.md")
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "Você é um assistente de controle de missão espacial."

class MissionEngine:
    """Motor de análise oficial preenchido com a lógica do projeto."""
    
    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()
        
        # Importação interna para evitar dependências cíclicas
        from src.telemetria import ler_telemetria
        self._ler_telemetria = ler_telemetria
        
        # PONTE DE MEMÓRIA: Sorteia a primeira telemetria ao ligar o sistema
        self.dados_atuais = self._ler_telemetria()
        
    def is_ready(self):
        # Retorna True para ativar a CLI
        return True

    def status_snapshot(self):
        """Retorna texto resumindo o estado atual da telemetria e salva na memória."""
        try:
            # Sincroniza a memória global da classe com uma nova leitura gerada
            self.dados_atuais = self._ler_telemetria()
            
            return (
                f"🛰️  [bold #06B6D4]STATUS ATUAL DO SATÉLITE ({self.trilha.upper()}):[/]\n"
                f"• NDVI Médio: {self.dados_atuais['ndvi_medio']}\n"
                f"• Temperatura do Sensor: {self.dados_atuais['temperatura_sensor_optico']}°C\n"
                f"• Bateria Restante: {self.dados_atuais['bateria_satelite']}%"
            )
        except Exception as e:
            return f"⚠️ Erro ao carregar snapshot de telemetria: {e}"

    def analyze(self, pergunta_usuario):
        """Analisa a pergunta integrando a MESMA telemetria do status + alertas + IA."""
        from src.alertas import processar_alertas
        
        # A MÁGICA DA PONTE: A IA agora consome o dado travado na memória da classe
        dados_telemetria = self.dados_atuais
        alertas = processar_alertas(dados_telemetria)
        
        # Se o operador rodar o diagnóstico automático (/diagnostico sem pergunta)
        if pergunta_usuario == "":
            pergunta_usuario = "Gere um diagnóstico técnico completo com base nas leituras atuais de telemetria."
        
        # Monta o contexto que será enviado para enriquecer a IA
        contexto_da_missao = f"""
=== DADOS ATUAIS DE TELEMETRIA DO SATÉLITE ===
- NDVI Médio: {dados_telemetria['ndvi_medio']}
- Temperatura do Sensor Óptico: {dados_telemetria['temperatura_sensor_optico']}°C
- Capacidade de Bateria: {dados_telemetria['bateria_satelite']}%

=== ALERTAS ATIVOS NO SISTEMA ===
"""
        if not alertas:
            contexto_da_missao += "-> Nenhum alerta lógico detectado pelo Python.\n"
        else:
            for al in alertas:
                contexto_da_missao += f"- [{al['status']}] {al['parametro']}: {al['valor']} -> {al['mensagem']}\n"
                
        prompt_final = f"{contexto_da_missao}\n=== PERGUNTA DO OPERADOR ===\n{pergunta_usuario}"
        
        return llm(prompt_final, system=self.system_prompt)