from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Cloud Incident Replay Simulator")

app.include_router(router)
