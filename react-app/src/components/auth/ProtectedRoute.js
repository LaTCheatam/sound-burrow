import React from 'react';
import { useSelector } from "react-redux";
import { Route, Redirect } from 'react-router-dom';

const ProtectedRoute = props => {
  const user = useSelector(state => state.session.user)
  const sessionLoaded = useSelector(state => state.session.loaded);

  return (
    <Route {...props}>
      {(sessionLoaded && user)
      ? props.children  
      : (sessionLoaded && !user)
        ? <Redirect to="/" />
        : null}
    </Route>
  )
};


export default ProtectedRoute;
