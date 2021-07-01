import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";

import DataForm from "./DataForm";
import PredictionPage from "./PredictionPage";

const Webpages = () => {
    return (
        <Router>
            {/*router paths*/}
            <Route exact path="/" component={DataForm}/>
            <Route path="/predict" component={PredictionPage}/>
        </Router>
    );
};


export default Webpages;