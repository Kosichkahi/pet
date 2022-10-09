from fastapi import APIRouter

from app.routers.default import models
from database import models as db_models

router = APIRouter(prefix='/specializations')


@router.post('', response_model=models.CreationResponse)
async def create_faculty(payload: models.SpecializationInfoIn) -> models.CreationResponse:
    specialization_obj = await db_models.Specialization.create(name=payload.name)
    return models.CreationResponse(id=specialization_obj.id)
