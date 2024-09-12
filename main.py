from fastapi import FastAPI
from app.views import item_view, build_view

app = FastAPI()

# Подключаем роуты
app.include_router(item_view.router)
app.include_router(build_view.router)