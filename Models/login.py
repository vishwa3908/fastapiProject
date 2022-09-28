from pydantic import BaseModel
from typing import Optional
import pymysql
from Config.connection import connection

class Login(BaseModel):
    Id:int
    Password:str



