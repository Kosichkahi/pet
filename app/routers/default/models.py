from enum import Enum

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


class StudentInfo(Person):
    faculty: Faculty
    group_info: GroupInfo
