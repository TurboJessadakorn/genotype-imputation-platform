<template>
  <label for="my-modal1" class="flex items-center text-white bg-blue-600 dark:bg-blue-700 rounded-md py-2 px-8 cursor-pointer">
    <font-awesome-icon :icon="['fas', 'fa-plus']" class="pr-2" size="xl" style="color: white;" />
    <span class="flex-1 whitespace-nowrap">Add organization</span>  
    <input type="checkbox" id="my-modal1" class="modal-toggle" />
    <label for="my-modal1" class="modal cursor-pointer">
      <label class="modal-box relative" for="">
        <form @submit.prevent="addOrganization" class="p-2">
          <div class="mb-6">
              <label for="org_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Organization Name</label>
              <input type="text" id="org_name" v-model="organization.Organization_name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="NSTDA" required>
          </div> 
          <div class="grid gap-6 mb-6 md:grid-cols-2">
            <div>
                <label for="address" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Address</label>
                <input type="text" id="address" v-model="organization.Organization_address" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="111 Thailand Science Park" required>
            </div>
            <div>
                <label for="subdistrict" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Subdistrict</label>
                <input type="text" id="subdistrict" v-model="organization.Organization_subdistrict" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Khlong Nueng" required>
            </div>
            <div>
                <label for="district" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">District</label>
                <input type="text" id="district" v-model="organization.Organization_district" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Khlong Luang" required>
            </div>
            <div>
                <label for="province" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Province</label>
                <input type="text" id="province" v-model="organization.Organization_province" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Pathum Thani" required>
            </div>
            <div class="mb-6">
              <label for="zipcode" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Zipcode</label>
              <input type="text" id="zipcode" v-model="organization.Organization_zipcode" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="12120" required>
            </div>
          </div>
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
      organization: {
        Organization_name: '',
        Organization_address: '',
        Organization_district: '',
        Organization_subdistrict: '',
        Organization_province: '',
        Organization_zipcode: '',
      },
    };
  },
  methods: {
    addOrganization() {
      axios.post('http://127.0.0.1:8000/organization', this.organization)
      .then(response => {
            console.log(response.data);
            this.closeModal(); 
        })
        .catch((error) => {
          // Handle error
          console.error(error);
        });
    },
    closeModal() {
      const checkbox = document.getElementById('my-modal1');
      checkbox.checked = false;
    },
  },
};
</script>