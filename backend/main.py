from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import StreamingResponse
from youtube import search_videos, get_video_stats
from analyzer import get_comments, analyze_comments
from ranker import recency_score, final_score
import requests

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/proxy-image")
def proxy_image(url: str):
    """Proxy images through backend to avoid CORS issues"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return StreamingResponse(
            iter([response.content]),
            media_type=response.headers.get("content-type", "image/jpeg"),
            headers={"Cache-Control": "max-age=86400"}
        )
    except Exception as e:
        return {"error": str(e)}


@app.get("/recommend")
def recommend(query: str):
    videos = search_videos(query)

    video_ids = [v["videoId"] for v in videos]
    stats = get_video_stats(video_ids)

    results = []

    for video in videos:
        vid = video["videoId"]

        comments = get_comments(vid)
        sentiment = analyze_comments(comments)

        video_stats = stats.get(vid, {})

        like_ratio = video_stats.get("like_ratio", 0)
        recency = recency_score(
            video_stats.get("published", "2000-01-01T00:00:00Z")
        )

        score = final_score(sentiment, like_ratio, recency)

        results.append({
            "title": video["title"],
            "videoId": vid,
            "score": round(score, 3),
            "url": f"https://youtube.com/watch?v={vid}"
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:3]
