from fastapi import FastAPI
from app.routers import item_router, build_router

app = FastAPI(
    title="Path of Exile Build Parser",
    description="Приложение для парсинга предметов из XML и возврата их в формате NDJSON.",
    version="1.0.0"
)

# Подключение маршрутов
app.include_router(item_router.router, prefix="/api")
app.include_router(build_router.router, prefix="/build")

# Опциональные настройки для проверки состояния сервера
@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
