<template>
    <form @submit.prevent="uploadFile"
        class="page-container">
        <div class="header">
            <h1 class="title">
                Create Imputation Project
            </h1>
        </div>
        <div class="col-container">
            <div class="w-full">
                <h6 class="text-base font-semibold text-black">Project Name</h6>
                <input type="text" v-model="formData.diseaseName" id="disease-name"
                    class="w-full border border-gray-300 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block p-2 mt-2"
                    placeholder="Short disease name" required />
            </div>
        </div>
        <div class="col-container md:space-x-2">
            <div class="input-container basis-1/2">
                <div class="input-header">
                    <!-- <font-awesome-icon :icon="['fa', 'atom']" size="xl" style="color: #6d6f74" /> -->
                    <h6 class="">Please select the Genome build of your data</h6>
                </div>
                <div class="radio-container">
                    <div class="radio-select">
                        <input checked id="default-radio-1" name="buildversion" type="radio" value="hg38"
                            v-model="formData.buildversion"
                            class="radio radio-primary w-4 h-4" required />
                        <label for="default-radio-1" class="ml-2 cursor-pointer">GRCh38/hg38</label>
                    </div>
                    <div class="radio-select">
                        <input id="default-radio-2" name="buildversion" type="radio" value="hg19" v-model="formData.buildversion"
                            class="radio radio-primary w-4 h-4"/>
                        <label for="default-radio-2" class="ml-2 cursor-pointer">GRCh37/hg19</label>
                    </div>
                </div>
            </div>

            <div class="input-container basis-1/2">
                <div class="input-header">
                    <!-- <font-awesome-icon :icon="['fa', 'atom']" size="xl" style="color: #6d6f74" /> -->
                    <h6 class="">Upload genotype file for imputation</h6>
                </div>
                <div class="radio-container">
                    <div class="radio-select">
                        <input checked id="default-radio-3" name="inputtype" type="radio" value="pedmap"
                            v-model="formData.inputtype"
                            class="radio radio-primary w-4 h-4"
                            required />
                        <label for="default-radio-3" class="ml-2 cursor-pointer ">PED MAP format</label>
                    </div>
                    <div class="radio-select">
                        <input id="default-radio-4" name="inputtype" type="radio" value="bedbimfam"
                            v-model="formData.inputtype"
                            class="radio radio-primary w-4 h-4" />
                        <label for="default-radio-4" class="ml-2 cursor-pointer ">BED BIM FAM format</label>
                    </div>
                    <div class="radio-select">
                        <input id="default-radio-v" name="inputtype" type="radio" value="vcfformat"
                            v-model="formData.inputtype"
                            class="radio radio-primary w-4 h-4" />
                        <label for="default-radio-v" class="ml-2 cursor-pointer ">VCF format</label>
                    </div>
                </div>
            </div>
        </div>

        <!-- <div class="bg-gray-100 justify-center text: text-center px-6 py-8 rounded-md m-4">
            <input class="file:bg-blue-500 file:py-1.5 file:rounded-md file:text-white file:border-0 file:px-4 file:cursor-pointer" type="file"
                ref="fileInput" @change="handleUpload" required/>
        </div> -->

        <div class="col-container pb-0">
            <div class="w-full">
                <div class="input-header">
                    <!-- <font-awesome-icon :icon="['fa', 'atom']" size="xl" style="color: #6d6f74" /> -->
                    <h6 class="">Genotype imputation</h6>
                </div>
            </div>
        </div>

        <div class="col-container py-1">
            <div class="basis-2/5">
                <h6 class="">Reference panels</h6>
            </div>
            <div class="basis-3/5">
                <div class="radio-select">
                    <input checked id="default-radio-5" type="radio" value="ref_raw1kghg38"
                        v-model="formData.ref_raw" name="Holotype"
                        class="radio radio-primary w-4 h-4"
                        required />
                    <label for="default-radio-5" class="ml-2 cursor-pointer ">1,000 Genomes Project (hg38)</label>
                </div>
                <div class="radio-select">
                    <input checked id="default-radio-6" type="radio" value="ref_rawGAsP"
                        v-model="formData.ref_raw" name="Holotype"
                        class="radio radio-primary w-4 h-4" />
                    <label for="default-radio-6" class="ml-2 cursor-pointer">GenomeAsia Pilot (GAsP) Project</label>
                </div>
                <!-- <div class="radio-select">
                    <input checked id="default-radio-7" type="radio" value="ref_rawWGS1175"
                        v-model="formData.ref_raw" name="Holotype"
                        class="radio radio-primary w-4 h-4" />
                    <label for="default-radio-7" class="ml-2 cursor-pointer ">WGS1175 reference data</label>
                </div> -->
                <div class="radio-select">
                    <input checked id="default-radio-8" type="radio" value="ref_rawWGSthaiOnly"
                        v-model="formData.ref_raw" name="Holotype"
                        class="radio radio-primary w-4 h-4" />
                    <label for="default-radio-8" class="ml-2 cursor-pointer">1,000 Thais Reference Panel</label>
                </div>
            </div>
        </div>

        <div class="col-container">
            <div class="basis-2/5">
                <h6 class="">Imputation algorithm</h6>
            </div>
            <div class="basis-3/5">
                <div class="radio-select">
                    <input disabled checked id="default-radio-8" type="radio" value="SHAPEIT"
                         name="algorithm"
                        class="radio radio-primary w-4 h-4"
                        required />
                    <label for="default-radio-8" class="ml-2 cursor-pointer ">SHAPEIT5 followed by IMPUTE5</label>
                </div>
            </div>
        </div>

        <div class="col-container2">
            <div class="input-header w-full">
                <!-- <font-awesome-icon :icon="['fa', 'atom']" size="xl" style="color: #6d6f74" /> -->
                <h6 class="">Preprocessing data</h6>
            </div>

            <mafInput :initialValue="formData.mafvalue" :handlemafValue="setmafValue" />
                        
            <genoInput :initialValue="formData.genovalue" :handlegenoValue="setgenoValue" />
                       
            <hewInput :initialValue="calculateInitialHewValue(formData.hewvalue)" :handlehewValue="sethewValue" />

            <div class="flex mt-3 pb-2 border-b-2 border-gray-200 text-base font-semibold text-black w-full">
                <h6 class="">Post-imputation SNP-QC</h6>
            </div>

            <snpInput :initialValue="formData.infoscore" :handlesnpValue="setsnpValue" />
        </div>

        <div class="text-right p-4 rounded-md">
            <button type="submit" class="px-4 py-1.5 bg-blue-500 rounded-md text-white">
                Next
            </button>
        </div>
    </form>
</template>


<script>
import axios from "axios";
import mafInput from '@/components/impute/mafInput.vue';
import genoInput from '@/components/impute/genoInput.vue';
import snpInput from '@/components/impute/snpInput.vue';
import hewInput from '@/components/impute/hewInput.vue';

export default {
    middleware: ['auth', 'userApproval'],
    head: {
        title: "Create imputation",
    },
    data() {
        return {
            formData: {
                diseaseName: "",
                buildversion: "hg38",
                inputtype: "pedmap",
                ref_raw: "ref_raw1kghg38",
                mafvalue: 0.10,
                genovalue: 0.05,
                hewvalue: 1e-6,
                infoscore: 0.30,
                user: null,
            },
            file: null,
        };
    },
    created() {
        if (this.$route.query.projectData && this.$route.query.back === "true") {
            const projectData = JSON.parse(this.$route.query.projectData);
            this.formData = { ...this.formData, ...projectData };
        }
    },
    methods: {
        setmafValue(value) {
            this.formData.mafvalue = value;
        },
        setgenoValue(value) {
            this.formData.genovalue = value;
        },
        setsnpValue(value) {
            this.formData.infoscore = value;
        },
        sethewValue(value) {
            if (value === "") {
                this.formData.hewvalue = null;
            } else {
                const hewPow = Math.pow(10, -value);
                const parsedValue = hewPow.toFixed(value);
                this.formData.hewvalue = parseFloat(parsedValue);
            }
        },
        calculateInitialHewValue(hewvalue) {
            const hewPow = Math.log10(1 / parseFloat(hewvalue));
            return hewPow;
        },
        handleUpload(event) {
            this.file = event.target.files[0];
            this.formData.input = this.file.name;
        },
        uploadFile() {
            console.log(this.formData);
            this.formData.user = this.$store.state.userId;
            this.$store.dispatch('setFileType', this.formData.inputtype);
            if (this.$route.query.back === "true") {
                const projectId = this.$store.state.projectId;
                this.$axios.put(`/edit_project/${projectId}/`, this.formData)
                    .then((response) => {
                        this.$store.dispatch('setProjectId', projectId);
                        this.editProjectLog();
                        this.$router.push({
                            path: '/imputation/upload',
                            query: { projectData: JSON.stringify(this.formData), back: 'true' }
                        });
                    })
                    .catch((error) => {
                        console.error(error);
                        if (error.response && error.response.status === 400) {
                            alert('Error: Disease name already exists. Please choose a different name.');
                        } else {
                            alert('An error occurred. Please try again later.');
                        }
                    });
            }
            else{
                this.$axios.post("/create_project/", this.formData)
                .then((response) => {
                    const projectId = response.data.project_id;
                    this.$store.dispatch('setProjectId', projectId);
                    this.createProjectLog();
                    this.$axios.get(`/add-ongoing-project/?user_id=${this.formData.user}&project_id=${projectId}`)
                    this.$router.push({
                        path: '/imputation/upload',
                        query: { projectData: JSON.stringify(this.formData), back: 'true' }
                    });
                })
                .catch((error) => {
                    console.error(error);
                    if (error.response && error.response.status === 400) {
                        alert('Error: Disease name already exists. Please choose a different name.');
                    } else {
                        alert('An error occurred. Please try again later.');
                    }
                });
            }
        },
        async createProjectLog() {
            try {
                const apiUrl = '/create-activity-log/';
                const userid = this.$store.state.userId;

                // Create the form data using URLSearchParams
                const formData = new URLSearchParams();
                formData.append('user', userid);
                formData.append('activity_type', 'project_create');

                const config = {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                };

                const response = await this.$axios.post(apiUrl, formData.toString(), config);
                console.log(response.data); // This will log the API response data

                // Handle successful response here (if needed)
            } catch (error) {
                console.error(error);
                // Handle error here (if needed)
            }
        },
        async editProjectLog() {
            try {
                const apiUrl = '/create-activity-log/';
                const userid = this.$store.state.userId;

                // Create the form data using URLSearchParams
                const formData = new URLSearchParams();
                formData.append('user', userid);
                formData.append('activity_type', 'project_edit');

                const config = {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                };

                const response = await this.$axios.post(apiUrl, formData.toString(), config);
                console.log(response.data); // This will log the API response data

                // Handle successful response here (if needed)
            } catch (error) {
                console.error(error);
                // Handle error here (if needed)
            }
        },
    },
    components: {
        mafInput,
        genoInput,
        snpInput,
        hewInput,
    },
};
</script>
