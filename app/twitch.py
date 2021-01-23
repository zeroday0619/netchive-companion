from typing import Dict
from youtube_dl.YoutubeDL import YoutubeDL
from youtube_dl.utils import DownloadError
from app.config import load_config as _config

config = _config()


class TwitchDL:
    params = {
        "cookies": config.twitch.cookies,
        "quiet": True
    }
    source_ = YoutubeDL(params=params)

    def __init__(self, user_name: str) -> None:
        """

        :param user_name: twitch streamer id
        :type user_name: str
        """
        self.source: YoutubeDL = self.source_
        self.user_name = user_name

    def get_source(self) -> dict:
        """

        :return: twitch source
        :rtype: dict
        """
        source: dict = self.source.extract_info(
            url=f"https://twitch.tv/{self.user_name}", download=False,
        )
        return source

    def is_live(self) -> bool:
        """Live check

        :return: live status
        :rtype: bool
        """
        try:
            source: dict = self.get_source()
            status = source.get("is_live")
            return status
        except DownloadError:
            return False

    def get_stream_information(self) -> dict:
        """get stream information

        :return: stream info
        :rtype: Dict[str, str, str, str, str, float]
        """
        source: dict = self.get_source()
        info = {
            "streamer_uuid": source.get("id"),
            "streamer_id": source.get("display_id"),
            "streamer_name": source.get("uploader"),
            "title": source.get("title"),
            "description": source.get("description"),
            "timestamp": source.get("timestamp"),
        }
        return info

    def get_stream_url(self) -> dict:
        """Get twitch live stream url

        :return: stream url
        :rtype: Dict[str, str]
        """
        source = self.get_source()
        stream_url = [
            {
                "url": i.get("manifest_url")
            } for i in source.get("formats")
        ][-1]
        return stream_url
