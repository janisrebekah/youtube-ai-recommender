from fastapi import FastAPI
from youtube import search_videos, get_video_stats
from analyzer import get_comments, analyze_comments
from ranker import recency_score, final_score

app = FastAPI()


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
