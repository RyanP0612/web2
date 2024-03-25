

<script setup>
import ChildComponent from '~/components/CustomComp.vue';
import ChildComponent2 from '~/components/CustomComp.vue';

const selectOptions = [
  { name: 'Instagram', value: 'al', iconImg: "https://cdn-icons-png.flaticon.com/256/4138/4138124.png" },
  { name: 'Gmail', value: 'ala', iconImg: 'https://cdn.iconscout.com/icon/free/png-256/free-gmail-2923657-2416660.png?f=webp' },
  { name: 'Github', value: 'alaa', iconImg: 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/GitHub_Invertocat_Logo.svg/800px-GitHub_Invertocat_Logo.svg.png' },
];

const selectOptions2 = [
  { name: 'soma', value: '1', iconImg: "https://cdn-icons-png.flaticon.com/256/4138/4138124.png" },
  { name: 'subtração', value: '2', iconImg: 'https://cdn.iconscout.com/icon/free/png-256/free-gmail-2923657-2416660.png?f=webp' },
  { name: 'divisão', value: '3', iconImg: "https://cdn-icons-png.flaticon.com/256/4138/4138124.png" },
  { name: 'multiplicação', value: '4', iconImg: 'https://cdn.iconscout.com/icon/free/png-256/free-gmail-2923657-2416660.png?f=webp' },
  { name: 'Raiz quadrada', value: '5', iconImg: 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/GitHub_Invertocat_Logo.svg/800px-GitHub_Invertocat_Logo.svg.png' },
];

const ex2 = () =>{
 navigateTo("/exercicio2");
}

let selectedValue = '';
let selectedValue2 = '';

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
        <h4>Suas opções</h4>
        <ChildComponent
      iconImg="https://efootballhub.net/br/pes21/player/191929760"
      name="Escolha uma opção"
      :options="selectOptions"
      v-model="selectedValue"
      :selectedOption="selectedValue"
      
    />
    
    <br><br><br>
    <button @click="ex2">Avançar</button>
        
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
        background-color: var(--light-background-color);
    }
    .teste{
        display: flex;
        width: 100%;
        
        
    }
</style> 