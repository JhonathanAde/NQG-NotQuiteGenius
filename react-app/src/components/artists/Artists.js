import React, { useState, useEffect, } from 'react';
import { NavLink, Link, useParams } from 'react-router-dom';
import {getArtist} from '../../services/artists'
import SongTile from '../home/SongTile';
import './artists.css'


const Artist = () => {
    const [artist, setArtist] = useState(null)
    const {artistId} = useParams();

    useEffect( () => {
        (async () => {
            const res = await getArtist(artistId)
            setArtist(res)
        })()
    },[]);
    console.log(artist)
  return (
    <div className="songpage">
      <header className="songpage-header">
        <img className="songpage-image" alt="Album Cover"/>
        <div className="songpage-info">
          {artist && <h1 className="songpage-title">{artist.name}</h1> }
        </div>
      </header>
      <div className="artistpage-content">
            {artist && artist.songs.map((song, idx) => (
                <SongTile song={song} idx={idx + 1}/>
            ))}
      </div>
    </div>
  )
}

export default Artist
