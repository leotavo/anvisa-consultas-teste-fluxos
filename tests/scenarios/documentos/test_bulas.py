import logging
import pytest
from tests.pages.documentos.bulas_page import BulasPage
from tests.config.test_data import TEST_DATA_BULAS
from tests.services.browser_service import BrowserService

class BulasTestRunner:
    def __init__(self, browser_type="chromium", headless=False, timeout=30000):
        """
        Inicializa o serviço do navegador.

        :param browser_type: Tipo do navegador ('chromium', 'firefox', 'webkit').
        :param headless: Se True, roda em modo headless (sem interface gráfica).
        :param timeout: Tempo limite para carregamento da página e ações (em milissegundos).
        """
        self.browser_service = BrowserService(browser_type, headless=headless)
        self.timeout = timeout

    async def executar_teste(self, acao):
        """
        Executa um teste usando o Page Object Model (POM).

        :param acao: Função que recebe a instância de `BulasPage` e executa um teste.
        """
        page = await self.browser_service.iniciar_navegador()
        page.set_default_timeout(self.timeout)
        bulas = BulasPage(page, self.browser_service)

        try:
            logging.info("Acessando a página de bulas...")
            await bulas.acessar_pagina()
            logging.info("Página acessada com sucesso.")

            logging.info("Executando a ação de teste...")
            await acao(bulas)

            logging.info("Obtendo resultados...")
            resultado = await bulas.obter_resultados()
            if not resultado:
                raise AssertionError("Nenhum resultado encontrado na busca.")

            logging.info("Teste finalizado com sucesso.")

        except Exception as e:
            logging.error(f"Erro durante o teste: {e}")
            pytest.fail(f"Teste falhou com erro: {e}")

        finally:
            logging.info("Fechando o navegador...")
            await self.browser_service.fechar_navegador()

    async def finalizar(self):
        """Finaliza o navegador após todos os testes."""
        await self.browser_service.fechar_navegador()

# Instância global do BulasTestRunner para ser usada nos testes
test_runner = BulasTestRunner()

@pytest.mark.asyncio
async def test_busca_bula_por_medicamento():
    """Testa a busca por Nome do Medicamento."""
    async def acao(bulas):
        logging.info("Buscando por nome do medicamento...")
        try:
            await bulas.buscar_por_nome(TEST_DATA_BULAS["nome_medicamento"])
            logging.info("Busca por nome do medicamento concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por nome do medicamento: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_por_numero_registro():
    """Testa a busca pelo Número de Registro."""
    async def acao(bulas):
        logging.info("Buscando por número de registro...")
        try:
            await bulas.buscar_por_numero_registro(TEST_DATA_BULAS["numero_registro"])
            logging.info("Busca por número de registro concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por número de registro: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_por_empresa():
    """Testa a busca pelo CNPJ da Empresa."""
    async def acao(bulas):
        logging.info("Buscando por CNPJ da empresa...")
        try:
            await bulas.buscar_por_empresa(TEST_DATA_BULAS["cnpj_empresa"])
            logging.info("Busca por CNPJ da empresa concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por CNPJ da empresa: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_por_nome_empresa():
    """Testa a busca pelo Nome da Empresa através do modal e verifica se o campo foi preenchido corretamente."""
    async def acao(bulas):
        logging.info("Buscando por nome da empresa...")
        try:
            await bulas.buscar_por_nome_empresa(TEST_DATA_BULAS["nome_empresa"])
            logging.info("Busca por nome da empresa concluída.")
            
            # Captura o valor preenchido no campo após a seleção
            empresa_preenchida = await bulas.page.input_value(bulas.campo_empresa_nome).strip()
            
            # Validação: O nome da empresa preenchido deve ser igual ao esperado
            assert empresa_preenchida == TEST_DATA_BULAS["nome_empresa"], (
                f"Erro: Razão Social não foi preenchida corretamente. "
                f"Esperado: '{TEST_DATA_BULAS['nome_empresa']}', Obtido: '{empresa_preenchida}'"
            )
        except Exception as e:
            logging.error(f"Erro ao buscar por nome da empresa: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_por_categoria():
    """Testa a busca por Categoria Regulatória."""
    async def acao(bulas):
        logging.info("Buscando por categoria regulatória...")
        try:
            await bulas.buscar_por_categoria(TEST_DATA_BULAS["categoria_regulatoria"])
            logging.info("Busca por categoria regulatória concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por categoria regulatória: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_por_multiplas_categorias():
    """Testa a busca por múltiplas categorias regulatórias."""
    async def acao(bulas):
        logging.info("Buscando por múltiplas categorias regulatórias...")
        try:
            await bulas.buscar_por_categoria(TEST_DATA_BULAS["categorias_regulatorias"])
            logging.info("Busca por múltiplas categorias regulatórias concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por múltiplas categorias regulatórias: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_por_periodo():
    """Testa a busca por Período de Publicação."""
    async def acao(bulas):
        logging.info("Buscando por período de publicação...")
        try:
            await bulas.buscar_por_periodo(TEST_DATA_BULAS["data_inicial"], TEST_DATA_BULAS["data_final"])
            logging.info("Busca por período de publicação concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por período de publicação: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_por_periodo_data_inicial_vazia():
    """Testa a busca por Período de Publicação com data inicial vazia."""
    async def acao(bulas):
        logging.info("Buscando por período de publicação com data inicial vazia...")
        try:
            await bulas.buscar_por_periodo(TEST_DATA_BULAS["data_inicial_vazia"], TEST_DATA_BULAS["data_final"])
            logging.info("Busca por período de publicação com data inicial vazia concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por período de publicação com data inicial vazia: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_por_periodo_data_final_vazia():
    """Testa a busca por Período de Publicação com data final vazia."""
    async def acao(bulas):
        logging.info("Buscando por período de publicação com data final vazia...")
        try:
            await bulas.buscar_por_periodo(TEST_DATA_BULAS["data_inicial"], TEST_DATA_BULAS["data_final_vazia"])
            logging.info("Busca por período de publicação com data final vazia concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por período de publicação com data final vazia: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_por_numero_expediente():
    """Testa a busca pelo Número de Expediente."""
    async def acao(bulas):
        logging.info("Buscando por número de expediente...")
        try:
            await bulas.buscar_por_numero_expediente(TEST_DATA_BULAS["numero_expediente"])
            logging.info("Busca por número de expediente concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por número de expediente: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_campos_vazios():
    """Testa a busca com todos os campos vazios."""
    async def acao(bulas):
        logging.info("Clicando no botão consultar com campos vazios...")
        try:
            await bulas.clicar(bulas.botao_consultar)
            logging.info("Clique no botão consultar concluído.")
        except Exception as e:
            logging.error(f"Erro ao clicar no botão consultar com campos vazios: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_dados_invalidos():
    """Testa a busca com dados inválidos."""
    async def acao(bulas):
        logging.info("Buscando por nome do medicamento inválido...")
        try:
            await bulas.buscar_por_nome(TEST_DATA_BULAS["nome_medicamento_invalido"])
            logging.info("Busca por nome do medicamento inválido concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por nome do medicamento inválido: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_numero_registro_invalido():
    """Testa a busca com Número de Registro inválido."""
    async def acao(bulas):
        logging.info("Buscando por número de registro inválido...")
        try:
            await bulas.buscar_por_numero_registro(TEST_DATA_BULAS["numero_registro_invalido"])
            logging.info("Busca por número de registro inválido concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por número de registro inválido: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_cnpj_invalido():
    """Testa a busca com CNPJ da Empresa inválido."""
    async def acao(bulas):
        logging.info("Buscando por CNPJ da empresa inválido...")
        try:
            await bulas.buscar_por_empresa(TEST_DATA_BULAS["cnpj_empresa_invalido"])
            logging.info("Busca por CNPJ da empresa inválido concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por CNPJ da empresa inválido: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_categoria_invalida():
    """Testa a busca com Categoria Regulatória inválida."""
    async def acao(bulas):
        logging.info("Buscando por categoria regulatória inválida...")
        try:
            await bulas.buscar_por_categoria(TEST_DATA_BULAS["categoria_invalida"])
            logging.info("Busca por categoria regulatória inválida concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por categoria regulatória inválida: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_periodo_invalido():
    """Testa a busca com Período de Publicação inválido."""
    async def acao(bulas):
        logging.info("Buscando por período de publicação inválido...")
        try:
            await bulas.buscar_por_periodo(TEST_DATA_BULAS["data_inicial_invalida"], TEST_DATA_BULAS["data_final_invalida"])
            logging.info("Busca por período de publicação inválido concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por período de publicação inválido: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_numero_expediente_invalido():
    """Testa a busca com Número de Expediente inválido."""
    async def acao(bulas):
        logging.info("Buscando por número de expediente inválido...")
        try:
            await bulas.buscar_por_numero_expediente(TEST_DATA_BULAS["numero_expediente_invalido"])
            logging.info("Busca por número de expediente inválido concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por número de expediente inválido: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def test_busca_bula_nome_empresa_invalido():
    """Testa a busca com Nome da Empresa inválido."""
    async def acao(bulas):
        logging.info("Buscando por nome da empresa inválido...")
        try:
            await bulas.buscar_por_nome_empresa(TEST_DATA_BULAS["nome_empresa_invalido"])
            logging.info("Busca por nome da empresa inválido concluída.")
        except Exception as e:
            logging.error(f"Erro ao buscar por nome da empresa inválido: {e}")
            raise
    await test_runner.executar_teste(acao)

@pytest.mark.asyncio
async def teardown_module(module):
    """Finaliza o navegador após todos os testes."""
    await test_runner.finalizar()