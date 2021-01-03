import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './NavBar.css'
import Search from './search/Search'

const NavBar = ({ setAuthenticated, authenticated, setUser, user }) => {
  const [lastSearch, setLastSearch] = useState('')

  const clearSearch = (e) => {
    const target = e.target;

    if (target
        && !target.classList.contains('search-link')
        && !target.closest('.search-close')) {
      if (target.closest('.search-container')) return;
    }
    const searchInput = document.getElementById('search');
    searchInput.value = null;
    document.getElementById('search-results').style.display = null;
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
      <Search clearSearch={clearSearch} lastSearch={lastSearch} setLastSearch={setLastSearch}/>
      <div className="user-buttons">
        {authenticated?
        <>
          <button className="nav-button" onClick={rerouteProfile}>
            <div className="profileButton">
              {<i className="fas fa-user-circle " ></i>}
            </div>
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
