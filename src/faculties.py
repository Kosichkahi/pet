from fastapi import HTTPException
from starlette import status

from database import models as db_models


async def get_faculty_by_id(faculty_id: int) -> db_models.Faculty:
    faculty_obj = await db_models.Faculty.get_or_none(id=faculty_id)
    if faculty_obj is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Unknown faculty with id={faculty_id}'
        )
    return faculty_obj
