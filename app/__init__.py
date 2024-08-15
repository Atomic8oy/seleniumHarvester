from fastapi import FastAPI

from app.tsetmc import get_stock_history

__version__ = "0.2.0"

app = FastAPI(
    title="Untitled",
    version=__version__,
    docs_url='/docs',
    redoc_url='/redoc'
)

@app.get("/history")
def get_history(keyword:str)-> dict[list]:
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
        return {"history": get_stock_history(keyword)}