<script setup>
import { defineProps, ref, defineEmits } from 'vue';
import Dropdown from 'primevue/dropdown';

const props = defineProps({
  name: { type: String },
  options: { type: Array, required: true },
  selectedOption: { type: String, required: true },
});

const selectedOption = ref(props.selectedOption);
const emits = defineEmits(['customEvent']);

const formattedOptions = props.options.map(option => ({
  name: option.name
}));

const a = ref('thjrjr6j6'); // Use ref para criar uma variável reativa

const teste = () => {
  
  
  emits('customEvent', selectedOption.value.name); // Use a.value para obter o valor atual
};
</script>

<template>
  <div>

    <Dropdown v-model="selectedOption" :options="formattedOptions" optionLabel="name" @change="teste"/>

    <div>
      <br>
     
    </div>
  </div>
</template>
