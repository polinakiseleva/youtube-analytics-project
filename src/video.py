import os
from googleapiclient.discovery import build


class Video:
    __API_KEY: str = os.getenv('API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__API_KEY)

    def __init__(self, video_id):
        self.__video_id = video_id
        self.__video_response = self.__youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                             id=self.__video_id).execute()
        self.__video_title = self.__video_response['items'][0]['snippet']['title']
        self.__video_url = f"https://www.youtube.com/watch?v={self.__video_id}"
        self.__view_count = self.__video_response['items'][0]['statistics']['viewCount']
        self.__like_count = self.__video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.__video_title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
