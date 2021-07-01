import React, { Component } from 'react';
import axios from 'axios';
//import {AiOutlineSearch} from 'react-icons/ai';

//file upload component

export default class DataForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
          //add global variable here -- not thread safe
            picture: null,
            isLoaded: false,
            data: null,
            errorMessage: ''
        };
    }

    //*********************************************************
    //for file upload and all
    //do it separately first, then see if I can combine the two
    handleFileChange = event => {
        this.setState({picture: event.target.files[0]});
    }

    handleFileUpload = () => {
        const fileData = new FormData();

        fileData.append(
            "thisFile",
            this.state.picture,
            this.state.picture.name
        );

        console.log('file uploaded');

        //axios.post('', fileData);
    }


//*********************************************************

    handleInputChanged = (e) => {
        this.setState({description: e.target.value});
    }

    handleSubmit = async (e) => {
        e.preventDefault();
        this.props.history.push('/predict')

        const description = this.state;

        const search = {
            description
        };

        // test body form to trigger backend response
        var bodyFormData = new FormData();
        bodyFormData.append('description', 'example description');
        bodyFormData.append('imageData', 'example image stub');

        await axios.post('http://127.0.0.1:5000/predict', bodyFormData)
            .then((result) => {
                this.setState({
                    isLoaded: true,
                    data: result,
                })
            })
            .catch(error => {
                this.setState({errorMessage: error.message});
                console.error('There was an error!', error);
            });
    };

    render() {
        return (
            <div className={'page-container'}>
                <div className={"form-container"}>
                        <h1 className="heading">Input Data</h1>
                            <form onSubmit={this.handleSubmit}>
                                {/*make into a text box, make button below*/}
                                <textarea type="input" name={"description"} placeholder={"Search Description"} onChange={this.handleInputChanged}/>
                                <input type={"file"} name={"file"}/>
                                <button type="submit" id="search-button" className="btn btn-primary">
                                    <i>Search</i>
                                </button>
                            </form>
                </div>
            </div>
        )
    }

}
