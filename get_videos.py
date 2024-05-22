import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

if os.path.isfile('gapikey'):  # Check if gapikey is a valid file
    with open('gapikey', 'r') as f:  # Open in read mode
        DEVELOPER_KEY = f.read().strip()  # Read and strip whitespace
else:
    print("Error: File '{}' not found.".format('gapikey'))

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def get_videos(query):
    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=DEVELOPER_KEY)

        response = youtube.search().list(
            part='snippet',
            q=query,
            type='video',
            #order='viewCount',
            maxResults=10  # Limit the number of results
        ).execute()

        videos = response.get('items', [])
        print(f"Fetched {len(videos)} videos")
        return [{
            'title': video['snippet']['title'],
            'video_id': video['id']['videoId'],
            'description': video['snippet']['description'],
            'thumbnail': video['snippet']['thumbnails']['default']['url']
        } for video in videos]
    except HttpError as e:
        print(f"Error fetching videos")
        print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")
        return []
