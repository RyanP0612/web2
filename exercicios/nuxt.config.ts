// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  
  modules: [
    'nuxt-primevue'
  ],
  primevue: {
    components: {
      include: ['Listbox', 'listbox', 'List-box', 'ListBox', 'list-box', 'List-Box']
    }
  },

css: [
 //variáveis css global customizado para toda a aplicação
  '~/assets/style/global-project.scss',  //css global customizado para toda a aplicação
],

})