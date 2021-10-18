import React from "react";
import MainRouter from './MainRouter'
import { BrowserRouter } from 'react-router-dom'

export function App() {
    return (
        <BrowserRouter>
            <MainRouter />
        </BrowserRouter>
    )
}