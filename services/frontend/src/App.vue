// App.vue
<template>
  <div id="nav" Align=Center>
    <p/>
    <router-link tag="button" to="/">Home</router-link>
    <router-link tag="button" to="/suser">User</router-link>
    <router-link tag="button" to="/ctext">Write new text</router-link>
    <router-link tag="button" to="/quizz">Quizz</router-link>
    <router-link tag="button" to="/cuser">Register</router-link>
    <p/>
    <div class="couverture">
      <h1 style="background-color:powderblue;color:black;font-family:Verdana, sans-serif;"> AI or Human ? </h1>
    </div>
    <router-view/>
  </div>
</template>


<style lang="scss" scoped>
  @import "@/form.scss";
</style>