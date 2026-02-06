# YouTube AI Tutorial Recommender

An AI-powered backend that recommends the best YouTube tutorial for a topic using:

- YouTube Data API
- Comment sentiment analysis (TextBlob)
- Like ratio + recency scoring
- FastAPI REST backend

## Run locally

pip install -r requirements.txt  
uvicorn main:app --reload

## Endpoint

/recommend?query=your_topic
