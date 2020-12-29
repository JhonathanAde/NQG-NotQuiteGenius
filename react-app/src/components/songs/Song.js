import React, { useState, useEffect } from 'react';
import { NavLink, Link, useParams } from 'react-router-dom';
import './Song.css';


const Song = () => {
  const [annotation, setAnnotation] = useState("");
  const [song, setSong] = useState("");
  const {songId} = useParams();

  useEffect(() => {
    (async () => {
      const response = await fetch(`/api/songs/${songId}`);
      const song = await response.json();
      setSong(song);
    })();
  }, [annotation, songId]);

  const onAnnotationClick = (e) => {
    const elementToReset = document.querySelector('.annotation-key.active');
    if (elementToReset) elementToReset.classList.remove('active');
    if (e.target.classList.contains('annotation-key')) {
      e.target.classList.add('active')
      const annotationKey = e.target.innerHTML;
      // TODO fetch actual annotation and set it
      document.querySelector('.songpage-annotation-text').innerHTML = annotationKey
      setAnnotation(annotationKey)
    }
    else {
      setAnnotation("")
    }
  }

  return (
    <div className="songpage" onClick={onAnnotationClick}>
      <header className="songpage-header">
        <img className="songpage-image" alt="Album Cover"/>
        <div className="songpage-info">
          <h1 className="songpage-title">Song Title</h1>
          <Link to="/artists/1" className="artist-name">Artist's Name</Link>
        </div>
      </header>
      <div className="songpage-content">
        <section className="songpage-lyrics">
          <p> {
              song
            }
          </p>
          <p><span className="annotation-key" >Lyrics will go here</span> based of DB information<br />
          <span className="annotation-key">Second line</span> of text<br />
          Third line<br />
          <span className="annotation-key">A really long fourth line of lyrics that may lap to two lines in a narrow window and show how the functionality will work with that.</span><br />
          Fifth line<br />
          Sixth line<br />
          <span className="annotation-key">Seventh</span> line<br />
          </p>
        </section>
        <section className="songpage-sidebar">
          <div className={`songpage-annotation ${(annotation ? " active" : "")}`}>Some active annotation comment
          <p className="songpage-annotation-text">
          </p>
          </div>
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
