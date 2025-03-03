# Anvisa Consultas - Teste de Fluxos

Este repositório contém testes automatizados para validar os fluxos do Sistema Consultas Externas da ANVISA.

## 📌 Funcionalidades Testadas

### **Seção Documentos**
- [Bulas de Medicamentos](https://consultas.anvisa.gov.br/#/bulario/)
- [Pareceres Públicos](https://consultas.anvisa.gov.br/#/pareceres/)
- [Documentos Administrativos](https://consultas.anvisa.gov.br/#/documentos/administrativo/)
- [Documentos Técnicos](https://consultas.anvisa.gov.br/#/documentos/tecnicos/)

### **Seção Empresas e Fiscalização de Produtos**
- [Certificados de Boas Práticas](https://consultas.anvisa.gov.br/#/certificadosdeboaspraticas/)
- [Certificados de Boas Práticas - Medicamento](https://consultas.anvisa.gov.br/#/certificadosdeboaspraticas-medicamento/)
- [Empresas](https://consultas.anvisa.gov.br/#/empresas/empresas/)
- [Empresas Internacionais](https://consultas.anvisa.gov.br/#/empresas/empresasInternacionais/)
- [Dossiês](https://consultas.anvisa.gov.br/#/dossie/)

### **Seção Informações Regulatórias**
- [Consulta de Assuntos](https://consultas.anvisa.gov.br/#/consultadeassuntos/)
- [Nomes Técnicos](https://consultas.anvisa.gov.br/#/nomes-tecnicos/)
- [Filas de Processos](https://consultas.anvisa.gov.br/#/filas/)
- [Listas Regulatórias](https://consultas.anvisa.gov.br/#/listas/)
- [Legislação - Anvisalegis](https://anvisalegis.datalegis.net/)

### **Seção Produtos**
- [Alimentos](https://consultas.anvisa.gov.br/#/alimentos/)
- [Cosméticos Registrados](https://consultas.anvisa.gov.br/#/cosmeticos/registrados/)
- [Cosméticos Regularizados](https://consultas.anvisa.gov.br/#/cosmeticos/regularizados/)
- [Ensaios Clínicos](https://consultas.anvisa.gov.br/#/ensaiosclinicos/)
- [Medicamentos](https://consultas.anvisa.gov.br/#/medicamentos/)
- [Produtos à Base de Cannabis](https://consultas.anvisa.gov.br/#/cannabis/)
- [Produtos para Saúde](https://consultas.anvisa.gov.br/#/saude/)
- [Saneantes Registrados](https://consultas.anvisa.gov.br/#/saneantes/produtos/)
- [Saneantes Notificados](https://consultas.anvisa.gov.br/#/saneantes/notificados/)
- [Produtos de Tabaco](https://consultas.anvisa.gov.br/#/tabacos/)

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

## 📂 Estrutura do Repositório
```
📂 anvisa-consultas-teste-fluxos
 ├── 📁 tests/                 # Scripts de testes automatizados
 ├── 📁 reports/               # Relatórios e logs de testes
 ├── 📁 configs/               # Configurações e variáveis de ambiente
 ├── 📄 README.md              # Documentação do projeto
 ├── 📄 requirements.txt       # Dependências (Python)
 ├── 📄 test_suite.py          # Execução principal dos testes
```

---
Criado para garantir a estabilidade e a confiabilidade das consultas no sistema da ANVISA.
