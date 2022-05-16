import React from 'react';
import { HashRouter as Router } from 'react-router-dom'; // added
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
ReactDOM.render(
  <Router>
    <App />
  </Router>
  , document.getElementById('root'));
