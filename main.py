from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uuid
import sqlite3
import json

app = FastAPI(title="Payment Gateway API | Marvin Site Builders")

# --- CONFIGURAÇÃO DO BANCO DE DADOS (SQLite) ---
def init_db():
    """Cria o arquivo do banco de dados e a tabela se não existirem."""
    conn = sqlite3.connect("pagamentos.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id TEXT PRIMARY KEY,
            method TEXT,
            amount REAL,
            customer_email TEXT,
            gateway_info TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Roda a função para garantir que o banco existe quando o app iniciar
init_db()

# --- MODELOS DE DADOS (Pydantic) ---
class CustomerInput(BaseModel):
    name: str
    email: str
    cpf: str

class PaymentRequest(BaseModel):
    amount: float
    payment_method: str  # 'pix', 'credit_card', 'boleto'
    customer: CustomerInput
    card_token: Optional[str] = None

# --- FUNÇÕES SIMULADAS (MOCKS) DO ABACATEPAY ---
def process_abacatepay_pix(amount, customer):
    return {
        "status": "pending",
        "qr_code": "00020126580014br.gov.bcb.pix0136mock-uuid-aqui...",
        "qr_code_url": "https://abacatepay.mock/pix/qrcode.png"
    }

def process_abacatepay_card(amount, customer, card_token):
    if not card_token:
        raise ValueError("Token do cartão é obrigatório.")
    return {"status": "approved", "receipt_url": "https://abacatepay.mock/receipt/123"}

def process_abacatepay_boleto(amount, customer):
    return {
        "status": "pending",
        "barcode": "34191.09008 63571.277308 71444.640008 5 90000000000000",
        "pdf_url": "https://abacatepay.mock/boleto/123.pdf"
    }

# --- ENDPOINTS (ROTAS) ---

@app.get("/")
async def root():
    return {"message": "Gateway de Pagamento Online Operacional com Banco de Dados"}

@app.post("/api/v1/checkout", tags=["Pagamentos"])
async def process_checkout(request: PaymentRequest):
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="Valor inválido")

    transaction_id = str(uuid.uuid4())
    
    try:
        # 1. Processa no Gateway (Mock)
        if request.payment_method == "pix":
            gateway_response = process_abacatepay_pix(request.amount, request.customer)
        elif request.payment_method == "credit_card":
            gateway_response = process_abacatepay_card(request.amount, request.customer, request.card_token)
        elif request.payment_method == "boleto":
            gateway_response = process_abacatepay_boleto(request.amount, request.customer)
        else:
            raise HTTPException(status_code=400, detail="Método de pagamento inválido.")

        # 2. Salva no Banco de Dados SQLite
        conn = sqlite3.connect("pagamentos.db")
        cursor = conn.cursor()
        
        # Como o gateway_info é um dicionário, convertemos para texto (JSON) para salvar no banco
        gateway_info_str = json.dumps(gateway_response)
        
        cursor.execute('''
            INSERT INTO transactions (transaction_id, method, amount, customer_email, gateway_info)
            VALUES (?, ?, ?, ?, ?)
        ''', (transaction_id, request.payment_method, request.amount, request.customer.email, gateway_info_str))
        
        conn.commit()
        conn.close()

        # 3. Retorna a resposta para o usuário
        return {
            "status": "sucesso", 
            "dados": {
                "transaction_id": transaction_id,
                "method": request.payment_method,
                "amount": request.amount,
                "customer_email": request.customer.email,
                "gateway_info": gateway_response
            }
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Erro: {e}") # Imprime o erro no terminal para ajudar a debugar
        raise HTTPException(status_code=500, detail="Erro interno ao processar pagamento.")

@app.get("/api/v1/transactions", tags=["Consultas"])
async def get_transactions():
    """Retorna todas as transações salvas no banco de dados."""
    conn = sqlite3.connect("pagamentos.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    
    # Formatando os dados para ficarem bonitos no JSON
    transactions = []
    for row in rows:
        transactions.append({
            "transaction_id": row[0],
            "method": row[1],
            "amount": row[2],
            "customer_email": row[3],
            "gateway_info": json.loads(row[4]) # Transforma o texto de volta em Dicionário
        })
        
    return {"total": len(transactions), "transactions": transactions}

@app.get("/api/v1/transactions/{transaction_id}", tags=["Consultas"])
async def buscar_transacao_por_id(transaction_id: str):
    """Busca uma transação específica pelo ID no banco de dados."""
    conn = sqlite3.connect("pagamentos.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM transactions WHERE transaction_id = ?", (transaction_id,))
    row = cursor.fetchone() # Pega apenas um resultado
    conn.close()
    
    if row:
        dados = {
            "transaction_id": row[0],
            "method": row[1],
            "amount": row[2],
            "customer_email": row[3],
            "gateway_info": json.loads(row[4])
        }
        return {"status": "encontrado", "dados": dados}
    
    raise HTTPException(status_code=404, detail="Transação não encontrada")