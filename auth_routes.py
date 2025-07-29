from fastapi import APIRouter, Depends
from models import Usuario
from depedendencies import pegar_sessao

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação do nosso sistema.
    """
    return {"mensagem": "voce acessou a rota padrão de autenticacao", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()

    if usuario:
        # ja existe um usuario com esse email
        return {"ja existe um usuario com esse email"}
    
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "usuaurio cadastrado com sucesso"}
        
    

    