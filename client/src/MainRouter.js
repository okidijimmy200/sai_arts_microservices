import React from 'react'
import {Route, Switch} from 'react-router-dom'
import Menu from './core/Menu'
import Home from './core/home'
import Login from './users/login'

export default function MainRouter() {
    return (
        <>
            {/* <Menu /> */}
            <Switch>
                <Route path='/login' component={Login} />
                <Route exact path='/' component={Home} />
            </Switch>
            
        </>
    )
}
