# VideoFind - AI-Powered YouTube Recommender

A creative application that discovers the best YouTube videos based on AI sentiment analysis, engagement metrics, and recency. Combines a Python FastAPI backend with a modern React frontend.

---

## 🎥 Features

- **Smart Video Search**: Search YouTube for any topic
- **AI Sentiment Analysis**: Analyzes video comments using VADER sentiment analysis
- **Quality Ranking**: Rank videos based on:
  - 💬 Comment sentiment (what viewers say)
  - 👍 Like ratio (engagement)
  - ⏰ Recency (how recent the content is)
- **Beautiful UI**: Modern dark theme with animations and gradients
- **Responsive Design**: Works on mobile, tablet, and desktop
- **Image Proxy**: Bypasses CORS restrictions for YouTube thumbnails

---

## 🔧 Prerequisites

- **Python 3.8+** (Backend)
- **Node.js 16+** & **npm** (Frontend)
- **YouTube Data API Key** (from [Google Cloud Console](https://console.cloud.google.com/))

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd utube
```

### 2. Backend Setup

```bash
cd backend
```

**Create Virtual Environment:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Install Dependencies:**
```bash
pip install fastapi uvicorn requests python-dotenv vaderSentiment
```

**Create `.env` file** in the `backend/` folder:
```env
YOUTUBE_API_KEY=your_youtube_api_key_here
```

### 3. Frontend Setup

```bash
cd frontend
```

**Install Dependencies:**
```bash
npm install
```

---

## 🚀 Running the Application

### Start Backend

```bash
cd backend
venv\Scripts\activate
uvicorn main:app --reload
```

Backend runs on: `http://localhost:8000`

### Start Frontend

In a new terminal:
```bash
cd frontend
npm run dev
```

Frontend runs on: `http://localhost:5173`

---

## 📋 How to Use

1. Open `http://localhost:5173` in your browser
2. Search for any topic (e.g., "React tutorials", "cooking", "Python")
3. View the top 3 recommended videos with scores
4. Click "Watch on YouTube →" to view the video

---

## 🏗️ Project Structure

```
utube/
├── backend/
│   ├── main.py           # FastAPI app & endpoints
│   ├── youtube.py        # YouTube API integration
│   ├── analyzer.py       # Sentiment analysis
│   ├── ranker.py         # Scoring algorithm
│   └── requirements.txt   # Dependencies
├── frontend/
│   ├── src/
│   │   ├── App.jsx       # Main app component
│   │   ├── App.css       # App styling
│   │   ├── main.jsx      # Entry point
│   │   └── components/
│   │       ├── SearchBar.jsx
│   │       ├── VideoCard.jsx
│   │       └── *.css
│   ├── package.json
│   └── vite.config.js
├── .gitignore
└── README.md
```

---

## 🔌 API Endpoints

### `/recommend`
**GET** - Get top 3 recommended videos for a query

**Query Parameters:**
- `query` (string, required): Search term

**Response:**
```json
[
  {
    "title": "Video Title",
    "videoId": "abc123",
    "score": 0.875,
    "url": "https://youtube.com/watch?v=abc123"
  }
]
```

### `/proxy-image`
**GET** - Proxy YouTube thumbnails to bypass CORS

**Query Parameters:**
- `url` (string, required): Image URL to proxy

---

## 🛠️ Technologies

### Backend
- **FastAPI** - Modern web framework
- **Python-dotenv** - Environment variables
- **Requests** - HTTP client
- **VADER Sentiment** - Sentiment analysis
- **YouTube Data API** - Video search & stats

### Frontend
- **React 19** - UI framework
- **Vite** - Build tool
- **CSS3** - Styling with animations
- **ES6+** - Modern JavaScript

---

## 🎯 Scoring Algorithm

Videos are scored based on:

```
Final Score = (Sentiment × 0.5) + (Like Ratio × 0.3) + (Recency × 0.2)
```

- **Sentiment (50%)**: Average sentiment from video comments (VADER)
- **Like Ratio (30%)**: Likes divided by total views
- **Recency (20%)**: How recent the video was published

---

## 📝 Environment Variables

Create a `.env` file in the `backend/` folder:

```env
YOUTUBE_API_KEY=your_api_key_here
```

**Get Your API Key:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable YouTube Data API v3
4. Create an API key credential
5. Copy and paste in `.env`

---

## 🐛 Troubleshooting

**Problem: "Failed to fetch recommendations"**
- Ensure backend is running on `http://localhost:8000`
- Check backend console for errors
- Verify YouTube API key is valid

**Problem: Thumbnails not displaying**
- Backend proxy endpoint should be working
- Check browser console for network errors (F12)
- Hard refresh browser (Ctrl+F5)

**Problem: No comments found**
- Some videos have comments disabled
- API may hit rate limits
- Try a different video/search term

---

## 📄 License

This project is open source and available under the MIT License.

---

## 💡 Future Enhancements

- [ ] Add filter by upload date
- [ ] Save favorite videos
- [ ] Sort by different metrics
- [ ] Dark/Light theme toggle
- [ ] Video preview on hover
- [ ] Share recommendations
- [ ] Trending topics

---

## 🤝 Contributing

Contributions welcome! Feel free to open issues or submit pull requests.

---

## 📧 Support

For issues or questions, open an issue on the repository.

---

**Happy video hunting! 🎬**
