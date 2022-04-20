import accessTokenReducer from "./access-token-reducer";
import refreshTokenReducer from "./refresh-token-reducer";


const reducer = (state = {}, action) => {
    return {
        accessToken: accessTokenReducer(state.accessToken, action),
        refreshToken: refreshTokenReducer(state.refreshToken, action)
    }
}

export default reducer;