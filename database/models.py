from tortoise import Model
from tortoise.fields import DatetimeField, CharField, IntField, ForeignKeyField, CASCADE, CharEnumField

from app.routers.default import models


class Faculty(Model):
    id = IntField(pk=True)
    name = CharEnumField(enum_type=models.Faculty, max_length=255, unique=True)
    created_at = DatetimeField(auto_now_add=True)
    updated_at = DatetimeField(auto_now=True)

    class Meta:
        table = 'faculty'


class Specialization(Model):
    id = IntField(pk=True)
    name = CharField(max_length=128, unique=True)
    created_at = DatetimeField(auto_now_add=True)
    updated_at = DatetimeField(auto_now=True)

    class Meta:
        table = 'specialization'


class Student(Model):
    id = IntField(pk=True)
    first_name = CharField(max_length=128)
    last_name = CharField(max_length=128)
    faculty = ForeignKeyField('models.Faculty', related_name='student', on_delete=CASCADE)
    specialization = ForeignKeyField('models.Specialization', related_name='student', on_delete=CASCADE)
    group_number = IntField()
    created_at = DatetimeField(auto_now_add=True)
    updated_at = DatetimeField(auto_now=True)

    class Meta:
        table = 'student'
