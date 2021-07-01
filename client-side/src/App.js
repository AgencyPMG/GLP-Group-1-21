import './App.scss';
import './index.css'
import React, { Component } from "react";
//import pages for router
import {
    BrowserRouter as Router,
    Route,
    Switch,
    Link,
    Redirect
} from "react-router-dom";
import './index.css'

//pages
import Webpages from './pages';





function App() {
    return (
        <div>
            <Webpages/>
        </div>
  );
}



export default App;
