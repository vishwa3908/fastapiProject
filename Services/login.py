from fastapi import APIRouter
from Models.login import Login
from Config.connection import connection
from typing import Optional
router = APIRouter()




@router.post("/login")
async def login(login_Data:Login,Id:Optional[int]=None,Password:Optional[str]=None):
    
    # check if user exists in the users table

    conn = connection()
    cursorObject = conn.cursor()
    sqlQuery = '''SELECT * FROM users WHERE Id = %s AND Password = %s'''
    values = (login_Data.Id,login_Data.Password)
    cursorObject.execute(sqlQuery,values)
    result =  cursorObject.fetchall()
    if result:
        result_data = {
            "Name":result[0][0],
            "Id":result[0][1],
            "Age":result[0][2],
            "Gender":result[0][3],
            "Email":result[0][4],
            "Phone":result[0][5]
        }
        return result_data
    else:
        return "record not found check credentials"
