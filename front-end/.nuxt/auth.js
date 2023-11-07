import Middleware from './middleware'
import { Auth, authMiddleware, ExpiredAuthSessionError } from '~auth/runtime'

// Active schemes
import { Oauth2Scheme } from '~auth/runtime'

Middleware.auth = authMiddleware

export default function (ctx, inject) {
  // Options
  const options = {
  "resetOnError": false,
  "ignoreExceptions": false,
  "scopeKey": "scope",
  "rewriteRedirects": false,
  "fullPathRedirect": true,
  "watchLoggedIn": true,
  "redirect": {
    "login": "/login",
    "logout": "/",
    "home": "/login/success",
    "callback": "/callback"
  },
  "vuex": {
    "namespace": "auth"
  },
  "cookie": {
    "prefix": "auth.",
    "options": {
      "path": "/"
    }
  },
  "localStorage": {
    "prefix": "auth."
  },
  "defaultStrategy": "keycloak"
}

  // Create a new Auth instance
  const $auth = new Auth(ctx, options)

  // Register strategies
  // keycloak
  $auth.registerStrategy('keycloak', new Oauth2Scheme($auth, {
  "endpoints": {
    "authorization": "https://sso.nbt.or.th/auth/realms/nbt-dev/protocol/openid-connect/auth",
    "token": "https://sso.nbt.or.th/auth/realms/nbt-dev/protocol/openid-connect/token",
    "userInfo": "https://sso.nbt.or.th/auth/realms/nbt-dev/protocol/openid-connect/userinfo",
    "logout": "https://sso.nbt.or.th/auth/realms/nbt-dev/protocol/openid-connect/logout?redirect_uri=http://localhost:4000"
  },
  "token": {
    "property": "access_token",
    "type": "Bearer",
    "name": "Authorization",
    "maxAge": 86400
  },
  "refreshToken": {
    "property": "refresh_token",
    "maxAge": 2592000
  },
  "responseType": "code",
  "grantType": "authorization_code",
  "clientId": "tissue-culture",
  "scope": [
    "openid",
    "profile",
    "email"
  ],
  "codeChallengeMethod": "S256",
  "name": "keycloak"
}))

  // Inject it to nuxt context as $auth
  inject('auth', $auth)
  ctx.$auth = $auth

  // Initialize auth
  return $auth.init().catch(error => {
    if (process.client) {
      // Don't console log expired auth session errors. This error is common, and expected to happen.
      // The error happens whenever the user does an ssr request (reload/initial navigation) with an expired refresh
      // token. We don't want to log this as an error.
      if (error instanceof ExpiredAuthSessionError) {
        return
      }

      console.error('[ERROR] [AUTH]', error)
    }
  })
}
