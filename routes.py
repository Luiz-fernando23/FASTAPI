from fastapi import APIRouter 

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do nosso sistema. Todas as rotas dos pedidos precisam de autenticao
    """
    return {"mensagem": "Voce acessou a rota de pedidos"}