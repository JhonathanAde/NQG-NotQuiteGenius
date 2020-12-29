import React, { useState, useEffect, } from 'react';
import { NavLink, Link, useParams } from 'react-router-dom';
import './Artists.css';
import {getArtist} from '../../services/artists'
import SongTile from '../home/SongTile';


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
      <div className="songpage-content">
        <section className="songpage-lyrics">
            {artist && artist.songs.map((song, idx) => (
                <SongTile song={song} idx={idx + 1}/>
            ))}
        </section>
        <section className="songpage-sidebar">
          <div className="songpage-sidelinks">
            <NavLink to="/songs/1">Song 1</NavLink>
            <NavLink to="/songs/2">Song 2</NavLink>
          </div>
        </section>
      </div>
    </div>
  )
}

export default Artist
