import React from 'react';
import { useHistory } from 'react-router-dom';
import ReactHtmlParser from 'react-html-parser';
import "./AnnotationList.css"

const AnnotationList = ({annoInfo, idx}) => {

  let history = useHistory();

  const {content, lyricKey, song} = annoInfo
  
  const {artist} = song

  const songReroute = () => {
    history.push(`/songs/${song.id}`)
  }
  const artistReroute = () => {
    history.push(`/artists/${artist.id}`)
  }
  return(
    <div className="annoblock">
      <div className="annoblock-header">
        <h3 className="annoblock-header_title" onClick={songReroute}>
          {song.title}
        </h3>
        <div className="divider">
        </div>
      <div className="annoblock-header_artist" onClick={artistReroute}>{artist.name}</div>
      </div>
      <div className="annoblock-content">
      <p className="annotation-lyrickey_header">Lyrics:</p>
      <p className="annotation-lyrickey">{ReactHtmlParser(lyricKey)}</p>
      <div>
      <p className="annotation-header">Annotation</p>
      <p className="annotation-content">"{content}"</p>
      </div>
      </div>
    </div>
  )
}

export default AnnotationList;