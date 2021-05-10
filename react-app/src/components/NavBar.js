import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import { useDispatch } from 'react-redux';

import { showModal, setCurrentModal } from '../store/modal';
import LoginForm from '../components/auth/LoginForm';
import SignupForm from '../components/auth/SignUpForm';

const NavBar = () => {
  const dispatch = useDispatch();
  const showLogin = () => { 
    dispatch(setCurrentModal(LoginForm))
    dispatch(showModal())
  };

  const showLogin = () => { 
    dispatch(setCurrentModal(SignupForm))
    dispatch(showModal())
  };

  return (
    <nav>
      <ul>
        <li>
          <NavLink to="/" exact={true} activeClassName="active">
            Home
          </NavLink>
        </li>
        <li>
          <button onClick={showLogin}>
            Log In
          </button>
        </li>
        <li>
          <button onClick={showSignup}>
            Sign Up
          </button>
        </li>
        <li>
          <NavLink to="/users" exact={true} activeClassName="active">
            Users
          </NavLink>
        </li>
        <li>
          <LogoutButton />
        </li>
      </ul>
    </nav>
  );
}

export default NavBar;
