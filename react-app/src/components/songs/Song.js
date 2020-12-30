import React, { useState, useEffect } from 'react';
import { NavLink, Link, useParams } from 'react-router-dom';
import ReactHtmlParser from 'react-html-parser'
import './Song.css';


const Song = (authenticated) => {
  const [annotation, setAnnotation] = useState("");
  const [song, setSong] = useState("");
  const [lyricsHTML, setLyricsHTML] = useState("");
  const [validSelect, setValidSelect] = useState(false);
  const [newAnnotationKey, setNewAnnotationKey] = useState("");
  const {songId} = useParams();

  useEffect(() => {
    // Load the song information
    (async () => {
      const response = await fetch(`/api/songs/${songId}`);
      const song = await response.json();
      setSong(song);
      let lyrics = song.lyrics;
      song.annotations.forEach((annot, i) => {
        const key = annot.lyricKey
        lyrics = lyrics.replaceAll(key, `<span class="annotation-key" data-index="${i}">${key}</span>`)
      })
      setLyricsHTML(ReactHtmlParser(lyrics));
    })();
  }, [songId, authenticated]);

  useEffect(() => {
    //Remove any previous selections
    const priorSelection = document.querySelectorAll('.songpage-new-annotation');
    for n in priorSelection {
      const text = n.innerHTML;
      n.after(text)
      n.remove()
    }
    //Make new selections
    if (newAnnotationKey) {

    };
  }, [newAnnotationKey])

  const onAnnotationClick = (e) => {
    setNewAnnotationKey("");
    const elementToReset = document.querySelector('.annotation-key.active');
    if (elementToReset) elementToReset.classList.remove('active');
    if (e.target.classList.contains('annotation-key')) {
      e.target.classList.add('active')
      const annotationKey = e.target.innerHTML;
      const annotation = song.annotations[parseInt(e.target.getAttribute("data-index"))].content;
      document.querySelector('.songpage-annotation-text').innerHTML = annotation
      setAnnotation(annotation)
    }
    else {
      setAnnotation("")
    }
  }

  const trackSelectionStart = (e) => {
    if (!authenticated) return;
    setValidSelect(true)
  }

  const onLyricSelection = (e) => {
      if (!validSelect || !authenticated) return;
      var text = "";
      if (window.getSelection) {
          text = window.getSelection().toString();
      } else if (document.selection && document.selection.type != "Control") {
          text = document.selection.createRange().text;
      }
      console.log('setting new annotation:', text)
      setNewAnnotationKey(text);
      setValidSelect(false);
      return text;
  }

  return (
    <div className="songpage" onClick={onAnnotationClick}>
      <header className="songpage-header">
        <img className="songpage-image" alt="Album Cover"/>
        <div className="songpage-info">
          { song &&
          <>
            <h1 className="songpage-title">{song.title}</h1>
            <Link to={`/artists/${song.artist.id}`} className="artist-name">{song.artist.name}</Link>
          </>
          }
        </div>
      </header>
      <div className="songpage-content">
        <section className="songpage-lyrics" onMouseDown={trackSelectionStart} onMouseUp={onLyricSelection}>
          {song &&
            <p> {
                lyricsHTML
              }
            </p>
          }
        </section>
        <section className="songpage-sidebar">
          <div className={`songpage-annotation ${(annotation ? " active" : "")}`}>
          <p className="songpage-annotation-text">
          </p>
          </div>
          <div className={`songpage-add-annotation ${(annotation ? " active" : "")}`}>
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
