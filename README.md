# 💳 Gateway de Pagamento em Python | LuizaLabs Project

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Uvicorn](https://img.shields.io/badge/uvicorn-20232A?style=for-the-badge&logo=python&logoColor=white)

Este projeto simula um **Gateway de Pagamento** de alto desempenho, desenvolvido com foco em Engenharia de Software. Ele segue os padrões de arquitetura discutidos no programa da **LuizaLabs**, utilizando FastAPI para garantir velocidade e escalabilidade no processamento de transações.

## 🚀 Funcionalidades

- [x] **Processamento Assíncrono:** Utilização de `async/await` para alta performance.
- [x] **Validação com Pydantic:** Tipagem forte para garantir que apenas dados válidos sejam processados.
- [x] **Geração de UUID:** Cada transação recebe um ID único universal para rastreabilidade.
- [x] **Histórico em Memória:** Endpoint dedicado para auditoria de todas as transações realizadas.
- [ ] **Persistência em Banco de Dados:** Migração planejada para SQLite/PostgreSQL.
- [ ] **Segurança:** Implementação de API Key para proteção de dados sensíveis.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.14+
- **Framework:** FastAPI
- **Servidor ASGI:** Uvicorn
- **Validação:** Pydantic

## 📂 Endpoints Principais

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `POST` | `/processar` | Processa um novo pagamento e gera ID de transação. |
| `GET` | `/historico` | Retorna a lista completa de transações realizadas. |
| `GET` | `/transacao/{id}` | Busca os detalhes de uma transação específica por ID. |

## ⚙️ Como executar o projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/MarcosSoftwareEngineering/python-payment-gateway.git](https://github.com/MarcosSoftwareEngineering/python-payment-gateway.git)
   cd python-payment-gateway

 2. **Ative o ambiente virtual:**

   # Windows
.\venv\Scripts\activate

3. **Inicie o servidor:**

uvicorn main:app --reload
4.  **Acesse a documentação interativa:**

Vá para http://127.0.0.1:8000/docs para testar os endpoints via Swagger UI.

O seu README atual está bom, mas como você elevou o nível do projeto hoje usando **FastAPI** e **Swagger**, ele precisa refletir essa maturidade técnica. Vamos adicionar a parte do **LuizaLabs**, as instruções de como rodar o servidor e a tabela de endpoints.

Aqui está o código Markdown atualizado para você copiar e colar no seu `README.md`:

```markdown
# 💳 Gateway de Pagamento em Python | LuizaLabs Project

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Uvicorn](https://img.shields.io/badge/uvicorn-20232A?style=for-the-badge&logo=python&logoColor=white)

Este projeto simula um **Gateway de Pagamento** de alto desempenho, desenvolvido com foco em Engenharia de Software. Ele segue os padrões de arquitetura discutidos no programa da **LuizaLabs**, utilizando FastAPI para garantir velocidade e escalabilidade no processamento de transações.

## 🚀 Funcionalidades

- [x] **Processamento Assíncrono:** Utilização de `async/await` para alta performance.
- [x] **Validação com Pydantic:** Tipagem forte para garantir que apenas dados válidos sejam processados.
- [x] **Geração de UUID:** Cada transação recebe um ID único universal para rastreabilidade.
- [x] **Histórico em Memória:** Endpoint dedicado para auditoria de todas as transações realizadas.
- [ ] **Persistência em Banco de Dados:** Migração planejada para SQLite/PostgreSQL.
- [ ] **Segurança:** Implementação de API Key para proteção de dados sensíveis.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.14+
- **Framework:** FastAPI
- **Servidor ASGI:** Uvicorn
- **Validação:** Pydantic

## 📂 Endpoints Principais

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `POST` | `/processar` | Processa um novo pagamento e gera ID de transação. |
| `GET` | `/historico` | Retorna a lista completa de transações realizadas. |
| `GET` | `/transacao/{id}` | Busca os detalhes de uma transação específica por ID. |

## ⚙️ Como executar o projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/MarcosSoftwareEngineering/python-payment-gateway.git](https://github.com/MarcosSoftwareEngineering/python-payment-gateway.git)
   cd python-payment-gateway

```

2. **Ative o ambiente virtual:**
```bash
# Windows
.\venv\Scripts\activate

```


3. **Inicie o servidor:**
```bash
uvicorn main:app --reload

```


4. **Acesse a documentação interativa:**
Vá para [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs) para testar os endpoints via Swagger UI.

---

Desenvolvido por **Marcos Vinicius** - [MarcosSoftwareEngineering](https://marcos-dev-zeta.vercel.app/))

```

### O que mudou:
1. **Badges:** Adicionei os selos de **FastAPI** e **Uvicorn** para mostrar o stack moderno.
2. **Contexto:** Adicionei a menção ao **LuizaLabs**, o que valoriza muito o seu aprendizado.
3. **Tabela de Endpoints:** Deixa claro para quem ler o que a sua API faz sem precisar ler o código.
4. **Instruções de Execução:** Agora inclui o comando do `uvicorn` e o link do Swagger.

Deseja que eu te ajude a dar o `git commit` final nesse README para fecharmos o dia?

```
