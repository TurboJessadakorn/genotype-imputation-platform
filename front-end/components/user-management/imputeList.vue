<template>
    <div class="modal" v-if="selectedUser">
      <div class="modal-content">
        <h2>Imputation List for {{ selectedUser.Efirstname }} {{ selectedUser.Elastname }}</h2>
        <ul>
          <li v-for="imputation in selectedUser.imputations" :key="imputation.id">
            {{ imputation.name }} - Progress: {{ imputation.progress }}
          </li>
        </ul>
        <button @click="closeModal">Close</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['selectedUser'],
    methods: {
      closeModal() {
        this.$emit('close');
      }
    }
  }
  </script>
  