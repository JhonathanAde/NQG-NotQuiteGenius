import React, { useState, useEffect } from 'react';
import { NavLink, Link, useParams } from 'react-router-dom';
import ReactHtmlParser from 'react-html-parser';
import {getArtist} from '../../services/artists'
import './Song.css';
import AnnotationForm from './AnnotationForm';


const Song = ({authenticated, user}) => {
  const [annotation, setAnnotation] = useState("");
  const [annotations, setAnnotations] = useState([]);
  const [song, setSong] = useState("");
  const [artistSongs, setArtistSongs] = useState([]);
  const [lyricsHTML, setLyricsHTML] = useState("");
  const [newAnnotationKey, setNewAnnotationKey] = useState("");
  const {songId} = useParams();

  useEffect(() => {
    (async () => {
      const response = await fetch(`/api/songs/${songId}`);
      const song = await response.json();
      setSong(song);
      setAnnotations(song.annotations)
    })();
  }, [songId, authenticated]);

  useEffect(() => {
    clearNewAnnotationKey(true);
    updateAnnotations(song, annotations)
  }, [annotations, song])

  const updateAnnotations = (song, annotations) => {
    let lyrics = song.lyrics;
      annotations.forEach((annot, i) => {
        const key = annot.lyricKey
        lyrics = lyrics.replaceAll(key, `<span class="annotation-key" data-index="${i}">${key}</span>`)
      })
      setLyricsHTML(ReactHtmlParser(lyrics));
  }

  useEffect( () => {
    if (!song) return;
    (async () => {
        const res = await getArtist(song.artist.id)
        setArtistSongs(res.songs);
    })();
  },[song]);

  useEffect(() => {
    switchActiveSideBar()
  }, [newAnnotationKey, annotation]);

  const unHighlightKey = () => {
    const elementToReset = document.querySelector('.annotation-key.active');
    if (elementToReset) elementToReset.classList.remove('active');
  }

  const switchActiveSideBar = () => {
    const removeActive = document.querySelector('.songpage-sidebar > .active');
    if (removeActive) removeActive.classList.remove('active');
    if (annotation) {
      document.querySelector('.songpage-annotation').classList.add('active');
    } else if (newAnnotationKey) {
      document.querySelector('.songpage-add-annotation').classList.add('active');
    } else {
      document.querySelector('.songpage-sidelinks').classList.add('active');
    }
  }

  const onAnnotationClick = (e) => {
    if (!e.target.classList.contains('annotation-key')) {
      setAnnotation("");
      unHighlightKey();
      return;
    }
    clearNewAnnotationKey();
    unHighlightKey();
    e.target.classList.add('active')
    const annotationKey = e.target.innerHTML;
    const annotation = annotations[parseInt(e.target.getAttribute("data-index"))].content;
    document.querySelector('.songpage-annotation-text').innerHTML = annotation
    setAnnotation(annotation)
  }

  const onLyricSelection = (e) => {
      if (!authenticated) return;
      let text = "";
      let sel;
      let range;

      if (window.getSelection) {
        sel = window.getSelection();
        if (sel.toString() === '') return;
        range = sel.getRangeAt(0)
        if (!validSelectionCheck(range)) {
          clearNewAnnotationKey();
          return;
        }
        text = sel.toString();
        processSelection(text, range);
        if(sel.empty) {
          sel.empty()
        } else if (sel.removeAllRanges) {
          sel.removeAllRanges()
        }
      }
      else if (document.selection && document.selection.type != "Control") {
        sel = document.selection;
        if (sel.text === '') return;
        range = sel.createRange();
        if (!validSelectionCheck(range)) {
          clearNewAnnotationKey();
          return;
        }
        text = sel.text;
        processSelection(text, range)
        sel.empty()
      }

      return;

      //Helper functions

      function validSelectionCheck(range) {
        const contents = range.cloneContents();
        const startParent = range.startContainer.parentElement;
        const endParent = range.endContainer.parentElement;

        //Make sure new key does exist in current key
        const startNotNestedInKey = startParent.closest('.annotation-key') === null;
        const endNotNestedInKey = endParent.closest('.annotation-key') === null;
        const notNestedInKey = startNotNestedInKey && endNotNestedInKey;

        //Make sure selection does not wrap a current key
        let notIntersectingKey = true;
        if (contents) {
          if (contents.querySelector('.annotation-key')) {
            notIntersectingKey = false;
          }
        }

        //Make sure selection is within lyrics only
        const startInLyrics = startParent.closest('.songpage-lyrics') !== null;
        const endInLyrics = endParent.closest('.songpage-lyrics') !== null;
        const isInLyrics = startInLyrics && endInLyrics;

        return notNestedInKey && notIntersectingKey && isInLyrics
      }

      function processSelection(text, range) {
        clearNewAnnotationKey();
        setNewAnnotationKey(text);
        const wrap = document.createElement('span');
        wrap.classList.add('songpage-new-annotation');
        range.surroundContents(wrap);
      }
  }

  const clearNewAnnotationKey = (clear = false) => {
    const existing = document.querySelector('.songpage-new-annotation')

    if (existing) {
      if (clear) {
        // bandaid fix
        existing.replaceWith("")
      } else {
        existing.replaceWith(...existing.childNodes)
      }
    }
    setNewAnnotationKey("");
  }

  return (
    <div className="songpage" onClick={onAnnotationClick}>
      <header className="songpage-header">
        <img className="songpage-image" alt="Album Cover" src={song.image}/>
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

        <section className="songpage-lyrics" onMouseUp={onLyricSelection}>
          <h3>Lyrics</h3>
          {song &&
            <p> {
                lyricsHTML
              }
            </p>
          }
        </section>
        <section className="songpage-sidebar">
          <div className="songpage-annotation">
            <p className="songpage-annotation-text">
            </p>
          </div>
          <div className="songpage-add-annotation">
              Add annotation for key "{newAnnotationKey}"
              <AnnotationForm 
              lyricKey={newAnnotationKey}  
              songId={songId} 
              userId={user.id} 
              setAnnotations={setAnnotations}
              annotations={annotations}
              clearNewAnnotationKey={clearNewAnnotationKey}/>            
          </div>
          <div className="songpage-sidelinks">
            {(  authenticated &&
                <h3>{`${user.username}`}&mdash;select non-annotated lyric text to create a new annotation.</h3>
              )
              ||
              <h3>You must login to annotate lyrics.</h3>
            }

            {song && artistSongs &&
              <>
              <h3>Other songs by this artist</h3>
              {artistSongs.map((song, idx) => (
                <NavLink to={`/songs/${song.id}`} key={`${song.id}`}>{song.title}</NavLink>
              ))}
              </>
            }
          </div>
        </section>
      </div>
    </div>
  )
}

export default Song
