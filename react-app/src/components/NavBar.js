import React from 'react';
import { NavLink, useHistory } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './NavBar.css'
import Search from './search/Search'

const NavBar = ({ setAuthenticated, authenticated, setUser, user }) => {

  const clearSearch = (e) => {
    const target = e.target;
    if (target) {
      if (target.closest('.search-container')) return;
    }
    document.getElementById('search').value = null;
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
      <Search clearSearch={clearSearch}/>
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
