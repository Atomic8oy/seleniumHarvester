from fastapi import FastAPI, HTTPException
from json import loads, dumps

from app.tsetmc import get_stock_history
from config import SAVE_OUTPUT

__version__ = "0.2.0" # Software version

# Initializing FastAPI
app = FastAPI(
    title="Untitled",
    version=__version__,
    docs_url='/docs',
    redoc_url='/redoc'
)

# Initializing a GET API in /history
@app.get("/history")
def get_history(keyword:str)-> dict:
    # Checking if keyword is valid
    passed = True
    for x in range(len(keyword)):
        if x < 17:
            if keyword[x] not in "0123456789":
                passed = False
                break
        elif x == 17:
            if keyword[x] != "/":
                passed = False
                break
        elif x > 17:
            if keyword[x] not in "0123456789":
                passed = False
                break

    if len(keyword) != 26:
        passed = False
    
    if passed:
        try:
            # If the file already exists in history folder just return it otherwise scarping the data
            file = open("history/" + keyword.replace("/", "") + ".json", 'r')
            data = loads(file.read())
            file.close()
        except FileNotFoundError:    
            data = get_stock_history(keyword) # Scraping data and returning it to the user
            
            if not data:
                raise HTTPException(404)

            if SAVE_OUTPUT:
                file = open("history/" + keyword.replace("/", "") + ".json", 'w')
                file.write(dumps(data))
                file.close()
        
        return {"history": data}
    else:
        raise HTTPException(400, "Invalid keyword")