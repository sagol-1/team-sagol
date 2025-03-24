from fastapi import FastAPI
from controllers.validation_controller import validation_router
import ssl

app = FastAPI()


@app.get("/")
def read_root() -> str:
    return "This is a proxy server!"

app.include_router(validation_router, prefix="/validate", tags=["Validation"])