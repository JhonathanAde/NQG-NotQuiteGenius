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
import Profile from "./components/profile/Profile";
import SongForm from "./components/SongForm"
// import { user } from "./components/User"; 
// import Player from "./components/audioPlayer/AudioPlayer"

function App() {
  const [authenticated, setAuthenticated] = useState(false);
  const [user, setUser] = useState({})
  const [loaded, setLoaded] = useState(false);
  const [active, setActive] = useState(false)

  useEffect(() => {
    (async() => {
      const data = await authenticate();
      if (!data.errors) {
        setAuthenticated(true);
        setUser(data)
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
        <NavBar setAuthenticated={setAuthenticated} authenticated={authenticated} setUser={setUser} user={user}/>
        <Switch>
          <Route path="/sign-up" exact={true}>
            <div  className={`partition ${active? 'partition-login': 'partition-sign-up'}`}>
              <div className="switch-container">
                <h1 className={active? 'login-hidden' : 'login-active'} onClick={toggleClass}>Login</h1>
                <h1 className={active? 'sign-up-active' : 'sign-up-hidden'} onClick={toggleClass}>Sign Up</h1>
                <div className="laptop-icon"></div>
              </div>
            </div>
            <div className="form-page">
              <LoginForm authenticated={authenticated} active={active}setAuthenticated={setAuthenticated} setUser={setUser} />
              <SignUpForm authenticated={authenticated} active={active} setAuthenticated={setAuthenticated}  setUser={setUser}/>
            </div>
          </Route>
          <Route path="/songs/:songId" exact={true}>
            <Song authenticated={authenticated} user={user}/>
          </Route>
          <Route path="/artists/:artistId" exact={true}>
              <Artist />
          </Route>
          <ProtectedRoute path="/profile" exact={true} authenticated={authenticated}>
              <Profile user={user} />
          </ProtectedRoute>
          <ProtectedRoute path="/users" exact={true} authenticated={authenticated}>
            <UsersList/>
          </ProtectedRoute>
          <ProtectedRoute path="/users/:userId" exact={true} authenticated={authenticated}>
            <User />
          </ProtectedRoute>
          <ProtectedRoute path="/create-song" exact={true} authenticated={authenticated}>
            <SongForm />
          </ProtectedRoute>
          <Route path="/" exact={true} authenticated={authenticated}>
            <Home />
          </Route>

          {/* <Route path="/song-form-test" exact={true}>
            <SongForm />
          </Route>
          <Route path="/audio-player" exact={true}>
            <Player />
          </Route> */}
      </Switch>
        <div className="push"></div>
      </div>
      <Footer className="footer"/>
    </BrowserRouter>
  );
}

export default App;
