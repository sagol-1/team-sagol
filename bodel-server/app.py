from fastapi import FastAPI, Request, Response, status
from controllers.validation_controller import validation_router
import ssl

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    with open('whitelist.txt', 'r') as whitelist_file:
        whitelist = whitelist_file.readlines()

        
    if request.client.host in whitelist:
        response = await call_next(request)
            
        return response

    return Response(status_code=status.HTTP_403_FORBIDDEN)

@app.get("/")
def read_root() -> str:
    return "This is a proxy server!"

app.include_router(validation_router, prefix="/validate", tags=["Validation"])