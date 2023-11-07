<template>
    <aside id="logo-sidebar"
        class="fixed top-0 left-0 z-40 w-56 text-xs h-screen pt-20 transition-transform -translate-x-full bg-white border-r border-gray-200 sm:translate-x-0 shadow-2xl shadow-zinc-400"
        aria-label="Sidebar">
        <div class="h-full px-3 pb-4 overflow-y-auto bg-white">
            <p class="font-bold text-xs p-2 text-gray-400">NAVIGATION</p>
            <ul class="space-y-2 font-semibold text-gray-400">
                <li>
                    <NuxtLink to="/" exact-active-class="font-bold text-gray-700" class="flex items-center p-2 py-4 rounded-lg hover:bg-gray-100">
                        <font-awesome-icon :icon="['fas', 'house-chimney']" size="lg" />
                        <span class="flex-1 ml-3 whitespace-nowrap">Home </span>
                    </NuxtLink>
                </li>
                <!-- <li>
                    <NuxtLink to="/summary" exact-active-class="font-bold text-sm text-gray-700" class="flex items-center p-2 py-4  rounded-lg hover:bg-gray-100">
                        <font-awesome-icon :icon="['fas', 'file-image']" class="px-1" size="lg"/>
                        <span class="flex-1 ml-3 whitespace-nowrap">Summary</span>
                    </NuxtLink>
                </li>
                <li>
                    <NuxtLink to="/dashboard" exact-active-class="font-bold text-sm text-gray-700" class="flex items-center p-2 py-4  rounded-lg hover:bg-gray-100">
                        <font-awesome-icon :icon="['fass', 'chart-pie']" class="" size="lg"/>
                        <span class="flex-1 ml-3 whitespace-nowrap">Dashboard</span>
                    </NuxtLink>
                </li> -->
                <li>
                    <NuxtLink to="/imputation/" exact-active-class="font-bold text-gray-700" class="flex items-center p-2 py-4  rounded-lg hover:bg-gray-100">
                        <font-awesome-icon :icon="['fas', 'file-import']" class="pr-1" size="lg" />
                        <span class="flex-1 ml-3 whitespace-nowrap">Genotype imputation</span>
                    </NuxtLink>
                </li>
                <li>
                    <NuxtLink to="/imputation/list" exact-active-class="font-bold text-gray-700" class="flex items-center p-2 py-4  rounded-lg hover:bg-gray-100">
                        <font-awesome-icon :icon="['fas', 'folder-open']" class="pl-1" size="lg" />
                        <span class="flex-1 ml-3 whitespace-nowrap">All imputations</span>
                    </NuxtLink>
                </li>

                <li v-if="Role == 'admin'">
                    <details class="group [&_summary::-webkit-details-marker]:hidden flex items-center pl-0  rounded-lg cursor-pointer">
                        <summary
                            class="flex items-center p-2 py-4  rounded-lg hover:bg-gray-100">
                            <font-awesome-icon :icon="['fas', 'fa-key']" class="pr-1" size="lg" />
                            <span class="flex-1 ml-3 whitespace-nowrap">User Management</span>
                            <span class="transition duration-300 shrink-0 group-open:-rotate-180 group-open:translate-y-1">
                                <font-awesome-icon :icon="['fas', 'fa-caret-down']" class="pl-1 pr-1" size="lg"
                                 />
                            </span>
                        </summary>

                        <nav aria-label="Users Nav" class="flex flex-col mt-2 space-y-1">
                            <li>
                                <NuxtLink to="/admin/user" exact-active-class="font-bold text-gray-700"
                                    class="flex items-center p-4  rounded-lg hover:bg-gray-100">
                                    <font-awesome-icon :icon="['fas', 'fa-user']" class="pl-1 pr-1" size="lg" />
                                    <span class="flex-1 ml-3 whitespace-nowrap">User</span>
                                </NuxtLink>
                            </li>

                            <!-- <li>
                                <NuxtLink to="/admin/organization" exact-active-class="font-bold text-gray-700"
                                    class="flex items-center p-4  rounded-lg hover:bg-gray-100">
                                    <font-awesome-icon :icon="['fas', 'fa-user-group']" class="" size="lg" />
                                    <span class="flex-1 ml-3 whitespace-nowrap">Organization</span>
                                </NuxtLink>
                            </li> -->

                            <li>
                                <NuxtLink to="/admin/activity_log" exact-active-class="font-bold text-gray-700"
                                    class="flex items-center p-4  rounded-lg hover:bg-gray-100">
                                    <font-awesome-icon :icon="['fas', 'list']" class="" size="lg" />
                                    <span class="flex-1 ml-3 whitespace-nowrap">Activity log</span>
                                </NuxtLink>
                            </li>
                        </nav>
                    </details>
                </li>
            </ul>
            <hr>
        </div>
    </aside>
</template>

<style>
details[open] summary ~ * {
  animation: sweep .5s ease-in-out;
}

@keyframes sweep {
  0%    {opacity: 0; transform: translateX(-10px)}
  100%  {opacity: 1; transform: translateX(0)}
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userData: [],
      Role: ''
    };
  },
  mounted() {
    this.fetchRole();
  },
  methods: {
    fetchRole() {
        if (this.$auth.user){
            const email = this.$auth.user.email;
            this.$axios.get(`/useremail/${email}`)
                .then(response => {
                this.userData = response.data;
                this.Role = this.userData.role;
                })
                .catch(error => {
                console.error(error);
                });
        }
    },
  },
};
</script>
