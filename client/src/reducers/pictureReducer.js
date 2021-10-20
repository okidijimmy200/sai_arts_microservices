import {
    PICTURE_CREATE_REQUEST,
    PICTURE_CREATE_SUCCESS,
    PICTURE_CREATE_FAIL,
    PICTURE_CREATE_RESET
} from './../constants/pictureConstants'


export const pictureCreateReducer = (state = {}, action) => {
    switch(action.type) {
        case PICTURE_CREATE_REQUEST:
            return { loading: true }
        case PICTURE_CREATE_SUCCESS:
            return { loading: false, success: true, picture: action.payload }
        case PICTURE_CREATE_FAIL:
            return { loading: false, error: action.payload }
        case PICTURE_CREATE_RESET:
            return {}
        default:
            return state
    }
}