# 💳 Payment Gateway API | LuizaLabs Ecosystem

![Python](https://img.shields.io/badge/Python-3.14+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Uvicorn](https://img.shields.io/badge/Uvicorn-20232A?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)

Este microsserviço simula um **Gateway de Pagamento** de alta disponibilidade e baixo acoplamento. Desenvolvido sob a ótica da Engenharia de Software moderna e inspirado nos desafios arquiteturais do ecossistema , o projeto utiliza FastAPI para garantir processamento assíncrono, validação estrita de contratos de dados e escalabilidade horizontal.

---

## 🏗️ Arquitetura e Decisões de Design

A aplicação foi estruturada focando em **Separação de Preocupações (SoC)** e performance de I/O:

* **Processamento Assíncrono:** Utilização intensiva de `async/await` no event loop do FastAPI para lidar com alto volume de concorrência sem bloqueio de threads.
* **Data Transfer Objects (DTOs):** Implementação de tipagem estrita e validação de schemas de entrada/saída através do Pydantic V2, garantindo que o core da aplicação processe apenas dados íntegros.
* **Idempotência e Rastreabilidade:** Geração de identificadores únicos universais (UUIDv4) no momento da ingestão da requisição, facilitando auditoria e tracing distribuído.

---

## 🚀 Funcionalidades

**Core Financeiro**
* [x] Processamento transacional assíncrono.
* [x] Geração automática de `transaction_id` (UUID).
* [x] Auditoria em tempo real via buffer de memória.

**Infraestrutura e Segurança (Roadmap)**
* [ ] **Persistência Volumétrica:** Migração do estado em memória para um banco de dados relacional (PostgreSQL) via ORM (SQLAlchemy).
* [ ] **Autenticação:** Implementação de API Keys e JWT (Bearer) para proteção de endpoints sensíveis.
* [ ] **Qualidade:** Cobertura de testes unitários e de integração utilizando `pytest`.

---

## 📂 Contrato de API (Endpoints)

A documentação interativa completa (OpenAPI/Swagger) está disponível em `/docs` ao rodar a aplicação.

| Método | Endpoint | Descrição Técnica | Status Esperado |
| :--- | :--- | :--- | :--- |
| `POST` | `/processar` | Ingestão de payload, validação de regras e efetivação do pagamento. | `201 Created` |
| `GET` | `/historico` | Recupera a coleção completa do log de operações transacionais. | `200 OK` |
| `GET` | `/transacao/{id}` | Busca granular por chave primária (UUID) de uma transação específica. | `200 OK` / `404 Not Found` |

---

## ⚙️ Guia de Desenvolvimento

### Pré-requisitos
* Python 3.14 ou superior instalado.
* Gerenciador de pacotes `pip`.

### Setup do Ambiente

1. **Clonagem do Repositório:**
   ```bash
   git clone [https://github.com/MarcosSoftwareEngineering/python-payment-gateway.git](https://github.com/MarcosSoftwareEngineering/python-payment-gateway.git)
   cd python-payment-gateway
   ```

2. **Isolamento de Ambiente (Virtualenv):**
   ```bash
   python -m venv venv
   
   # Ativação (Windows)
   .\venv\Scripts\activate
   
   # Ativação (Linux/macOS)
   source venv/bin/activate
   ```

3. **Instalação de Dependências:**
   ```bash
   pip install fastapi uvicorn pydantic
   ```

### Execução Local

Para subir o servidor ASGI com hot-reload ativo (ideal para desenvolvimento):
```bash
uvicorn main:app --reload
```

Acesse a interface visual para testes de chamadas HTTP:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 👨‍💻 Autor

**Marcos Vinicius**
*Estudante de Engenharia de Software | Desenvolvedor full stack*

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white)](https://github.com/MarcosSoftwareEngineering)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat-square&logo=vercel&logoColor=white)](https://marcos-dev-zeta.vercel.app/)
