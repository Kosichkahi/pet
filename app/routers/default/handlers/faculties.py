from fastapi import APIRouter

from app.routers.default import models
from database import models as db_models

router = APIRouter(prefix='/faculties')


@router.post('', response_model=models.CreationResponse)
async def create_faculty(payload: models.FacultyInfoIn) -> models.CreationResponse:
    faculty_obj = await db_models.Faculty.create(name=payload.name)
    return models.CreationResponse(id=faculty_obj.id)
