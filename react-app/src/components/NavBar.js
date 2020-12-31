import React from 'react';
import { NavLink, useParams } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './NavBar.css'

const NavBar = ({ setAuthenticated, authenticated, setUser, user }) => {

  return (
    <nav className="nav-bar">
      <div className="logo">
          <NavLink to="/" exact={true} activeClassName="active">
            NQG
          </NavLink>
      </div>
      <div className="search-container">
        <input type="search" className="search-bar" placeholder="search" />
      </div>
      <div className="user-buttons">
<<<<<<< HEAD
        {authenticated?
        <>
          <LogoutButton setAuthenticated={setAuthenticated} setUser={setUser} />
          <NavLink to="/profile">
            {`${user.username}`}
            </NavLink>
        </>
          :
=======
        {authenticated? 
          <>
            <LogoutButton setAuthenticated={setAuthenticated} setUser={setUser}/>
            <NavLink to="/create-song" exact={true} activeClassName="active">
              Create Song
            </NavLink>
          </>
          : 
>>>>>>> main
          <>
            <NavLink to="/sign-up" exact={true} activeClassName="active">
              Register
            </NavLink>
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
