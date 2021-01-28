from typing import Dict
from TwitchX.stream import Stream
from TwitchX.ext.login import Login
from app.config import load_config as _config

config = _config()


class TwitchDL:
    def __init__(self, user_name: str) -> None:
        """

        :param user_name: twitch streamer id
        :type user_name: str
        """
        self.st = Stream()
        self.login = Login(
            client_id="kimne78kx3ncx6brgo4mv6wki5h1ko",
            username=config.twitch.username,
            password=config.twitch.password
        )
        self.user_name = user_name

    async def _login(self) -> dict:
        """

        :return: twitch source
        :rtype: dict
        """
        source = await self.login.login()
        return source

    async def get_stream_url(self) -> dict:
        """Get twitch live stream url

        :return: stream url
        :rtype: Dict[str, str]
        """
        token = await self._login()
        s = await self.st.get_twitch_live_playlist_url(user_name=self.user_name, token=token["auth-token"])
        res = {
            "url": s
        }
        return res
