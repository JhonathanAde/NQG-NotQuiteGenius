import React from 'react';
import { NavLink, useHistory } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './NavBar.css'

const NavBar = ({ setAuthenticated, authenticated, setUser, user }) => {

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

  const rerouteProfile = () => {
    history.push("/profile")
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
        <input type="search" className="search-bar" placeholder="search" />
      </div>
      <div className="user-buttons">
        {authenticated?
        <>
          <button onClick={rerouteCreate}>
            CREATE SONG
          </button>
          <button onClick={rerouteProfile}>
            {`${user.username}`}
            </button>
          <LogoutButton setAuthenticated={setAuthenticated} setUser={setUser} />
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
