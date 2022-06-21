from fastapi import FastAPI, Depends
import models
from database import engine
from routers import auth, todos, users, address, todosfullstack, authfullstack
from company import companyapis, dependencies
from starlette.staticfiles import StaticFiles

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
app.include_router(address.router)
app.include_router(todosfullstack.router)
app.include_router(authfullstack.router)
app.include_router(
    companyapis.router,
    prefix="/companyapis",
    tags=["companyapis"],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={
        418: {
            "description": "Internal use only"
        }
    }
)
