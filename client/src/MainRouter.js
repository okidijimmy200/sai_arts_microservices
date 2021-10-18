import React from 'react'
import {Route, Switch} from 'react-router-dom'
import Menu from './core/Menu'
import Home from './core/home'

export default function MainRouter() {
    return (
        <>
            <Menu />
            <Switch>
                <Route exact path='/' component={Home} />
            </Switch>
            
        </>
    )
}
