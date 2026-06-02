import os
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from prompt_toolkit import PromptSession

console = Console()

def show_banner():
    """Exibe o banner ASCII grande e o menu de boas-vindas inicial."""
    banner = pyfiglet.figlet_format("Mission Control", font="ansi_shadow")
    console.print(Text(banner, style="bold #06B6D4"))
    
    welcome_text = (
        "[bold white]Sistema de monitoramento e análise por IA generativa.[/]\n\n"
        "  [cyan]❯ /status[/]      - Varre a telemetria atual do satélite.\n"
        "  [cyan]❯ /run[/]         - Pede à IA uma nova análise da telemetria atual.\n"
        "  [cyan]❯ /help[/]        - Exibe os comandos operacionais suportados.\n"
        "  [cyan]❯ /clear[/]       - Limpa o histórico de logs do painel.\n"
        "  [cyan]❯ /exit[/]        - Encerra a conexão e fecha o terminal.\n\n"
        "[dim]Modelo ativo: gpt-oss:120b via Ollama Cloud[/]"
    )
    
    console.print(Panel(
        welcome_text, 
        title="◆ MISSION CONTROL AI", 
        border_style="#06B6D4"
    ))

def show_help():
    """Exibe um painel exclusivo de ajuda integrado ao histórico do terminal."""
    help_text = (
        "[bold white]Guia de Operação de Órbita — Comandos Disponíveis:[/]\n\n"
        "  [cyan]❯ /status[/]      - Retorna o snapshot atual dos dados do satélite.\n"
        "  [cyan]❯ /run[/]         - Força o recálculo e reanálise dos dados dinâmicos.\n"
        "  [cyan]❯ /help[/]        - Exibe esta lista de instruções técnicas.\n"
        "  [cyan]❯ /clear[/]       - Limpa o terminal por completo.\n"
        "  [cyan]❯ /exit[/]        - Finaliza a sessão com segurança.\n\n"
        "[dim]Para interagir com o analista, basta digitar a sua pergunta diretamente.[/]"
    )
    
    console.print(Panel(
        help_text, 
        title="◆ HELPDESK SISTÊMICO", 
        border_style="#E11D48"
    ))

def show_response(text):
    """Renderiza as respostas normais da IA ou dados do status."""
    console.print(Panel(text, title="◆ RESPOSTA DO SISTEMA", border_style="#06B6D4"))

def run_cli(engine):
    """Loop principal da CLI — Processa os comandos de forma limpa e inteligente."""
    session = PromptSession()
    
    # Inicialização limpa com apagamento total do terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    show_banner()
    
    # Dispara o diagnóstico inteligente automático na largada do programa
    console.print("\n[bold #06B6D4]◆ INICIANDO DIAGNÓSTICO AUTOMÁTICO DE ÓRBITA...[/]")
    with console.status("[bold dim]Coletando telemetria e consultando IA...[/]"):
        try:
            analise_inicial = engine.analyze("") 
            show_response(analise_inicial)
        except Exception as e:
            console.print(f"[bold red]Erro ao gerar diagnóstico inicial:[/] {e}")
            
    if not engine.is_ready():
        console.print(" ⚠ Engine status: AGUARDANDO IMPLEMENTAÇÃO X\n", style="yellow")
        
    while True:
        try:
            user_input = session.prompt("❯ ").strip()
        except (KeyboardInterrupt, EOFError):
            break
            
        if not user_input:
            continue
            
        comando_limpo = user_input.lstrip("/").lower()
        
        if comando_limpo == "exit":
            print("Encerrando conexão de órbita...")
            break
            
        elif comando_limpo == "help":
            show_help()
            continue
            
        elif comando_limpo == "status":
            show_response(engine.status_snapshot())
            continue
            
        elif comando_limpo in ["run", "scan"]:
            console.print("\n[bold #06B6D4]◆ REAVALIANDO TELEMETRIA VIA IA...[/]")
            with console.status("[bold dim]Consultando Ollama Cloud com os novos dados...[/]"):
                try:
                    nova_analise = engine.analyze("") 
                    show_response(nova_analise)
                except Exception as e:
                    console.print(f"[bold red]Erro ao recalcular diagnóstico:[/] {e}")
            continue
            
        elif comando_limpo == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            show_banner()
            continue
            
        else:
            resposta = engine.analyze(user_input)
            show_response(resposta)