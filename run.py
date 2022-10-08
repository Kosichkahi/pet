import uvicorn

from app.app import get_application
from config.config import app_config
from database.database import get_database

if __name__ == '__main__':
    database = get_database()
    uvicorn.run(
        app=get_application(on_startup=[database.connect], on_shutdown=[database.disconnect]),
        debug=app_config.DEBUG
    )
