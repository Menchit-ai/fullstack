// App.vue
<template>
  <div id="nav" Align=Center>
    <p/>
    <button><router-link to="/">Home</router-link></button>
    <button><router-link to="/suser">User</router-link></button>
    <button><router-link to="/ctext">Write new text</router-link></button>
    <button><router-link to="/quizz">Quizz</router-link></button>
    <button><router-link to="/cuser">Register</router-link></button>
    <p/>
    <div class="couverture">
      <h1 style="background-color:powderblue;color:black;font-family:Verdana, sans-serif;"> IA ou Humain ? </h1>
    </div>
    <router-view/>
  </div>
</template>


<style lang="scss" scoped>
  @import "@/form.scss";
</style>