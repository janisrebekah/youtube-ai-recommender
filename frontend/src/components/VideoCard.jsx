import { useState } from 'react'
import './VideoCard.css'

function VideoCard({ video, rank }) {
  const [imageError, setImageError] = useState(false)
  const scorePercentage = Math.round(video.score * 100)
  const getScoreColor = (score) => {
    if (score >= 0.75) return '#10b981' // green
    if (score >= 0.5) return '#3b82f6' // blue
    if (score >= 0.25) return '#f59e0b' // amber
    return '#ef4444' // red
  }

  const placeholderImage = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 180"%3E%3Crect fill="%231e293b" width="320" height="180"/%3E%3Ctext x="50%25" y="50%25" font-size="24" fill="%23cbd5e1" text-anchor="middle" dy=".3em"%3E🎬 Video%3C/text%3E%3C/svg%3E'
  
  // Use backend proxy to serve images
  const imageUrl = imageError ? placeholderImage : `http://localhost:8000/proxy-image?url=${encodeURIComponent(video.thumbnail)}`

  return (
    <div className="video-card">
      <div className="rank-badge">#{rank}</div>
      
      <div className="thumbnail-wrapper">
        <img 
          src={imageUrl}
          alt={video.title}
          className="thumbnail"
          onError={() => setImageError(true)}
        />
        <div className="score-overlay">
          <div className="score-circle" style={{ borderColor: getScoreColor(video.score) }}>
            <span className="score-value" style={{ color: getScoreColor(video.score) }}>
              {scorePercentage}%
            </span>
            <span className="score-label">SCORE</span>
          </div>
        </div>
      </div>

      <div className="card-content">
        <h3 className="video-title">{video.title}</h3>
        
        <div className="card-footer">
          <a 
            href={video.url} 
            target="_blank" 
            rel="noopener noreferrer"
            className="watch-button"
          >
            Watch on YouTube →
          </a>
        </div>
      </div>

      <div className="card-shine"></div>
    </div>
  )
}

export default VideoCard
