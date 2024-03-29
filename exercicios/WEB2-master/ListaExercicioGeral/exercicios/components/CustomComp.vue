
<script setup>
import { defineProps, ref } from 'vue';
import Listbox from 'primevue/listbox';

// Definindo e tipando as props
const props = defineProps({
  iconImg: { type: String },
  name: { type: String },
  options: { type: Array, required: true },
  selectedOption: { type: String, required: true },
});

// Criando uma variável reativa para armazenar o valor selecionado
const selectedOption = ref(props.selectedOption);

// Formatando as opções para o formato esperado pelo Listbox do PrimeVue
const formattedOptions = props.options.map(option => ({
  name: option.name,
  iconImg: option.iconImg,
}));

const img = props.options.iconImg



</script>

<style scoped>
/* Estilos podem ser adicionados conforme necessário */
</style>



<template>
    <div>
      <!-- Utilizando o Listbox do PrimeVue -->
      <Listbox v-model="selectedOption" :options="formattedOptions" optionLabel="name" class="list-box">
        <template #option="slotProps">
        <div class="flex align-items-center">
            <img :alt="slotProps.option.name" :src="slotProps.option.iconImg" style="width: 18px" />
            <span> - {{ slotProps.option.name }}</span>
        </div>
    </template>
      </Listbox>

      <p v-if="selectedOption">Opção selecionada: {{ selectedOption.name }}</p>
    <p v-else>Nenhum item selecionado</p>
    </div>
  </template>
  
<style  scoped>
.list-box{
  width: 150px;
}

</style>