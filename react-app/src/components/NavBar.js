import React from 'react';
import { NavLink, useHistory } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './NavBar.css'

const NavBar = ({ setAuthenticated, authenticated, setUser, user }) => {

  const doSearch = (e) => {
    e.stopPropagation();
    const value = document.getElementById('search').value;
    if (value) {
      (async () => {
        const response = await fetch(`/api/search?search_string=${value}`);
        const results = await response.json();
        console.log(results)
      })();
    }
  }

  const clearSearch = (e) => {
    const target = e.target;
    if (target) {
      if (target.closest('.search-container')) return;
    }
    console.log('hiding', e.target)
    document.getElementById('search').value = null;
    document.getElementById('search-results').style.display = null;
  }

  const displaySearchInfo = (e) => {
    console.log("displaying")
    document.getElementById('search-results').style.display = 'block';
  }

  let history = useHistory()
  const rerouteHome = () => {
    history.push("/")
  }

  const rerouteRegister = () => {
    history.push("/sign-up")
  }
  const rerouteProfile = () => {
    history.push("/profile")
  }

  const rerouteCreate = () => {
    history.push("/create-song")
  }

  return (
    <nav className="nav-bar" onClick={clearSearch}>
      <div className="logo">
        <div className="radio"></div>
        <div className="home-link" onClick={rerouteHome}>
          NQG
        </div>
      </div>
      <div className="search-container" onClick={displaySearchInfo} >
        <input id="search" type="search" className="search-bar" placeholder="search" />
        <button className="search-button" onClick={doSearch}><i className="fas fa-search"></i></button>
        <div id="search-results"></div>
      </div>
      <div className="user-buttons">
        {authenticated?
        <>
          <button className="nav-button" onClick={rerouteProfile}>
            <i className="profileButton fas fa-user-circle" ></i>
            </button>
            <button className="nav-button" onClick={rerouteCreate}>
              Create Song
            </button>
            <LogoutButton setAuthenticated={setAuthenticated} setUser={setUser} />
          </>
          :
          <>
            <button className="nav-button" onClick={rerouteRegister}>Register</button>
          </>
        }
      </div>
    </nav>
  );
}

export default NavBar;
