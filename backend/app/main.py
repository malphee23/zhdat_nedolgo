from fastapi import FastAPI

app = FastAPI(title="Ждать недолго API")


@app.get("/")
def root():
    return {"message": "Сервис доставки работает"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    return {
        "order_id": order_id,
        "status": "создан",
        "delivery_service": "Ждать недолго"
    }