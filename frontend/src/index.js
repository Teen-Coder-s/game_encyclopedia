import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import axios from 'axios';

// import components
import App from './App';

// import styles
import 'react-toastify/dist/ReactToastify.css';

axios.defaults.baseURL = 'http://127.0.0.1:8000';

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
          <ToastContainer
                position="top-right"
                autoClose={2500}
                draggable={false}
                pauseOnHover={false}
                closeOnClick
            />
          <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);
