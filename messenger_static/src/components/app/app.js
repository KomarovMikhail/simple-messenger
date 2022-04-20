import './app.css';
import SignInComponent from '../sign-in/sign-in';
import SignUpComponent from "../sign-up/sign-up";
import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";
import { urlSignIn, urlSignUp, urlRoot } from "../../const/const";

const App = () => {
    return (
      <div id="app-background">
        <div id="app-secondary-background">
          <div id='app-header'>
            <div id='app-title'>simple messenger</div>
          </div>
          <div id="app-header-separator"></div>
          <BrowserRouter>
            <Routes>
              <Route exact path={ urlRoot } element={ <Navigate to={ urlSignIn } replace /> } />
              <Route exact path={ urlSignIn } element={ <SignInComponent /> } />
              <Route exact path={ urlSignUp } element={ <SignUpComponent /> } />
            </Routes>
          </BrowserRouter>
        </div>
      </div>
    );
}

export default App;
