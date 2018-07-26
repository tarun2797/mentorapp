import React from 'react';
class CollegesList extends React.Component{
    state={
        data:null
    }
    componentDidMount(){
        fetch('http://127.0.0.1:8000/api/colleges/')
            .then(response=>response.json())
            .then(responseJson => {console.log(responseJson);this.setState({data:responseJson});})
            .catch(e=>{console.log("Error Occured");});
    }
    render()
    {
        return(
            <div>
                <h2>
                    Colleges List
                </h2>
                {
                    this.state.data ?this.state.data.map(college =><p> {college.name} is at {college.location}</p>): <p>loading...</p>
                }
            </div>
        );
    }
}

export default CollegesList;