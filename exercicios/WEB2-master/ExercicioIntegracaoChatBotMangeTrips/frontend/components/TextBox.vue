<script setup>
import { defineProps } from 'vue';

const props = defineProps({
    avatarImage: { type: String },
    name: { type: String },
    message: { type: String },
    type: { type: String },
    image: { type: Array }
});
</script>

<template>
    <div class="text-box" :class="props.type === 'right' ? 'right-style' : 'left-style'">
        <Fieldset>
            <template #legend>
                <div class="flex align-items-center pl-2">
                    <Avatar :image="props.avatarImage" shape="circle" />
                    <span class="font-bold">{{ props.name }}</span>
                </div>
            </template>
            <p class="m-0">{{ props.message }}</p>
            <!-- <div v-if="props.image" class="image-container">
                <img :src="props.image[0]" alt="Image from chatbot response">
            </div> -->
        </Fieldset>
    </div>
</template>

<style scoped lang="scss">
.text-box {
    .p-fieldset {
        font-size: 1rem;
        color: black;       
    }
}

.right-style {
    .p-fieldset {
        background-color: rgb(78, 78, 94);
    }
}

.left-style {
    .p-fieldset {
        background-color: rgb(69, 52, 55);
    }
}

.image-container {
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
}

.image-container img {
    max-width: 100px; /* Adjust as needed */
    height: auto;
}
</style>
