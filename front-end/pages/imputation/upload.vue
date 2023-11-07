<template>
  <div>
    <div class="page-container">
      <div class="header">
            <h1 v-if="fileType === 'pedmap'" class="title">
                Upload Selected File Types (.ped, .map)
            </h1>
            <h1 v-if="fileType === 'bedbimfam'" class="title">
                Upload Selected File Types (.bed, .bim, .fam)
            </h1>
            <h1 v-if="fileType === 'vcfformat'" class="title">
                Upload Selected File Type (.vcf)
            </h1>
        </div>
      <div
        v-if="fileType === 'pedmap'"
        class="justify-center text-center px-6 py-8 rounded-md m-4"
      >
        <file-pond
          name="test"
          ref="pond"
          allow-multiple="true"
          maxFiles="2"
          label-idle='Drag & Drop your .ped .map files or <span class="filepond--label-action"> Browse </span>'
          v-on:input="updateFiles"
          v-bind:server="myServer"
          v-on:init="handleFilePondInit"
          v-on:processfilerevert="handleFileRevert"
        />
        <button @click="updateFilePath" class="btn btn-sm btn-wide btn-primary" :disabled="isUploadButtonDisabled">Upload all</button>
      </div>

      <div
        v-if="fileType === 'bedbimfam'"
        class="justify-center text-center px-6 py-8 rounded-md m-4"
      >
        <file-pond
          name="test"
          ref="pond"
          allow-multiple="true"
          maxFiles="3"
          label-idle='Drag & Drop your.bed .bim .fam files or <span class="filepond--label-action"> Browse </span>'
          v-on:input="updateFiles"
          v-bind:server="myServer"
          v-on:init="handleFilePondInit"
          v-on:processfilerevert="handleFileRevert"
        />
        <button @click="updateFilePath" class="btn btn-sm btn-wide btn-primary" :disabled="isUploadButtonDisabled">Upload all</button>
      </div>
      <!-- for debugging -->
      <div
        v-if="fileType === 'vcfformat'"
        class="justify-center text-center px-6 py-8 rounded-md m-4"
      >
        <file-pond
          name="test"
          ref="pond"
          allow-multiple="true"
          maxFiles="1"
          label-idle='Drag & Drop your .vcf file or <span class="filepond--label-action"> Browse </span>'
          v-on:input="updateFiles"
          v-bind:server="myServer"
          v-on:init="handleFilePondInit"
          v-on:processfilerevert="handleFileRevert"
        />
        <button @click="updateFilePath" class="btn btn-sm btn-wide btn-primary" :disabled="isUploadButtonDisabled">Upload all</button>
      </div>
    </div>
    <div class="page-container mt-4">
      <div class="justify-center text-center px-6 py-8 rounded-md m-4">
        <table class="table-auto mt-4 w-full">
          <thead class="bg-gray-700 text-white">
            <tr>
              <th class="px-4 py-2 w-[80%]">File Name</th>
              <th class="px-4 py-2 w-[10%]">File Size</th>
              <th class="px-4 py-2 w-[10%]">Action</th>
            </tr>
          </thead>
          <tbody>
            <!-- Loop through the uploaded files and display them in the table -->
            <tr v-for="(file, index) in uploadedFiles" :key="index">
              <td class="border px-4 py-2">{{ file.name }}</td>
              <td class="border px-4 py-2">{{ formatFileSize(file.size) }}</td>
              <td class="border px-4 py-2">
                <button
                  @click="deleteFile(index)"
                  class="btn btn-xs btn-outline btn-danger"
                >
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <div class="flex justify-between p-6 m-4 rounded-md">
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
          
          const remainingExtensions = this.getRemainingExtensions.filter(
            ext => !this.uploadedExtensions.includes(ext)
          );
          
          
          setTimeout(() => {
            load(file.name);
          }, 500);
          if (remainingExtensions.length > 0) {
            const remainingFiles = remainingExtensions.map(ext => `${this.myFiles[0].file.name.split('.')[0]}${ext}`).join('\n- ');
            const alertMessage = `The remaining files:\n- ${remainingFiles}`;
            alert(alertMessage);
            return;
          }
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
    getRemainingExtensions() {
      switch (this.fileType) {
        case 'pedmap':
          return ['.ped', '.map'];
        case 'bedbimfam':
          return ['.bed', '.bim', '.fam'];
        case 'vcf':
          return ['.vcf'];
        default:
          return [];
      }
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
        case "vcf":
          mFiles = 1;
          break;
        default:
          mFiles = 0; // Set to 0 or any other value if you want to disable the upload button for unknown fileType.
      }
      return this.uploadedExtensions.length < mFiles;
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
    handleFileRevert(file) {
      const extension = `.${file.file.name.split(".").pop().toLowerCase()}`;
      
      // Remove the extension from the array
      this.uploadedExtensions = this.uploadedExtensions.filter(ext => ext !== extension);
    },
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
    async updateFilePath() {
      const user_id = this.$store.state.userId;
      const project_id = this.$store.state.projectId;

      const file_path = `${user_id}/${project_id}`;
      try {
        const Link = `/projects/file/${project_id}/`;

        const response = await this.$axios.post(Link, {
          input_file_path: file_path,
        });
        console.log(response.data);
      } catch (error) {
        console.error("Error updating file path:", error);
      }

      // get presigned url
      const presignedUrls = [];
      for (const file of this.myFiles) {
        console.log(file);
        const file_name = file.filename;
        const presignedUrlLink = `/generate_presigned_url/?user_id=${user_id}&project_id=${project_id}&file_name=${file_name}`;
        const response = await this.$axios.get(presignedUrlLink, {});
        presignedUrls.push(response.data.presigned_url);
      }
      console.log(presignedUrls);
      try {
        for (let i = 0; i < this.myFiles.length; i++) {
          const file = this.myFiles[i];
          const presignedUrl = presignedUrls[i];
          const file_path = `${user_id}/${project_id}/${file.name}`;

          const uploadResponse = await axios.put(presignedUrl, file.file, {
            headers: {
              "x-amz-meta-file-path": file_path, // Add a custom header to store the file path
            },
          });
        }

        const listLink = `/minio_list/?user_id=${user_id}&project_id=${project_id}`;
        this.$axios
          .get(listLink)
          .then((response) => {
            this.uploadedFiles = response.data; // Update the users array with the fetched data
          })
          .catch((error) => {
            console.error(error);
          });
        this.UploadFileLog();
        const conLink = `/delete-ongoing-project/?user_id=${user_id}`;
        this.$axios.delete(conLink);
        this.fetchFileList();
        this.fileListFetched = true;
      } catch (error) {
        console.error("Error uploading files:", error);
      }
    },
    async fetchFileList() {
      const user_id = this.$store.state.userId;
      const project_id = this.$store.state.projectId;
      const listLink = `/minio_list/?user_id=${user_id}&project_id=${project_id}`;

      try {
        const response = await this.$axios.get(listLink);
        if (response.data.status === "success") {
          // Update the uploadedFiles array with the fetched data
          this.uploadedFiles = response.data.myfile.map((file) => ({
            name: file[0],
            size: file[1],
          }));
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
      console.log(this.formdata)
      this.$router.push({
        path: '/imputation',
        query: { projectData: JSON.stringify(this.formData), back: 'true' }
      });
    },
    submitNextflow() {
      const projectId = this.$store.state.projectId;
      this.$axios.post(`/projects/submitproject/${projectId}/`)
          .then((response) => {
              this.submitProjectLog();
              this.$router.push('list')
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
