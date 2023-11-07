<template>
  <div class="post-number-container">
    <div class="basis-2/5 flex items-center">
      <label class="relative inline-flex items-center cursor-pointer">
        <input type="checkbox" :checked="switchValue" @click="toggleSwitchValue" class="sr-only peer" />
        <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600">
        </div>
      </label>
      <h6 class="ml-2">Hardy-Weinberg test (--hwe)</h6>
    </div>
    <div class="basis-3/5 flex">
      <div class="pr-32">
        <div class="h-10 w-32" v-bind:class="{ 'opacity-50': !switchValue }">
          <div class="flex flex-row h-10 rounded-lg relative bg-transparent mt-1">
            <p class="text-lg mr-1 whitespace-nowrap flex items-center">1e -</p>
            <input required type="number" step="1" min="4" max="8" v-model="power" id="power"
              class="flex-1 outline-none focus:outline-none text-center border border-gray-300 font-semibold text-md rounded-md md:text-base cursor-text flex items-center"
              @input="handleInput" @keydown="preventEInput" :disabled="!switchValue"/>
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
      switchValue: !isNaN(this.initialValue) && this.initialValue !== null, 
      power: this.initialValue,
      swPower: null,
    };
  },
  methods: {
    toggleSwitchValue() {
      this.switchValue = !this.switchValue;
      if (!this.switchValue) {
        this.swPower = this.power;
        
        this.handlehewValue("")
      } else {
        this.power = this.swPower;
        this.updateNumber();
      }
    },
    handleInput() {
      if (this.power === "") {
      
      }else if (this.power < 4) {
        this.power = 4;
      } else if (this.power > 8) {
        this.power = 8;
      }
      this.updateNumber();
    },
    handlePlus() {
      this.power += 1;
      this.updateNumber();
    },
    handleMinus() {
      this.power -= 1;
      this.updateNumber();
    },
    updateNumber() {
      this.handlehewValue(this.power);
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
    },
    handlehewValue: {
      type: Function,
    },
  },
};
</script>
