from fastapi import FastAPI
from routers.router import MyRouter

app = FastAPI()
app.include_router(MyRouter)



