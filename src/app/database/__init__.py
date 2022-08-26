import uvicorn

from fastapi import FastAPI
from core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME, 
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    openapi_tags=settings.TAGS_METADATA
)

app.add_middleware(CORSMiddleware, allow_origins=['*'], aloow_credentials=True,
        allow_methods=['*'], allow_headers=['*'])


if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.HOST, port=settings.PORT,
            debug=settings.DEBUG, reload=settings.DEBUG)

