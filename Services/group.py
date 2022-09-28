from fastapi import APIRouter
from Models.group import Group,create_group_table
from Config.connection import connection
from typing import Optional
router = APIRouter()




@router.post("/login/creategroup")
async def create_group(group_data :Group):
    create_group_table()
    conn = connection()
    cursorObject = conn.cursor()

    # first checking the user exists in database or not
    user_check_value = (group_data.Id,group_data.Password)
    user_check_sql_query = '''SELECT * FROM users WHERE Id = %s AND Password = %s'''
    cursorObject.execute(user_check_sql_query,user_check_value)
    user_check_result = cursorObject.fetchall()
    if user_check_result:
        # updating the group database
        group_sql_query = '''INSERT IGNORE INTO MoviesGroup(GroupId,GroupName,OwnerId)Values(%s,%s,%s)'''
        group_sql_value = (group_data.GroupId,group_data.GroupName,group_data.Id)
        cursorObject.execute(group_sql_query,group_sql_value)
        conn.commit()
        return f"Group Name {group_data.GroupName} with Group Id {group_data.GroupId} Created"
    else:
        return "Invalid User Credentials"