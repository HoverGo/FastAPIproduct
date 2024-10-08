from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.config.database.db_settings import DB_URL


engine = create_async_engine(DB_URL)

async_session = async_sessionmaker(engine, expire_on_commit=False)
