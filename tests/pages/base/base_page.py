from undetected_playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url

    def acessar_pagina(self):
        """Acessa a página informada na URL da classe."""
        self.page.goto(self.url)
        self.page.wait_for_timeout(3000)

    def preencher_campo(self, seletor: str, valor: str):
        """Preenche um campo de input na página."""
        self.page.fill(seletor, valor)

    def clicar(self, seletor: str):
        """Clica em um botão na página."""
        self.page.click(seletor)

    def esperar_elemento_visivel(self, seletor: str, timeout: int = 30000):
        """Espera até que o elemento esteja visível na página."""
        self.page.wait_for_selector(seletor, state='visible', timeout=timeout)

    def elemento_presente(self, seletor: str) -> bool:
        """Verifica se o elemento está presente na página."""
        return self.page.query_selector(seletor) is not None

    def selecionar_opcao(self, seletor: str, valor: str):
        """Seleciona uma opção em um dropdown ou autocomplete."""
        self.page.select_option(seletor, label=valor)
