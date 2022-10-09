import uvicorn
from tortoise.transactions import in_transaction

from app.app import get_application
from config.config import app_config
from database.database import get_database

faculty_query = """
CREATE TABLE IF NOT EXISTS "faculty" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
"""
specialization_query = """
CREATE TABLE IF NOT EXISTS "specialization" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
"""
student_cuery = """
CREATE TABLE IF NOT EXISTS "student" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "group_number" INT,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "faculty_id" INT NOT NULL REFERENCES "faculty" ("id") ON DELETE CASCADE,
    "specialization_id" INT NOT NULL REFERENCES "specialization" ("id") ON DELETE CASCADE
);
"""


async def main():
    async with in_transaction() as conn:
        await conn.execute_query(faculty_query, [])
        await conn.execute_query(specialization_query, [])
        await conn.execute_query(student_cuery, [])


if __name__ == '__main__':
    database = get_database()
    uvicorn.run(
        app=get_application(on_startup=[database.connect, main], on_shutdown=[database.disconnect]),
        debug=app_config.DEBUG
    )
