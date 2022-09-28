from fastapi import APIRouter
from Models.member import Member
from Config.connection import connection
from typing import Optional
router = APIRouter()




@router.post("/login/group/addmember")
async def add_member(data:Member):
    conn = connection()
    cursorObject = conn.cursor()
    # first checking if the user exists in the database or not
    check_owner_exists_sqlQuery = '''SELECT * FROM users WHERE Id = %s AND Password = %s'''
    check_owner_exists_values = (data.Id,data.Password)
    cursorObject.execute(check_owner_exists_sqlQuery,check_owner_exists_values)
    check_owner_exists_result =  cursorObject.fetchall()
    if check_owner_exists_result:
        
        # check if the group  with given group id  exists
        check_group_exists_sql_query = '''SELECT * FROM MoviesGroup WHERE GroupId = %s'''
        check_group_exists_value = (data.GroupId)
        cursorObject.execute(check_group_exists_sql_query,check_group_exists_value)
        check_group_exists_result = cursorObject.fetchall()
        if check_group_exists_result:
            # if member is already present inside the group
                # check if member present or not 
                check_member_present_sql_query = '''SELECT MemberId FROM MoviesGroup WHERE GroupId = %s'''
                check_member_present_value = (data.GroupId)
                cursorObject.execute(check_member_present_sql_query,check_member_present_value)
                check_member_present_result = cursorObject.fetchall()
                if check_member_present_result:

                    # you have to concat the member id
                    # first extract all the member id
                    member_already = check_member_present_result[0][0] 
                    # updating MoviesGroup table
                    adding_member_sql_query = '''UPDATE MoviesGroup SET MemberId = CONCAT(%s,",",%s) WHERE GroupId = %s'''
                    adding_member_value = (member_already,data.MemberId,data.GroupId)
                    cursorObject.execute(adding_member_sql_query,adding_member_value)
                    conn.commit()
                    return f"Member {data.MemberId} added "

                else:

                    # if member not present inside the group
                    # add the member into the group
                    add_new_member_sql_query = '''UPDATE MoviesGroup SET MemberId = %s WHERE GroupId = %s'''
                    add_new_member_value = (data.MemberId,data.GroupId)
                    cursorObject.execute(add_new_member_sql_query,add_new_member_value)
                    conn.commit()
                    return "Member Added"

        else:
            return  "Group not found create group first"

    else:
        return "no record found of the user"