import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json


class Video:
    """"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.video_id = video_id

        try:
            video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()

            if not video_response['items'] or len(video_response['items']) == 0:
                self.video_title = None
                self.view_count = None
                self.like_count = None
                self.comment_count = None

            else:
                self.video_title: str = video_response['items'][0]['snippet']['title']
                self.view_count: int = video_response['items'][0]['statistics']['viewCount']
                self.like_count: int = video_response['items'][0]['statistics']['likeCount']
                self.comment_count: int = video_response['items'][0]['statistics']['commentCount']
                self.url = f'https://youtu.be/{self.video_id}'

        except HttpError:
            self.video_title = None
            self.view_count = None
            self.like_count = None
            self.comment_count = None



    def __str__(self):
        return self.video_title


class PLVideo(Video):
    """"""

    def __init__(self, video_id, video_playlist):
        super().__init__(video_id)
        self.video_playlist = video_playlist

    def __str__(self):
        return self.video_title
