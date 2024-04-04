from fastapi import FastAPI

import uvicorn

from controller.meme import router

app = FastAPI(root_path='/api/v1')

app.include_router(router=router, prefix='/meme')

@app.get('/')
def index():
    return {'hello' : 'world'}

if __name__ == '__main__':
    
    uvicorn.run("__main__:app", host='127.0.0.1', port=5051, reload=True)