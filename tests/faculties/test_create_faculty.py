import pytest
from httpx import AsyncClient
from starlette import status
from tortoise.exceptions import IntegrityError

from app.routers.default.models import FacultyInfoIn, Faculty
from database import models as db_models


@pytest.mark.usefixtures('_database')
class TestCreateFaculty:
    """Проверка создания нового факультета"""

    URL = '/faculties'

    @pytest.mark.asyncio
    async def test_create_faculty__success(self, _async_client: AsyncClient):
        """Успешное создание нового факультета"""
        response = await _async_client.post(self.URL, data=FacultyInfoIn(name=Faculty.MATH).json())
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.asyncio
    async def test_create_faculty__unique_name(self, _async_client: AsyncClient):
        """
        Попытка создания факультета с именем, которое уже занято
        Ожидается:
            соответствующая ошибка
        """

        faculty_name = Faculty.MATH

        await db_models.Faculty.create(name=faculty_name)

        with pytest.raises(IntegrityError):
            await _async_client.post(self.URL, data=FacultyInfoIn(name=Faculty.MATH).json())
