import React from 'react';
import { NavLink, useHistory } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './NavBar.css'

const NavBar = ({ setAuthenticated, authenticated, setUser, user }) => {

  const doSearch = (e) => {
    const value = document.getElementById('search').value;
    (async () => {
      const response = await fetch(`/api/search?search_string=${value}`);
      const results = await response.json();
      console.log(results)
    })();
  }

  let history = useHistory()
  const rerouteHome = () => {
    history.push("/")
  }

  const rerouteRegister = () => {
    history.push("/sign-up")
  }

  const rerouteCreate = () => {
    history.push("/create-song")
  }

  return (
    <nav className="nav-bar">
      <div className="logo">
        <div className="radio"></div>
        <div className="home-link" onClick={rerouteHome}>
          NQG
        </div>
      </div>
      <div className="search-container">
        <input id="search" type="search" className="search-bar" placeholder="search" />
        <button onClick={doSearch}>Search</button>
      </div>
      <div className="user-buttons">
        {authenticated?
        <>
          <LogoutButton setAuthenticated={setAuthenticated} setUser={setUser} />
          <NavLink to="/profile">
            {`${user.username}`}
            </NavLink>
            <button onClick={rerouteCreate}>
              CREATE SONG
            </button>
          </>
          :
          <>
            <button onClick={rerouteRegister}>Register</button>
            {/* <NavLink to="/" */}
            {/* <NavLink to="/sign-up" exact={true} activeClassName="active">
              Sign Up
            </NavLink> */}
            {/* <NavLink to="/users" exact={true} activeClassName="active">
              Users
            </NavLink> */}
          </>
        }
      </div>
    </nav>
  );
}

export default NavBar;
