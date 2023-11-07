<template>
    <section v-if="dataFetched" class="bg-gray-50">
        <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
            <div class="w-full bg-white rounded-lg shadow md:mt-0 sm:max-w-md xl:p-0">
                <div class="p-6 space-y-4 md:space-y-6 sm:p-8 sm:px-12 items-center">
                    <div class="flex justify-center">
                        <font-awesome-icon :icon="['fasr', 'circle-check']" size="2xl" color="#0e7490"/>
                    </div>
                    <div class="space-y-2">
                        <h1 class="text-xl text-cyan-700 font-bold leading-tight tracking-tight md:text-2xl text-center">
                        LOGIN SUCCESSFUL
                         </h1>
                        <h1 class="text-md text-center">
                            You have successfully signed into your account. Your role is  <b>{{userRole}}</b>
                        </h1>
                    </div>
                    <div class="flex justify-center">
                        <NuxtLink to="/" class="text-white bg-cyan-700 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-md text-sm px-8 py-2.5 text-center">
                            <span class="flex-1">Go To Homepage</span>
                        </NuxtLink>
                    </div>
                </div>
            </div> 
        </div>
        <input type="checkbox" id="modal-toggle-6" class="modal-toggle" />
            <div class="modal">
                <div class="modal-content bg-white rounded-md p-5 shadow-md space-y-2">
                    <h2 class="mb-4 text-black text-lg">Continue your project?</h2>
                    <div>
                        <p class="border-t border-gray-200 py-4">You have an ongoing project. Do you want to continue it?</p>
                    </div>
                    <div class="modal-actions space-x-2">
                        <button class="text-white bg-blue-500 px-5 py-2.5 rounded-md" @click="continueProject()">Continue Project</button>
                        <label class="border border-gray-200 px-5 py-2.5 rounded-md cursor-pointer" @click="clearProject()" for="modal-toggle-6">Start Over</label>
                    </div>
                </div>
            </div>
    </section>
    <div v-else class="flex items-center justify-center h-screen">
        <div class="text-center">
        <div class="flex items-center justify-center" role="status">
            <svg aria-hidden="true" class="inline w-24 h-24 mr-2 text-gray-200 animate-spin fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
            </svg>
            <span class="sr-only">Loading...</span>
        </div>
    </div>
</div>
</template>

<script>
import axios from "axios";
export default {
    middleware: 'auth',
    layout:'empty',
    data() {
        return {
            resubmit:false,
            users: [],
            userRole: '',
            user_id:'',
            dataFetched: false,
        };
    },
    mounted() {
        this.approvalCheck();
    },
    methods: {
        async fetchUserInfo(mail) {
            const apiUrl = `/useremail/${mail}`;
            const userData = {
                    first_name: this.$auth.user.given_name,
                    last_name: this.$auth.user.family_name,
                    email: mail,
                };
            try {
                const response = await this.$axios.get(apiUrl);
                if (response.data) {
                    this.userRole = response.data.role;
                    this.user_id = response.data.user_id;
                    if (response.data.approval !== 'approved') {
                        await this.$axios.get(`/send-email/${mail}/`);
                    }
                    console.log('Data:', response.data);
                } else {
                    this.userRole = 'User';
                    await this.$axios.post('/user/', userData);
                    await this.$axios.get(`/send-email/${mail}/`);
                    console.log('Posted userData:', userData);
                    this.dataFetched = true;
                }
            } catch (error) {
                await this.$axios.post('/user/', userData);
                this.dataFetched = true;
                console.error('Error:', error);
            }
            this.$axios.get(`/check-ongoing-project/?user_id=${this.user_id}`)
                .then((response) => {
                if (response.data.has_ongoing_project) {
                    this.resubmit = response.data.resubmit;
                    this.showContinueModal();
                    const projectId = response.data.project_id;
                    this.$store.dispatch('setProjectId', projectId);
                }
                })
                .catch((error) => {
                console.error('Error checking ongoing project:', error);
                });
            this.dataFetched = true;
        },
        showContinueModal() {
            const modalToggle = document.getElementById(`modal-toggle-6`);
            modalToggle.checked = true;
        },
        approvalCheck() {
            const email = this.$auth.user.email;
            this.fetchUserInfo(email)
        },
        async continueProject() {
            try {
                const response = await this.$axios.get(`/projects/getproject/${this.$store.state.projectId}`);
                const fileType = response.data.inputtype;
                this.$store.dispatch('setFileType', fileType);
                this.$store.dispatch('setUserId', this.user_id);
                if (this.resubmit === true) {
                    const inputField = response.data.input;
                    const continueProject = inputField.split('/')[1];
                    this.$store.dispatch('setProjectId', continueProject);
                    this.$store.dispatch('setEditProjectId', response.data.project_id);
                    this.$router.push({
                    path: '/imputation/resubmit/upload',
                    query: { projectData: JSON.stringify(response.data), back: 'true' }
                });
                } else{
                    if (response.data.input === null) {
                        this.$router.push({
                        path: '/imputation/upload',
                        query: { projectData: JSON.stringify(response.data), back: 'true' }
                    });
                    } else {
                        const inputField = response.data.input;
                        const continueProject = inputField.split('/')[1];
                        this.$store.dispatch('setProjectId', continueProject);
                        this.$router.push({
                            path: '/imputation/upload',
                            query: { projectData: JSON.stringify(response.data) }
                        });
                    }
                }
            } catch (error) {
                console.error('Error fetching project data:', error);
            }
        },
        clearProject() {
            this.$axios.delete(`/delete-ongoing-project/?user_id=${this.user_id}`);
            this.$axios.delete(`/delete_project/${this.$store.state.projectId}/`);  
            this.$router.push({
                        path: '/imputation/',
                    });
        },
    },
}
</script>