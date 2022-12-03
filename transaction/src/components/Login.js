
import React, { useState } from "react"
import {useNavigate} from "react-router-dom"

export default function (props) {
  let [authMode, setAuthMode] = useState("signin")
  let history= useNavigate();

  const changeAuthMode = () => {
    setAuthMode(authMode === "signin" ? "signup" : "signin")
  }

  const [fullName, setfullName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  
  const handleClick = async (e) => {
    e.preventDefault();
    console.log("hi") 
    try {
      const response = await fetch('http://localhost:8080/Createuser', {
        method: 'POST',
        body: JSON.stringify({
          first_name: fullName,
          username: email,
          password: password
        }),
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'

        },
      }).then((response) => response.json())
        .then((data) => {
          console.log(data);
          if (data.Message === "User Created"){
            window.alert("User Successfully Created")
            changeAuthMode();
          }
        })

      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }

      const result = await response.json();

      console.log('result is: ', JSON.stringify(result, null, 4));

    }

    catch (err) {
      console.log(err.message);
    }

  };

  const LoginClick = async (e) => {
    e.preventDefault();
    console.log("hi") 
    try {
      const response = await fetch('http://localhost:8080/login', {
        method: 'POST',
        body: JSON.stringify({
          username: email,
          password: password
        }),
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'

        },
      }).then((response) => response.json())
        .then((data) => {
          console.log(data);
          if (data === "Login Successfully"){
            history("/home")
          }
        })

      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }

      const result = await response.json();

      console.log('result is: ', JSON.stringify(result, null, 4));

    }

    catch (err) {
      console.log(err.message);
    }

  };

  if (authMode === "signin") {
    return (
      <div className="Auth-form-container">
        <form className="Auth-form">
          <div className="Auth-form-content">
            <h3 className="Auth-form-title">Sign In</h3>
            <div className="text-center">
              Not registered yet?{" "}
              <span className="link-primary" onClick={changeAuthMode}>
                Sign Up
              </span>
            </div>
            <div className="form-group mt-3">
              <label>Email address</label>
              <input
                type="email"
                className="form-control mt-1"
                placeholder="Enter email"
              />
            </div>
            <div className="form-group mt-3">
              <label>Password</label>
              <input
                type="password"
                className="form-control mt-1"
                placeholder="Enter password"
              />
            </div>
            <div className="d-grid gap-2 mt-3">
              <button onClick = {(LoginClick)} type="submit" className="btn btn-primary">
                Submit
              </button>
            </div>
            <p className="text-center mt-2">
              Forgot <a href="#">password?</a>
            </p>
          </div>
        </form>
      </div>
    )
  }


  return (
    <div className="Auth-form-container">
      <form className="Auth-form">
        <div className="Auth-form-content">
          <h3 className="Auth-form-title">Sign Up</h3>
          
          <div className="text-center">
            Already Registered?{" "}
            <span className="link-primary" onClick={changeAuthMode}>
              Sign In
            </span>
          </div>
          <div className="form-group mt-3">
            <label>First Name</label>
            <input
              type="text"
              className="form-control mt-1"
              name="firstname"
              value={fullName}
              onChange={(event) => setfullName(event.target.value)}
              placeholder="e.g Jane"
            />
          </div>
          <div className="form-group mt-3">
          <label>Last Name</label>
            <input
              type="text"
              className="form-control mt-1"
              name="lastname"
              value={fullName}
              onChange={(event) => setfullName(event.target.value)}
              placeholder="e.g Lim"
            />
          </div>
          <div className="form-group mt-3">
            <label>Username</label>
            <input
              type="text"
              className="form-control mt-1"
              name="username"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              placeholder="Email Address"
            />
          </div>
          <div className="form-group mt-3">
            <label>Email address</label>
            <input
              type="email"
              className="form-control mt-1"
              name="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              placeholder="Email Address"
            />
          </div>
          <div className="form-group mt-3">
            <label>Password</label>
            <input
              type="password"
              className="form-control mt-1"
              name="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              placeholder="Password"
            />
          </div>
          <div className="d-grid gap-2 mt-3">
            <button onClick= {(handleClick)} className="btn btn-primary">
              Submit
            </button>
          </div>
          <p className="text-center mt-2">
            Forgot <a href="#">password</a>?
          </p>
        </div>
      </form>
    </div>
  )
}
