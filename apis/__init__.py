from fastapi import APIRouter, HTTPException
from youtube_dl.utils import DownloadError
from app.twitch import TwitchDL

router = APIRouter()


@router.get("/twitch/{user}", tags=["twitch"])
async def get_stream_url(user: str):
    try:
        source = TwitchDL()
        url = source.get_stream_url(user_name=user)
        return url
    except DownloadError as ex:
        dx = []
        _dx = dx.append
        for item in ex.exc_info:
            _dx(item)
        raise HTTPException(status_code=404, detail=str(dx[1]))
