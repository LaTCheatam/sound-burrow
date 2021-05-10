import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";    
import { BrowserRouter, Route, Switch } from "react-router-dom";

import NavBar from "./components/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import Modal from './components/Modal';

import { authenticate } from "./store/session";

export default function App() {
  const dispatch = useDispatch()

  const user = useSelector(state => state.session.user)

  useEffect(() => {
    dispatch(authenticate());
  }, [dispatch]);

  return (
    <BrowserRouter>
      <NavBar />
      <Modal />
      <Switch>
        <ProtectedRoute path="/users" exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path="/users/:userId/dashboard" exact={true} >
          <User />
        </ProtectedRoute>
        <Route path="/" exact={true}>
          <h1>My Home Page</h1>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

