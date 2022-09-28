from fastapi import APIRouter
from Models.signin import Signin
from Models.signin import create_users_table
from Config.connection import connection
router = APIRouter()




@router.post("/signin")
async def signin(data:Signin):
    create_users_table()

    # inserting user data in users table  BUT first checking the criteria of table 
    if (data.Id < 100 or data.Id > 5000):
        return 'Id must be between 100 and 5000'
    else:
        conn = connection()
        cursorObject = conn.cursor()
        sqlQuery = '''INSERT IGNORE INTO users(Name,Id,Age,Gender,Email,Phone,Password)Values(%s,%s,%s,%s,%s,%s,%s)'''
        values = (data.Name,data.Id,data.Age,data.Gender,data.Email,data.Phone,data.Password)
        cursorObject.execute(sqlQuery,values)
        conn.commit()
        return f"Name{data.Name},Age{data.Age}"