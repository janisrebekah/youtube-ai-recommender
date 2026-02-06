import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"


def search_videos(query: str, max_results: int = 5):
    params = {
        "part": "snippet",
        "q": query,
        "key": API_KEY,
        "maxResults": max_results,
        "type": "video",
    }

    response = requests.get(SEARCH_URL, params=params)
    data = response.json()

    videos = []

    for item in data.get("items", []):
        videos.append(
            {
                "title": item["snippet"]["title"],
                "videoId": item["id"]["videoId"],
                "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
            }
        )

    return videos

STATS_URL = "https://www.googleapis.com/youtube/v3/videos"


def get_video_stats(video_ids: list):
    params = {
        "part": "statistics,snippet",
        "id": ",".join(video_ids),
        "key": API_KEY,
    }

    response = requests.get(STATS_URL, params=params)
    data = response.json()

    stats = {}

    for item in data.get("items", []):
        vid = item["id"]

        views = int(item["statistics"].get("viewCount", 0))
        likes = int(item["statistics"].get("likeCount", 0))
        published = item["snippet"]["publishedAt"]

        like_ratio = likes / views if views > 0 else 0

        stats[vid] = {
            "views": views,
            "likes": likes,
            "like_ratio": like_ratio,
            "published": published,
        }

    return stats
