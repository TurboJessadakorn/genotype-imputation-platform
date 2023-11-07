<template>
    <div class="page-container">
        <div class="header">  
            <h1 class="title">Activity log</h1>
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
            <!-- logs table -->
            <table class="w-full text-xs text-left shadow-lg font-medium text-gray-500 border-t-2 border-gray-50">
                <thead class="border-b-2 border-gray-200">
                    <tr>
                        <th scope="col" class="pl-3 py-3">
                            <div class="flex items-center cursor-pointer" @click="sortData('Organization_name')">
                            ID
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                            </div>
                        </th>
                        <th scope="col" class="py-3">
                            <div class="flex justify-center items-center cursor-pointer" @click="sortData('user.username')">
                            USERNAME
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                            </div>
                        </th>
                        <th scope="col" class="py-3">
                            <div class="flex justify-center items-center cursor-pointer" @click="sortData('Organization_address')">
                            ACTION
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                            </div>
                        </th>
                        <th scope="col" class="py-3">
                            <div class="flex justify-center items-center cursor-pointer" @click="sortData('Organization_subdistrict')">
                            DATE
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                            </div>
                        </th>
                        <th scope="col" class="py-3">
                            <div class="flex justify-center items-center cursor-pointer" @click="sortData('Organization_district')">
                            DESCRIPTION
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                            </div>
                        </th>
                    </tr>
                </thead>
                <tbody class="">
                    <tr class="hover:bg-gray-100" v-for="(log, index) in filteredLogs" :key="index">
                        <td class="py-4 pl-3">{{ log.id }}</td>
                        <td class="py-4 text-center">{{ log.user.username }}</td>
                        <td class="py-4 text-center">{{ log.activity_type }}</td>
                        <td class="py-4 text-center">{{ log.activity_time }}</td>
                        <td class="py-4 text-center">{{ log.description }}</td>
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
        title:"log management",
    },
    data() {
        return {
            logs: [],
            users: [],
            selectedOrganization: null,
            searchInput: '',
            sortColumn: '',
            sortOrder: '',
            fetchComplete: false,
         }
    },
    components:{
        addOrganization,
    },
    mounted() {
        this.fetchActivities();
        
    },
    computed: {
        filteredLogs() {
            if (this.searchInput) {
            // If a search term is entered, filter the logs based on the organization name
            return this.logs.filter(log => {
                return log.user.username.toLowerCase().includes(this.searchInput.toLowerCase());
            });
            } else {
            // If no search term is entered, return all the logs
            return this.logs;
            }
        },
    },
    methods: {
        async fetchActivities() {
            try {
            const response = await this.$axios.get('/get-activity-log/');
            this.logs = response.data;
            this.fetchComplete = true;
            } catch (error) {
            console.error('Error:', error);
            }
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
            this.filteredLogs.sort((a, b) => {
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