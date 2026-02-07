import { useState } from 'react'
import './App.css'
import VideoCard from './components/VideoCard'
import SearchBar from './components/SearchBar'

function App() {
  const [results, setResults] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const [query, setQuery] = useState('')

  const handleSearch = async (searchQuery) => {
    if (!searchQuery.trim()) return

    setLoading(true)
    setError('')
    setQuery(searchQuery)
    setResults([])

    try {
      const response = await fetch(`http://localhost:8000/recommend?query=${encodeURIComponent(searchQuery)}`)
      if (!response.ok) {
        throw new Error(`API error: ${response.status} ${response.statusText}`)
      }
      const data = await response.json()
      setResults(data)
    } catch (err) {
      console.error('Fetch error:', err)
      setError(`Failed to fetch recommendations: ${err.message}. Make sure the backend is running on http://localhost:8000`)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <div className="background-glow"></div>
      
      <header className="header">
        <div className="header-content">
          <div className="brand">
            <span className="brand-icon">▶</span>
            <h1>VideoFind</h1>
            <span className="subtitle">AI-Powered Video Recommendations</span>
          </div>
        </div>
      </header>

      <main className="main-content">
        <SearchBar onSearch={handleSearch} />

        {error && <div className="error-message">{error}</div>}

        <div className="results-container">
          {loading && (
            <div className="loading-state">
              <div className="spinner"></div>
              <p>Finding the best videos for you...</p>
            </div>
          )}

          {!loading && results.length === 0 && query && (
            <div className="empty-state">
              <p>🎬 No results found. Try a different search!</p>
            </div>
          )}

          {!loading && results.length > 0 && (
            <div className="videos-grid">
              {results.map((video, index) => (
                <VideoCard 
                  key={video.videoId} 
                  video={video} 
                  rank={index + 1}
                />
              ))}
            </div>
          )}

          {!loading && query === '' && results.length === 0 && (
            <div className="welcome-state">
              <div className="welcome-content">
                <h2>🎥 Welcome to VideoFind</h2>
                <p>Search for any topic and discover the best-rated YouTube videos based on:</p>
                <ul className="features">
                  <li>💬 <strong>Comment Sentiment</strong> - Real viewer feedback</li>
                  <li>👍 <strong>Like Ratio</strong> - Community engagement</li>
                  <li>⏰ <strong>Recency</strong> - Recent, relevant content</li>
                </ul>
                <p className="hint">Try searching for "React tutorials", "cooking recipes", or anything else!</p>
              </div>
            </div>
          )}
        </div>
      </main>

      <footer className="footer">
        <p>Powered by AI sentiment analysis & YouTube data</p>
      </footer>
    </div>
  )
}

export default App
