import React from 'react';
import $ from 'jquery';
import { Link, useNavigate } from "react-router-dom";
import {contentTypeApplicationJson, urlSignIn, authServerRegisterUrl }
    from "../../const/const";
import { useState } from "react";


const SignUpComponent = () => {
    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');
    const [repeatPassword, setRepeatPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    let navigate = useNavigate()

    const onLoginSuccess = () => {
        navigate(urlSignIn, { replace: true });
    }

    const onLoginError = (data) => {
        setErrorMessage(data.responseText)
    }

    const onSignUp = (event) => {
        event.preventDefault();
        setErrorMessage('');
        if (login === '') {
            setErrorMessage('you haven\'t filled the login yet');
            return;
        }
        if (password === '') {
            setErrorMessage('you haven\'t filled the password yet');
            return;
        }
        if (repeatPassword === '') {
            setErrorMessage('you haven\'t repeated the password yet');
            return;
        }
        if (password !== repeatPassword) {
            setErrorMessage('passwords don\'t match');
            return;
        }
        let data = {
            "login": login,
            "password": password,
        };
        $.ajax({
            method: "POST",
            url: authServerRegisterUrl,
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

    const onUpdateRepeatPassword = (event) => {
        setRepeatPassword(event.target.value);
        setErrorMessage('');
    }

    return (
        <div className="center-block">
            <div>please, sign up:</div>

            <p className="input-title">login:</p>
            <input className="input-field" value={ login } onChange={ onUpdateLogin }/>

            <p className="input-title">password:</p>
            <input className="input-field password-input" value={ password } onChange={ onUpdatePassword }/>

            <p className="input-title">repeat password:</p>
            <input className="input-field password-input" value={ repeatPassword } onChange={ onUpdateRepeatPassword }/>

            <div className="colored-button" onClick={ onSignUp }>sign up</div>
            <div className="redirect-message">if you already have an account, please <Link to={ urlSignIn } className='redirect-link'> sign in</Link></div>
            <div className="error-message">{ errorMessage }</div>
        </div>
    );
}

export default SignUpComponent;