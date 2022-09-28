from fastapi import FastAPI
from Services import signin
from Services import login
from Services import group
from Services import member
app = FastAPI()


app.include_router(signin.router)
app.include_router(login.router)
app.include_router(group.router)
app.include_router(member.router)

@app.get("/")
def home():
    return 'WELCOME TO MOVIEDUNIA'