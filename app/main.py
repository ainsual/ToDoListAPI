from typing import Optional, List

from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session, engine, Base
from models import ToDoModel
from shemas import TasksBaseShemas, TasksCreateShemas

app =FastAPI()

session_depends = Depends(get_session)

@app.post("/startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

@app.post('/tasks')
async def create_task(
        data: TasksBaseShemas,
        session: AsyncSession = session_depends) -> TasksCreateShemas:

    new_task = ToDoModel(**data.model_dump())
    session.add(new_task)
    await session.commit()
    return new_task

@app.get('/tasks/{task_id}')
async def get_one_task(
        task_id: int,
        session: AsyncSession = session_depends) -> TasksCreateShemas:
    if task_id <= 0:
        raise HTTPException(status_code=400, detail='Плохой запрос')

    query = select(ToDoModel).where(ToDoModel.id == task_id)
    result = await session.execute(query)
    task: Optional[TasksCreateShemas] = result.scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404, detail='Такого запорса не существует')

@app.get('/task')
async def get_all_tasks(session: AsyncSession = session_depends) -> List[TasksCreateShemas]:
    query = await session.execute(select(ToDoModel))
    result = query.scalars().all()
    return [TasksCreateShemas.from_orm(t) for t in result]
