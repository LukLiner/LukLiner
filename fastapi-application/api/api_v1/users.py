from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.shemas.user import UserRead, UserCreate
from crud import users as user_crud

router = APIRouter(
    prefix=settings.prefix.v1.users,
    tags=["Users"]
)

@router.get("",response_model=list[UserRead])
async def get_users(
        #session: AsyncSession = Depends(db_helper.session_getter),
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
        users = await user_crud.get_all_users(session=session)
        return users

@router.post("",response_model=UserRead)
async def create_user(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        user_create:UserCreate,
):
    user = await user_crud.create_user(session=session,
                             user_create=user_create)
    return user