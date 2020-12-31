import React, {useState, useEffect} from 'react';
import { Navlink, Link, useParams } from 'react-router-dom';
import "./AnnotationList.css"

const AnnotationList = ({annoInfo, idx}) => {

  const {content, lyricKey, song} = annoInfo
  console.log(content)
  console.log(song)
  const {artist} = song
  return(
    <div className="annoblock">
      <div className="annoblock-header">
      <h3 className="annoblock-header_title">{song.title}</h3>
      <h7 className="annoblock-header_artist">{artist.name}</h7>
      </div>
      <div className="annoblock-content">
      <p className="annotation-lyrickey_header">Lyrics:</p>
      <p className="annotation-lyrickey">{lyricKey}</p>
      <div>
      <p className="annotation-header">Annotation</p>
      <p className="annotation-content">"{content}"</p>
      </div>
      </div>
    </div>
  )
}

export default AnnotationList;