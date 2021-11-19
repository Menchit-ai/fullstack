<template>
  <div>
    <button v-on:click="getUser">Get user : </button>
    <input type="text" placeholder="put 0 to get all users" v-model="id">

    <div v-if="users !== null">
        <div v-for="user in users" :key="user.id">
            <p> {{ user.email }} </p>
            <ul>
                <li v-for='text in user.texts' :key="text.id">
                    {{ text.body }}
                </li>
            </ul>
        </div>
    </div>

    <p style="color:red; font-weight:bold"> {{ warning }} </p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      id: null,
      users: null,
      warning: null
    };
  },
  
  methods: {

    async getAllUsers() {
      try{
        this.warning = null
        this.users = null
        const response = await axios.get("users/")
        this.users = response.data
      }catch(error){
        console.log(error)
      }
    },

    async getUser() {
    try {
        if (this.id == 0){
            await this.getAllUsers()
            return
            }
        const response = await axios.get("users/" + this.id)
        this.users = [response.data]
        this.warning = null
    } catch (error) {
        this.users = null
        console.log(error)
        if (this.id == null || this.id < 0){this.warning = "Please put a valid id."}
        else{this.warning = "User not found."}
      }
    },
  },
};
</script>

<style lang="scss" scoped>
  @import "@/form.scss"; //Here i add extra "./"(current directory)
</style>