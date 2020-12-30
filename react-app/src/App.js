import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import { authenticate } from "./services/auth";
import Home from "./components/home/Home";
import './index.css'
import Footer from "./components/Footer";
import Song from "./components/songs/Song";
import Artist from "./components/artists/Artists";

import SongForm from "./components/SongFormTest"

function App() {
  const [authenticated, setAuthenticated] = useState(false);
  const [loaded, setLoaded] = useState(false);
  const [active, setActive] = useState(false)

  useEffect(() => {
    (async() => {
      const user = await authenticate();
      if (!user.errors) {
        setAuthenticated(true);
      }
      setLoaded(true);
    })();
  }, []);

    const toggleClass = () => {
      const currentState = active
      setActive(!currentState);
  };


  if (!loaded) {
    return null;
  }


  return (
    <BrowserRouter>
      <div className="wrapper">
        <NavBar setAuthenticated={setAuthenticated} authenticated={authenticated}/>
        <Switch>
          <Route path="/login" exact={true}>
            <LoginForm
              authenticated={authenticated}
              setAuthenticated={setAuthenticated}
            />
            <SignUpForm
              authenticated={authenticated}
              setAuthenticated={setAuthenticated}
            />
          </Route>
          <Route path="/sign-up" exact={true}>
            <div  className={`partition ${active? 'partition-login': 'partition-sign-up'}`}>
              <h1 className={active? 'login-hidden' : 'login-active'} onClick={toggleClass}>Login</h1>
              <h1 className={active? 'sign-up-active' : 'sign-up-hidden'} onClick={toggleClass}>Sign Up</h1>
            </div>
            <div className="form-page">
              <LoginForm authenticated={authenticated} setAuthenticated={setAuthenticated} />
              <SignUpForm authenticated={authenticated} setAuthenticated={setAuthenticated} />
            </div>
          </Route>
          <Route path="/songs/:songId" exact={true} authenticated={authenticated}>
            <Song />
          </Route>
          <Route path="/artists/:artistId" exact={true}>
              <Artist />
          </Route>
          <ProtectedRoute path="/users" exact={true} authenticated={authenticated}>
            <UsersList/>
          </ProtectedRoute>
          <ProtectedRoute path="/users/:userId" exact={true} authenticated={authenticated}>
            <User />
          </ProtectedRoute>
          <Route path="/" exact={true} authenticated={authenticated}>
            <Home />
          </Route>


          <Route path="/song-form-test" exact={true}>
            <SongForm />
          </Route>

        </Switch>
        <div className="push"></div>
      </div>
      <Footer className="footer"/>
    </BrowserRouter>
  );
}

export default App;
