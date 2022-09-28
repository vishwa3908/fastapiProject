from pydantic import BaseModel
from typing import Optional
import pymysql
from Config.connection import connection

class Member(BaseModel):
    Id:int
    Password:str
    GroupId:int
    MemberId:int

