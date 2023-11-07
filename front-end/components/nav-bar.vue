<template>
    <nav class="fixed top-0 z-50 w-full bg-white border-b border-gray-200">
        <div class="px-3 py-3 lg:px-5 lg:pl-3">
            <div class="flex items-center justify-between">
                <div class="flex items-center justify-start">
                    <button data-drawer-target="logo-sidebar" data-drawer-toggle="logo-sidebar" aria-controls="logo-sidebar" type="button" class="inline-flex items-center p-2 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200">
                        <span class="sr-only">Open sidebar</span>
                        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path clip-rule="evenodd" fill-rule="evenodd" d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"></path>
                        </svg>
                    </button>

                    <a href="/" class="flex ml-2 md:mr-24">
                        <span
                            class="self-center md:text-xl font-semibold sm:text-md whitespace-nowrap">Genotype Imputation Platform</span>
                    </a>
                </div>
                <div class="flex items-center">
                    <div class="flex items-center">
                        <div class="flex flex-row">
                            <!-- <div class="collapse collapse-arrow bg-white rounded-xl border">
                      <input type="checkbox"/>
                      <div class="collapse-title text-lg font-bold">
                        <h1 class="self-center text-md font-semibold sm:text-md whitespace-nowrap pr-2 text-gray-500">Jessadakorn Paopatimakorn</h1>
                        <img class="w-8 h-8 rounded-full" src="https://static.vecteezy.com/system/resources/previews/005/544/718/original/profile-icon-design-free-vector.jpg" alt="user photo">
                      </div>
                      <div class="collapse-content">
                        <li>
                            <NuxtLink to="/login" class="flex items-center p-4 text-gray-900 rounded-lg">
                              <span class="">Login</span>
                            </NuxtLink>
                        </li>
                
                        <li>
                            <div @click="logout()" class="flex items-center p-4 text-gray-900 rounded-lg">
                              <span class="">Logout</span>
                            </div>
                        </li>
                      </div>
                    </div> -->
                            <div class="flex flex-row dropdown dropdown-end">
                                <button @click="isOpen = !isOpen" class="flex transition duration-300 ease-in-out">
                                    <img class="w-8 h-8 rounded-full"
                                        src="https://static.vecteezy.com/system/resources/previews/005/544/718/original/profile-icon-design-free-vector.jpg"
                                        alt="user photo">
                                </button>
                                <div class="dropdown-menu absolute m-4 mt-8 w-48 right-0 shadow-lg rounded-md"
                                    :class="{ 'show': isOpen }"
                                    v-if="isOpen"
                                >
                                    <!-- Dropdown items -->
                                    <ul class="space-y-2 text-sm font-medium bg-white p-1 ml-auto text-gray-700 rounded-md">
                                        <li>
                                            <div class="flex py-2 px-4">
                                                <!-- <img class="w-8 h-8 rounded-full" src="https://static.vecteezy.com/system/resources/previews/005/544/718/original/profile-icon-design-free-vector.jpg" alt="user photo"> -->
                                                <span class="text-center">Your Profile</span>
                                            </div>
                                        </li>
                                        <!-- <li>
                                            <div class="flex py-2 px-4">
                                
                                                <span class="text-center">Setting</span>
                                            </div>
                                        </li> -->
                                        <li>
                                            <template v-if="$auth.loggedIn">
                                                <div @click="logout"
                                                    class="flex px-4 py-2 rounded-md hover:bg-gray-100">
                                                    <!-- <font-awesome-icon :icon="['fas', 'fa-right-from-bracket']" class="pr-1" size="xl" style="color: #6d6f74;" /> -->
                                                    <span class="">Logout</span>
                                                </div>
                                            </template>
                                            <template v-else>
                                                <NuxtLink to="/login"
                                                    class="flex px-4 py-2 rounded-md hover:bg-gray-100">
                                                    <!-- <font-awesome-icon :icon="['fas', 'fa-right-to-bracket']" class="pr-1" size="xl" style="color: #6d6f74;" /> -->
                                                    <span class="">Login</span>
                                                </NuxtLink>
                                            </template>
                                        </li>

                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<style>
  .dropdown-menu {
    display: none;
  }

  .show {
    display: block;
    animation: fadeIn 0.3s ease-in-out;
  }

  @keyframes fadeIn {
    0% {
      opacity: 0;
      transform: translateY(-10px);
    }
    100% {
      opacity: 1;
      transform: translateY(0);
    }
  }
</style>


<script>

export default {
    data() {
        return {
            isOpen: false,
         }
    },
  methods:{
    async logout(){
        await this.$auth.logout()
    },
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