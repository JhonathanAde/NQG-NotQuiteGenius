import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import { login } from "../../services/auth";
import './form.css'

const LoginForm = ({active, authenticated, setAuthenticated, setUser }) => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await login(email, password);
    if (!data.errors) {
      setAuthenticated(true);
      setUser(data)
    } else {
      setErrors(data.errors);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (authenticated) {
    return <Redirect to="/" />;
  }

  return (
    <div className="form-container">
      {active? <form className="form-transition" onSubmit={onLogin}>
        <div>
          {errors.map((error) => (
            <div>{error}</div>
          ))}
        </div>
        <div className="form-inputs">
          <div className="form-input">
              {/* <label htmlFor="email">Email</label> */}
              <input
                name="email"
                type="text"
                placeholder="Email"
                value={email}
                onChange={updateEmail}
              />
          </div>
          <div className="form-input">
            {/* <label htmlFor="password">Password</label> */}
            <input
              name="password"
              type="password"
              placeholder="Password"
              value={password}
              onChange={updatePassword}
              />
          </div>
          <div className="form-input">
            <button type="submit">Login</button>
          </div>
        </div>
      </form> :
      <></>}
    </div>
  );
};

export default LoginForm;
