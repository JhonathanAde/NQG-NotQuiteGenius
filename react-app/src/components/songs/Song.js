import React, { useState, useEffect } from 'react';
import { NavLink, Link, useParams } from 'react-router-dom';
import ReactHtmlParser from 'react-html-parser';
import {getArtist} from '../../services/artists'
import './Song.css';
import AnnotationForm from './AnnotationForm';
import PlayButton from '../audioPlayer/PlayButton';
import Lyrics from './Lyrics';


const Song = ({authenticated, user}) => {
  const [annotation, setAnnotation] = useState("");
  const [annotations, setAnnotations] = useState([]);
  const [lyricsKey, setLyricsKey] = useState(annotations.length);
  const [activateAnnotation, setActivateAnnotation] = useState(0);
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
    const updateAnnotations = async (song, annotations) => {
      let lyrics = song.lyrics;
      if (lyrics) {
        //Insure breaks are formatted for finding
        lyrics = lyrics.replaceAll(/<br ?\/?>/g, "<br>")
        annotations.forEach((annot, i) => {
          const key = annot.lyricKey
          lyrics = lyrics.replaceAll(key, `<span class="annotation-key" data-index="${i}">${key}</span>`)
        })
        setLyricsHTML(ReactHtmlParser(lyrics));

        await setLyricsKey(annotations.length)
        //Using async to be sure lyrics key is set prior to resetting activate annotation
        if (activateAnnotation) {
          setActivateAnnotation(0)
        }
      }
    }

    clearNewAnnotationKey(true);
    updateAnnotations(song, annotations);
    // Next line disables the warning on activateAnnotation
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [annotations, song])

  useEffect( () => {
    if (!song) return;
    (async () => {
        const res = await getArtist(song.artist.id)
        setArtistSongs(res.songs);
    })();
  },[song]);

  useEffect(() => {
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

    switchActiveSideBar();
  }, [newAnnotationKey, annotation]);


  const unHighlightKey = () => {
    const elementToReset = document.querySelector('.annotation-key.active');
    if (elementToReset) elementToReset.classList.remove('active');
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
        processSelection(range);
        if(sel.empty) {
          sel.empty()
        } else if (sel.removeAllRanges) {
          sel.removeAllRanges()
        }
      }
      else if (document.selection && document.selection.type !== "Control") {
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

      function processSelection(range) {
        clearNewAnnotationKey();
        const wrap = document.createElement('span');
        wrap.classList.add('songpage-new-annotation');
        range.surroundContents(wrap);
        setNewAnnotationKey(wrap.innerHTML);
      }
  }

  const clearNewAnnotationKey = () => {
    const existing = document.querySelector('.songpage-new-annotation')
    if (existing) {
      existing.replaceWith(...existing.childNodes)
    }
    setNewAnnotationKey("");
  }

  return (
    <div className="songpage" onClick={onAnnotationClick}>
      <header className="songpage-header">
        <div className="header-container">
          <img className="songpage-image" alt="Album Cover" src={song.image}/>
          <div className="songpage-info">
            { song &&
            <>
              <div className="songpage-title">
                <h1>{song.title}</h1>
                <PlayButton song={song}/>
              </div>
              <Link to={`/artists/${song.artist.id}`} className="artist-name">{song.artist.name}</Link>
            </>
            }
          </div>
        </div>
      </header>
      <div className="songpage-content">

        <section className="songpage-lyrics" onMouseUp={onLyricSelection}>
          <h3>Lyrics</h3>
          {song &&
            <Lyrics key={lyricsKey} lyricsHTML={lyricsHTML} activateAnnotation={activateAnnotation} />
          }
        </section>
        <section className="songpage-sidebar">
          <div className="songpage-annotation">
            <p className="songpage-annotation-text songpage-sticky">
            </p>
          </div>
          <div className="songpage-add-annotation">
            <div className="songpage-sticky">
              Add annotation for key:
              <div className="songpage-display-selection">
                {ReactHtmlParser(newAnnotationKey)}
              </div>
              <AnnotationForm
              lyricKey={newAnnotationKey}
              songId={songId}
              userId={user.id}
              setAnnotations={setAnnotations}
              annotations={annotations}
              clearNewAnnotationKey={clearNewAnnotationKey}
              setActivateAnnotation={setActivateAnnotation}/>
            </div>
          </div>
          <div className="songpage-sidelinks">
            <div className="songpage-sticky">
            {(  authenticated &&
                <h3>{`${user.username}`}&mdash;select non-annotated lyric text to create a new annotation.</h3>
              )
              ||
              <h3>You must login to annotate lyrics.</h3>
            }

            {song && artistSongs &&
              <>
              <h3>Songs by this artist:</h3>
              {artistSongs.map((song, idx) => (
                <NavLink className="song-link" to={`/songs/${song.id}`} key={`${song.id}`}>{song.title}</NavLink>
              ))}
              </>
            }
            </div>
          </div>
        </section>
      </div>
    </div>
  )
}

export default Song
