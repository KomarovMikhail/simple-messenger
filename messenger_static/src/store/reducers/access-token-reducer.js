import SET_ACCESS_TOKEN from "../actions/set-access-token";

const accessTokenReducer = (state = '', action) => {
    if (action.type === SET_ACCESS_TOKEN) {
        return action.accessToken;
    } else {
        return state;
    }
}

export default accessTokenReducer