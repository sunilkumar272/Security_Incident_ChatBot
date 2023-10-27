# -*- coding: utf-8 -*-
"""

@author: SUNIL

Test your FastAPI connection in the browser

"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
