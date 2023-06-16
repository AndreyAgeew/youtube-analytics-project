from src.channel import Channel


class Video:
    """
    Класс для представления видео.

    Атрибуты:
        video_id (str): Идентификатор видео.
        title (str): Название видео.
        url (str): URL-адрес видео.
        view_count (int): Количество просмотров видео.
        like_count (int): Количество лайков видео.
    """

    def __init__(self, video_id: str) -> None:
        """
        Инициализирует экземпляр класса Video.

        Аргументы:
            video_id (str): Идентификатор видео.
        """
        self.__video_id = video_id
        self.__title = None
        self.__url = None
        self.__view_count = None
        self.__like_count = None
        self.fetch_video_data()

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Video.

        Возвращает:
            str: Строковое представление объекта Video.
        """
        return self.__title

    def fetch_video_data(self) -> None:
        """
        Получает данные о видео с помощью YouTube API и обновляет соответствующие атрибуты объекта.

        Возвращает:
            None
        """
        try:
            youtube = Channel.get_service().videos().list(
                part='snippet,statistics', id=self.video_id
            ).execute()
            video_data = youtube.get('items')[0]
            self.__title = video_data.get('snippet').get('title')
            self.__url = f'https://www.youtube.com/watch?v={self.video_id}'
            self.__view_count = int(video_data.get('statistics').get('viewCount'))
            self.__like_count = int(video_data.get('statistics').get('likeCount'))
        except IndexError:
            print('Неверная ссылка!')

    @property
    def video_id(self) -> str:
        """str: Геттер для идентификатора видео."""
        return self.__video_id

    @video_id.setter
    def video_id(self, value) -> None:
        """str: Cеттер для идентификатора видео."""
        self.__video_id = value


class PLVideo(Video):
    """
    Класс для представления видео в плейлисте.

    Атрибуты:
        video_id (str): Идентификатор видео.
        playlist_id (str): Идентификатор плейлиста.
    """

    def __init__(self, video_id: str, playlist_id: str) -> None:
        """
        Инициализирует экземпляр класса PLVideo.

        Аргументы:
            video_id (str): Идентификатор видео.
            playlist_id (str): Идентификатор плейлиста.
        """
        self.__playlist_id = playlist_id
        super().__init__(video_id)
