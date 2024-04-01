from fastapi import APIRouter


route = APIRouter()

@route.get('/a1')
def a1():
    return {'this is' : 'a1'}