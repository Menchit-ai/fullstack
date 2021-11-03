<template>
  <div id="app">
    <p style="color:blue; font-size:200%; font-weight:bold"> Hello World </p>
    <HelloWorld/>
    <p style="color:blue; font-size:200%; font-weight:bold"> Show User </p>
    <ShowUser/>
    <p style="color:blue; font-size:200%; font-weight:bold"> Create User </p>
    <CreateUser/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import ShowUser from './components/ShowUser.vue'
import CreateUser from './components/CreateUser.vue'

export default {
  name: 'App',
  components:{HelloWorld,ShowUser,CreateUser}
}
</script>
 

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
