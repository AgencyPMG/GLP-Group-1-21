import React, { Component, useEffect } from 'react';
//import axios from 'axios';


class PredictionPage extends Component {
    constructor(props) {
        super(props)
        this.state = {
            categories: [
                {category: "jeans", prediction: "95%"},
                {category: "shirt", prediction: "5%"}
            ]
        }
        }

    renderTableData() {
        return this.state.categories.map((item, index) => {
            const {category, prediction} = item
            return (
                <tr key={category}>
                    <td>{category}</td>
                    <td>{prediction}</td>
                </tr>
            )
        })
    }

    renderTableHeader() {
        let header = Object.keys(this.state.categories[0])
        return header.map((key, index) => {
            return <th key={index}>{key.toUpperCase()}</th>
        })
    }

    render() {
        return (
            <div className={"page-container"} id={"second-page"}>
                <div className={"pred-container"}>
                    <h1>Model Prediction</h1>
                    <h2 className={"heading-pred"}>Confidence Prediction Table</h2>
                    <div className={"table-container"}>
                        <table id={"categories"}>
                            <tbody>
                            <tr>{this.renderTableHeader()}</tr>
                            {this.renderTableData()}
                            </tbody>
                        </table>
                    </div>
                    <div className={"category-container"}>
                        <form onSubmit={this.handleSubmit}>
                            <input className={"input-form"} id="category-product" type={"text"} name={"correct-category"} placeholder={"Enter Correct Category"} onChange={this.handleInputChanged}/>
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



export default PredictionPage;


