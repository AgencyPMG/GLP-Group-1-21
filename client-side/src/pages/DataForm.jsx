import React, {Component, useEffect} from 'react';
import axios from 'axios';
import Logo from '../assets/PMG_Logo_CMYK_FullColor_RLSD (1).png';


export default class DataForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
          //add global variable here -- not thread safe
            description: '',
            age: '',
            gender: '',
            size: '',
            image_url: '',
            isLoaded: false,
            errorMessage: '',
            data: ''
        };
        this.handleInputChanged = this.handleInputChanged.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    //*********************************************************
    //for file upload and all
    //do it separately first, then see if I can combine the two
    /*
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
*/

//*********************************************************

    handleInputChanged = (e) => {
        this.setState({[ e.target.name]: e.target.value });
    }

    handleSubmit = async (e) => {
        e.preventDefault();

        var bodyFormData = this.state.description + '+' + this.state.gender + '+' + this.state.age+ '+' +
            this.state.size+ '+' + this.state.image_url;

        await axios.get('http://127.0.0.1:5000/predict?seq=' + bodyFormData)
            .then((result) => {

                this.setState({data: result})
            })
            .catch(error => {
                this.setState({errorMessage: error.message});
                console.error('There was an error!', error);
            });
        this.props.history.push({
            pathname: '/predict',
            data: this.state.data}) //redirects to predict route
    };


    render() {
        return (
            <div className={'page-container'}>
                <div className={"form-container"}>
                    <img src={Logo} className={"logo-photo"} alt={"PMG Logo"}/>
                        <h1 className="heading">Find Product Category</h1>
                    <div className={"container"}>
                            <form onSubmit={this.handleSubmit}>
                                {/*<input className={"file-upload"} type={"file"} name={"file"}/>*/}
                                <textarea className={"text-box"} name={"description"} placeholder={"Description"} onChange={this.handleInputChanged}/>
                                <input className={"input-form"} type={"text"} name={"gender"} placeholder={"gender"} onChange={this.handleInputChanged}/>
                                <input className={"input-form"}  type={"text"} name={"age"} placeholder={"age group"} onChange={this.handleInputChanged}/>
                                <input className={"input-form"}  type={"text"} name={"size"} placeholder={"size"} onChange={this.handleInputChanged}/>
                                <input className={"input-form"}  type={"text"} name={"image-url"} placeholder={"image url"} onChange={this.handleInputChanged}/>
                                <button type="submit" id="search-button" className="btn-gradient blue">Submit</button>
                            </form>
                </div>
            </div>
            </div>
        )
    }

}
