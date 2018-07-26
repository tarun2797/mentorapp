
import React, { Component } from 'react';
class ExampleComponent extends Component
{
    render()
    {
        const isLoggedIn = 0;
        return (
        <div>
        The user is <b>{isLoggedIn ? 'currently' : 'not'}</b> logged in.
        </div>
        );
    }
}

export default ExampleComponent;
