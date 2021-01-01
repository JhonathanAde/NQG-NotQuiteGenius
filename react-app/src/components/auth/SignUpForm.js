import React, { useState } from "react";
import { Redirect } from 'react-router-dom';
import { signUp } from '../../services/auth';
import './form.css'

const SignUpForm = ({active, authenticated, setAuthenticated, setUser}) => {
  const [username, setUsername] = useState("");
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await signUp(username, email, password);
      if (!data.errors) {
        setAuthenticated(true);
        setUser(data)
      }  else {
      setErrors(data.errors);
      }
    } else {
      setErrors(["Your passwords must match"])
    }

  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (authenticated) {
    return <Redirect to="/" />;
  }

  return (
    <div className="form-container">
      {!active? <form className="form-transition" onSubmit={onSignUp}>
        <div>
          {errors.map((error) => (
            <div>{error}</div>
          ))}
        </div>
        <div className="form-inputs">
          <div className="form-input">
            {/* <label>User Name</label> */}
            <input
              type="text"
              name="username"
              placeholder="User Name"
              onChange={updateUsername}
              value={username}
            ></input>
          </div>
          <div className="form-input">
            {/* <label>Email</label> */}
            <input
              type="text"
              name="email"
              placeholder="Email"
              onChange={updateEmail}
              value={email}
            ></input>
          </div>
          <div className="form-input">
            {/* <label>Password</label> */}
            <input
              type="password"
              name="password"
              placeholder="Password"
              onChange={updatePassword}
              value={password}
            ></input>
          </div>
          <div className="form-input">
            {/* <label>Repeat Password</label> */}
            <input
              type="password"
              name="repeat_password"
              placeholder="Repeat Password"
              onChange={updateRepeatPassword}
              value={repeatPassword}
              required={true}
            ></input>
          </div>
          <div className="form-input">
            <button type="submit">Sign Up</button>
          </div>
        </div>
      </form> :
      <></>}
    </div>
  );
};

export default SignUpForm;
