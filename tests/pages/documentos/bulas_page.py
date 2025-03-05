import logging
from undetected_playwright.sync_api import Page
from tests.pages.base.base_page import BasePage
from tests.interfaces.busca_page_interface import BuscaPageInterface

class BulasPage(BasePage, BuscaPageInterface):
    def __init__(self, page: Page, browser_service):
        super().__init__(page, "https://consultas.anvisa.gov.br/#/bulario/")
        self.browser_service = browser_service

        # Campos do formulário
        self.campo_nome_medicamento = "input.form-control[ng-model='filter.nomeProduto']"
        self.campo_numero_registro = "input#txtNumeroRegistro"
        self.campo_numero_expediente = "input#txtNumeroExpedienteBula"
        self.campo_empresa_cnpj = "input[ng-model='empresa.cnpj']"
        self.campo_empresa_nome = "input[ng-model='empresa.razaoSocial']"
        self.campo_data_inicial = "input[ng-model='filter.periodoPublicacaoInicial']"
        self.campo_data_final = "input[ng-model='filter.periodoPublicacaoFinal']"
        self.dropdown_categoria = "div.anvs-multiselect[ng-model='filter.categoriasRegulatorias']"
        self.campo_busca_categoria = "input[placeholder='Pesquisar...']"
        self.botao_consultar = "input.btn.btn-primary[type='submit']"
        self.botao_lupa_empresa = "button[ng-click='abrirModalEmpresa()']"
        self.campo_modal_razao_social = "input[ng-model='modal.razaoSocial']"
        self.botao_pesquisar_modal = "button[ng-click='pesquisarEmpresa()']"
        self.resultado_modal_empresa = "table#resultadoEmpresas tbody tr:first-child"
        self.botao_selecionar_modal = "button[ng-click='selecionarEmpresa()']"

    def esperar_elemento_visivel(self, seletor: str, timeout=10000):
        """Espera que um elemento fique visível antes de interagir."""
        try:
            logging.info(f"Verificando se o elemento {seletor} está visível...")
            self.page.wait_for_selector(seletor, state="visible", timeout=timeout)
            logging.info(f"Elemento {seletor} encontrado e visível.")
        except Exception as e:
            logging.error(f"Erro ao verificar o campo {seletor}: {e}")
            self.page.screenshot(path=f"erro_{seletor.replace('[', '').replace(']', '').replace('=', '_')}.png")
            raise

    def realizar_busca(self, campo: str, valor: str):
        """Preenche um campo e executa a busca."""
        logging.info(f"Preenchendo o campo {campo} com o valor '{valor}'...")
        try:
            self.esperar_elemento_visivel(campo)
            elemento = self.page.query_selector(campo)
            if elemento and elemento.is_visible() and elemento.is_enabled():
                logging.info("Elemento encontrado e está visível e habilitado.")
                self.page.screenshot(path=f"antes_preenchendo_campo_{campo}.png")
                self.preencher_campo(campo, valor)
                self.page.screenshot(path=f"depois_preenchendo_campo_{campo}.png")
                logging.info("Esperando sugestões de autocomplete aparecerem...")
                self.page.wait_for_selector("select[ng-show='results.length > 0']", timeout=10000)
                logging.info("Sugestões de autocomplete apareceram.")
                logging.info("Clicando no botão consultar...")
                self.clicar(self.botao_consultar)
                logging.info("Esperando o corpo da página ficar visível...")
                self.esperar_elemento_visivel("body")
            else:
                logging.error(f"Erro: O campo {campo} não está visível ou habilitado.")
                raise ValueError(f"O campo {campo} não está visível ou habilitado.")
        except Exception as e:
            logging.error(f"Erro ao preencher o campo {campo}: {e}")
            self.page.screenshot(path=f"erro_preenchendo_campo_{campo}.png")
            raise

    def buscar_por_nome(self, nome: str):
        logging.info(f"Buscando por nome do medicamento: {nome}")
        self.realizar_busca(self.campo_nome_medicamento, nome)

    def buscar_por_numero_registro(self, numero: str):
        logging.info(f"Buscando por número de registro: {numero}")
        self.realizar_busca(self.campo_numero_registro, numero)

    def buscar_por_numero_expediente(self, expediente: str):
        logging.info(f"Buscando por número de expediente: {expediente}")
        self.realizar_busca(self.campo_numero_expediente, expediente)

    def buscar_por_empresa(self, cnpj: str):
        logging.info(f"Buscando por CNPJ da empresa: {cnpj}")
        self.realizar_busca(self.campo_empresa_cnpj, cnpj)

    def buscar_por_nome_empresa(self, razao_social: str):
        """Interage com o modal de empresas para buscar por Razão Social."""
        logging.info(f"Buscando por nome da empresa: {razao_social}")
        self.clicar(self.botao_lupa_empresa)
        logging.info("Esperando o campo de razão social do modal ficar visível...")
        self.esperar_elemento_visivel(self.campo_modal_razao_social, timeout=20000)
        logging.info(f"Preenchendo o campo de razão social do modal com: {razao_social}")
        self.preencher_campo(self.campo_modal_razao_social, razao_social)
        logging.info("Clicando no botão pesquisar do modal...")
        self.clicar(self.botao_pesquisar_modal)
        logging.info("Esperando o resultado da pesquisa no modal ficar visível...")
        self.esperar_elemento_visivel(self.resultado_modal_empresa, timeout=20000)
        logging.info("Selecionando o resultado da pesquisa no modal...")
        self.clicar(self.resultado_modal_empresa)
        logging.info("Clicando no botão selecionar do modal...")
        self.clicar(self.botao_selecionar_modal)
        logging.info("Esperando o campo de nome da empresa ficar visível...")
        self.esperar_elemento_visivel(self.campo_empresa_nome, timeout=20000)

        # Verificação final para garantir que o campo foi preenchido corretamente
        empresa_selecionada = self.page.input_value(self.campo_empresa_nome)
        if not empresa_selecionada or empresa_selecionada != razao_social:
            logging.error(f"Erro: Nome da empresa '{razao_social}' não foi preenchido corretamente, valor encontrado: '{empresa_selecionada}'")
            raise ValueError(f"Nome da empresa '{razao_social}' não foi preenchido corretamente.")
        logging.info(f"Empresa '{razao_social}' selecionada corretamente.")

    def buscar_por_categoria(self, categorias: list, busca_textual: bool = False):
        logging.info(f"Buscando por categorias: {categorias}")
        self.esperar_elemento_visivel(self.dropdown_categoria)
        self.clicar(self.dropdown_categoria)
        self.esperar_elemento_visivel(self.campo_busca_categoria)
        for categoria in categorias:
            logging.info(f"Selecionando a categoria: {categoria}")
            self.selecionar_opcao_generica(self.campo_busca_categoria, categoria, busca_textual)
        logging.info("Clicando no botão consultar...")
        self.clicar(self.botao_consultar)
        logging.info("Esperando o corpo da página ficar visível...")
        self.esperar_elemento_visivel("body")

    def buscar_por_periodo(self, data_inicial: str, data_final: str):
        logging.info(f"Buscando por período: {data_inicial} a {data_final}")
        self.realizar_busca(self.campo_data_inicial, data_inicial)
        self.realizar_busca(self.campo_data_final, data_final)

    def obter_resultados(self):
        """Retorna os resultados da busca."""
        logging.info("Obtendo resultados da busca...")
        return self.page.text_content("body")

    def selecionar_opcao_generica(self, campo_busca: str, valor: str, busca_textual: bool):
        """Método genérico para selecionar opções em dropdowns e autocompletes."""
        logging.info(f"Selecionando opção genérica: {valor}")
        if busca_textual:
            self.preencher_campo(campo_busca, valor)
            self.clicar(self.detectar_estrutura_dropdown(valor))
        else:
            self.clicar(self.detectar_estrutura_dropdown(valor))

    def detectar_estrutura_dropdown(self, valor: str) -> str:
        """Detecta dinamicamente a estrutura do dropdown para selecionar a opção correta, garantindo que foi aplicada corretamente."""
        logging.info(f"Detectando estrutura do dropdown para o valor: {valor}")
        # Simular scroll para garantir carregamento de todas as opções
        self.page.mouse.wheel(0, 1000)
        self.page.wait_for_timeout(500)  # Pequena pausa para permitir carregamento

        seletores = [
            f"css=div.option >> text={valor}",
            f"css=li.option >> text={valor}",
            f"css=span.option >> text={valor}",
            f"css=button.option >> text={valor}",
            f"css=[data-value='{valor}']",
            f"css=[data-option='{valor}']"
        ]

        for seletor in seletores:
            elemento = self.page.query_selector(seletor)
            if elemento and elemento.is_visible() and elemento.is_enabled():
                logging.info(f"Opção encontrada: {seletor}")
                self.esperar_elemento_visivel(seletor)
                elemento.click()
                self.page.wait_for_timeout(300)  # Pequena pausa para garantir a seleção
            
                # Verifica se o dropdown fechou e se a opção foi realmente aplicada
                if not self.page.is_visible(self.dropdown_categoria) and self.page.input_value(self.dropdown_categoria) == valor:
                    logging.info(f"Opção '{valor}' selecionada corretamente.")
                    return seletor
                else:
                    logging.warning(f"Possível erro: '{valor}' foi clicado, mas não está marcado como selecionado.")

        # Fallback: tentar uma solução alternativa antes de falhar
        logging.error(f"Erro: Opção '{valor}' não encontrada no dropdown. Tentativas: {seletores}")
        self.page.screenshot(path=f"erro_dropdown_{valor}.png")
        raise ValueError(f"Opção '{valor}' não encontrada no dropdown.")