import SET_REFRESH_TOKEN from "../actions/set-refresh-token";

const refreshTokenReducer = (state = '', action) => {
    if (action.type === SET_REFRESH_TOKEN) {
        return action.refreshToken;
    } else {
        return state;
    }
}

export default refreshTokenReducer