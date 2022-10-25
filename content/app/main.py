"""
Author: Ammar Saqib
"""
# pylint: disable=E0611
from fastapi import FastAPI
from routes import test


# Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(test.router)
