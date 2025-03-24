from fastapi import FastAPI
from controllers.validation_controller import validation_router
import ssl

app = FastAPI()
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile='certificates\cert.pem', keyfile='certificates\key.pem')


@app.get("/")
def read_root():
    return "This is a proxy server!"

app.include_router(validation_router, prefix="/validate", tags=["Validation"])