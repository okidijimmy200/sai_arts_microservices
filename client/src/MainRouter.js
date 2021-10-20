import React from 'react'
import {Route, Switch} from 'react-router-dom'
import Menu from './core/Menu'
import Home from './core/home'
import Login from './users/login'
import NewPicture from './pictures/NewPicture'

export default function MainRouter() {
    return (
        <>
            {/* <Menu /> */}
            <Switch>
                <Route path='/login' component={Login} />
                <Route path='/artist' component={NewPicture} exact/>
                <Route exact path='/' component={Home} />
            </Switch>
            
        </>
    )
}
