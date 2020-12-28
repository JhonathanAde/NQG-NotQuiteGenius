import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './NavBar.css'

const NavBar = ({ setAuthenticated }) => {
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
          <NavLink to="/login" exact={true} activeClassName="active">
            Login
          </NavLink>
          <NavLink to="/sign-up" exact={true} activeClassName="active">
            Sign Up
          </NavLink>
          <NavLink to="/users" exact={true} activeClassName="active">
            Users
          </NavLink>
          <LogoutButton setAuthenticated={setAuthenticated} />
      </div>
    </nav>
  );
}

export default NavBar;