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
            <div>
                <h1>This is our prediction blah blah blah</h1>
                <h2 className={"heading-pred"}>Confidence Prediction Table</h2>
                <div className={"table-container"}>
                    <table id={"categories"}>
                        <tbody>
                        <tr>{this.renderTableHeader()}</tr>
                        {this.renderTableData()}
                        </tbody>
                    </table>
                </div>
            </div>
        )
    }
}



export default PredictionPage;


