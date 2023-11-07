<template>
    <div class="page-container">

        <!-- delete modal -->
        <input type="checkbox" id="my_modal_6" class="modal-toggle" />
        <div class="modal">
            <div class="modal-content bg-white rounded-md p-5 shadow-md space-y-2">
                <h2 class="mb-4 text-black text-lg">Confirm Deletion</h2>
                <div>
                    <p class="border-t border-gray-200 py-4">Are you sure you want to delete this user's data? If you delete the data you can't recover it.</p>
                </div>
                <div class="modal-actions space-x-2">
                    <button class="text-white bg-red-500 px-5 py-2.5 rounded-md" @click="deleteImpute(itemToDelete)">Delete</button>
                    <label class="border border-gray-200 px-5 py-2.5 rounded-md cursor-pointer" for="my_modal_6">Cancel</label>
                </div>
            </div>
        </div>
        
        <!-- header     -->
        <div class="header">
            <h1 class="title">
                Imputation list
            </h1>
        </div>
        <div class="col-container justify-center">
            <div class="py-2 basis-3/4 flex flex-row">
                <h6 class="mt-2">Show</h6>
                <input
                    type="number"
                    v-model.number="itemsPerPage"
                    id="org_province"
                    class="w-16 mx-1 flex flex-row px-3 py-1.5 space-x-4 border-gray-300 border-2 rounded-md"
                    placeholder="10"
                />
                <h6 class="mt-2">entries</h6>
            </div>
            <!-- search -->
            <div class="py-2 basis-1/4 flex flex-row">
                <h6 class="mt-2">Search:</h6>
                <input type="platform" name="search" id="search" v-model="searchInput"
                    class="border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full ml-2 p-2"
                    placeholder="" required="" />
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
        <div v-if="fetchComplete == true" class="px-6 py-4 pt-0">
            <div class="text-xs">
                <table class="w-full text-xs text-left shadow-zinc-300 shadow-lg font-medium border-t-2 border-gray-100 rounded-md">
                    <thead class="px-2 border-b-2 border-gray-200">
                        <tr>
                            <th scope="col" class="pl-3 py-2 w-[17%]">
                                <div class="" @click="sortData('diseaseName')">
                                    <span class="align-middle">Project Name</span>
                                    <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1 inline-block align-middle" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512">
                                        <path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/>
                                    </svg>
                                </div>
                            </th>
                            <th scope="col" class="py-2 w-[18%]">
                                <div class="flex justify-center" @click="sortData('diseaseName')">
                                    Imputation Reference
                                    <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                                </div>
                            </th>
                            <th scope="col" class="py-2 w-[14%]">
                                <div class="flex justify-center" @click="sortData('diseaseName')">
                                    SNP-QC
                                    <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                                </div>
                            </th>
                            <th scope="col" class="py-2 w-[14%]">
                                <div class="flex justify-center" @click="sortData('status')">
                                    Status
                                    <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                                </div>
                            </th>
                            <th scope="col" class="py-2">
                                <div class="flex justify-center" @click="sortData('progress')">
                                    Progress
                                    <svg xmlns="http://www.w3.org/2000/svg" class="w-3 h-3 ml-1" aria-hidden="true" fill="currentColor" viewBox="0 0 320 512"><path d="M27.66 224h264.7c24.6 0 36.89-29.78 19.54-47.12l-132.3-136.8c-5.406-5.406-12.47-8.107-19.53-8.107c-7.055 0-14.09 2.701-19.45 8.107L8.119 176.9C-9.229 194.2 3.055 224 27.66 224zM292.3 288H27.66c-24.6 0-36.89 29.77-19.54 47.12l132.5 136.8C145.9 477.3 152.1 480 160 480c7.053 0 14.12-2.703 19.53-8.109l132.3-136.8C329.2 317.8 316.9 288 292.3 288z"/></svg>
                                </div>
                            </th>
                            <!-- <th scope="col" class="py-2 w-[15%]">
                                <div class="flex justify-center justify-center">
                                    Upload to GWAS analysis
                                </div>
                            </th> -->
                            <th scope="col" class="py-2 text-center w-[22%]">Manage</th>
                        </tr>
                    </thead>
                    <tbody class="">
                        <tr class="hover:bg-gray-100" v-for="(item, index) in paginatedItems" :key="index" :style="{ opacity: item.status === 'Queueing' ? '0.5' : '1' }">
                            <td class="pl-3 py-2">{{ item.diseaseName }}</td>
                            <td class="py-2 tracking-tighter text-center">{{ getDisplayRef(item.ref_raw) }}</td>
                            <td class="py-2 text-center">
                                <ul class="">
                                    <li>MAF: {{ item.mafvalue !== null ? item.mafvalue : '-' }}</li>
                                    <li>Geno: {{ item.genovalue !== null ? item.genovalue : '-' }}</li>
                                    <li>HEW: {{ item.hewvalue !== null ? item.hewvalue : '-' }}</li>
                                    <li>Info: {{ item.infoscore !== null ? item.infoscore : '-' }}</li>
                                </ul>
                            </td>
                            <td class="py-2 text-center">{{ item.status }}</td>
                            <td class="py-2 text-center">
                                <template v-if="item.status === 'Complete!'">
                                    Complete!
                                </template>
                                <template v-else-if="item.status === 'Queueing'">
                                    <div class="relative w-auto h-2 bg-gray-200 rounded-full mx-2">
                                        <div class="absolute top-0 left-0 h-full bg-blue-700 rounded-full" :style="{ width: item.progress }"></div>
                                    </div>
                                </template>
                                <template v-else>
                                    <div class="relative w-auto h-2 bg-gray-200 rounded-full mx-2">
                                        <div class="bg-primary absolute top-0 left-0 h-full rounded-2xl" :style="{ width: item.progress }">
                                            <span class="bg-primary absolute -right-4 bottom-full mb-2 rounded-sm py-1 px-2 text-xs font-medium text-white">
                                                <span class="bg-primary absolute bottom-[-2px] left-1/2 -z-10 h-2 w-2 -translate-x-1/2 rotate-45 rounded-sm"></span>
                                                {{ item.progress }}
                                            </span>
                                        </div>
                                    </div>
                                </template>
                            </td>
                            <td class="py-3">
                                <div class="flex justify-center space-x-1 font-normal">
                                    <button @click="downloadImputationFile(item)" class="px-2.5 py-1 bg-blue-500 rounded-md text-xs text-white focus:ring-2 focus:outline-none focus:ring-blue-300">
                                        Download
                                    </button>
                                    <button @click="resubmitImpute(item)" class="px-2.5 py-1 bg-emerald-600 rounded-md text-xs text-white focus:ring-2 focus:outline-none focus:ring-emerald-300">
                                        Resubmit
                                    </button>
                                    <label @click="openModal(item)" for="my_modal_6" class="px-2.5 py-1 bg-red-500 rounded-md text-xs text-white focus:ring-2 focus:outline-none focus:ring-red-300 cursor-pointer">
                                        Delete
                                    </label>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="p-4 pt-1 mb-3">
            <div class="flex justify-between items-center"> <!-- Use flex container -->
                <div class="px-2">
                    <!-- <h6 class="px-1">
                        Showing {{ startIndex }} to {{ endIndex }} of {{ totalItems }} entries
                    </h6> -->
                    <NuxtLink to="/imputation/" exact-active-class="font-bold text-gray-700" class="px-4 py-1.5 bg-blue-600 rounded-md text-white"> <!-- Apply flex-grow -->
                        <font-awesome-icon :icon="['fas', 'file-import']" class="" size="md" />
                        <span class="ml-3 whitespace-nowrap">Create new project</span>
                    </NuxtLink>
                </div>
                <div class="flex justify-end space-x-1"> <!-- Remove width class -->
                   <!-- First button -->
                    <button class="pagination-btn"
                        @click="goToPage(1)" :disabled="currentPage === 1">
                        <font-awesome-icon :icon="['fas', 'angle-double-left']" />
                    </button>
                    <!-- Previous button -->
                    <button class="pagination-btn"
                        @click="goToPreviousPage" :disabled="currentPage === 1">
                        <font-awesome-icon :icon="['fas', 'angle-left']" />
                    </button>
                    <div v-for="page in visiblePageNumbers" :key="page" @click="goToPage(page)"
                        class="px-3 py-1.5 rounded-full transition-all duration-300 cursor-pointer"
                        :class="{ 'bg-blue-600': currentPage === page, 'text-white': currentPage === page, 'bg-transparent': currentPage !== page, 'hover:bg-neutral-100': currentPage !== page}">
                        <h1>{{ page }}</h1>
                    </div>
                    <!-- Next button -->
                    <button class="pagination-btn"
                        @click="goToNextPage" :disabled="currentPage === totalPages">
                        <font-awesome-icon :icon="['fas', 'angle-right']" />
                    </button>
                    <!-- Last button -->
                    <button class="pagination-btn"
                        @click="goToPage(totalPages)" :disabled="currentPage === totalPages">
                        <font-awesome-icon :icon="['fas', 'angle-double-right']" />
                    </button>

                </div>
            </div>
        </div>

    </div>
    
</template>

    

<style scoped>
input[type=number]::-webkit-inner-spin-button {
    opacity: 1
}
</style>

<script>
import axios from "axios";
export default {
    middleware: ['auth', 'userApproval'],
    head: {
        title: "All imputation",
    },
    data() {
        return {
            items: [],
            searchInput: "",
            itemsPerPage: 5,
            currentPage: 1,
            sortColumn: '',
            sortOrder: '',
            itemToDelete: null,
            fetchComplete: false,
        };
    },
    mounted() {
        this.fetchImpute();
    },
    computed: {
        filteredItems() {
            return this.items.filter((item) => {
                return item.diseaseName
                    .toLowerCase()
                    .includes(this.searchInput.toLowerCase());
            });
        },
        paginatedItems() {
            const startIndex = (this.currentPage - 1) * this.itemsPerPage;
            const endIndex = startIndex + this.itemsPerPage;
            return this.sortedItems.slice(startIndex, endIndex);
        },
        visiblePageNumbers() {
            const totalPages = this.totalPages;
            const currentPage = this.currentPage;

            if (totalPages <= 5) {
                // If there are less than or equal to 5 pages, show all pages.
                return Array.from({ length: totalPages }, (_, i) => i + 1);
            } else {
                // If there are more than 5 pages, calculate which pages to show.
                const visiblePages = [];

                if (currentPage <= 3) {
                    // Show the first 5 pages.
                    visiblePages.push(1, 2, 3, 4, 5);
                } else if (currentPage >= totalPages - 2) {
                    // Show the last 5 pages.
                    visiblePages.push(totalPages - 4, totalPages - 3, totalPages - 2, totalPages - 1, totalPages);
                } else {
                    // Show 2 pages before and after the current page.
                    visiblePages.push(currentPage - 2, currentPage - 1, currentPage, currentPage + 1, currentPage + 2);
                }

                return visiblePages;
            }
        },
        totalPages() {
            return Math.ceil(this.filteredItems.length / this.itemsPerPage);
        },
        startIndex() {
            if (this.filteredItems.length === 0) {
                return 0;
            }
            return (this.currentPage - 1) * this.itemsPerPage + 1;
        },
        endIndex() {
            return Math.min(
                this.currentPage * this.itemsPerPage,
                this.filteredItems.length
            );
        },
        totalItems() {
            return this.filteredItems.length;
        },
        sortedItems() {
            if (this.sortColumn) {
            const sorted = [...this.filteredItems];
            sorted.sort((a, b) => {
                const valueA = a[this.sortColumn].toUpperCase();
                const valueB = b[this.sortColumn].toUpperCase();

                if (valueA < valueB) {
                return this.sortOrder === 'asc' ? -1 : 1;
                }
                if (valueA > valueB) {
                return this.sortOrder === 'asc' ? 1 : -1;
                }
                return 0;
            });
            return sorted;
            }
            return this.filteredItems;
        },
        getDisplayRef() {
            return (refRawValue) => {
            const refMap = {
                ref_raw1kghg38: "1,000 Genomes Project (hg38)",
                ref_rawGAsP: "GenomeAsia Pilot (GAsP) Project",
                ref_rawWGS1175: "WGS1175 reference data",
                ref_rawWGSthaiOnly: "Only THAI from WGS1175 data",
            };
            return refMap[refRawValue] || refRawValue;
            };
        },
    },
    methods: {
        fetchImpute() {
            const listlink = `/projects/getnextflow/${this.$store.state.userId}/`;
            this.$axios.get(listlink)
                .then((response) => {
                    this.items = response.data;
                    this.fetchComplete = true;
                    console.log(this.items)
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        downloadImputationFile(item) {
            const apiUrl = `/generate_presigned_download_url/?user_id=${this.$store.state.userId}&project_id=${item.project_id}`;

            // Make an HTTP request to obtain the presigned URL
            this.$axios.get(apiUrl)
                .then(response => {
                    console.log(response);
                    const presignedUrl = response.data.presigned_url;

                    // Open a new tab or window to initiate the download
                    window.open(presignedUrl, "_blank");
                })
                .catch(error => {
                    console.error('Error obtaining the presigned URL:', error);
                });
        },
        resubmitImpute(item) {
            console.log(item)
            this.$router.push({
                path: 'resubmit/',
                query: { projectData: JSON.stringify(item) }
            });
        },
        deleteImpute(item) {
            const apiUrl = `/delete_project/${item.project_id}/`;
            this.$axios.delete(apiUrl)

            .then(response => {
                console.log('Item deleted:', response.data);
                const modalToggle = document.getElementById("my_modal_6");
                if (modalToggle) {
                    modalToggle.checked = false;
                };
                this.fetchImpute();
                // this.$router.go();
            })
            .catch(error => {
                console.error('Error deleting item:', error);
            });
        },
        openModal(item) {
            this.itemToDelete = item;
            console.log(this.itemToDelete)
        },
        closeModal() {
            const modal = document.querySelector('.modal');
            modal.classList.remove('show');
        },
        goToPage(page) {
            this.currentPage = page;
        },
        goToPreviousPage() {
            if (this.currentPage > 1) {
                this.currentPage--;
            }
        },
        goToNextPage() {
            if (this.currentPage < this.totalPages) {
                this.currentPage++;
            }
        },
        sortData(column) {
            if (this.sortColumn === column) {
                this.sortOrder = this.sortOrder === "asc" ? "desc" : "asc";
            } else {
                this.sortColumn = column;
                this.sortOrder = "asc";
            }

            // Sort the data array based on the selected column and order
            this.sortedItems = [...this.items].sort((a, b) => {
                const valueA = a[column].toUpperCase();
                const valueB = b[column].toUpperCase();

                if (valueA < valueB) {
                return this.sortOrder === "asc" ? -1 : 1;
                }
                if (valueA > valueB) {
                return this.sortOrder === "asc" ? 1 : -1;
                }
                return 0;
            });
        },
    },
};
</script>