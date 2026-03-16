from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API do Gateway de Pagamento rodando com sucesso!"}