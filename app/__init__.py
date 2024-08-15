from fastapi import FastAPI, HTTPException

from app.tsetmc import get_stock_history

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
        return {"history": get_stock_history(keyword)} # Scraping data and returning it to the user
    else:
        raise HTTPException(400, "Invalid keyword")