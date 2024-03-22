<script setup lang="ts">
const {signOut} = useAuth();

definePageMeta({
    middleware: 'auth'
})

const sair = ()=>{
    signOut({redirect: false}).then(()=>{
            navigateTo('/');
        })
}

</script>

<template>
    <div>
        <h1>Letícia eu te amo sua linda e maravilhosa!!!</h1>    
        <button @click="sair" class="customButton">SAIR</button>
    </div>
</template>

<style lang="scss">

</style>