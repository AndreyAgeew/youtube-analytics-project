import json
from googleapiclient.discovery import build

from src.config import API_KEY_YOUTUBE


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__youtube = build('youtube', 'v3', developerKey=API_KEY_YOUTUBE).channels(). \
            list(id=self.__channel_id, part='snippet,statistics').execute()

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, value):
        self.__channel_id = value

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__youtube, indent=2, ensure_ascii=False))
