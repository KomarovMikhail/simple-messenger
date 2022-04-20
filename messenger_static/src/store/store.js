import { createStore } from 'redux';
import reducer from "./reducers/reducer";
import initialState from "./initial-state";

const store = createStore(reducer, initialState);

export default store;