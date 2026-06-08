# Mission Control AI — Trilha AgroSat

## Integrantes do Grupo
* **Luis Fernando de Azevedo** - RM: 574167
* **Aline Medri Marcolino** -    RM: 569349

## Link do YouTube
https://www.youtube.com/watch?v=RtcALBy7GOE
---

## Descrição do Projeto
O **Mission Control AI** é um sistema de monitoramento e análise operacional para satélites artificiais baseado em Inteligência Artificial Generativa. O ecossistema simula o recebimento de pacotes de telemetria de um satélite em órbita (focado na vertical agrícola **AgroSat**) e utiliza técnicas avançadas de *Prompt Engineering* para analisar o estado do satélite e prever impactos operacionais diretamente na Terra.

A interface simula o terminal de estilo CLI inspirado no *Claude Code*, permitindo que operadores humanos interajam com o motor de IA (`gpt-oss:120b`) por meio de comandos e perguntas em linguagem natural.

---

## Arquitetura do Sistema
O projeto foi estruturado seguindo as boas práticas de desenvolvimento modular em Python, dividindo-se em:

* `main.py`: Ponto de entrada que inicializa o motor e o loop da CLI.
* `banner_ascii.py`: Módulo responsável pela identidade visual e renderização do logo em ASCII Art.
* `src/ui.py`: Interface de linha de comando baseada nas bibliotecas `rich` e `prompt-toolkit`.
* `src/engine.py`: Integra as regras lógicas de negócio do Python com a API do Ollama Cloud.
* `src/telemetria.py`: Componente responsável por gerar/ler as simulações dos sensores (NDVI, Temperatura e Bateria).
* `src/alertas.py`: Camada algorítmica que processa os dados brutos e gera alertas lógicos antes do envio para a IA.
* `prompts/system_prompt.md`: Engenharia de prompt contendo o contexto de persona, restrições e diretrizes do especialista espacial.

---

## Como Executar o Projeto

### Pré-requisitos
* Python 3.10 ou superior instalado.
* Chave de API válida para o ambiente **Ollama Cloud**.

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Configure as Variáveis de Ambiente:**
    Duplique o arquivo `.env.example` e renomeie a cópia para `.env`:
    ```bash
    cp .env.example .env
    ```
    Abra o arquivo `.env` e insira o seu token de autenticação:
    ```env
    OLLAMA_API_KEY=sua_chave_secreta_aqui
    ```

3.  **Instale as Dependências:**
    Instale todos os pacotes oficiais exigidos pelo projeto:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicie a Aplicação:**
    Execute o arquivo principal para abrir o painel de controle:
    ```bash
    python main.py
    ```

---

## Comandos Disponíveis na CLI

Dentro do terminal `Mission Control`, você pode utilizar os seguintes comandos:
* `/status`: Varre o arquivo de telemetria local e exibe um snapshot rápido das métricas do satélite.
* `/clear`: Limpa a tela do terminal e reinstancia o banner principal.
* `/help`: Lista os comandos operacionais suportados.
* `/exit`: Encerra a sessão do terminal de forma segura.
* `Qualquer pergunta em texto`: Envia os dados simulados do satélite junto com a sua dúvida diretamente para a análise técnica da IA (`gpt-oss:120b`).

---

## Segurança e Boas Práticas
* O arquivo contendo as credenciais locais (`.env`) foi devidamente adicionado ao `.gitignore` para prevenir o vazamento de chaves privadas em escopos públicos.
* A configuração de dependências utiliza controle estrito de versões no arquivo `requirements.txt` com o operador lógico `==`.

---
