<script setup>
import InputSwitch from 'primevue/inputswitch';
import ChildComponent from '~/components/DropDown.vue';
import { ref } from 'vue';
const inputValue1 = ref('');
const inputValue2 = ref('');
const operacao = ref({});
const colors = ref("white");
const colorsText = ref("black");
const checked = ref(false);






const changee = () => {
  if(checked.value){
    console.log("ejfiwerlhfwihfyi4wbg")
    colors.value = 'black';
    colorsText.value = "white";
  }
  else{
    colors.value = 'white';
    colorsText.value = 'black';
  }
};


const handleCustomEvent = (variable) => {
  console.log('Variável recebida:', variable);
  operacao.value = variable;
};


const voltar = (variable) => {
    navigateTo("/");
};


const selectOptions = [
  { name: '×', value: '1' },
  { name: '÷', value: '2'},
  { name: '+', value: '3'},
  { name: '-', value: '4'},
  { name: '√', value: '5'},
];

const resultado = ref("????"); 

const calc = () => {
    
  if ( String(operacao.value) == "+") {
    resultado.value = inputValue1.value + inputValue2.value;
     
  }
  if ( String(operacao.value) == "-") {
    resultado.value = inputValue1.value - inputValue2.value;
     
  }
  if ( String(operacao.value) == "×") {
    resultado.value = inputValue1.value * inputValue2.value;
     
  }
  if ( String(operacao.value) == "÷") {
    resultado.value = inputValue1.value / inputValue2.value;
     
  }
  if ( String(operacao.value) == "√") {
    resultado.value = Math.sqrt(inputValue1.value + inputValue2.value);
     
  }

//   resultado.value = "lero";
};
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
       <div class="tela" :style="{ backgroundColor: colors, color:  colorsText } ">
        
        <h1>exercicio 2</h1>
    <div class="testee">
        
        <label for="">N1: </label>
        <input v-model="inputValue1" type="number">
    
        <ChildComponent
        @customEvent="handleCustomEvent" 
      iconImg="https://efootballhub.net/br/pes21/player/191929760"
      name="Escolha uma opção"
      :options="selectOptions"
      v-model="selectedValue"
      :selectedOption="selectedValue"
      
    />
   
    
        <input v-model="inputValue2" type="number">
        <label for="">:N2 </label>

    </div>
    <br>
    <h1>{{ operacao }}</h1>
    <!-- <h3>aaa{{ a }}</h3> -->
    <button @click="calc">Results</button>
<h3>Resultado: {{ resultado}}</h3>
<br><hr>
        <label for="">Modo de tela</label>
        <InputSwitch v-model="checked"  @change="changee"/>
        
        <br><br><hr>
        <button @click="voltar">Back</button>
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
    .testee{
        display: flex;
        width: 100%;
        
        
    }
</style> 