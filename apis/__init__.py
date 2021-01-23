from fastapi import APIRouter, HTTPException
from youtube_dl.utils import DownloadError
from app.twitch import TwitchDL

router = APIRouter()


async def error(ex):
    dx = []
    _dx = dx.append
    for item in ex.exc_info:
        _dx(item)
    return dx


@router.get("/twitch/{user}/status", tags=["twitch"])
async def is_live(user: str):
    try:
        source = TwitchDL(user_name=user)
        status: bool = source.is_live()
        return {
            "is_live": status
        }
    except DownloadError as ex:
        dx = await error(ex=ex)
        raise HTTPException(status_code=404, detail=str(dx[1]))


@router.get("/twitch/{user}/info", tags=["twitch"])
async def get_stream_info(user: str):
    try:
        source = TwitchDL(user_name=user)
        if source.is_live():
            info = source.get_stream_information()
            return {
                "status": True,
                "result": info
            }
        else:
            return {
                "status": False
            }
    except DownloadError as ex:
        dx = await error(ex=ex)
        raise HTTPException(status_code=404, detail=str(dx[1]))


@router.get("/twitch/{user}", tags=["twitch"])
async def get_stream_url(user: str):
    try:
        source = TwitchDL(user_name=user)
        if source.is_live():
            url = source.get_stream_url()
            return {
                "status": True,
                "result": url
            }
        else:
            return {
                "status": False
            }
    except DownloadError as ex:
        dx = await error(ex=ex)
        raise HTTPException(status_code=404, detail=str(dx[1]))
