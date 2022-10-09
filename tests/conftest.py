from typing import Generator

import pytest
from httpx import AsyncClient
from tortoise.contrib.test import finalizer, initializer, _restore_default

from app.app import get_application


@pytest.fixture()
def _database() -> Generator:
    initializer(['database.models'])
    _restore_default()
    try:
        yield
    finally:
        finalizer()


@pytest.fixture()
async def _async_client() -> Generator:
    async with AsyncClient(app=get_application(), base_url='http://test') as client:
        yield client
