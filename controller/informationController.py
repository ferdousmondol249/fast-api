from fastapi import UploadFile, File, Form, HTTPException
from model.information import person
from DbConfig.db import person_collection
import shutil, os

async def create_person(
    name: str = Form(...),
    age: float = Form(...),
    image: UploadFile = File(...)
):
    try:
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)
        image_path = f"{upload_dir}/{image.filename}"

        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        person_data = {
            "name": name,
            "age": age,
            "image": image_path
        }

        result = await person_collection.insert_one(person_data)
        person_data["_id"] = str(result.inserted_id)  # fix here

        return {
            "message": "Person created successfully",
            "data": person_data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
