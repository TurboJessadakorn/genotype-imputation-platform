<template>
  <div class="post-number-container pt-1">
    <div class="basis-2/5 flex items-center">
      <label class="relative inline-flex items-center cursor-pointer">
        <input type="checkbox" :checked="switchValue" @click="toggleSwitchValue" class="sr-only peer" />
        <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600">
        </div>
      </label>
      <h6 class="ml-2">Minor allele frequency (--maf)</h6>
    </div>
    <div class="basis-3/5">
      <div class="pr-32">
        <div class="h-10 w-32" v-bind:class="{ 'opacity-50': !switchValue }">
          <div class="flex flex-row h-10 w-full rounded-lg relative bg-transparent mt-1">
            <button type="button" @click="handleMinus"
              class="border border-r-0 border-gray-300 text-blue-600 hover:text-gray-700 hover:bg-gray-200 h-full w-20 rounded-l cursor-pointer outline-none">
              <span class="m-auto text-2xl font-md">−</span>
            </button>
            <input required type="number" step=".01" min="0.00" max="0.50" v-model="roundedmafValue" id="mafValue"
              name="mafValue"
              class="outline-none focus:outline-none text-center w-full border-y border-gray-300 font-semibold text-md md:text-base cursor-text flex items-center"
              @input="handleInput" @keydown="preventEInput" :disabled="!switchValue"/>
            <button type="button" @click="handlePlus"
              class="border border-l-0 border-gray-300 text-blue-600 hover:text-gray-700 hover:bg-gray-200 h-full w-20 rounded-r cursor-pointer">
              <span class="m-auto text-2xl font-md">+</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>

<script>
export default {
  data() {
    return {
      switchValue: this.initialValue !== null, 
      mafValue: this.initialValue,
      roundedmafValue: this.initialValue,
    };
  },
  watch: {
    roundedmafValue(newValue) {
      this.mafValue = parseFloat(newValue);
      this.handlemafValue(this.mafValue);
    },
  },
  methods: {
    toggleSwitchValue() {
      this.switchValue = !this.switchValue;
      if (!this.switchValue) {
        this.mafValue = null;
        this.handlemafValue(this.mafValue);
      } else {
        this.mafValue = parseFloat(this.roundedmafValue);
        this.handlemafValue(this.mafValue);
      }
    },
    handleInput() {
      const numericValue = parseFloat(this.roundedmafValue);
      if (numericValue < 0.00) {
        this.roundedmafValue = 0.00;
      } else if (numericValue > 0.50) {
        this.roundedmafValue = 0.50;
      } else {
        this.mafValue = numericValue;
        this.handlemafValue(this.mafValue);
      }
    },
    handlePlus() {
      if (this.switchValue) {
        if (this.mafValue.toFixed(2) < 0.5) {
                this.mafValue += 0.05;
                this.roundedmafValue = this.mafValue.toFixed(2);
                this.handlemafValue(this.mafValue);
        }
      }
      
    },
    handleMinus() {
      if (this.switchValue) {
        if (this.mafValue.toFixed(2) > 0) {
          this.mafValue -= 0.05;
          this.roundedmafValue = this.mafValue.toFixed(2);
          this.handlemafValue(this.mafValue);
        }
      }
    },
    preventEInput(event) {
      if (event.key === "e") {
        event.preventDefault();
      }
    },
  },
  props: {
    initialValue: {
      type: Number,
      default: 0.1,
    },
    handlemafValue: {
      type: Function,
    },
  },
};
</script>
