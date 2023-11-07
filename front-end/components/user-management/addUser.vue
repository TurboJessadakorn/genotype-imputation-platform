<template>
    <label for="my-modal1" class="flex items-center text-white bg-blue-600 dark:bg-blue-700 rounded-md py-2 px-8 cursor-pointer">
        <font-awesome-icon :icon="['fas', 'fa-plus']" class="pr-2" size="xl" style="color: white;" />
        <span class="flex-1 whitespace-nowrap">Create group</span>  
            <input type="checkbox" id="my-modal1" class="modal-toggle" />
            <label for="my-modal1" class="modal cursor-pointer">
            <label class="modal-box relative" for="">
                <form @submit.prevent="addEmployee" class="p-2">
                    <div class="grid gap-6 mb-6 md:grid-cols-2">
                        <div>
                            <label for="first_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">First name</label>
                            <input type="text" id="first_name" v-model="employee.Efirstname" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Jessadakorn" required>
                        </div>
                        <div>
                            <label for="last_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Last name</label>
                            <input type="text" id="last_name" v-model="employee.Elastname" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Paopatimakorn" required>
                        </div>
                    </div>
                    <div class="mb-6">
                        <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email address</label>
                        <input type="email" id="email" v-model="employee.Eemail" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="jessadakorn.paopati@gmail.com" required>
                    </div>
                    <div class="mb-6">
                        <label for="organization" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Organization</label>
                        <select id="organization" v-model="employee.Organization_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
                            <option value="">Choose organization</option>
                            <option v-for="org in organizations" :key="org.Organization_id" :value="org.Organization_name">{{ org.Organization_name }}</option>
                        </select>
                    </div>
                    <div class="mb-6">
                        <label for="role" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Role</label>
                        <select id="role" v-model="employee.Erole" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
                            <option value="">Choose role</option>
                            <option value="admin">Admin</option>
                            <option value="curator">Curator</option>
                            <option value="worker">Worker</option>
                        </select>
                    </div> 
                    <!-- <div class="mb-6">
                        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                        <input type="password" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="•••••••••" required>
                    </div> 
                    <div class="mb-6">
                        <label for="confirm_password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Confirm password</label>
                        <input type="password" id="confirm_password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="•••••••••" required>
                    </div>  -->
                    <div class="flex items-start mb-6">
                        <div class="flex items-center h-5">
                        <input id="remember" type="checkbox" value="" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800" required>
                        </div>
                        <label for="remember" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">I agree with the <a href="#" class="text-blue-600 hover:underline dark:text-blue-500">terms and conditions</a>.</label>
                    </div>
                    <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
                </form>
            </label>
            </label>
    </label>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      employee: {
        Efirstname: '',
        Elastname: '',
        Eemail: '',
        Erole: '',
        Organization_name: '',
    },
      organizations: [ ] // Fetch or assign the organizations data
    };
  },
  mounted(){
    this.fetchOrga();
  },
  methods: {
    addEmployee() {
      // Send the employee data to the backend API
      // You can use Axios or the Fetch API to make the HTTP request to your backend
      // Example using Axios:
        axios.post('http://127.0.0.1:8000/employee', this.employee)
            .then(response => {
            console.log(response.data); // Handle the response as needed
            this.closeModal();
            })
            .catch(error => {
            console.error(error); // Handle the error
            });
        },
    fetchOrga() {
            axios.get('http://127.0.0.1:8000/organization')
                .then(response => {
                this.organizations = response.data; // Update the groups array with the fetched data
                })
                .catch(error => {
                console.error(error);
                });
        },
    closeModal() {
      const checkbox = document.getElementById('my-modal1');
      checkbox.checked = false;
    },
  }
};
</script>