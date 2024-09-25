import uvicorn
from fastapi import FastAPI

from supermarket_service.routers.router import router

app=FastAPI()

app.include_router(router)

def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()