from fastapi import APIRouter

router = APIRouter()


@router.get('/random_meme')
def random_meme(country: str = 'en'):
    if country == 'ko':
        
        return {'korean':'meme'}
    else:
        return {'english' : 'meme'}