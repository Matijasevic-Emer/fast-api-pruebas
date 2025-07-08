import jwt
import os
from dotenv import load_dotenv

load_dotenv()  # carga variables del .env
secret = os.getenv("SECRET_KEY", "default_secret")

def createToken(data: dict) -> str:
    token: str = jwt.encode(
        payload=data,
        key=secret,
        algorithm='HS256'
    )
    return token

def validateToken(token: str) -> dict:
    data : dict = jwt.decode(token,key=secret,algorithm='HS256' )
    return data