<template>
  <div>
    <div class="page-container mt-4">
      <div class="header">
        <h1 class="title">
          Uploaded Files
        </h1>
      </div>
      <div class="justify-center text-center px-6 py-8 rounded-md mx-4">
        <table class="table-auto w-full">
          <thead class="bg-gray-700 text-white">
            <tr>
              <th class="px-4 py-2 w-[80%]">File Name</th>
              <th class="px-4 py-2 w-[10%]">File Size</th>
              <!-- <th class="px-4 py-2 w-[10%]">Action</th> -->
            </tr>
          </thead>
          <tbody>
            <!-- Loop through the uploaded files and display them in the table -->
            <tr v-for="(file, index) in uploadedFiles" :key="index">
              <td class="border px-4 py-2">{{ file.name }}</td>
              <td class="border px-4 py-2">{{ formatFileSize(file.size) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <div class="flex justify-between px-6 m-4 rounded-md">
        <button @click="navigateBack" class="px-4 py-1.5 bg-gray-300 rounded-md text-gray-700">
          Back
        </button>
        <div>
          <button @click="submitNextflow" v-if="fileListFetched" class="px-4 py-1.5 bg-blue-500 rounded-md text-white">
            Submit
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import vueFilePond from "vue-filepond";
import "filepond/dist/filepond.min.css";
import FilePondPluginFileValidateType from "filepond-plugin-file-validate-type";

const FilePond = vueFilePond(FilePondPluginFileValidateType);
export default {
  data() {
    return {
      formData:{},
      allowedFileFormats: [],
      uploadedExtensions: [],
      fileListFetched: false,
      myServer: {
        process: (
          fieldName,
          file,
          metadata,
          load,
          error,
          progress,
          abort,
          transfer,
          options
        ) => {
          const fileExtension = `.${file.name.split(".").pop().toLowerCase()}`;
          const fileNameWithoutExtension = file.name
            .split(".")
            .slice(0, -1)
            .join("."); // Get the file name without the extension

          if (!this.allowedFileFormats.includes(fileExtension)) {
            error("!!error file type");
            alert("Wrong file extension");
            return;
          }

          // Check if any uploaded file has a different name (excluding the extension)
          const hasDifferentNamedFile = this.myFiles.some((uploadedFile) => {
            const uploadedFileNameWithoutExt = uploadedFile.file.name
              .split(".")
              .slice(0, -1)
              .join(".");
            return fileNameWithoutExtension !== uploadedFileNameWithoutExt;
          });

          if (hasDifferentNamedFile) {
            error("!!error different named files");
            alert("The files name must be the same.");
            return;
          }

          if (this.uploadedExtensions.includes(fileExtension)) {
            error("!!error duplicate extension");
            alert("1 file per extension");
            return;
          }

          this.uploadedExtensions.push(fileExtension);
          setTimeout(() => {
            load(file.name);
          }, 500);
        },
      },
      myFiles: [],
      uploadedFiles: [],
      formData: {}
    };
  },
  computed: {
    fileType() {
      return this.$store.state.fileType;
    },
    isUploadButtonDisabled() {
      let mFiles;
      switch (this.fileType) {
        case "pedmap":
          mFiles = 2;
          break;
        case "bedbimfam":
          mFiles = 3;
          break;
        default:
          mFiles = 0; // Set to 0 or any other value if you want to disable the upload button for unknown fileType.
      }
      return this.myFiles.length < mFiles;
    },
  },
  created() {
        if (this.$route.query.projectData) {
        const projectData = JSON.parse(this.$route.query.projectData);
        this.formData = { ...this.formData, ...projectData };
        }
    },
  mounted() {
    this.updateallowedFileFormats();
    this.fetchFileList();
  },
  methods: {
    formatFileSize(sizeInGB) {
      if (sizeInGB === undefined) {
        return "N/A";
      }
      if (sizeInGB < 1) {
        return `${Math.round(sizeInGB * 1024)} MB`;
      } else {
        return `${sizeInGB.toFixed(2)} GB`;
      }
    },
    updateFiles(files) {
      this.myFiles = files;
    },
    handleFilePondInit() {
      console.log("FilePond has initialized");
    },
    async fetchFileList() {
      const user_id = this.$store.state.userId;
      const inputField = this.formData.input;
      const project_id = inputField.split('/')[1];
      const listLink = `/minio_list/?user_id=${user_id}&project_id=${project_id}`;

      try {
        const response = await this.$axios.get(listLink);
        if (response.data.status === "success") {
          // Update the uploadedFiles array with the fetched data
          this.uploadedFiles = response.data.myfile.map((file) => ({
            name: file[0],
            size: file[1],
          }));
          this.fileListFetched = true;
        } else {
          console.error("Error fetching file list:", response.data.message);
        }
      } catch (error) {
        console.error("Error fetching file list:", error);
      }
    },
    updateallowedFileFormats() {
      switch (this.fileType) {
        case "bedbimfam":
          this.allowedFileFormats = [".bed", ".bim", ".fam"];
          break;
        case "pedmap":
          this.allowedFileFormats = [".ped", ".map"];
          break;
        default:
          this.allowedFileFormats = [];
          break;
      }
    },
    async deleteFile(index) {
      const fileToDelete = this.uploadedFiles[index];
      const user_id = this.$store.state.userId;
      const project_id = this.$store.state.projectId;
      const filename = fileToDelete.name;

      try {
        const formData = new FormData();
        formData.append("user_id", user_id);
        formData.append("project_id", project_id);
        formData.append("filename", filename);

        const deleteLink = "/minio_del/";
        const response = await this.$axios.post(deleteLink, formData, {});

        if (response.data.status === "success") {
          this.uploadedFiles.splice(index, 1);
        } else {
          console.error("Error deleting file:", response.data.message);
        }
      } catch (error) {
        console.error("Error deleting file:", error);
      }
    },
    async UploadFileLog() {
      try {
        const apiUrl = "/create-activity-log/";
        const userid = this.$store.state.userId;

        // Create the form data using URLSearchParams
        const formData = new URLSearchParams();
        formData.append("user", userid);
        formData.append("activity_type", "file_upload");

        const config = {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
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
    async navigateBack() {
      this.$router.push({
        path: '/imputation/resubmit',
        query: { projectData: JSON.stringify(this.formData), back: 'true' }
      });
    },
    submitNextflow() {
      const projectId = this.$store.state.EditprojectId;
      this.$axios.post(`/projects/submitproject/${projectId}/`)
          .then((response) => {
              this.submitProjectLog();
              this.$router.push('/imputation/list')
          })
    },
    async submitProjectLog() {
            try {
                const apiUrl = '/create-activity-log/';
                const userid = this.$store.state.userId;

                // Create the form data using URLSearchParams
                const formData = new URLSearchParams();
                formData.append('user', userid);
                formData.append('activity_type', 'project_submit_to_nextflow');

                const config = {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                };

                const response = await this.$axios.post(apiUrl, formData.toString(), config);
                console.log(response.data);
            } catch (error) {
                console.error(error);
            }
        },
  },
  components: {
    FilePond,
  },
};
</script>
