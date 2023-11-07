<template>
  <div>

    <navBar />

    <sideBar />

    <div class="bg-gray-50 text-gray-600">  
      <div class="md:ml-56 sm:ml-0 mt-14">
        <div class="py-4 sm:px-12">
          <Nuxt />
        </div>
      </div>
    </div>
  </div>

</template>

<style>
body {
  background-color: #f9fafb;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

</style>

<script>
import navBar from '../components/nav-bar.vue';
import sideBar from '../components/side-bar.vue';
export default {
  data() {
    return {
      showDropdown: false,
      isOpen: false,
    }
  },
  methods: {
    async logout() {
      await this.$auth.logout()
      showModal = false
    },
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    }
  },
  components: {
    navBar,
    sideBar,
  }
}
</script>

<style>
.dropdown-content {
  display: none;
}

.dropdown-content.show {
  display: block;
}
</style>