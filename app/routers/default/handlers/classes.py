from typing import List

from fastapi import APIRouter

from app.routers.default import models

router = APIRouter(prefix='/students')


@router.get('', response_model=List[models.StudentInfo])
async def get_students() -> List[models.StudentInfo]:
    return []
