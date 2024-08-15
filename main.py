from config import HOST, PORT
from app import app

import uvicorn

def main()-> None:
    try:
        uvicorn.run("main:app", host=HOST, port=PORT) # Starting Uvicorn and FastAPI
    except FileNotFoundError: # to prevent error on removing unix sock
        pass    

if __name__ == "__main__":
    main()