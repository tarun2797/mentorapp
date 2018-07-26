import React,{ Component } from 'react';

class Header extends Component
{
    state=
    {
        isLoggedIn:this.props.isLoggedIn
    }

    toggleLoggedIn = () =>
    {
        this.setState(prev =>({isLoggedIn : !prev.isLoggedIn }))
    }

    render(){

        const {title} = this.props;
        const {isLoggedIn} = this.state;
        return(
            <div classname = "header">
            <h1> {title} </h1>
            <div classname = "menu" onClick = {this.toggleLoggedIn}>
            {
                isLoggedIn ? <span> LoggedOut </span> : <span> LoggedIn </span>
            }
            </div>
            </div>
        )
    }
}

export default Header