import React, { useState, useEffect, } from 'react';
import { NavLink, Link, useParams } from 'react-router-dom';
import './Profile.css';
import {getArtist} from '../../services/artists'
import {getAnnotations} from '../../services/annotation'
import SongTile from '../home/SongTile';


const Profile = ({authenticated, user}) => {
    const [annotation, setAnnotation] = useState(null)
    const [artist, setArtist] = useState(null)
    const {artistId, userId} = useParams();
    console.log(user.id)
    console.log(artistId)
    useEffect( () => {
        (async () => {
            const res = await getAnnotations(user.id)
            setAnnotation(res.annotations)
        })()
    },[]);
    console.log("annotations", annotation)
  return (
    <div className="profilepage">
      <header className="profilepage-header">
        <img className="profilepage-image" alt="Cover Image"/>
        <div className="profilepage-info">
           <h1 className="profilepage-title">{user.username}</h1> 
        </div>
      </header>
      <div className="profilepage-content">
        <section className="profilepage-lyrics">
        </section>
        <section className="profilepage-sidebar">
          <div className="profilepage-sidelinks">
            <NavLink to="/songs/1">Song 1</NavLink>
            <NavLink to="/songs/2">Song 2</NavLink>
          </div>
        </section>
      </div>
    </div>
  )
}

export default Profile
