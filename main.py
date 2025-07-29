from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from routes import router

app.include_router(auth_router)
app.include_router(router)


#executar no terminal para deixar online nosso server uvicorn main:app --reload 