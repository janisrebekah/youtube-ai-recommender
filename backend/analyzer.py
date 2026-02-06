import os
import requests
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
analyzer = SentimentIntensityAnalyzer()

COMMENTS_URL = "https://www.googleapis.com/youtube/v3/commentThreads"


def get_comments(video_id: str, max_comments: int = 50):
    params = {
        "part": "snippet",
        "videoId": video_id,
        "key": API_KEY,
        "maxResults": max_comments,
        "textFormat": "plainText",
    }

    response = requests.get(COMMENTS_URL, params=params)
    data = response.json()

    comments = []

    for item in data.get("items", []):
        text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(text)

    return comments


def analyze_comments(comments):
    if not comments:
        return 0

    scores = []

    for comment in comments:
        sentiment = analyzer.polarity_scores(comment)["compound"]
        scores.append(sentiment)

    # average sentiment score
    return sum(scores) / len(scores)
