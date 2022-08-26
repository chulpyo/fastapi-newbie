import os
from fastapi import APIRouter
from core.router import collect_api

api_router = APIRouter()
collect_api('api.v1.endpoints',
    os.path.join(os.path.dirname(__file__), 'endpoints'), api_router)
