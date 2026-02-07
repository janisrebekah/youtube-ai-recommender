import { useState } from 'react'
import './SearchBar.css'

function SearchBar({ onSearch }) {
  const [input, setInput] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    onSearch(input)
    setInput('')
  }

  const handleChange = (e) => {
    setInput(e.target.value)
  }

  return (
    <div className="search-container">
      <form onSubmit={handleSubmit} className="search-form">
        <div className="search-input-wrapper">
          <input
            type="text"
            value={input}
            onChange={handleChange}
            placeholder="Search YouTube videos..."
            className="search-input"
          />
          <button type="submit" className="search-button">
            <span>🔍 Search</span>
          </button>
        </div>
      </form>
    </div>
  )
}

export default SearchBar
