from typing import List, Optional, Union

from fastapi import APIRouter, Path, HTTPException, Depends, Query
from starlette import status

from app.routers.default import models
from database import models as db_models

router = APIRouter(prefix='/students')


@router.get('', response_model=List[models.StudentInfo])
async def get_students(
    first_name: Optional[str] = Query(default=None),
    last_name: Optional[str] = Query(default=None),
    specialization_ids: Optional[List[int]] = Query(default=None)
) -> List[models.StudentInfo]:
    student_objs = await filter_students(
        query_params=models.StudentQueryParams(
            first_name=first_name,
            last_name=last_name,
            specialization_ids=specialization_ids
        )
    )

    return [
        models.StudentInfo(
            first_name=student.first_name,
            last_name=student.last_name,
            faculty=student.faculty.name,
            group_info=models.GroupInfo(specialization=student.specialization.name, number=student.group_number)
        )
        for student in student_objs
    ]


@router.post('', response_model=models.CreationResponse)
async def create_student(payload: models.CreateStudentInfo) -> models.CreationResponse:
    faculty_obj = await get_faculty_by_id(faculty_id=payload.faculty_id)
    specialization_obj = await get_specialization_by_id(specialization_id=payload.specialization_id)
    student_obj = await db_models.Student.create(
        first_name=payload.first_name,
        last_name=payload.last_name,
        faculty=faculty_obj,
        specialization=specialization_obj,
        group_number=payload.group_number
    )
    return models.CreationResponse(id=student_obj.id)


@router.put('/{studentId}', response_model=models.MessageResponse)
async def update_student(
        payload: models.UpdateStudentInfo,
        student_id: int = Path(..., alias='studentId')
) -> models.MessageResponse:
    student_obj = await get_student_by_id(student_id=student_id)
    await student_obj.update_from_dict(data=payload.dict(exclude_none=True))
    await student_obj.save()
    return models.MessageResponse()


@router.delete('/{studentId}', response_model=models.MessageResponse)
async def delete_student(student_id: int = Path(..., alias='studentId')) -> models.MessageResponse:
    student_obj = await get_student_by_id(student_id=student_id)
    await student_obj.delete()
    return models.MessageResponse()


async def get_faculty_by_id(faculty_id: int) -> db_models.Faculty:
    faculty_obj = await db_models.Faculty.get_or_none(id=faculty_id)
    if faculty_obj is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Unknown faculty with id={faculty_id}'
        )
    return faculty_obj


async def get_specialization_by_id(specialization_id: int) -> db_models.Specialization:
    specialization_obj = await db_models.Specialization.get_or_none(id=specialization_id)
    if specialization_obj is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Unknown specialization with id={specialization_id}'
        )
    return specialization_obj


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
