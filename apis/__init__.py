from fastapi import APIRouter
from app.twitch import TwitchDL

router = APIRouter()


@router.get("/twitch/{user}", tags=["twitch"])
async def get_stream_url(user: str):
    ap = TwitchDL(user_name=user)
    return await ap.get_stream_url()
