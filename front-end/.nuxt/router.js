import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _ed790242 = () => interopDefault(import('..\\pages\\callback.vue' /* webpackChunkName: "pages/callback" */))
const _4b1c59fe = () => interopDefault(import('..\\pages\\imputation\\index.vue' /* webpackChunkName: "pages/imputation/index" */))
const _dbc25d3a = () => interopDefault(import('..\\pages\\login\\index.vue' /* webpackChunkName: "pages/login/index" */))
const _03508bf9 = () => interopDefault(import('..\\pages\\admin\\activity_log.vue' /* webpackChunkName: "pages/admin/activity_log" */))
const _2db42b98 = () => interopDefault(import('..\\pages\\admin\\organization.vue' /* webpackChunkName: "pages/admin/organization" */))
const _ac4c89a0 = () => interopDefault(import('..\\pages\\admin\\user.vue' /* webpackChunkName: "pages/admin/user" */))
const _1df52bbc = () => interopDefault(import('..\\pages\\imputation\\list.vue' /* webpackChunkName: "pages/imputation/list" */))
const _debe56da = () => interopDefault(import('..\\pages\\imputation\\resubmit\\index.vue' /* webpackChunkName: "pages/imputation/resubmit/index" */))
const _3fecd9f6 = () => interopDefault(import('..\\pages\\imputation\\upload.vue' /* webpackChunkName: "pages/imputation/upload" */))
const _28f80dd4 = () => interopDefault(import('..\\pages\\login\\success.vue' /* webpackChunkName: "pages/login/success" */))
const _00aea873 = () => interopDefault(import('..\\pages\\login\\unauthorized.vue' /* webpackChunkName: "pages/login/unauthorized" */))
const _4b146b10 = () => interopDefault(import('..\\pages\\imputation\\resubmit\\upload.vue' /* webpackChunkName: "pages/imputation/resubmit/upload" */))
const _8a1ba9b0 = () => interopDefault(import('..\\pages\\index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/callback",
    component: _ed790242,
    name: "callback"
  }, {
    path: "/imputation",
    component: _4b1c59fe,
    name: "imputation"
  }, {
    path: "/login",
    component: _dbc25d3a,
    name: "login"
  }, {
    path: "/admin/activity_log",
    component: _03508bf9,
    name: "admin-activity_log"
  }, {
    path: "/admin/organization",
    component: _2db42b98,
    name: "admin-organization"
  }, {
    path: "/admin/user",
    component: _ac4c89a0,
    name: "admin-user"
  }, {
    path: "/imputation/list",
    component: _1df52bbc,
    name: "imputation-list"
  }, {
    path: "/imputation/resubmit",
    component: _debe56da,
    name: "imputation-resubmit"
  }, {
    path: "/imputation/upload",
    component: _3fecd9f6,
    name: "imputation-upload"
  }, {
    path: "/login/success",
    component: _28f80dd4,
    name: "login-success"
  }, {
    path: "/login/unauthorized",
    component: _00aea873,
    name: "login-unauthorized"
  }, {
    path: "/imputation/resubmit/upload",
    component: _4b146b10,
    name: "imputation-resubmit-upload"
  }, {
    path: "/",
    component: _8a1ba9b0,
    name: "index"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
