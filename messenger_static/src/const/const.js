const authServerBaseUrl = "http://localhost:5433/api/auth";

export const authServerLoginUrl = authServerBaseUrl + "/login";
export const authServerLogoutUrl = authServerBaseUrl + "/logout";
export const authServerRefreshTokensUrl = authServerBaseUrl + "/refresh-tokens";
export const authServerDeleteUserUrl = authServerBaseUrl + "/delete-user";
export const authServerRegisterUrl = authServerBaseUrl + "/register";

export const jsonKeyLogin = "login";
export const jsonKeyPassword = "password";
export const jsonKeyFingerprint = "fingerprint";
export const jsonKeyAccessToken = "access-token";
export const jsonKeyRefreshToken = "refresh-token";

export const contentTypeApplicationJson = "application/json"

export const urlMessages = "/messages"
export const urlSignIn = "/sign-in"
export const urlSignUp = "/sign-up"
export const urlRoot = "/"