import {
    PICTURE_CREATE_REQUEST,
    PICTURE_CREATE_SUCCESS,
    PICTURE_CREATE_FAIL,
    PICTURE_CREATE_RESET
} from './../constants/pictureConstants'
import axios from 'axios'

export const createPicture = () => async (dispatch, getState) => {
    try {
        dispatch({
            type: PICTURE_CREATE_REQUEST
        })

        const {
            userLogin: { userInfo },
        } = getState()
        

        const config = {
            headers: {
                Authorization: `Bearer ${userInfo.token}`,
            },
        }
        const { data } = await axios.post(`http://192.168.49.2:31964/api/artpiece/artpiece/`, {}, config)

        dispatch({
            type: PICTURE_CREATE_SUCCESS,
            payload: data
        })
    } catch (error) {
        dispatch({
            type: PICTURE_CREATE_FAIL,
            payload:
            error.response && error.response.data.message
            ? error.response.data.message
            : error.message,
        })
    }
}