export { default as NavBar } from '../..\\components\\nav-bar.vue'
export { default as SideBar } from '../..\\components\\side-bar.vue'
export { default as ImputeGenoInput } from '../..\\components\\impute\\genoInput.vue'
export { default as ImputeHewInput } from '../..\\components\\impute\\hewInput.vue'
export { default as ImputeMafInput } from '../..\\components\\impute\\mafInput.vue'
export { default as ImputeSnpInput } from '../..\\components\\impute\\snpInput.vue'
export { default as UserManagementAddOrganization } from '../..\\components\\user-management\\addOrganization.vue'
export { default as UserManagementAddUser } from '../..\\components\\user-management\\addUser.vue'
export { default as UserManagementImputeList } from '../..\\components\\user-management\\imputeList.vue'

// nuxt/nuxt.js#8607
function wrapFunctional(options) {
  if (!options || !options.functional) {
    return options
  }

  const propKeys = Array.isArray(options.props) ? options.props : Object.keys(options.props || {})

  return {
    render(h) {
      const attrs = {}
      const props = {}

      for (const key in this.$attrs) {
        if (propKeys.includes(key)) {
          props[key] = this.$attrs[key]
        } else {
          attrs[key] = this.$attrs[key]
        }
      }

      return h(options, {
        on: this.$listeners,
        attrs,
        props,
        scopedSlots: this.$scopedSlots,
      }, this.$slots.default)
    }
  }
}
