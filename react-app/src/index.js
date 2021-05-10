import React, { useEffect, useRef } from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';

import { setModalMount } from './store/index'
import App from './App';
import configureStore from './store'

import './index.css';

const store = configureStore();

function Root () {
  const dispatch = useDispatch();
  const modalMooringRef = useRef(null)

  useEffect(() => {
    dispatch(setModalMount(modalMooringRef.current));
  }, [dispatch]);

  return (
    <>
      <App />
      <div ref={modalMooringRef} className='modal' />
    </>
  );
};

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);
