<template>
    <div>
      <!-- Utilizando o Listbox do PrimeVue -->
      <Listbox v-model="selectedOption" :options="formattedOptions" optionLabel="name" class="w-full md:w-14rem" listStyle="max-height:250px">
        <template #option="{ option }">
          <div class="flex align-items-center">
            <img :alt="option.iconImg" :src="getIconSrc(option.iconImg)" :class="`flag flag-${option.iconImg.toLowerCase()} mr-2`" style="width: 18px" />
            <div>{{ option.name }}</div>
          </div>
        </template>
      </Listbox>
    </div>
  </template>
  
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
  
  // Função para obter o caminho da imagem do ícone
  const getIconSrc = (iconImg) => {
    // Substitua esta lógica pela lógica real de obtenção do caminho da imagem do ícone
    return `https://primefaces.org/cdn/primevue/images/flag/flag_placeholder.png`;
  };
  </script>
  
  <style scoped>
  /* Estilos podem ser adicionados conforme necessário */
  </style>
  