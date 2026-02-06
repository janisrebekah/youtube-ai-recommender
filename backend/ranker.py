from datetime import datetime


# def recency_score(published_date: str):
#     published = datetime.fromisoformat(published_date.replace("Z", "+00:00"))
#     days_old = (datetime.utcnow() - published).days

#     # newer videos get higher score
#     return max(0, 1 - (days_old / 3650))  # decay over ~10 years

from datetime import datetime, timezone


def recency_score(published_date: str):
    # Convert YouTube date to timezone-aware datetime
    published = datetime.fromisoformat(
        published_date.replace("Z", "+00:00")
    )

    # Current time with timezone
    now = datetime.now(timezone.utc)

    days_old = (now - published).days

    # Newer videos → higher score
    return max(0, 1 - (days_old / 3650))  # decay over ~10 years


def final_score(sentiment, like_ratio, recency):
    return (
        0.4 * sentiment +
        0.3 * like_ratio +
        0.3 * recency
    )
