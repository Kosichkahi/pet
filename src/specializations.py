from fastapi import HTTPException
from starlette import status

from database import models as db_models


async def get_specialization_by_id(specialization_id: int) -> db_models.Specialization:
    specialization_obj = await db_models.Specialization.get_or_none(id=specialization_id)
    if specialization_obj is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Unknown specialization with id={specialization_id}'
        )
    return specialization_obj
