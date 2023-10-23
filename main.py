import io
import os
import uvicorn
import numpy as np
import nest_asyncio
from enum import Enum
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from lib.engine import app
import cv2

def cv_version(name=cv2.__version__):
    banku=f"({name})"
    return banku

# Allows the server to be run in this interactive environment
nest_asyncio.apply()

# Host depends on the setup you selected (docker or virtual env)
host = "0.0.0.0" if os.getenv("DOCKER-SETUP") else "127.0.0.1"

if __name__=="__main__":
# Spin up the server!    
    uvicorn.run(app, host=host, port=8000)