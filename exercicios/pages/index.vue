<!-- <script setup lang="ts">
import { ref, computed, reactive } from 'vue'
const countries = [{
  name: 'United States',
  value: 'US'
}, {
  name: 'Canada',
  value: 'CA',
  disabled: true
}, {
  name: 'Mexico',
  value: 'MX'
}]

const country = ref('CA')
</script>

<template>
    <div>
        
       <div class="teste">
            <h1>LETICIA EU TE AMOOOOOOOOOOOOOOOOOO</h1>
       </div>
       <div class="magalu">
        
        <img class="img" src="assets\img\acad.png" alt="">
        

        <h2>Exercicios</h2>
       </div>
       <div class="linha"></div>
       <div class="tela">
        <h1>
            Exercicio 1
        </h1>
        <select v-model="country">
            <option v-for="option in countries" :key="option.value" :value="option.value" :disabled="option.disabled">
            {{ option.name }}
            </option>
        </select>


       </div>
    </div>
</template>

<style scoped>
    .teste{
        width: 100%;
        height: 3rem;
        background-color: rgb(1, 2, 85);
        color: red;
    }
    .magalu{
        display: flex;
        width: 100%;
        height: 8rem;
        background-color: rgb(0, 132, 255);
    }
    .linha{
        width: 100%;
        height: 0.3rem;
        background: linear-gradient(45deg, red, orange, yellow, green, blue, indigo, violet);

    }
    .img{
        width: 120px;
        height: 120px;
    }
    .tela{
        width: 100%;
        height:100vh;
        background-color: white;
    }
</style> -->
<template>
  <div>
    <ChildComponent
      iconImg="icone"
      name="Escolha uma opção"
      :options="selectOptions"
      v-model="selectedValue"
    />
    <p v-if="selectedValue">Opção selecionada: {{ selectedValue }}</p>
    <p v-else>No selected item</p>
  </div>
</template>

<script>
import ChildComponent from '~/components/CustomComp.vue';

export default {
  components: {
    ChildComponent,
  },
  data() {
    return {
      selectOptions: [
        { name: 'Opção 1', value: 'al',  iconImg: 'icone1' },
        { name: 'Opção 2', value: 'ala', iconImg: 'icone2' },
        { name: 'Opção 3', value: 'alaa', iconImg: 'icone3' },
      ],
      selectedValue: '', // Certifique-se de inicializar selectedValue corretamente
    };
  },
};
</script>
