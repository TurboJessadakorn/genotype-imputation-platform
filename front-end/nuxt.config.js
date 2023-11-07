export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  env: {
    ssoUrl: process.env.ssoUrl,
    API_BASE_URL: process.env.API_BASE_URL,
    realms: process.env.REALMS,
    FRONT_URL: process.env.FRONT_URL,
  },
  axios: {
    baseURL: process.env.API_BASE_URL,
  },
  head: {
    title: 'Genotype Imputation Platform',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]

  },
  layoutTransition: {
    name: 'layout',
    mode: 'out-in'
  },
  /* Page Transitions */
  pageTransition: {
    name: "page",
    mode: "out-in"
  },
  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@/assets/css/main.css',
    '@fortawesome/fontawesome-svg-core/styles.css',
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    '~/plugins/fontawesome.js',
    
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/tailwindcss
    '@nuxtjs/tailwindcss',
    '@nuxtjs/dotenv'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
  ],

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    transpile: [
      'defu'
    ],
    postcss: {
      postcssOptions: {
        plugins: {
          tailwindcss: {},
          autoprefixer: {},
        },
      },
    },
  },
  auth: {
    strategies: {
      keycloak: {
        scheme: 'oauth2',
        endpoints: {
          authorization:
          `${process.env.ssoUrl}/auth/realms/${process.env.REALMS}/protocol/openid-connect/auth`,
          token:
            `${process.env.ssoUrl}/auth/realms/${process.env.REALMS}/protocol/openid-connect/token`,
          userInfo:
            `${process.env.ssoUrl}/auth/realms/${process.env.REALMS}/protocol/openid-connect/userinfo`,
          logout:
            `${process.env.ssoUrl}/auth/realms/${process.env.REALMS}/protocol/openid-connect/logout?redirect_uri=${process.env.FRONT_URL}`,
        },
        token: {
          property: 'access_token',
          type: 'Bearer',
          name: 'Authorization',
          maxAge: 86400,
        },
        refreshToken: {
          property: 'refresh_token',
          maxAge: 60 * 60 * 24 * 30,
        },
        responseType: 'code',
        grantType: 'authorization_code',
        // clientId: "vipp",
        clientId: process.env.CLIENTID || 'tissue-culture',
        scope: ['openid','profile', 'email'], // สามมารถเปลี่ยนไปถามข้อมลที่เราต้องการได้ setting SSO (clients > clients Scopes)
        codeChallengeMethod: 'S256',
      }
    },
    redirect: {
      login: '/login', // redirect user when not connected
      callback: '/callback', // redirect user after connection
      // login: "/auth/login/", // redirect user when not connected
      // logout: '/auth/login/', // redirect user after disconnection
      // callback: '/login', // redirect user after connection
      home: '/login/success', // the url to redirect to after a successful login
    },
    rewriteRedirects: false,
    // Default: true
    // If enabled, user will redirect back to the original guarded route instead of redirect.home.
    fullPathRedirect: true,
    // Default: false
    // If true, use the full route path with query parameters for redirect
    
  },
  server: {
    port: 4000, // default: 3000
    // host: '0.0.0.0' // default: localhost
  },
  middleware: ['auth'],
}
