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
        self.__customUrl = self._channel['items'][0]['snippet']['customUrl']
        self._link = f'https://www.youtube.com/{self.__customUrl}'
        self._num_subscribers = self._channel['items'][0]['statistics']['subscriberCount']
        self._num_videos = self._channel['items'][0]['statistics']['videoCount']
        self._total_views = self._channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self._channel, indent=2, ensure_ascii=False))


vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
# print(vdud.print_info())
print(vdud._num_subscribers)
print(vdud._num_videos)
print(vdud._total_views)