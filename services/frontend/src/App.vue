// App.vue
<template>
  <div id="nav">
    <img src="@/assets/ia.jpg">
    <p/>
    <button><router-link to="/">Home</router-link></button>
    <button><router-link to="/suser">User</router-link></button>
    <button><router-link to="/ctext">Write new text</router-link></button>
    <button><router-link to="/quizz">Quizz</router-link></button>
    <button><router-link to="/cuser">Register</router-link></button>
    <p/>
    <router-view/>
  </div>
</template>


<style lang="scss" scoped>
  @import "@/form.scss";
</style>