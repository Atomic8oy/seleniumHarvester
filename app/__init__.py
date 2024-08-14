from fastapi import FastAPI

__version__ = "0.2.0"

app = FastAPI(
    title="Untitled",
    version=__version__,
    docs_url='/docs',
    redoc_url='/redoc'
)

@app.get("/")
def get_root()-> dict:
    return {'message': 'The shits working; YIPEEEEE'}