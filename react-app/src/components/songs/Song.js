import React, { useState, useEffect } from 'react';
import { NavLink, Link } from 'react-router-dom';
import './Song.css';


const Song = () => {
  const [annotation, setAnnotation] = useState('');

  useEffect(() => {
    if (annotation === '') {
      return
    }
    // Need to fetch new annotation if it changed
  }, [annotation]);

  return (
    <div className="songpage">
      <header className="songpage-header">
        <img className="songpage-image" alt="Album Cover"/>
        <div className="songpage-info">
          <h1 className="songpage-title">Song Title</h1>
          <Link to="/artists/1" className="artist-name">Artist's Name</Link>
        </div>
      </header>
      <div className="songpage-content">
        <section className="songpage-lyrics">
          <p><span className="annotation-key active">Lyrics will go here based of DB information</span><br />
          <span className="annotation-key ">Second line</span> of text<br />
          Third line
          </p>
        </section>
        <section className="songpage-sidebar">
          <div className={`songpage-annotation ${(!annotation ? " active" : "")}`}>Some active annotation comment</div>
          <div className="songpage-sidelinks">
            <NavLink to="/songs/1">Song 1</NavLink>
            <NavLink to="/songs/2">Song 2</NavLink>
          </div>
        </section>
      </div>
    </div>
  )
}

export default Song
