<template>
    <div class="page-container">
        <div class="header">  
            <h1 class="title">Manage Organizations</h1>
        </div>

        <div class="col-container justify-center">
            <div class="basis-3/4 flex flex-row items-center">
                <!-- search --> 
                <input type="platform" v-model="searchInput" id="search" class="border border-gray-300 text-gray-900 focus:ring-primary-600 focus:border-primary-600 block p-2 pr-8 rounded-l-md" placeholder="Search..." required="">
                
                <div class="p-2 text-white bg-blue-600 rounded-r-md">
                    <font-awesome-icon :icon="['fa-solid', 'fa-magnifying-glass']" class="" size="xl" style="color: white;" />
                </div>
            </div>

            <div class="p-2 basis-1/4 flex flex-row justify-end">
                <!-- add group -->
                <addOrganization />
            </div>
        </div>

        <div class="col-container">
            <!-- groups table -->
            <table class="w-full text-xs text-left shadow-lg font-medium text-gray-500 border-t-2 border-gray-50">
                <thead class="border-b-2 border-gray-200">
                    <tr>
                        <th scope="col" class="pl-3 py-3">
                            <div class="flex items-center cursor-pointer" @click="sortData('Organization_name')">
                            ORGANIZATION NAME
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                            </div>
                        </th>
                        <th scope="col" class="py-3">
                            <div class="flex justify-center items-center cursor-pointer" @click="sortData('AMOUNT')">
                            AMOUNT
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                            </div>
                        </th>
                        <th scope="col" class="py-3">
                            <div class="flex justify-center items-center cursor-pointer" @click="sortData('Organization_address')">
                            ADDRESS
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                            </div>
                        </th>
                        <th scope="col" class="py-3">
                            <div class="flex justify-center items-center cursor-pointer" @click="sortData('Organization_subdistrict')">
                            SUBDISTRICT
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                            </div>
                        </th>
                        <th scope="col" class="py-3">
                            <div class="flex justify-center items-center cursor-pointer" @click="sortData('Organization_district')">
                            DISTRICT
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                            </div>
                        </th>
                        <th scope="col" class="py-3">
                            <div class="flex justify-center items-center cursor-pointer" @click="sortData('Organization_province')">
                            PROVINCE
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                            </div>
                        </th>
                        <th scope="col" class="text-center py-3">
                            <div class="flex justify-center items-center cursor-pointer" @click="sortData('Organization_zipcode')">
                            ZIPCODE
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                            </div>
                        </th>  
                    </tr>
                </thead>
                <tbody class="">
                    <tr class="hover:bg-gray-100" v-for="(group, index) in filteredGroups" :key="index">
                        <td class="py-4 pl-3">{{ group.Organization_name }}</td>
                        <td class="py-4 text-center">{{ getuserCount(group.Organization_name) }}</td>
                        <td class="py-4 text-center">{{ group.Organization_address }}</td>
                        <td class="py-4 text-center">{{ group.Organization_subdistrict }}</td>
                        <td class="py-4 text-center">{{ group.Organization_district }}</td>
                        <td class="py-4 text-center">{{ group.Organization_province }}</td>
                        <td class="py-4 pr-3 text-center">{{ group.Organization_zipcode }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>



<script>
import axios from 'axios';
import addOrganization from '@/components/user-management/addOrganization.vue';
export default{
    middleware: ['auth', 'adminApproval'],
    head: {
        title:"group management",
    },
    data() {
        return {
            groups: [],
            users: [],
            selectedOrganization: null,
            searchInput: '',
            sortColumn: '',
            sortOrder: '',
         }
    },
    components:{
        addOrganization,
    },
    mounted() {
        this.fetchGroups();
        this.fetchUsers();
        const modalToggles = document.querySelectorAll('.modal-toggle');
            modalToggles.forEach((toggle) => {
            toggle.addEventListener('change', () => {
                if (toggle.checked) {
                toggle.parentElement.querySelector('.modal').classList.add('open');
                } else {
                toggle.parentElement.querySelector('.modal').classList.remove('open');
                }
            });
        });

        const modalCloses = document.querySelectorAll('.modal-close');
            modalCloses.forEach((close) => {
            close.addEventListener('click', () => {
                close.parentElement.parentElement.parentElement.querySelector('.modal-toggle').checked = false;
                close.parentElement.parentElement.parentElement.querySelector('.modal').classList.remove('open');
            });
        });
        
    },
    computed: {
        filteredGroups() {
            if (this.searchInput) {
            // If a search term is entered, filter the groups based on the organization name
            return this.groups.filter(group => {
                return group.Organization_name.toLowerCase().includes(this.searchInput.toLowerCase());
            });
            } else {
            // If no search term is entered, return all the groups
            return this.groups;
            }
        },
    },
    methods: {
        getuserCount(organizationName) {
            return this.users.filter(
                (user) => user.Organization_name === organizationName
            ).length;
        },
        fetchUsers() {
            this.$axios.get('/employee')
                .then(response => {
                this.users = response.data; // Update the users array with the fetched data
                })
                .catch(error => {
                console.error(error);
                });
        },
        fetchGroups() {
            this.$axios.get('/organization')
                .then(response => {
                this.groups = response.data; // Update the groups array with the fetched data
                })
                .catch(error => {
                console.error(error);
                });
        },
        editItem(index) {
        // Handle edit functionality for the item at the specified index
        // e.g., this.items[index].edit = true;
        },
        showDeleteModal(index) {
            const modalToggle = document.getElementById(`modal-toggle-${index}`);
            modalToggle.checked = true;
        },
        deleteItem(index) {
            // Use splice to remove the item at the given index from the items array
            this.items.splice(index, 1);
            const modalToggle = document.getElementById(`modal-toggle-${index}`);
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
        sortData(column) {
            // If the same column is clicked, toggle the sort order
            if (column === 'AMOUNT') {
                this.data.sort((a, b) => this.getUserCount(a.Organization_name) - this.getUserCount(b.Organization_name));
            } else if (this.sortColumn === column) {
                this.sortOrder = this.sortOrder === 'asc' ? 'desc' : 'asc';
            } else {
                // If a new column is clicked, set the sort column and default to ascending order
                this.sortColumn = column;
                this.sortOrder = 'asc';
            }
            // Sort the data based on the selected column and sort order
            this.filteredGroups.sort((a, b) => {
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
    }
}
</script>