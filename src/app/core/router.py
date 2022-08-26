import os 

from importlib import import_module
from typing import List
from fastapi import APIRouter

from core.config import settings


def collect_api(module_prefix: str, endpoint_path: str, target_router: APIRouter,
        path_prefix: List[str] = [], exclude: List[str] = ['__pycache__', '__init__.py']):
    """현재 위치의 하위 경로에 포함된 모든 API 수집"""

    endpoints = os.listdir(endpoint_path)

    for endpoint in endpoints:
        if endpoint in exclude: continue

        target_path = os.path.join(endpoint_path, endpoint)

        if os.path.isfile(target_path):
            name, ext = os.path.splitext(endpoint)
            relative_path = "/".join(path_prefix + [name]).replace('_', '-')
            endpoint_module = import_module(f'{module_prefix}.{name}')
            sub_router = getattr(endpoint_module, 'router')
            docstr = getattr(endpoint_module, '__doc__')
            target_router.include_router(sub_router,prefix=f'/{relative_path}',
                    tags=[relative_path])

            settings.TAGS_METADATA.append({'name': relative_path, 'description': docstr})

        elif os.path.isdir(target_path):
            collect_api(f'{module_prefix}.{endpoint}', os.path.join(endpoint_path, endpoint),
                    target_router, path_prefix=path_prefix + [endpoint], exclude=exclude)


    