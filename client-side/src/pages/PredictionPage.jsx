import React, { Component, useEffect } from 'react';


class PredictionPage extends Component {
    constructor(props) {
        super(props)
            this.state = {
                //add global variable here -- not thread safe
                categories: this.props.location.data.data
            };

            console.log(this.state.categories);
    }

    renderTableData() {
        //make an array to convert dictionary to list of objects
        var arr = [];
        for (var key of Object.entries(this.state.categories)) {
            var cat = key[0];
            var val = key[1];
            console.log(cat)
            console.log(val)
            arr.push({category : key[0], prediction : key[1]})
        }

        console.log(arr)

        return arr.map((item, index) => {
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
        let header = ['Category', 'Predictions']
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
                        <form>
                            <input id={"category-product"} className={"input-form"} type={"text"} placeholder={"Enter the correct category"}/>
                            <button type="button" id="search-button" className="btn-gradient blue">Submit</button>
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


