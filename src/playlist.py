from src.channel import Channel
from datetime import timedelta


class PlayList:
    """
    Класс для представления плейлиста.

    Атрибуты:
        __playlist_id (str): Идентификатор плейлиста.
        __title (str): Название плейлиста.
        __url (str): Ссылка на плейлист.
        __videos (list): Список видео в плейлисте.
    """

    def __init__(self, playlist_id: str) -> None:
        """
        Инициализирует экземпляр класса PlayList.

        Аргументы:
            playlist_id (str): Идентификатор плейлиста.
        """
        self.__playlist_id = playlist_id
        self.__title = None
        self.__url = None
        self.__videos = []
        self.fetch_playlist_data()

    def fetch_playlist_data(self) -> None:
        """
        Получает данные о плейлисте с помощью YouTube API и обновляет соответствующие атрибуты объекта.

        Возвращает:
            None
        """
        try:
            youtube = Channel.get_service().playlistItems().list(
                playlistId=self.__playlist_id,
                part='snippet,contentDetails,id,status',
                maxResults=10,
            ).execute()
            playlist_data = youtube.get('items')[0]
            self.__title = playlist_data.get('snippet').get('title').split(".")[0]
            self.__url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'

            video_ids = [video['contentDetails']['videoId'] for video in youtube['items']]
            videos = Channel.get_service().videos().list(
                part='contentDetails,statistics',
                id=','.join(video_ids)
            ).execute()
            self.__videos = videos.get('items')
        except IndexError:
            print('Неверный идентификатор плейлиста!')

    @property
    def playlist_id(self) -> str:
        """str: Геттер для идентификатора плейлиста."""
        return self.__playlist_id

    @property
    def title(self) -> str:
        """str: Геттер для названия плейлиста."""
        return self.__title

    @property
    def url(self) -> str:
        """str: Геттер для ссылки на плейлист."""
        return self.__url

    @property
    def videos(self):
        """list: Геттер для списка видео в плейлисте."""
        return self.__videos

    @property
    def total_duration(self) -> timedelta:
        """datetime.timedelta: Геттер для суммарной длительности плейлиста."""
        total_duration = timedelta()
        for video in self.__videos:
            duration = video.get('contentDetails').get('duration')
            video_duration = self.parse_duration(duration)
            total_duration += video_duration
        return total_duration

    @staticmethod
    def parse_duration(duration: str) -> timedelta:
        """
        Преобразует строку длительности видео в объект timedelta.

        Аргументы:
            duration (str): Строка с длительностью видео в формате ISO 8601.

        Возвращает:
            timedelta: Объект timedelta, представляющий длительность видео.
        """
        parts = duration.split('T')
        time_part = parts[1]
        hours = int(time_part.split('H')[0]) if 'H' in time_part else 0
        minutes = int(time_part.split('M')[0].split('H')[-1]) if 'M' in time_part else 0
        seconds = int(time_part.split('S')[0].split('M')[-1]) if 'S' in time_part else 0
        video_duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        return video_duration

    def show_best_video(self) -> str:
        """
        Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков).
        """
        best_video = max(self.__videos, key=lambda video: video.get('statistics').get('likeCount'))
        video_id = best_video.get('id')
        return f'https://youtu.be/{video_id}'
