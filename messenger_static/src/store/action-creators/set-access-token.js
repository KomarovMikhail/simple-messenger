import SET_ACCESS_TOKEN from "../actions/set-access-token"

const setAccessToken = (value) => {
    return {
        type: SET_ACCESS_TOKEN,
        accessToken: value
    };
}

export default setAccessToken;