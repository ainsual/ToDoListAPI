from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

load_dotenv()

engine = create_async_engine('sqlite+aiosqlite:///./tasks.db', echo=True)

new_session = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

async def get_session():
    async with new_session() as session:
        yield session

