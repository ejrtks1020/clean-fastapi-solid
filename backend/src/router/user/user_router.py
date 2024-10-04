from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from icecream import ic
from db.session import get_session
from schema.user.user_schema import Token, ChangePasswordIn, UserIn, UserOut
from service.user.user_service import UserService

router = APIRouter(tags=["User"], prefix="/user")


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    user_data: UserIn,
    session: AsyncSession = Depends(get_session),
):
    return await UserService.register_user(user_data, session)


@router.post("/token", status_code=status.HTTP_200_OK)
async def token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[AsyncSession, Depends(get_session)],
) -> Token:
    ic("token - form_data ", form_data)
    
    return await UserService.login(form_data, session)


@router.get("/login", status_code=status.HTTP_200_OK)
async def login(current_user=Depends(UserService.get_current_user)) -> UserOut:
    return UserOut.model_validate(current_user)


@router.get("/get_by_id/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(get_session),
) -> UserOut:
    return await UserService.get_user_by_id(user_id, session)


@router.get("/get_all", status_code=status.HTTP_200_OK)
async def get_all_users(session: AsyncSession = Depends(get_session)) -> list[UserOut]:
    return await UserService.get_all_users(session)


@router.delete("/delete_by_id/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    return await UserService.delete_user_by_id(user_id, session)


@router.delete("/delete_all", status_code=status.HTTP_200_OK)
async def delete_all_users(session: AsyncSession = Depends(get_session)):
    return await UserService.delete_all_users(session)


@router.patch(
    "/change_password",
    status_code=status.HTTP_200_OK,
    summary="Change password for current user that is logged in",
)
async def change_password(
    password_data: ChangePasswordIn,
    current_user=Depends(UserService.get_current_user),
    session: AsyncSession = Depends(get_session),
):
    return await UserService.change_password(password_data, current_user, session)
