import os
import logging
from undetected_playwright.async_api import async_playwright

# Configuração básica de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class BrowserService:
    def __init__(self, browser_type='chromium', headless=False, reuse_session=True):
        """
        Inicializa o serviço do navegador.

        :param browser_type: Tipo do navegador ('chromium', 'firefox', 'webkit').
        :param headless: Se True, roda em modo headless (sem interface gráfica).
        :param reuse_session: Se True, reutiliza cookies/sessão para evitar logins repetidos.
        """
        self.playwright = None
        self.browser_type = browser_type
        self.headless = headless
        self.reuse_session = reuse_session
        self.storage_state = "session.json"  # Armazena cookies/sessão
        self.browser = None
        self.context = None
        self.page = None

    async def _launch_browser(self):
        """Inicia o navegador com base no tipo especificado."""
        launch_options = {
            "headless": self.headless,
            "args": [
                "--disable-blink-features=AutomationControlled",  # Ajuda a evitar detecção de automação
                "--disable-infobars",
                "--start-maximized"
            ]
        }

        if self.browser_type == 'chromium':
            return await self.playwright.chromium.launch(**launch_options)
        elif self.browser_type == 'firefox':
            return await self.playwright.firefox.launch(**launch_options)
        elif self.browser_type == 'webkit':
            return await self.playwright.webkit.launch(**launch_options)
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")

    async def _create_context(self):
        """Cria um novo contexto de navegação, reutilizando sessão se necessário."""
        context_options = {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "extra_http_headers": {
                "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
                "Referer": "https://consultas.anvisa.gov.br/",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin"
            },
            "viewport": {"width": 1280, "height": 720},
            "ignore_https_errors": True,
            "java_script_enabled": True
        }

        # Criar arquivo de sessão caso ele não exista
        if self.reuse_session:
            if not os.path.exists(self.storage_state):
                logging.warning(f"Arquivo {self.storage_state} não encontrado. Criando um novo estado de sessão...")
                with open(self.storage_state, 'w') as f:
                    f.write("{}")  # Criar um arquivo JSON vazio para evitar erro

            context_options["storage_state"] = self.storage_state
            logging.info(f"Reutilizando sessão armazenada em {self.storage_state}")

        context = await self.browser.new_context(**context_options)

        # Carregar o estado da sessão após a criação do contexto
        if self.reuse_session and os.path.exists(self.storage_state):
            await context.add_cookies(self._load_cookies_from_storage())

        return context

    def _load_cookies_from_storage(self):
        """Carrega cookies do arquivo de estado de armazenamento."""
        import json
        with open(self.storage_state, 'r') as f:
            storage = json.load(f)
        return storage.get('cookies', [])

    async def iniciar_navegador(self):
        """Retorna a instância da página."""
        if not self.playwright:
            self.playwright = await async_playwright().start()
        if not self.browser:
            self.browser = await self._launch_browser()
        if not self.context:
            self.context = await self._create_context()
        if not self.page:
            self.page = await self.context.new_page()
        return self.page

    async def salvar_sessao(self):
        """Salva o estado atual do navegador para reutilização futura."""
        try:
            await self.context.storage_state(path=self.storage_state)
            logging.info(f"Estado da sessão salvo em {self.storage_state}")
        except Exception as e:
            logging.error(f"Erro ao salvar estado da sessão: {e}")

    async def fechar_pagina(self):
        """Fecha a página, mas mantém o navegador aberto."""
        if self.page:
            await self.page.close()
            self.page = None
            logging.info("Página fechada.")

    async def fechar_navegador(self):
        """Fecha o navegador e o Playwright, garantindo que a sessão seja salva."""
        try:
            await self.salvar_sessao()  # Salva cookies/sessão antes de fechar
            if self.page:
                await self.page.close()
                self.page = None
            if self.browser:
                await self.browser.close()
                self.browser = None
            logging.info("Navegador fechado.")
        except Exception as e:
            logging.error(f"Erro ao fechar navegador: {e}")
        finally:
            try:
                if self.playwright:
                    await self.playwright.stop()  # Garante que o Playwright seja encerrado corretamente
                    self.playwright = None
                logging.info("Playwright encerrado.")
            except Exception as e:
                logging.error(f"Erro ao encerrar Playwright: {e}")
