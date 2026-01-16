from fastapi import FastAPI
from database import Base, engine
from routes import router

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(router)