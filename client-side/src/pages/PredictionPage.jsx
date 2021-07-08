import React, { Component, useEffect } from 'react';
import axios from "axios";
import data from "bootstrap/js/src/dom/data";
//import axios from 'axios';


class PredictionPage extends Component {
    constructor(props) {
        super(props)
        this.state = {
            data: '',
            isLoaded: false,
        }
    }

    renderTableData() {
        const data_dict = this.state.data;
        var dict_list = []

        Object.entries(data_dict).map(([key, value]) => {
            var entry = {}
            entry[key] = value;
            dict_list.push(entry);
        })
            return dict_list.map((item, index) => {
            const category = Object.keys(item)[0];
            const prediction = dict_list[Object.keys(item)[0]];
            console.log(item);
            console.log(dict_list[category]);
            return (
                <tr key={category}>
                    <td>{category}</td>
                    <td>{prediction}</td>
                </tr>
            )
        })
    }

    componentDidMount() {
        fetch('http://127.0.0.1:5000/predict?seq=' + this.state.description, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json;charset=UTF-8'
            },
        }).then(async (result) => {
                const resp = await result.json();
                if (result.status === 200) {
                    this.setState({
                        isLoaded: true,
                        data: resp
                    });
                } else {
                    alert(resp.message); // TODO make real notification
                    this.setState({
                        isLoaded: true,
                        error: resp
                    });
                }
            })
            .catch(error => {
                this.setState({errorMessage: error.message});
                console.error('There was an error!', error);
            });
    }

    render() {
        const {isLoaded, data, error} = this.state;
        if (error) {
            return <div className="error">Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            return (
                <div className={"page-container"} id={"second-page"}>
                    <div className={"pred-container"}>
                        <h1>Model Prediction</h1>
                        <h2 className={"heading-pred"}>Confidence Prediction Table</h2>
                        <div className={"table-container"}>
                            <table id={"categories"}>
                                <tbody>
                                <tr>test</tr>
                                {this.state.isLoaded ? this.renderTableData() : "Loading.."}
                                </tbody>
                            </table>
                        </div>
                        <div className={"category-container"}>
                            <form onSubmit={this.handleSubmit}>
                                <input id={"category-product"} className={"input-form"} type={"text"}
                                       name={"category-product"} placeholder={"Enter the correct category"}
                                       onChange={this.handleInputChanged}/>

                                <button type="submit" id="search-button" className="btn-gradient blue">Submit</button>
                            </form>
                        </div>
                        <div className={"button-container"}>
                            <a type="submit" href="/" id={"return-button"} className="btn-gradient blue">Return</a>
                        </div>
                    </div>
                </div>
            )
        }
    }
}



export default PredictionPage;


