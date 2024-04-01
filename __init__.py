from fastapi import FastAPI

from backend.apiv1 import route
import uvicorn

app = FastAPI()

app.include_router(route, prefix='/apiv1')

@app.get('/')
def index():
    return {'hello' : 'worlds'}

if __name__ == '__main__':
    
    uvicorn.run("__main__:app", host='0.0.0.0', reload=True)