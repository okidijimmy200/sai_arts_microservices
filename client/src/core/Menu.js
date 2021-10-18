import React from 'react'
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import Button from '@material-ui/core/Button'
import {Link, withRouter} from 'react-router-dom'
import { makeStyles } from '@material-ui/core/styles'
import { MenuItem } from '@material-ui/core'

const useStyles = makeStyles({
    root: {
        margin: '0 auto',
        backgroundColor: '#fff',
        color: '#000',
        fontFamily: 'sans-serif',
        boxShadow: '0px 0px 0px 0px',
        border: '1px solid #ddd',
        marginBottom: '30px'
    },
    capitalizeText: {
        textTransform: 'none',
        textAlign: 'center',
        fontWeight: 'bold',
        transition: {
           top:' 0.1s',
          ease: '0s', 
          borderColor: '0.1s ease 0s', 
          backgroundColor:' 0.1s ease 0s', 
          color: '0.1s ease 0s'},
        whiteSpace: 'nowrap',
        fontSize: '16px',
        lineHeight: '1.5',
        backgroundColor: 'rgb(255, 255, 255)',

        "&:hover": {
            backgroundColor: 'rgb(255, 255, 255)',
        },
      },
    menu: {
        textDecoration: 'none',
        "&:hover": {
            backgroundColor: 'rgb(255, 255, 255)',
            border: '1px solid red'
        },
    }
})

export default function Menu() {
    const classes = useStyles();
    return (
        <AppBar className={classes.root}>
            <Toolbar>
                <Typography variant="h2" color="inherit" style={{marginRight: '66rem'}}>
                    SaiArts 
                </Typography>
                <MenuItem className={classes.menu} >
                    <Link to=''style={{textDecoration: 'none'}} >
                        <Button className={classes.capitalizeText}>Artists</Button>
                    </Link>
                </MenuItem>
                <MenuItem className={classes.menu} >
                    <Link to='' style={{textDecoration: 'none'}}>
                        <Button className={classes.capitalizeText}>Exhibitions</Button>
                </Link>
                    </MenuItem>
                    <MenuItem className={classes.menu} >
                    <Link to='' style={{textDecoration: 'none'}}>
                        <Button className={classes.capitalizeText}>Fairs</Button>
                    </Link>
                    </MenuItem>
                    <MenuItem className={classes.menu} >
                    <Link to='' style={{textDecoration: 'none'}}>
                        <Button className={classes.capitalizeText}>Galleries</Button>
                    </Link>
                </MenuItem>
            </Toolbar>
            
        </AppBar>
    )
}
