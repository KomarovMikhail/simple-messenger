import SET_REFRESH_TOKEN from "../actions/set-refresh-token"

const setRefreshToken = (value) => {
    return {
        type: SET_REFRESH_TOKEN,
        refreshToken: value
    };
}

export default setRefreshToken;