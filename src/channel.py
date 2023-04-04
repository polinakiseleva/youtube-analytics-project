import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    _API_KEY: str = os.getenv('API_KEY')
    _youtube = build('youtube', 'v3', developerKey=_API_KEY)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id
        self._channel = self._youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        self._title = self._channel['items'][0]['snippet']['title']
        self._description = self._channel['items'][0]['snippet']['description']
        # чтобы сделать ссылку на канал действительной, сначала создаю customUrl, а только потом саму ссылку
        self.__customUrl = self._channel['items'][0]['snippet']['customUrl']
        self._link = f'https://www.youtube.com/{self.__customUrl}'
        self._num_subscribers = int(self._channel['items'][0]['statistics']['subscriberCount'])
        self._num_videos = self._channel['items'][0]['statistics']['videoCount']
        self._total_views = self._channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self._title} ({self._link})'

    def __add__(self, other):
        return self._num_subscribers + other._num_subscribers

    def __sub__(self, other):
        return self._num_subscribers - other._num_subscribers

    def __lt__(self, other):
        return self._num_subscribers < other._num_subscribers

    def __le__(self, other):
        return self._num_subscribers <= other._num_subscribers

    def __gt__(self, other):
        return self._num_subscribers > other._num_subscribers

    def __ge__(self, other):
        return self._num_subscribers >= other._num_subscribers

    def __eq__(self, other):
        return self._num_subscribers == other._num_subscribers

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self._channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """
        Создаем метод, возвращающий объект для работы с YouTube API
        """
        return cls._youtube

    def to_json(self, filename):
        """
        Создаем метод, сохраняющий в файл значения атрибутов экземпляра Channel
        """
        data = {
            "channel_id": self._channel_id,
            "title": self._title,
            "description": self._description,
            "url": self._link,
            "subscribers_count": self._num_subscribers,
            "video_count": self._num_videos,
            "view_count": self._total_views
        }

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
