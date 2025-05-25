from fastapi import APIRouter

from core.config import settings
from .users import router as user_router

router = APIRouter(
    prefix=settings.prefix.v1.api
)
router.include_router(user_router)