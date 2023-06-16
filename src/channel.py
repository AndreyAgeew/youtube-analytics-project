import json

import googleapiclient.discovery
from googleapiclient.discovery import build, Resource

from src.config import API_KEY_YOUTUBE


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """
        Инициализирует экземпляр класса Channel с указанным идентификатором канала.
        Данные о канале будут получены с помощью YouTube API.

        Аргументы:
            channel_id (str): Идентификатор YouTube-канала.

        Атрибуты:
            __channel_id (str): Идентификатор YouTube-канала.
            __channel_title (str): Название YouTube-канала.
            __channel_description (str): Описание YouTube-канала.
            __channel_url (str): Ссылка на YouTube-канал.
            __subscriber_count (str): Количество подписчиков YouTube-канала.
            __video_count (str): Количество видео на YouTube-канале.
            __view_count (str): Общее количество просмотров YouTube-канала.

        """
        self.__channel_id = channel_id
        self.__youtube = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.__channel_title = self.__youtube['items'][0]['snippet']['title']
        self.__channel_description = self.__youtube['items'][0]['snippet']['description']
        self.__channel_url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.__subscriber_count = int(self.__youtube['items'][0]['statistics']['subscriberCount'])
        self.__video_count = int(self.__youtube['items'][0]['statistics']['videoCount'])
        self.__view_count = int(self.__youtube['items'][0]['statistics']['viewCount'])

    @property
    def channel_id(self) -> str:
        """str: Геттер Идентификатора YouTube-канала."""
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.__youtube, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls) -> googleapiclient.discovery.Resource:
        """Возвращает объект службы YouTube API для выполнения запросов к API."""
        return build('youtube', 'v3', developerKey=API_KEY_YOUTUBE)

    def to_json(self, file_path: str) -> None:
        """
               Сохраняет информацию о канале в JSON-файл.

               Аргументы:
                   file_path (str): Путь к файлу JSON, в который будет сохранена информация.

        """
        channel_data = {
            'channel_id': self.__channel_id,
            'channel_title': self.__channel_title,
            'channel_description': self.__channel_description,
            'channel_url': self.__channel_url,
            'subscriberCount': self.__subscriber_count,
            'videoCount': self.__video_count,
            'viewCount': self.__view_count
        }
        with open(file_path, 'w') as file:
            json.dump(channel_data, file, indent=2, ensure_ascii=False)
