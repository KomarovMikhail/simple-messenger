import React from 'react';
import $ from 'jquery';
import { Link, useNavigate } from "react-router-dom";
import {authServerLoginUrl, contentTypeApplicationJson, urlMessages, jsonKeyAccessToken, jsonKeyRefreshToken, urlSignUp}
    from "../../const/const";
import setAccessToken from "../../store/action-creators/set-access-token";
import setRefreshToken from "../../store/action-creators/set-refresh-token";
import { useDispatch } from 'react-redux'
import { useState } from "react";


const SignInComponent = () => {
    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    // const accessToken = useSelector((state) => state.accessToken)
    const navigate = useNavigate();
    const dispatch = useDispatch()

    const onLoginSuccess = (data) => {
        if (!data.hasOwnProperty(jsonKeyAccessToken) && !data.hasOwnProperty(jsonKeyRefreshToken)) {
            setErrorMessage("Wrong auth response");
            return;
        }

        dispatch(setAccessToken(data[jsonKeyAccessToken]));
        dispatch(setRefreshToken(data[jsonKeyRefreshToken]));

        navigate(urlMessages, { replace: true });
    }

    const onLoginError = (data) => {
        setErrorMessage(data.responseText)
    }

    const onSignIn = (event) => {
        event.preventDefault();
        setErrorMessage('');
        if (login === '') {
            setErrorMessage('you haven\'t filled the "login" field yet');
            return;
        }
        if (password === '') {
            setErrorMessage('you haven\'t filled the "password" field yet');
            return;
        }
        let data = {
            "login": login,
            "password": password,
            "fingerprint": "fingerprint"
        };
        $.ajax({
            method: "POST",
            url: authServerLoginUrl,
            data: JSON.stringify(data),
            contentType: contentTypeApplicationJson,
            crossDomain: true,
            success: onLoginSuccess,
            error: onLoginError
        });
    }

    const onUpdateLogin = (event) => {
        setLogin(event.target.value);
        setErrorMessage('');
    }

    const onUpdatePassword = (event) => {
        setPassword(event.target.value);
        setErrorMessage('');
    }

    return (
        <div className="center-block">
            <div>please, sign in:</div>

            <p className="input-title">login:</p>
            <input className="input-field" value={ login } onChange={ onUpdateLogin }/>

            <p className="input-title">password:</p>
            <input className="input-field password-input" value={ password } onChange={ onUpdatePassword }/>

            <div className="colored-button" onClick={ onSignIn }>sign in</div>
            <div className="redirect-message">if you don't have an account, please <Link to={ urlSignUp } className='redirect-link'>sign up</Link></div>
            <div className="error-message">{ errorMessage }</div>
        </div>
    );
}

export default SignInComponent;