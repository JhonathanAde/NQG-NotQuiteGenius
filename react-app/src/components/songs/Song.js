import React from 'react';
import { Link } from 'react-router-dom';
import './Song.css';


const Song = () => {
  return (
    <div className="song">
      <header>
        <img className="song-image"/>
        <h1 className="song-title">Song Title</h1>
        <Link className="artist-name">Artist's Name</Link>
      </header>
      <section className="lyrics">
        <p>Lyrics will go here based of DB information</p>
      </section>
      <section className="sidebar">
        <div className="annotation">Some active annotation comment</div>
        <NavLink>Song 1</NavLink>
        <NavLink>Other Song 2</NavLink>
      </section>
    </div>
  )
}

export default Song
