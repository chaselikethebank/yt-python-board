from googleapiclient.discovery import build
import pandas as pd
from IPython.display import JSON

api_key = 'AIzaSyC8yfGrWzD4lqqTb4YlzQ83IZ0t09bOdms'
channel_ids = ['UC16niRr50-MSBwiO3YDb3RA', 'UC16niRr50-MSBwiO3YDb3RA']

youtube = build(
    'youtube', 'v3',
    developerKey = api_key
)

request = youtube.channels().list(
    part="snippet, contentDetails, statistics",
    id=','.join(channel_ids))

response = request.execute()

JSON(response)