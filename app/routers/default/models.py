from dataclasses import dataclass
from enum import Enum
from typing import Optional, List
from uuid import UUID

from fastapi import Query
from pydantic import BaseModel


class Faculty(Enum):
    MATH = 'math'
    PHILOSOPHY = 'philosophy'


class GroupInfo(BaseModel):
    specialization: str
    number: int


class Person(BaseModel):
    first_name: str
    last_name: str


@dataclass
class StudentQueryParams:
    first_name: Optional[str] = Query(default=None)
    last_name: Optional[str] = Query(default=None)
    specialization_ids: Optional[List[str]] = Query(default=list)


class CreateStudentInfo(Person):
    faculty_id: UUID
    specialization_id: UUID
    group_number: int


class UpdateStudentInfo(Person):
    first_name: Optional[str]
    last_name: Optional[str]
    faculty_id: Optional[UUID]
    specialization_id: Optional[UUID]
    group_number: Optional[int]


class StudentInfo(Person):
    faculty: Faculty
    group_info: GroupInfo


class FacultyInfoIn(BaseModel):
    name: Faculty


class SpecializationInfoIn(BaseModel):
    name: str


class CreationResponse(BaseModel):
    id: UUID


class MessageResponse(BaseModel):
    message: str = 'ok'
