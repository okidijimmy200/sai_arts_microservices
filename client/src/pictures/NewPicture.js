import React, {useState, useEffect} from 'react'
import Card from '@material-ui/core/Card'
import CardActions from '@material-ui/core/CardActions'
import CardContent from '@material-ui/core/CardContent'
import Button from '@material-ui/core/Button'
import FileUpload from '@material-ui/icons/AddPhotoAlternate'
import TextField from '@material-ui/core/TextField'
import Typography from '@material-ui/core/Typography'
import Icon from '@material-ui/core/Icon'
import MenuItem from '@material-ui/core/MenuItem'
import { makeStyles } from '@material-ui/core/styles'
import {useDispatch, useSelector } from 'react-redux'
import {
    createPicture
} from './../actions/pictureActions'
import { PICTURE_CREATE_RESET } from './../constants/pictureConstants'

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
    },
    input: {
      display: 'none'
    },
    filename:{
      marginLeft:'10px'
    }
  }))

export default function NewPicture({history, match}) {
    const classes = useStyles()
    const [values, setValues] = useState({
        name: '',
        slug: '',
        body: '',
        image: '',
        status: 'Created',
        error: ''
    })
    const dispatch = useDispatch()

    const pictureCreate = useSelector((state) => state.pictureCreate)
    const { loading: loadingCreate, error: errorCreate, success: successCreate, picture: picturedCreate } = pictureCreate

    const userLogin = useSelector(state => state.userLogin)
    const { userInfo } = userLogin

    const userId = userInfo.user_id

    useEffect(() => {
        if(successCreate) {
            setValues({...values, name: '', slug: '', body: '', image: '', status: 'created', })
            dispatch({ type: PICTURE_CREATE_RESET})
        }
    }, [dispatch, successCreate])

    const clickSubmit = (e) => {
        e.preventDefault()
        let postData = new FormData();
        values.name && postData.append('name', values.name)
        values.slug && postData.append('slug', values.slug)
        values.body && postData.append('body', values.body)
        values.image && postData.append('image', values.image)
        values.status && postData.append('status', values.status)
        dispatch(Create( userId, postData))
    }

    const handleChange = name => event => {
        const value = name === 'image'
          ? event.target.files[0]
          : event.target.value
        setValues({...values, [name]: value })
      }



    return (
        <>
            <Card className={classes.card}>
          <CardContent>
            <Typography variant="h6" className={classes.title}>
              New ArtPiece
            </Typography>
            <br/>
{/* In the form view, we first give the user an option to upload a course image file. */}
            <input accept="image/*" onChange={handleChange('image')} className={classes.input} id="icon-button-file" type="file" />
            <label htmlFor="icon-button-file">
              <Button variant="contained" color="secondary" component="span">
                Upload Photo
                <FileUpload/>
              </Button>
            </label> <span className={classes.filename}>{values.image ? values.image.name : ''}</span><br/>
{/* Then, we add the name, description, and category form fields using the
TextField components from Material-UI. */}
            <TextField id="name" label="Name" className={classes.textField} value={values.name} onChange={handleChange('name')} margin="normal"/><br/>
            <TextField
              id="multiline-flexible"
              label="Description"
              multiline
              rows="2"
              value={values.body}
              onChange={handleChange('body')}
              className={classes.textField}
              margin="normal"
            /><br/> 
            <TextField id="slug" label="Slug" className={classes.textField} value={values.slug} onChange={handleChange('slug')} margin="normal"/><br/>
            <TextField id="status" label="Status" className={classes.textField} value={values.status} onChange={handleChange('status')} select margin="normal">
                <MenuItem value="Created">Created</MenuItem>
                <MenuItem value="Exhibited">Exhibited</MenuItem>
              </TextField><br/>
            {
              values.error && (<Typography component="p" color="error">
                <Icon color="error" className={classes.error}>error</Icon>
                {values.error}</Typography>)
            }
          </CardContent>
          <CardActions>
{/* /**add the Submit button, which, when clicked, should call
a click-handling function */ }
            <Button color="primary" variant="contained" onClick={clickSubmit} className={classes.submit}>Submit</Button>
          </CardActions>
        </Card>
        </>
    )
}


