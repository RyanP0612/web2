<script setup>
import { ref } from 'vue';
import Carousel from 'primevue/carousel';
import 'primevue/resources/themes/saga-blue/theme.css'; // Tema do PrimeVue
import 'primevue/resources/primevue.min.css'; // Estilos gerais do PrimeVue
import 'primeicons/primeicons.css'; // Ícones do PrimeIcons

const produtos = ref([
  { name: 'sss', description: 'asmiksd', price: 555 },
  { name: 'aaa', description: 'neymar', price: 999 },
  { name: 'a', description: 'aaa', price: 695 },
  { name: 'leticiaLinda', description: 'cristiano', price: 612 },
]);

</script>

<template>
  <div>
    <CustomLayout/>
    <h1>Carousel do primevue, teste</h1>
    <Carousel :value="produtos">
      <template #item="produto ">

        <div class="car-card">
          <h3>{{produto.data.name}}</h3>
          <p>Price: aa</p>
        </div>
      </template>
    </Carousel>
    <h2>{{ produtos.price }}</h2>
  </div>
</template>

<style scoped>
.car-card {
  background-color: #f5f5f5;
  border-radius: 8px;
  padding: 20px;
  margin: 10px;
  text-align: center;
}
</style>
