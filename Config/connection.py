from Constants import constants
import pymysql
def connection():
    conn = pymysql.connect(
        host=constants.host,
        user=constants.user,
        password=constants.password,
        database=constants.database
    )
    return conn