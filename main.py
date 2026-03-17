from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uuid

app = FastAPI(title="Payment Gateway API | LuizaLabs")

# "Banco de dados" em memória (uma lista simples)
db_transacoes = []

class Pagamento(BaseModel):
    cliente_id: int
    valor: float
    metodo: str 
    descricao: Optional[str] = "Sem descrição"

@app.get("/")
async def root():
    return {"message": "Gateway de Pagamento Online"}

@app.post("/processar")
async def processar_pagamento(pagamento: Pagamento):
    if pagamento.valor <= 0:
        raise HTTPException(status_code=400, detail="Valor inválido")
    
    transacao_id = str(uuid.uuid4())
    
    # Criando o objeto completo para salvar no nosso "banco"
    nova_transacao = {
        "transacao_id": transacao_id,
        "cliente_id": pagamento.cliente_id,
        "valor": pagamento.valor,
        "metodo": pagamento.metodo,
        "confirmacao": "Pagamento aprovado pelo LuizaLabs"
    }
    
    db_transacoes.append(nova_transacao) # Salvando...
    
    return {"status": "sucesso", "dados": nova_transacao}

# --- NOVO ENDPOINT DE ALTO NÍVEL ---
@app.get("/historico", tags=["Consultas"])
async def listar_transacoes():
    """Retorna todas as transações processadas desde que o servidor subiu."""
    return {
        "total_processado": len(db_transacoes),
        "transacoes": db_transacoes
    }

    # --- BUSCA POR ID ESPECÍFICO ---
@app.get("/transacao/{id_procurado}", tags=["Consultas"])
async def buscar_transacao_por_id(id_procurado: str):
    """
    Busca uma transação específica no banco de dados usando o ID.
    """
    for t in db_transacoes:
        if t["transacao_id"] == id_procurado:
            return {"status": "encontrado", "dados": t}
    
    # Se percorrer tudo e não achar:
    raise HTTPException(status_code=404, detail="Transação não encontrada")