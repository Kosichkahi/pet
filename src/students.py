from typing import List

from fastapi import HTTPException
from starlette import status

from app.routers.default import models
from database import models as db_models


async def get_student_by_id(student_id: int) -> db_models.Student:
    student_obj = await db_models.Student.get_or_none(id=student_id)
    if student_obj is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Unknown student with id={student_id}'
        )
    return student_obj


async def filter_students(query_params: models.StudentQueryParams) -> List[db_models.Student]:
    query = db_models.Student.filter()
    if query_params.first_name is not None:
        query = query.filter(first_name=query_params.first_name)
    if query_params.last_name is not None:
        query = query.filter(last_name=query_params.last_name)
    if query_params.specialization_ids:
        query = query.filter(specialization__id__in=query_params.specialization_ids)
    return await query.prefetch_related('faculty', 'specialization')
