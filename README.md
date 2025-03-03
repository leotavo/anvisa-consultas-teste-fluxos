# Anvisa Consultas - Teste de Fluxos

Este repositório contém testes automatizados para validar os fluxos do Sistema Consultas Externas da ANVISA.

## 📌 Funcionalidades Testadas

### **📄 Seção Documentos**
- [Consulta de Bulas de Medicamentos](https://consultas.anvisa.gov.br/#/bulario/)
- [Consulta de Pareceres Públicos](https://consultas.anvisa.gov.br/#/pareceres/)
- [Consulta de Documentos Administrativos](https://consultas.anvisa.gov.br/#/documentos/administrativo/)
- [Consulta de Documentos Técnicos](https://consultas.anvisa.gov.br/#/documentos/tecnicos/)

### **🏭 Seção Empresas e Fiscalização de Produtos**
- [Consulta de Certificados de Boas Práticas](https://consultas.anvisa.gov.br/#/certificadosdeboaspraticas/)
- [Consulta de Certificados de Boas Práticas - Medicamentos](https://consultas.anvisa.gov.br/#/certificadosdeboaspraticas-medicamento/)
- [Consulta de Empresas Nacionais](https://consultas.anvisa.gov.br/#/empresas/empresas/)
- [Consulta de Empresas Internacionais](https://consultas.anvisa.gov.br/#/empresas/empresasInternacionais/)
- [Consulta de Dossiês Regulatórios](https://consultas.anvisa.gov.br/#/dossie/)

### **⚖️ Seção Informações Regulatórias**
- [Consulta de Assuntos Regulatórios](https://consultas.anvisa.gov.br/#/consultadeassuntos/)
- [Consulta de Nomes Técnicos](https://consultas.anvisa.gov.br/#/nomes-tecnicos/)
- [Consulta de Filas de Processos](https://consultas.anvisa.gov.br/#/filas/)
- [Consulta de Listas Regulatórias](https://consultas.anvisa.gov.br/#/listas/)
- [Legislação - AnvisaLegis](https://anvisalegis.datalegis.net/)

### **🛒 Seção Produtos**
- [Consulta de Alimentos Regulados](https://consultas.anvisa.gov.br/#/alimentos/)
- [Consulta de Cosméticos Registrados](https://consultas.anvisa.gov.br/#/cosmeticos/registrados/)
- [Consulta de Cosméticos Regularizados](https://consultas.anvisa.gov.br/#/cosmeticos/regularizados/)
- [Consulta de Ensaios Clínicos](https://consultas.anvisa.gov.br/#/ensaiosclinicos/)
- [Consulta de Medicamentos](https://consultas.anvisa.gov.br/#/medicamentos/)
- [Consulta de Produtos à Base de Cannabis](https://consultas.anvisa.gov.br/#/cannabis/)
- [Consulta de Produtos para Saúde](https://consultas.anvisa.gov.br/#/saude/)
- [Consulta de Saneantes Registrados](https://consultas.anvisa.gov.br/#/saneantes/produtos/)
- [Consulta de Saneantes Notificados](https://consultas.anvisa.gov.br/#/saneantes/notificados/)
- [Consulta de Produtos de Tabaco](https://consultas.anvisa.gov.br/#/tabacos/)

## 🛠️ Tecnologias Utilizadas
- **Selenium / Playwright** → Testes de interface web
- **Postman / Python Requests** → Testes de API *(se houver API disponível)*
- **JMeter / Locust** → Testes de carga
- **GitHub Actions / Jenkins** → Execução contínua dos testes

## 📌 Quadro Resumo dos Requisitos

| **Tipo de Teste** | **Ferramentas** | **Requisitos** |
|------------------|----------------|---------------|
| **Testes de Interface Web (UI Tests)** | Selenium, Playwright | ✅ Python 3.x ou Node.js<br>✅ WebDriver (ChromeDriver, GeckoDriver)<br>✅ Biblioteca Selenium/Playwright instalada<br>✅ Ambiente com navegador compatível (Chrome, Firefox, Edge) |
| **Testes de API** | Postman, Python Requests | ✅ Python 3.x<br>✅ Biblioteca Requests ou Postman CLI<br>✅ URL da API e credenciais (se necessário)<br>✅ JSON/XML para validação das respostas |
| **Testes de Carga** | JMeter, Locust | ✅ Python 3.x (para Locust) ou Java 8+ (para JMeter)<br>✅ Configuração do JMeter ou Locustfile<br>✅ Definição de usuários virtuais e taxa de requisições<br>✅ Servidor de testes adequado (para simular múltiplos acessos) |
| **Execução Contínua (CI/CD)** | GitHub Actions, Jenkins | ✅ Acesso ao repositório GitHub<br>✅ Configuração do pipeline YAML (GitHub Actions) ou servidor Jenkins<br>✅ Dependências dos testes instaladas no ambiente de build |

### 🛠️ Requisitos para Testes Automatizados

| **Tipo de Teste** | **Ferramentas** | **Requisitos** |
|------------------|----------------|---------------|
| **Testes de Interface Web (UI Tests)** | Selenium, Playwright | ✅ Python 3.x ou Node.js<br>✅ WebDriver (ChromeDriver, GeckoDriver)<br>✅ Biblioteca Selenium/Playwright instalada<br>✅ Ambiente com navegador compatível (Chrome, Firefox, Edge) |
| **Testes de API** | Postman, Python Requests | ✅ Python 3.x<br>✅ Biblioteca Requests ou Postman CLI<br>✅ URL da API e credenciais (se necessário)<br>✅ JSON/XML para validação das respostas |
| **Testes de Carga** | JMeter, Locust | ✅ Python 3.x (para Locust) ou Java 8+ (para JMeter)<br>✅ Configuração do JMeter ou Locustfile<br>✅ Definição de usuários virtuais e taxa de requisições<br>✅ Servidor de testes adequado (para simular múltiplos acessos) |
| **Execução Contínua (CI/CD)** | GitHub Actions, Jenkins | ✅ Acesso ao repositório GitHub<br>✅ Configuração do pipeline YAML (GitHub Actions) ou servidor Jenkins<br>✅ Dependências dos testes instaladas no ambiente de build |

---
## 🚀 Como Executar os Testes
1. Clone o repositório  
   ```bash
   git clone https://github.com/leotavo/anvisa-consultas-teste-fluxos.git
   cd anvisa-consultas-teste-fluxos
   ```
2. Instale as dependências  
   ```bash
   pip install -r requirements.txt
   ```
3. Execute os testes  
   ```bash
   python test_suite.py
   ```

## 📂 Estrutura do Projeto

```
📂 anvisa-consultas-teste-fluxos
 ├── 📂 tests/                      # 📌 Testes organizados por funcionalidade
 │   ├── 📂 pages/                  # 🏗️ Page Objects (Cada classe representa uma página de consulta)
 │   │   ├── documentos/            # 📄 Testes de Documentos
 │   │   │   ├── bulas_page.py
 │   │   │   ├── pareceres_page.py
 │   │   │   ├── documentos_administrativos_page.py
 │   │   │   ├── documentos_tecnicos_page.py
 │   │   ├── empresas/              # 🏭 Testes de Empresas e Fiscalização de Produtos
 │   │   │   ├── certificados_boas_praticas_page.py
 │   │   │   ├── certificados_boas_praticas_medicamento_page.py
 │   │   │   ├── empresas_nacionais_page.py
 │   │   │   ├── empresas_internacionais_page.py
 │   │   │   ├── dossies_page.py
 │   │   ├── regulatorio/            # ⚖️ Testes de Informações Regulatórias
 │   │   │   ├── consulta_assuntos_page.py
 │   │   │   ├── nomes_tecnicos_page.py
 │   │   │   ├── filas_processos_page.py
 │   │   │   ├── listas_regulatorias_page.py
 │   │   │   ├── legislacao_page.py
 │   │   ├── produtos/               # 🛒 Testes de Produtos
 │   │   │   ├── alimentos_page.py
 │   │   │   ├── cosmeticos_registrados_page.py
 │   │   │   ├── cosmeticos_regularizados_page.py
 │   │   │   ├── ensaios_clinicos_page.py
 │   │   │   ├── medicamentos_page.py
 │   │   │   ├── cannabis_page.py
 │   │   │   ├── produtos_saude_page.py
 │   │   │   ├── saneantes_registrados_page.py
 │   │   │   ├── saneantes_notificados_page.py
 │   │   │   ├── tabacos_page.py
 │   │   ├── base_page.py            # 🔄 Classe base para reuso (herança)
 │   ├── 📂 scenarios/               # 📖 Casos de teste organizados por funcionalidade
 │   │   ├── documentos/
 │   │   │   ├── test_bulas.py
 │   │   │   ├── test_pareceres.py
 │   │   │   ├── test_documentos_administrativos.py
 │   │   │   ├── test_documentos_tecnicos.py
 │   │   ├── empresas/
 │   │   │   ├── test_certificados_boas_praticas.py
 │   │   │   ├── test_certificados_boas_praticas_medicamento.py
 │   │   │   ├── test_empresas_nacionais.py
 │   │   │   ├── test_empresas_internacionais.py
 │   │   │   ├── test_dossies.py
 │   │   ├── regulatorio/
 │   │   │   ├── test_consulta_assuntos.py
 │   │   │   ├── test_nomes_tecnicos.py
 │   │   │   ├── test_filas_processos.py
 │   │   │   ├── test_listas_regulatorias.py
 │   │   │   ├── test_legislacao.py
 │   │   ├── produtos/
 │   │   │   ├── test_alimentos.py
 │   │   │   ├── test_cosmeticos_registrados.py
 │   │   │   ├── test_cosmeticos_regularizados.py
 │   │   │   ├── test_ensaios_clinicos.py
 │   │   │   ├── test_medicamentos.py
 │   │   │   ├── test_cannabis.py
 │   │   │   ├── test_produtos_saude.py
 │   │   │   ├── test_saneantes_registrados.py
 │   │   │   ├── test_saneantes_notificados.py
 │   │   │   ├── test_tabacos.py
 │   ├── 📂 utils/                   # 🔧 Helpers e funções auxiliares
 │   │   ├── playwright_helper.py    # Configuração do Playwright
 │   │   ├── logger.py               # Gerenciamento de logs
 │   │   ├── config.py               # Configuração global
 ├── 📂 reports/                     # 📊 Relatórios de testes
 ├── 📂 configs/                     # ⚙️ Configurações adicionais
 ├── requirements.txt                # 📌 Dependências do projeto
 ├── test_suite.py                   # 🚀 Ponto de entrada para execução dos testes
 ├── README.md                        # 📖 Documentação do projeto

---
Criado para garantir a estabilidade e a confiabilidade das consultas no sistema da ANVISA.
