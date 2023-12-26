from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base
from src.core.config import settings

Base = declarative_base()

engine = create_async_engine(
    str(settings.postgres_conn),
    future=True,
    connect_args={"options": "-c search_path=public,content"},
)
async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def create_database() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def purge_database() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
