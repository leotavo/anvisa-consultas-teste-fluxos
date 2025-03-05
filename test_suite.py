import time
import logging
import os
from undetected_playwright.sync_api import sync_playwright

# Configuração de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Lista de campos para verificar
CAMPOS = [
    {"nome": "Nome do Medicamento", "seletor": "input.form-control[ng-model='filter.nomeProduto']"},
    {"nome": "Número de Registro", "seletor": "input#txtNumeroRegistro"},
    {"nome": "Número de Expediente", "seletor": "input#txtNumeroExpedienteBula"},
    {"nome": "CNPJ da Empresa", "seletor": "input[ng-model='empresa.cnpj']"},
    {"nome": "Razão Social da Empresa", "seletor": "input[ng-model='empresa.razaoSocial']"},
    {"nome": "Data Inicial", "seletor": "input[ng-model='filter.periodoPublicacaoInicial']"},
    {"nome": "Data Final", "seletor": "input[ng-model='filter.periodoPublicacaoFinal']"},
    {"nome": "Dropdown Categoria", "seletor": "div.anvs-multiselect[ng-model='filter.categoriasRegulatorias']"},
    {"nome": "Campo Pesquisa Categoria", "seletor": "input[placeholder='Pesquisar...']"},
    {"nome": "Botão Consultar", "seletor": "input.btn.btn-primary[type='submit']"},
    {"nome": "Botão Abrir Modal Empresa", "seletor": "button[ng-click='abrirModalEmpresa()']"},
    {"nome": "Campo Razão Social no Modal", "seletor": "input[ng-model='modal.razaoSocial']"},
    {"nome": "Botão Pesquisar Empresa", "seletor": "button[ng-click='pesquisarEmpresa()']"},
    {"nome": "Tabela de Resultados do Modal", "seletor": "table#resultadoEmpresas tbody tr:first-child"},
    {"nome": "Botão Selecionar Empresa", "seletor": "button[ng-click='selecionarEmpresa()']"},
]

# Diretório para salvar prints de erro
ERRO_SCREENSHOT_DIR = "screenshots_erro"
os.makedirs(ERRO_SCREENSHOT_DIR, exist_ok=True)

def verificar_elementos(page):
    """
    Verifica se os campos da página estão visíveis e habilitados.
    """
    for campo in CAMPOS:
        nome = campo["nome"]
        seletor = campo["seletor"]

        try:
            logging.info(f"🔎 Verificando: {nome} ({seletor})")

            elemento = page.wait_for_selector(seletor, state="attached", timeout=10000)  # Increased timeout to 10000ms

            if elemento.is_visible():
                if elemento.is_enabled():
                    logging.info(f"✅ {nome} está VISÍVEL e HABILITADO.")
                else:
                    logging.warning(f"⚠️ {nome} está VISÍVEL, mas NÃO está habilitado.")
            else:
                logging.warning(f"⚠️ {nome} está PRESENTE, mas NÃO visível!")

        except Exception as e:
            logging.error(f"❌ {nome} NÃO encontrado! Erro: {e}")

            # Capturar print da tela para debug
            screenshot_path = os.path.join(ERRO_SCREENSHOT_DIR, f"erro_{nome.replace(' ', '_')}.png")
            page.screenshot(path=screenshot_path)
            logging.error(f"📸 Print salvo: {screenshot_path}")

            # Capturar estrutura do DOM e logar
            html_source = page.evaluate("() => document.body.innerHTML")
            with open(os.path.join(ERRO_SCREENSHOT_DIR, "dom_snapshot.html"), "w", encoding="utf-8") as f:
                f.write(html_source)
            logging.error(f"📝 Captura do HTML salva para análise!")

def main():
    with sync_playwright() as p:
        args = ["--disable-blink-features=AutomationControlled"]
        browser = p.chromium.launch(headless=False, slow_mo=500, args=args)
        context = browser.new_context()
        page = context.new_page()
        
        logging.info("🌐 Acessando a página de bulas...")
        page.goto("https://consultas.anvisa.gov.br/#/bulario/")
        page.wait_for_load_state("networkidle")
        time.sleep(5)  # Increased sleep time to ensure the page is fully loaded

        logging.info("🔍 Iniciando verificação dos campos...")
        verificar_elementos(page)

        logging.info("✅ Verificação concluída! Você pode fechar o navegador.")
        time.sleep(10)  # Mantém o navegador aberto para visualização
        browser.close()

if __name__ == "__main__":
    main()
