import React, {useState, useEffect} from 'react'
import { Link } from 'react-router-dom'
import Card from '@material-ui/core/Card'
import CardActions from '@material-ui/core/CardActions'
import CardContent from '@material-ui/core/CardContent'
import Button from '@material-ui/core/Button'
import TextField from '@material-ui/core/TextField'
import Typography from '@material-ui/core/Typography'
import Icon from '@material-ui/core/Icon'
import { makeStyles } from '@material-ui/core/styles'
import { useDispatch, useSelector } from 'react-redux'
import { login } from './../actions/userActions'

const useStyles = makeStyles(theme => ({
    card: {
      maxWidth: 600,
      margin: 'auto',
      textAlign: 'center',
      marginTop: theme.spacing(12),
      paddingBottom: theme.spacing(2)
    },
    error: {
      verticalAlign: 'middle'
    },
    title: {
      marginTop: theme.spacing(2),
      color: theme.palette.openTitle
    },
    textField: {
      marginLeft: theme.spacing(1),
      marginRight: theme.spacing(1),
      width: 300
    },
    submit: {
      margin: 'auto',
      marginBottom: theme.spacing(2)
    }
  }))

export default function Login({history, location}) {
    const classes = useStyles()
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

            <Card className={classes.card}>
        <CardContent>
          <Typography variant="h4" className={classes.title}>
            Sign In
          </Typography>
          <TextField id="email" type="email" label="Email" className={classes.textField} value={email} onChange={(e) => setEmail(e.target.value)} margin="normal"/><br/>
          <TextField id="password" type="password" label="Password" className={classes.textField} value={password} onChange={(e) => setPassword(e.target.value)} margin="normal"/>
          <br/> {
            error && (<Typography component="p" color="error">
              <Icon color="error" className={classes.error}>error</Icon>
              {error}
            </Typography>)
          }
          {loading && <div>loading...</div>}
        </CardContent>
        <CardActions>
          <Button color="primary" variant="contained" onClick={submitHandler} className={classes.submit}>Submit</Button>
        </CardActions>
      </Card>
        </>
    )
}
