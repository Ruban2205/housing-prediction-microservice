from typing import List
from fastapi import FastAPI
from utils.model import infer

server = FastAPI()

@server.get("/")
async def root():
    '''
    To check if the server is live
    '''
    return {"message": "The server is live!"}

@server.get("/inference")
async def read_item(area: int, bedrooms: int, \
        bathrooms: int, stories: int, mainroad: str, \
        guestroom: str, basement: str, hotwaterheating: str, \
        airconditioning: str, parking: int, prefarea: str, \
        semi_furnished: str, unfurnished: str):
    '''
    To predict the price of a house
    '''
    user_input : List = [area, bedrooms, bathrooms, stories, mainroad, \
            guestroom, basement, hotwaterheating, airconditioning, \
            parking, prefarea, semi_furnished, unfurnished]

    pred : float = infer(user_input, 'train/models/regression.pkl', 'train/models/processor.pkl')
    return {"result": pred}

# http://127.0.0.1:8000/inference/?area=600&bedrooms=4&bathrooms=1&stories=2&mainroad=yes&guestroom=no&basement=yes&hotwaterheating=no&airconditioning=no&parking=2&prefarea=no&semi_furnished=1&unfurnished=0

# curl -X 'GET' \
#     'http://127.0.0.1:8000/inference?area=600&bedrooms=3&bathrooms=2&stories=3&mainroad=no&guestroom=yes&basement=no&hotwaterheating=yes&airconditioning=no&parking=3&prefarea=no&semi_furnished=1&unfurnished=0' \
#     -H 'accept: application/json'
