from pydantic import BaseModel
from typing import Optional
import pymysql
from Config.connection import connection

class Group(BaseModel):
    Id:int
    Password:str
    GroupId:int
    GroupName:str



def create_group_table():
    conn = connection()
    cursorObject  = conn.cursor()
    sqlQuery = '''CREATE TABLE IF NOT EXISTS MoviesGroup(GroupId INT UNIQUE NOT NULL,GroupName VARCHAR(20) UNIQUE NOT NULL,OwnerId INT UNIQUE NOT NULL,MemberId varchar(255) UNIQUE ,check(GroupId >= 1 and GroupId <= 11))'''
    cursorObject.execute(sqlQuery)