from fastapi import FastAPI, File, UploadFile
from api.endpoints import processing_images
from utils.save_image_temporal import save_in_disk
from app import mostrar_sena
import tkinter as tk
from tkinter import *
from tkinter import ttk

from io import BytesIO
import os


app = FastAPI()

@app.post("/processing_images")
async def call_processing_images(image: UploadFile = File(...)): #se recibe la imagen
    image_bytes  = await image.read() #se almacena temporalmente
    image_path = save_in_disk(image_bytes)
    result = await processing_images.processing_images(image_path)
    return result

@app.get("/")
async def root():
    return {"message": "👋🌎"}