<template>
    <div class="page-container">
        <div class="header">  
            <h1 class="title">Manage Users</h1>
        </div>
        
        <div class="col-container">
            <div class="basis-3/4 flex flex-row items-center pt-2">
                <!-- Group filter -->
                <select id="group" v-model="selectedGroup" class="p-2 pr-8 border border-gray-300 text-sm rounded-l-md" @change="filterUsers">
                    <option value="">All Groups</option>
                    <option v-for="group in groups" :value="group">{{ group }}</option>
                </select>

                <!-- search --> 
                <input type="platform" v-model="searchInput" id="search"  class="border border-gray-300 text-gray-900 focus:ring-primary-600 focus:border-primary-600 block p-2 pr-5" placeholder="Search..." required="">
                
                <div class="p-2 text-white bg-blue-600 rounded-r-md">
                    <font-awesome-icon :icon="['fa-solid', 'fa-magnifying-glass']" class="" size="xl" style="color: white;" />
                </div>
            </div>
            <div class="p-2 basis-1/4 flex flex-row justify-end">
                <!-- add user -->
                <!-- <addUser /> -->
            </div>
        </div>

        <div v-if="fetchComplete == false" class="flex items-center justify-center my-20" role="status">
                <svg aria-hidden="true" class="inline w-24 h-24 mr-2 text-gray-200 animate-spin fill-blue-600"
                    viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                        fill="currentColor" />
                    <path
                        d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                        fill="currentFill" />
                </svg>
        </div>
        <div v-if="fetchComplete == true" class="col-container">
            <table class="w-full text-xs text-left shadow-lg font-medium border-t-2 border-gray-50">
                        <thead class="px-2 border-b-2 border-gray-200">
                            <tr>
                                <th scope="col" class="pl-3 py-3 w-[15%]">
                                    <div class="flex cursor-pointer items-center" @click="sortData('first_name')">
                                    NAME
                                    <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                                    </div>
                                </th>
                                <th scope="col" class="py-3">
                                    <div class="flex cursor-pointer justify-center items-center" @click="sortData('email')">
                                    EMAIL
                                    <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                                    </div>
                                </th>
                                <th scope="col" class="py-3">
                                    <div class="flex cursor-pointer justify-center items-center" @click="sortData('organization')">
                                    ORGANIZATION
                                    <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                                    </div>
                                </th>
                                <th scope="col" class="py-3">
                                    <div class="flex cursor-pointer justify-center items-center" @click="sortData('role')">
                                    ROLE
                                    <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                                    </div>
                                </th>
                                <th scope="col" class="py-3">
                                    <div class="flex cursor-pointer justify-center items-center" @click="sortData('role')">
                                    APPROVAL
                                    <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                                    </div>
                                </th>
                                <th scope="col" class="text-center py-3">
                                    ACTION
                                </th>
                                
                            </tr>
                        </thead>
                <tbody class="">
                <tr class="hover:bg-gray-100" v-for="(user, index) in filteredUsers" :key="index">
                <!-- <tr v-for="user in filteredUsers" :key="user.email"> -->
                    <td class="pl-3 py-4">{{ user.first_name}} {{ user.Elastname}}</td>
                    <td class="text-center py-4">{{ user.email }}</td>
                    <td class="text-center py-4">
                        <select v-model="user.organization" @change="showApprovalModal(index)">
                            <option v-for="group in groups" :value="group">{{ group }}</option>
                        </select>
                    </td>
                    <td class="text-center py-4">
                        <select v-model="user.role" @change="showApprovalModal(index)">
                            <option value="admin">Admin</option>
                            <option value="user">User</option>
                        </select>
                    </td>
                    <td class="text-center py-4">
                        <select v-model="user.approval" @change="showApprovalModal(index)">
                            <option value="approved">Approved</option>
                            <option value="pending">Pending</option>
                            <option value="rejected">Rejected</option>
                        </select>
                        <input type="checkbox" :id="'approval-modal-toggle-' + index" class="modal-toggle" />
                            <div class="modal">
                                <div class="modal-content bg-white rounded-md p-5 shadow-md space-y-2">
                                    <h2 class="mb-4 text-black text-lg">Confirm Modification</h2>
                                    <div>
                                        <p class="border-t border-gray-200 py-4">Are you sure you want to apdate this user's data?</p>
                                    </div>
                                    <div class="modal-actions space-x-2">
                                        <button class="text-white bg-blue-500 px-5 py-2.5 rounded-md" @click="updateUser(user, index)">Update</button>
                                        <button class="border border-gray-200 px-5 py-2.5 rounded-md" @click="closeApprovalModal(index)">Cancel</button>
                                    </div>
                                </div>
                            </div>
                    </td>
                    <td class="py-4">
                        <div class="flex justify-center">   
                            <!-- delete btn -->
                            <button @click="showDeleteModal(index)" class="opacity-80 px-4 py-1.5 bg-red-500 rounded-md text-xs text-white">Delete</button>
                                <input type="checkbox" :id="'modal-toggle-' + index" class="modal-toggle" />
                                <div class="modal">
                                    <div class="modal-content bg-white rounded-md p-5 shadow-md space-y-2">
                                        <h2 class="mb-4 text-black text-lg">Confirm Deletion</h2>
                                        <div>
                                            <p class="border-t border-gray-200 py-4">Are you sure you want to delete this user's data? If you delete the data you can't recover it.</p>
                                        </div>
                                        <div class="modal-actions space-x-2">
                                            <button class="text-white bg-red-500 px-5 py-2.5 rounded-md" @click="deleteItem(index)">Delete</button>
                                            <button class="border border-gray-200 px-5 py-2.5 rounded-md" @click="closeModal(index)">Cancel</button>
                                        </div>
                                    </div>
                                </div>
                        </div>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>  
    </div>
          
</template>

<script>
import axios from 'axios';
import addUser from '@/components/user-management/addUser.vue';

export default {
    middleware: ['auth', 'adminApproval'],
    head: {
        title:"employee mangament",
    },
    data() {
        return {
        users: [],
        selectedGroup: '',
        searchInput: '',
        sortColumn: '',
        sortOrder: '',
        fetchComplete: false,
        };
    },
    components:{
        addUser,
    },
    computed: {
        test() {
            return this.$auth.user
        },
        groups() {
            const uniqueGroups = new Set(this.users.map(user => user.organization));
            return Array.from(uniqueGroups);
        },
        filteredUsers() {
            if (this.selectedGroup && this.searchInput) {
                return this.users.filter(user => {
                const fullName = `${user.first_name} ${user.Elastname}`.toLowerCase();
                return (
                    user.organization === this.selectedGroup &&
                    fullName.includes(this.searchInput.toLowerCase())
                );
                });
            } else if (this.selectedGroup) {
                return this.users.filter(user => user.organization === this.selectedGroup);
            } else if (this.searchInput) {
                return this.users.filter(user => {
                const fullName = `${user.first_name} ${user.Elastname}`.toLowerCase();
                return fullName.includes(this.searchInput.toLowerCase());
                });
            } else {
                return this.users;
            }
        },
    },
    mounted() {
        console.log(this.$auth.user)
        
        this.fetchUsers();
    },
    methods: {
        fetchUsers() {
            this.$axios.get('/alluser/')
            
                .then(response => {
                this.users = response.data; // Update the users array with the fetched data
                this.fetchComplete = true;
                })
                .catch(error => {
                console.error(error);
                });
        },
        showDeleteModal(index) {
            const modalToggle = document.getElementById(`modal-toggle-${index}`);
            modalToggle.checked = true;
        },
        showApprovalModal(index) {
            const modalToggle = document.getElementById(`approval-modal-toggle-${index}`);
            modalToggle.checked = true;
        },
        deleteItem(index) {
          const userToDelete = this.filteredUsers[index];
          const userIndex = this.users.indexOf(userToDelete);
          this.users.splice(userIndex, 1);
          this.filteredUsers.splice(index, 1);

          const modalToggle = document.getElementById(`modal-toggle-${userIndex}`);
          modalToggle.checked = false;
          const modal = modalToggle.parentElement.querySelector('.modal');
          modal.classList.remove('open');
        },
        closeModal(index) {
            const modalToggle = document.getElementById(`modal-toggle-${index}`);
            modalToggle.checked = false;
            const modal = modalToggle.parentElement.querySelector('.modal');
            modal.classList.remove('open');
        },
        closeApprovalModal(index) {
            
            const modalToggle = document.getElementById(`approval-modal-toggle-${index}`);
            modalToggle.checked = false;
            const modal = modalToggle.parentElement.querySelector('.modal');
            modal.classList.remove('open');

        },
        filterUsers() {
          console.log('Selected Group:', this.selectedGroup);
        },
        sortData(column) {
            // If the same column is clicked, toggle the sort order
            if (this.sortColumn === column) {
                this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc';
            } else {
                // If a new column is clicked, set the sort column and default to ascending order
                this.sortColumn = column;
                this.sortOrder = 'asc';
            }

            // Sort the data based on the selected column and sort order
            this.filteredUsers.sort((a, b) => {
                const valueA = a[column].toLowerCase();
                const valueB = b[column].toLowerCase();

                if (this.sortOrder === 'asc') {
                if (valueA < valueB) return -1;
                if (valueA > valueB) return 1;
                return 0;
                } else {
                if (valueA < valueB) return 1;
                if (valueA > valueB) return -1;
                return 0;
                }
            });
        },
        updateUser(user, index) {
            this.$axios.put(`/user/${user.user_id}`, user)
            .then(response => {
                console.log('User updated successfully:', response.data);
                const modalToggle = document.getElementById(`approval-modal-toggle-${index}`);
                modalToggle.checked = false;
                const modal = modalToggle.parentElement.querySelector('.modal');
                modal.classList.remove('open');
            })
            .catch(error => {
                console.error('Error updating user:', error);
            });
        },
    }
}
</script>
