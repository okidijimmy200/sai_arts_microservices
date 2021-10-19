require('file-loader?name=[name].[ext]!../public/index.html')
import React from "react";
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import "@babel/polyfill";
import store from './store'
import { App } from './App'

import './index.scss'


ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>, 
    document.getElementById('root')
)