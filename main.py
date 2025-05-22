from fastapi import FastAPI
from routes.routes import router
from DbConfig.db import client
app=FastAPI()


app.include_router(router)



from fastapi.staticfiles import StaticFiles
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


@app.on_event("startup")
async def connect_to_db():
    try:
        await client.admin.command("ping")
        print(" Database connected successfully")
    except Exception as e:
        print(f" Database connection failed: {e}")
