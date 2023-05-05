import os
from googleapiclient.discovery import build
import json


class Video:
    """"""

    def __init__(self, video_id):
        self.video_id = video_id
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        # printj(video_response)
        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        self.comment_count: int = video_response['items'][0]['statistics']['commentCount']
        self.url = f'https://youtu.be/{self.video_id}'

    def __str__(self):
        return self.video_title


class PLVideo(Video):
    """"""
    def __init__(self, video_id, video_playlist):
        super().__init__(video_id)
        self.video_playlist = video_playlist

    def __str__(self):
        return self.video_title
