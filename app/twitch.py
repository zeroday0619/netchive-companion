from typing import Dict
from youtube_dl.YoutubeDL import YoutubeDL
from app.config import load_config as _config

config = _config()


class TwitchDL:
    params = {
        "cookies": config.twitch.cookies,
        "quiet": True
    }
    source_ = YoutubeDL(params=params)

    def __init__(self) -> None:
        self.source: YoutubeDL = self.source_

    def get_stream_url(self, user_name: str) -> Dict[str, str]:
        """Get twitch live stream url

        :param user_name: Twitch streamer id
        :type user_name: str
        :return: stream url
        :rtype: Dict[str]
        """
        source: dict = self.source.extract_info(
            url=f"https://twitch.tv/{user_name}", download=False
        )
        stream_url = [
            {
                "url": i.get("manifest_url")
            } for i in source.get("formats")
        ][-1]
        return stream_url
