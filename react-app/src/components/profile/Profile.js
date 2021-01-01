import React, { useState, useEffect, } from 'react';
import './Profile.css';
import {getAnnotations} from '../../services/annotation'
import AnnotationList from './AnnotationList';


const Profile = ({ user }) => {
    const [annotation, setAnnotation] = useState(null)
    useEffect( () => {
        (async () => {
            const res = await getAnnotations(user.id)
            setAnnotation(res)
        })()
    },[user.id]);
  return (
      <div className="profilepage">
      <header className="profilepage-header">
        <div className="header-container">
          <div className="profilepage-image" alt="Cover Image">
            <i className="fas fa-user-circle fa-10x" />
          </div>
          <div className="profilepage-info">
          <div className="profilepage-title">{user.username}</div> 
          <div className="profilepage-email">{user.email}</div>
        </div>
        </div>
      </header>
      <div className="profilepage-content">
        <section className="profilepage-lyrics">
          <h1>Annotations</h1>
        {annotation && annotation.annotations.map((annoInfo, idx) => (
          <AnnotationList key={idx} annoInfo={annoInfo} idx={idx}/>
        ))}
        </section>
      </div>
      </div>
  )
}

export default Profile
