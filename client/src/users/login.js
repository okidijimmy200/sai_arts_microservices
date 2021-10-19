import React, {useState, useEffect} from 'react'
import { Link } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import { login } from './../actions/userActions'

export default function Login({history, location}) {
    const [email , setEmail] = useState('')
    const [password, setPassword] = useState('')

    // define dispatch to be used
    const dispatch = useDispatch()

    const userLogin = useSelector(state => state.userLogin)

    const { loading, error, userInfo } = userLogin

    // perform redirect after successful login
    const redirect = location.search ? location.search.split('=')[1] : '/'

    useEffect(() => {
        if(userInfo) {
            history.push(redirect)
        }
    }, [history, userInfo, redirect])

    const submitHandler = (e) => {
        e.preventDefault()
        dispatch(login(email, password))
    }
    return (
        <>
            <div>
                <h1>Artist Login</h1>
                {error && <div>{error}</div>}
                {loading && <div>loading...</div>}
                <form onSubmit={submitHandler}>
                    <input placeholder='email' value={email} onChange={(e) => setEmail(e.target.value)}/>
                    <input placeholder='password' value={password} onChange={(e) => setPassword(e.target.value)} />
                    <button>Login</button>
                </form>
            </div>
        </>
    )
}
