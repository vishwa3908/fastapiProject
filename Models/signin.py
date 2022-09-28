from pydantic import BaseModel
from typing import Optional
import pymysql
from Config.connection import connection

class Signin(BaseModel):
    Name:str
    Id:int
    Age:int
    Gender:Optional[str]=None
    Email:Optional[str]=None
    Phone:Optional[str]=None
    Password:str


def create_users_table():
    conn = connection()
    cursorObject = conn.cursor()
    sqlQuery = '''CREATE TABLE IF NOT EXISTS users(Name VARCHAR(25) NOT NULL,Id INT UNIQUE NOT NULL,Age INT NOT NULL,Gender Varchar(9),Email VARCHAR(30) UNIQUE,Phone VARCHAR(20) UNIQUE,Password VARCHAR(40) NOT NULL,CHECK (Gender in('Male','M','Female','F')),check(Id >= 100 and Id <= 5000))'''
    cursorObject.execute(sqlQuery)


