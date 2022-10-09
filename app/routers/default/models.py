from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, Field


class Faculty(Enum):
    MATH = 'math'
    PHILOSOPHY = 'philosophy'


class GroupInfo(BaseModel):
    specialization: str
    number: int


class Person(BaseModel):
    first_name: str
    last_name: str


class StudentQueryParams(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    specialization_ids: Optional[List[int]] = Field(default_factory=list)


class CreateStudentInfo(Person):
    faculty_id: int
    specialization_id: int
    group_number: int


class UpdateStudentInfo(Person):
    first_name: Optional[str]
    last_name: Optional[str]
    faculty_id: Optional[int]
    specialization_id: Optional[int]
    group_number: Optional[int]


class StudentInfo(Person):
    faculty: Faculty
    group_info: GroupInfo


class FacultyInfoIn(BaseModel):
    name: Faculty


class SpecializationInfoIn(BaseModel):
    name: str


class CreationResponse(BaseModel):
    id: int


class MessageResponse(BaseModel):
    message: str = 'ok'
