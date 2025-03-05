from abc import ABC, abstractmethod

class BuscaPageInterface(ABC):
    @abstractmethod
    def buscar_por_nome(self, nome: str):
        pass

    @abstractmethod
    def buscar_por_numero_registro(self, numero: str):
        pass

    @abstractmethod
    def buscar_por_numero_expediente(self, expediente: str):
        pass

    @abstractmethod
    def buscar_por_empresa(self, cnpj: str):
        pass

    @abstractmethod
    def buscar_por_categoria(self, categorias: list, busca_textual: bool = False):
        pass

    @abstractmethod
    def buscar_por_periodo(self, data_inicial: str, data_final: str):
        pass

    @abstractmethod
    def obter_resultados(self):
        pass
