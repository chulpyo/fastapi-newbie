import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from api.v1.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME, 
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    openapi_tags=settings.TAGS_METADATA
)

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True,
        allow_methods=['*'], allow_headers=['*'])

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.HOST, port=settings.PORT,
            debug=settings.DEBUG, reload=settings.DEBUG)

